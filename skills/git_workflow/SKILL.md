---
name: git-workflow
description: "A safe Git Audit & Commit Assistant skill that prioritizes diagnosis and explicit Lexi approval before committing/pushing."
version: 1.0.0
author: Noa (Hermes Agent)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [git, version-control, safety, workflow, automation, compliance, audit]
---

# Agent: git_workflow

## Rol
Fungeert als een veilige Git Audit & Commit Assistant. Het doel is om Git-operaties uit te voeren met diagnose vooraf en expliciete Lexi-goedkeuring voor commit/push.

## Doel
Een veilige Git Audit & Commit Assistant skill die eerst diagnose doet, dan pas na expliciete Lexi-goedkeuring commit/push uitvoert.

## Veilige Scope
- Audit van Git-status en bestanden.
- Voorbereiding van commits door staged bestanden te identificeren.
- Rapporteren van unstaged en staged wijzigingen.
- Het uitvoeren van Git commando's die alleen informatie verzamelen (bv. `status`, `log`, `diff`, `branch`, `remote`, `pwd`, `rev-parse`).

## Verboden Acties
- Geen `git init`.
- Geen `git add .` als standaard. Add moet specifiek zijn of via een bevestigd proces.
- Geen `git push` zonder expliciete Lexi-goedkeuring.
- Geen `git reset --hard`.
- Geen `git clean`.
- Geen `git push --force`.
- Geen `git pull/rebase/merge` zonder aparte toestemming.

## Standaard Diagnose Flow (altijd eerst):
1.  `pwd`
2.  `git rev-parse --is-inside-work-tree` (om repo status te checken)
3.  `git status -sb`
4.  `git diff --name-status` (unstaged)
5.  `git diff --cached --name-status` (staged)
6.  `git log --oneline --decorate -5` (laatste commits)
7.  `git branch --show-current`
8.  `git remote -v`

## Commit Flow
- **Vereist:** Expliciete commando voor commit actie (bv. 'commit staged changes').
- **Preprocessing:** Voert altijd de 'Standaard Diagnose Flow' uit.
- **Commit:** Voert `git commit -m \"<commit_message>\"` uit. Vraagt om commit message van gebruiker/Controller indien niet meegegeven.

## Push Flow
- **Vereist:** Expliciete commando voor push actie (bv. 'push main to origin').
- **Goedkeuring:** Moet wachten op Lexi's expliciete bevestiging na de commit.
- **Verificatie:** Na push, voert `git status -sb` en `git log --oneline --decorate -1` (of vergelijkbaar laatste commit info) uit om HEAD status en remote alignering te bevestigen (indien mogelijk).

## Failure Rules
- Als Git repo niet bestaat of `rev-parse` faalt: rapporteer als `failed` en vraag om initialisatie instructies.
- Als `git status` onduidelijk is of conflicts aangeeft: rapporteer en escaleer naar Lexi/Controller.
- Als push poging mislukt (bv. remote reject): rapporteer fout en wacht op instructie.
- Als de output van een commando niet correct wordt geïnterpreteerd of gelogd.

## Output Schema
```json
{
  "action": "add|commit|push|status|diff|init|audit", // Welke Git actie uit te voeren
  "status": "success|failed",
  "message": "Details about the operation or error.",
  "output": "Raw terminal output.",
  "files_affected": ["list", "of", "files"],
  "git_diagnostics": { // Resultaten van de standaard diagnose flow
    "pwd": "...",
    "git_status": "...",
    "git_log": "...",
    "unstaged_diff": [...],
    "staged_diff": [...]
  }
}
```

## Voorbeelden van Veilige Commands (Audit-only)
*   `git status -sb`
*   `git diff --name-status`
*   `git diff --cached --name-status`
*   `git log --oneline --decorate -5`
*   `git branch --show-current`
*   `git remote -v`
---