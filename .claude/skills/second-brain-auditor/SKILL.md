# Second Brain Auditor

## Doel

Audit het second brain op:
- naming chaos
- duplicate meetings
- broken structure
- recursive folders
- invalid filenames
- orphan notes
- stale context
- raw dumps zonder promotie

## Regels

- Evidence first
- Nooit automatisch deleten
- Eerst rapporteren
- Daarna voorstellen
- Daarna expliciete confirmatie

## Controlepunten

### Naming
- geen dubbele datums
- geen :
- geen rare unicode
- consistente separators

### Structure
- geen nested second-brain copies
- geen recursive sync loops
- geen duplicate folders

### Wiki governance
- raw != truth
- wiki = curated canon
- duplicates markeren
- archive voorstellen

## Output

Per probleem:
- severity
- exact path
- oorzaak
- voorstel
- risico

## Canonical Brain Root

Use this path as the shared second brain:

`/home/sjoe/system/hermes-second-brain/second-brain`

Do not treat `/home/sjoe/Noa-Hermes/memory` as source of truth.
Never create nested second-brain copies.

## Meeting Sync Policy

Canonical meeting source:

`/home/sjoe/Noa-Hermes/autonomous/meetings/`

Derived synthesis target:

`/home/sjoe/system/hermes-second-brain/second-brain/wiki/synthesis/`

Never treat `wiki/synthesis/` as source of truth.
Never write meetings directly to synthesis before autonomous/meetings.
No underscores in meeting filenames.

---

## Claude Second Brain Rules

Canonical second brain:

`/home/sjoe/system/hermes-second-brain/second-brain`

Gebruik dit ALTIJD als shared brain voor Claude + Hermes.

---

## Read Policy

Claude mag lezen uit:

* `MOC/`
* `wiki/`
* `protocols/`
* `audits/`
* `decisions/`
* `open_loops/`
* `raw/inbox/`

---

## Write Policy

Claude mag ALLEEN schrijven wanneer Lexi expliciet opdracht geeft.

Toegestane write targets:

* `raw/inbox/mobile`
* `raw/inbox/windows-new`
* `audits/`
* `wiki/projects/`
* `wiki/decisions/`
* `wiki/fixes/`

---

## Meeting Policy

Canonical source:

`/home/sjoe/Noa-Hermes/autonomous/meetings`

Derived target:

`second-brain/wiki/synthesis`

Nooit rechtstreeks schrijven naar synthesis zonder canonical meeting source.

Geen underscores in nieuwe meeting filenames.

---

## Safety Rules

Verboden:

* nested `second-brain/second-brain`
* recursive sync loops
* writes naar legacy memory folders
* automatische cleanup
* automatische archive acties
* synthesis als source of truth behandelen

---

## Evidence Policy

Na ELKE write-back verplicht tonen:

* exact path
* `ls -la`
* `tail -20`

Nooit claimen dat iets opgeslagen is zonder bewijs.

---

## Git Policy

Nooit automatisch:

* `git add -A`
* mass deletes
* bulk rename acties

Altijd eerst audit + bewijs tonen.
