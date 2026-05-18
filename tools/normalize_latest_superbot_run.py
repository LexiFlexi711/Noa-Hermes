#!/usr/bin/env python3
import json
import re
from pathlib import Path

root = Path.home() / "Noa-Hermes"
runs_dir = root / "autonomous" / "runs"
outputs_dir = root / "autonomous" / "outputs"
state_path = root / "autonomous" / "state.json"

run_path = sorted(runs_dir.glob("run_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)[0]
stamp = run_path.stem.replace("run_", "")
output_path = outputs_dir / f"content_{stamp}.md"

run = json.loads(run_path.read_text())
output_text = output_path.read_text() if output_path.exists() else ""

def get_nested(d, *keys):
    cur = d
    for k in keys:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(k)
    return cur

critic_score = None
finance_score = None
final_status = None

# 1. Preferred contract paths
critic_score = get_nested(run, "critic", "output", "score")
finance_score = get_nested(run, "finance", "output", "roi_score")
final_status = run.get("final_status")

# 2. Hermes alternate schema paths
if critic_score is None:
    critic_score = get_nested(run, "agents", "critic", "score")
if finance_score is None:
    finance_score = get_nested(run, "agents", "finance", "roi_score")
if final_status is None:
    final_status = get_nested(run, "agents", "critic", "final_status")

# 3. Older final_scores path
if critic_score is None:
    critic_score = get_nested(run, "final_scores", "critic_score")
if finance_score is None:
    finance_score = get_nested(run, "final_scores", "finance_score")

# 4. Markdown fallback
if critic_score is None:
    m = re.search(r"critic\s*score\s*[:#]*\s*(\d+(?:\.\d+)?)", output_text, re.I)
    if m:
        critic_score = float(m.group(1))

if finance_score is None:
    m = re.search(r"finance\s*score\s*[:#]*\s*(\d+(?:\.\d+)?)", output_text, re.I)
    if m:
        finance_score = float(m.group(1))

if final_status is None:
    m = re.search(r"final\s*status\s*[:#]*\s*(accepted|rejected|failed|success)", output_text, re.I)
    if m:
        final_status = m.group(1).lower()

if final_status == "success":
    final_status = "accepted"

# If Critic accepted but score missing, do NOT invent a high score.
# Use 0 and mark failed unless exact score exists.
if critic_score is None:
    critic_score = 0
if finance_score is None:
    finance_score = 0
if final_status is None:
    final_status = "failed"

try:
    critic_score = float(critic_score)
except Exception:
    critic_score = 0

try:
    finance_score = float(finance_score)
except Exception:
    finance_score = 0

if not (0 <= finance_score <= 10):
    final_status = "failed"

# If score missing/zero because Hermes skipped contract, this remains a failed normalized run.
if critic_score == 0 and get_nested(run, "critic", "output", "score") is None and get_nested(run, "agents", "critic", "score") is None:
    final_status = "failed"

run.setdefault("critic", {"output": {}})
run["critic"].setdefault("output", {})
run["critic"]["output"]["score"] = critic_score
run["critic"]["output"]["accepted"] = final_status == "accepted"

run.setdefault("finance", {"output": {}})
run["finance"].setdefault("output", {})
run["finance"]["output"]["roi_score"] = finance_score
run["finance"]["output"]["recommendation"] = "continue" if final_status == "accepted" else "revise"

run["final_status"] = final_status
run["normalized_by"] = "tools/normalize_latest_superbot_run.py"
run["normalized_reason"] = "Normalized Hermes output into machine-readable Noa Superbot contract."

run_path.write_text(json.dumps(run, indent=2, ensure_ascii=False) + "\n")

# Restore/maintain canonical state schema without deleting useful run facts.
if state_path.exists():
    state = json.loads(state_path.read_text())
else:
    state = {}

canonical = {
    "bot_name": "Noa Superbot",
    "controller": "Hermes",
    "owner": "Lexi",
    "real_world_mirror": "Lexi",
    "version": state.get("version", "0.1.0"),
    "active_flow": "content_automation",
    "status": "last_run_normalized",
    "runs_completed": int(state.get("runs_completed", 0)),
    "last_run": stamp,
    "winning_patterns": state.get("winning_patterns", []),
    "rejected_patterns": state.get("rejected_patterns", []),
    "next_action": "Run verifier, then retry only if validator passes with accepted status.",
    "safety": {
        "no_external_api_without_lexi": True,
        "no_publishing_without_lexi": True,
        "no_trading_without_lexi": True,
        "no_git_push_without_lexi": True,
        "no_secrets_in_git": True
    }
}

if final_status == "accepted":
    canonical["status"] = "last_run_accepted"
else:
    canonical["status"] = "last_run_failed"

state_path.write_text(json.dumps(canonical, indent=2, ensure_ascii=False) + "\n")

print(f"NORMALIZED: {run_path}")
print(f"critic_score={critic_score}")
print(f"finance_score={finance_score}")
print(f"final_status={final_status}")
