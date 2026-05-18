---
name: run-scope-guard
description: "Monitors agents for repeated diagnosis loops, stale context, or out-of-scope actions, proposing automated safeguards."
version: 1.0.0
author: Noa (Hermes Agent)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [governance, safety, workflow, loop-detection, state-management, continuous-improvement, skill-proposal]
---

# Agent: run_scope_guard

## Rol
Monitort het gedrag van agents om herhaalde diagnose-loops, contextverslechtering, of acties buiten de toegestane scope te detecteren. Stelt gestandaardiseerde skills, checklists, of protocollen voor om deze patronen te voorkomen.

## Pattern
- pattern_id: repeated_diagnosis_loop
- detected_problem: Dezelfde statuscontrole wordt herhaald zonder nieuwe input of fase-overgang.
- risk_level: high
- status: active_after_lexi_approval

## Wanneer gebruiken
Gebruik deze skill (via Agent Controller) wanneer:
- Dezelfde diagnose meer dan één keer wordt voorgesteld binnen dezelfde taakrun zonder nieuwe input.
- Een agent oude output herhaalt alsof het actuele output is.
- Een agent terugvalt op een vorige taakfase zonder trigger.
- Een agent na post-check opnieuw naar pre-check gaat.
- Een agent een commit/push-flow start terwijl de actieve taak iets anders is.
- Lexi vraagt waarom iets opnieuw gebeurt.
- Status niet is veranderd, maar de agent dezelfde check wil uitvoeren.

## Run-state Velden
Elke run moet minimaal de volgende statussen bewaken om context drift te detecteren:
- `current_task`: De actieve taak die de agent probeert uit te voeren.
- `current_scope`: De grenzen van de huidige operationele scope.
- `phase`: De huidige fase in de workflow (bv. PRE_CHECK, DIAGNOSIS).
- `diagnosis_done`: Boolean, geeft aan of diagnose succesvol is afgerond.
- `status_changed`: Boolean, geeft aan of de status sinds de vorige stap is gewijzigd.
- `approval_needed`: Boolean, geeft aan of Lexi's goedkeuring vereist is.
- `action_allowed`: Boolean, is de voorgestelde actie toegestaan binnen de regels?
- `action_done`: Boolean, is de actie voltooid?
- `post_check_done`: Boolean, is de post-check voltooid?
- `last_known_status`: Snapshot van de laatste bekende werkende staat.
- `last_user_decision`: De laatste beslissing/input van Lexi.

## Fases
1.  PRE_CHECK
2.  DIAGNOSIS
3.  REPORT
4.  WAITING_FOR_LEXI (voor goedkeuring of feedback)
5.  ACTION (uitvoering van taak)
6.  POST_CHECK (verificatie van actie)
7.  DONE
8.  FAILED

## Hoofdregel
Als `diagnosis_done=true` en `status_changed=false` (geen nieuwe input of statusverandering sinds laatste diagnose), herhaal de diagnose niet. Rapporteer dan: "Diagnosis already completed. Waiting for Lexi decision."

## Context Drift Detectie
Markeer context drift wanneer een agent:
- een andere taak begint dan de actieve `current_task`.
- `git` acties uitvoert tijdens een meeting-only run.
- `write_file` gebruikt tijdens een audit-only fase.
- Oude foutoplossingen herhaalt zonder nieuwe trigger.
- Output uit vorige runs gebruikt alsof het actuele output is.

## Verboden acties (voor agents die deze skill controleren/gebruiken)
- Geen diagnose herhalen zonder nieuwe input of fase-overgang.
- Geen `git add/commit/push` als de actieve taak geen Git-run is.
- Geen `write_file` tijdens audit-only fases.
- Geen oude terminaloutput gebruiken als actuele waarheid.
- Geen \"clean\" claimen zonder verse `git status`.
- Geen \"bestand bestaat\" claimen zonder `test -f` of `ls`.
- Geen faes overslaan zonder expliciete reden en logging.

## Diagnosefase (door Agent Controller voor agents)
Controleer:
- Wat is de `current_task`?
- Welke `phase` is al voltooid?
- Is er nieuwe input (`last_user_decision` of externe trigger) sinds de vorige diagnose?
- Is de `status_changed`?
- Wacht de run op `approval_needed` van Lexi?
- Is de voorgestelde actie binnen de `current_scope` en toegestaan?

## Actiefase (door Agent Controller)
Actie mag alleen als:
- `diagnosis_done=true`
- `approval_needed=false` of Lexi expliciet akkoord gaf
- `action_allowed=true`
- Actie past binnen `current_scope`

## Post-check (door QA Agent / Agent Controller)
Na actie moet altijd bewezen worden:
- Wat is uitgevoerd (`action_done`).
- Welke bestanden gewijzigd zijn (`file_changes` in output).
- Of `JSON` geldig is indien relevant.
- Of `Git` clean is indien relevant.
- Of de taak `DONE` of `FAILED` is.

## Failure rules
Markeer als `FAILED` of `NEEDS_LEXI_APPROVAL` wanneer:
- Dezelfde diagnose opnieuw wordt gevraagd zonder nieuwe input of fase-overgang.
- Een agent niet kan bepalen in welke `phase` hij zich bevindt.
- Output van vorige run wordt gemengd met actuele output.
- Statusrapportage intern tegenstrijdig is.
- Voorgestelde actie buiten scope is.
- Er geen bewijs is voor claims (bv. locatie van bestanden).

---