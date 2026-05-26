# Meeting Sync Policy

Status: active
Type: protocol
Project: Noa-Hermes
Date: 2026-05-26

## Source of Truth

`/home/sjoe/Noa-Hermes/autonomous/meetings/`

is de canonieke bron voor meeting records.

## Derived Copy

`/home/sjoe/system/hermes-second-brain/second-brain/wiki/synthesis/`

is een afgeleide kopie/synthese voor Obsidian, graph en retrieval.

## Regels

- Meetings worden eerst geschreven naar `autonomous/meetings/`.
- `wiki/synthesis/` mag nooit de primaire bron zijn.
- Geen underscores in meeting filenames.
- Geen dubbele meetingnummers zonder topic/suffix.
- Geen invalid Windows chars.
- Geen timestamps met `:` in filenames.
- Geen nested `second-brain/second-brain`.
- Geen automatische delete zonder auditrapport.

## Canonieke naamvormen

Voor gewone meetings:

`meeting-NNN-topic.md`
`meeting-NNN-topic.json`

Voor teammeetings:

`team-meeting-NNN-topic.md`
`team-meeting-NNN-topic.json`

Voor eenvoudige bestaande records zonder topic:

`meeting-NNN.md`
`meeting-NNN.json`

## Sync-richting

autonomous/meetings → second-brain/wiki/synthesis

Niet omgekeerd, tenzij expliciet beslist na audit.

## Bewijsvereiste

Elke sync moet tonen:

- bronpad
- doelpad
- aantal bestanden
- git status vóór
- git status na
