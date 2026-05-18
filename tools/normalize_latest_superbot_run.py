#!/usr/bin/env python3
import json
import re
from pathlib import Path

root = Path.home() / "Noa-Hermes"
runs_dir = root / "autonomous" / "runs"
outputs_dir = root / "autonomous" / "outputs"

run_path = sorted(runs_dir.glob("run_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)[0]
stamp = run_path.stem.replace("run_", "")
output_path = outputs_dir / f"content_{stamp}.md"

run = json.loads(run_path.read_text())
output_text = output_path.read_text() if output_path.exists() else ""

critic_score = None
finance_score = None
final_status = None

m = re.search(r"critic\s*score\s*[:#]*\s*(\d+(?:\.\d+)?)", output_text, re.I)
if m:
    critic_score = float(m.group(1))

m = re.search(r"finance\s*score\s*[:#]*\s*(\d+(?:\.\d+)?)", output_text, re.I)
if m:
    finance_score = float(m.group(1))

m = re.search(r"final\s*status\s*[:#]*\s*(accepted|rejected|failed|success)", output_text, re.I)
if m:
    final_status = m.group(1).lower()

if final_status == "success":
    final_status = "accepted"

if critic_score is None:
    critic_score = 0
if finance_score is None:
    finance_score = 0
if final_status is None:
    final_status = "failed"

run.setdefault("critic", {"output": {}})
run["critic"]["output"]["score"] = critic_score
run["critic"]["output"].setdefault("accepted", final_status == "accepted")

run.setdefault("finance", {"output": {}})
run["finance"]["output"]["roi_score"] = finance_score
run["finance"]["output"].setdefault("recommendation", "continue" if final_status == "accepted" else "revise")

run["final_status"] = final_status
run["normalized_by"] = "tools/normalize_latest_superbot_run.py"
run["normalized_reason"] = "Hermes wrote human-readable output but missed machine-readable schema fields."

run_path.write_text(json.dumps(run, indent=2, ensure_ascii=False) + "\n")

print(f"NORMALIZED: {run_path}")
print(f"critic_score={critic_score}")
print(f"finance_score={finance_score}")
print(f"final_status={final_status}")
