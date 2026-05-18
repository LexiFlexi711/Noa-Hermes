***
### ANTI_LOOP_PROTOCOL SPECIFICATIE

**1. LOOP_DEFINITIONS**

*   **Outputherhaling**: `repeated_output_count` > 1 (zelfde output hash voor opeenvolgende tool calls).
*   **Tool/Input Herhaling**: `repeated_tool_count` > 1 INDIEN:
    *   Dezelfde `last_tool` herhaalt.
    *   Geen nieuwe input werd gegeven aan de tool.
    *   Geen nieuwe output werd gegenereerd door de tool.
    *   Geen fase-overgang (`phase`) plaatsvond sinds de vorige aanroep.
    *   Geen bewijsbare vooruitgang werd gerealiseerd (bv. via file access, state change).
*   **Fase Herhaling**: `phase` blijft hetzelfde voor > X acties (bv. V0: 3) zonder significante voortgang (bv. `action_count` stijgt niet, geen file I/O, geen state change).
*   **Intentie zonder Bewijs**: Agent claimt actie (bv. "schrijven", "aanmaken", "kopiëren", "bestaat", "config correct") maar `evidence_required` blijft True en er is geen bijhorend file-change log, tool output of verificatie die de claim ondersteunt. Hieronder valt ook het verzinnen van antwoorden zonder bron.
*   **Scope Overtreding / Forbidden Action**:
    *   Actie gedefinieerd in `forbidden_actions` wordt uitgevoerd (`simulated_agent_input_detected`, `call_meeting`, `commit`, `push`, `git_add`).
    *   `write_file` of `terminal` (met wijzigingen) wordt uitgevoerd op een bestandspad in `forbidden_files`.
    *   `terminal_write_action` wordt uitgevoerd buiten een expliciet toegestane scope.
    *   Tool call tijdens `phase` = `WAITING_FOR_LEXI`.
*   **Status Claim zonder Bewijs**: Agent claimt status (bv. "bestand bestaat", "config is correct") zonder expliciete verificatie tool call (`read_file`, `search_files`, `terminal_read_only`) die de claim ondersteunt binnen de huidige RUN_STATE.

**2. RUN_STATE velden**

*   `current_task`: String. Huidig hoofddoel.
*   `current_scope`: Enum {READ_ONLY, WRITE, AUDIT_ONLY, CUSTOM_SCOPE_X}.
    *   `AUDIT_ONLY`: read/check/report only; geen schrijfacties (write_file, git add/commit/push, systeemfile edits).
*   `allowed_files`: List/Pattern String. Bestandsfilters toegestaan voor wijzigingen (bv. `~/.config/*.yaml`).
*   `forbidden_files`: List/Pattern String. Bestandsfilters expliciet verboden (bv. `/etc/*`, `~/.hermes/*`).
*   `allowed_actions`: List String. Toegestane tool/commando types (bv. `read_file`, `search_files`, `terminal_read_only`).
*   `forbidden_actions`: List String. Verboden tool/commando types (bv. `simulated_agent_input_detected`, `call_meeting`, `commit`, `push`, `git_add`, `terminal_write_action`).
*   `phase`: Enum {PLANNING, EXECUTING, WAITING_FOR_LEXI, CODE_EXECUTION, VERIFICATION}.
*   `action_count`: Integer. Totaal aantal uitgevoerde acties sinds start.
*   `repeated_output_count`: Integer. Opeenvolgende gelijke tool outputs.
*   `repeated_tool_count`: Integer. Opeenvolgende relevante calls van dezelfde tool/commando.
*   `last_tool`: String. Naam van de laatst uitgevoerde tool/commando.
*   `last_output_hash`: String. Hash van de output van `last_tool`.
*   `evidence_required`: Boolean. Moet de actie/claim onderbouwd worden?
*   `stop_reason`: String. Reden van stopzetting.

**3. STOPREGELS**

*   `action_count` > 5.
*   `repeated_output_count` > 1 bij foutmeldingen of niet-voortschrijdende outputs.
*   `Gegenereerde Tool/Input Herhaling` conditie is voldaan.
*   `evidence_required` is True en geen bewijs na actie.
*   Overtreding van `current_scope` (bv. schrijven in `AUDIT_ONLY` mode).
*   Overtreding van `allowed_files`, `forbidden_files`, `allowed_actions`, `forbidden_actions`.
*   Detectie van `simulated_agent_input_detected`.
*   Expliciete STOP-opdracht van de user.

**4. RAPPORTFORMAAT BIJ STOP**

LOOP_RISK: [HIGH/MEDIUM/LOW]
STOP_REASON: [Concise explanation string]
LAST_SAFE_STATUS: { current_task: "...", current_scope: "...", phase: "...", action_count: N, last_tool: "...", ... }
FILES_CHANGED: ["/path/to/file1", "/path/to/file2"]
EVIDENCE: [Relevant logs, tool outputs, state snapshots that triggered stop]
NEXT_SAFE_ACTION: [User instruction, bv. "Verifieer scope definities" of "Voer volgende stap manueel uit"]

**5. TESTSCENARIO’S**

*   **Test 1 (Fase Herhaling)**: Agent blijft >1 beurt in `PLANNING` fase zonder output te genereren of `action_count` te verhogen. `action_count` stijgt niet, `last_tool` is consistent. Stop met `STOP_REASON: Fase Herhaling` en `LOOP_RISK: MEDIUM`.
*   **Test 2 (Scope Overtreding: Write)**: Agent start in `current_scope: AUDIT_ONLY` en probeert `write_file`. Stop met `STOP_REASON: Scope breach (AUDIT_ONLY)` en `LOOP_RISK: HIGH`.
*   **Test 3 (Intentie zonder Bewijs)**: Agent claimt "bestand X bestaat" (`evidence_required: True`) maar `read_file` of `search_files` (voor X) werd niet uitgevoerd in de huidige RUN_STATE. Stop met `STOP_REASON: Intentie zonder Bewijs` en `LOOP_RISK: LOW`.
*   **Test 4 (Simulated Agent Input)**: Agent detecteert `simulated_agent_input_detected` patroon in output. Stop met `STOP_REASON: Forbidden action (simulated_agent_input_detected)` en `LOOP_RISK: HIGH`.
*   **Test 5 (Tool Herhaling zonder Progress)**: Agent voert `read_file` uit op hetzelfde bestand 3x achter elkaar, zonder fase-overgang, zonder nieuwe input, zonder output hash verandering. De `repeated_tool_count` conditie wordt voldaan. Stop met `STOP_REASON: Tool/Input Herhaling` en `LOOP_RISK: MEDIUM`.

**6. IMPLEMENTATIEVOLGORDE**

NOW:
- CORE STATE MANAGEMENT: `RUN_STATE` velden implementatie, inclusief Enum en scope definities (bv. `AUDIT_ONLY`).
- DEFINITIE VAN LOOP_DEFINITIES: Vertaal regels naar checks, met specifieke condities voor `repeated_tool_count`, `terminal` acties (`terminal_read_only` vs `terminal_write_action`), en `simulated_agent_input_detected`.
- DEFINITIE VAN STOPREGELS: Vertaal condities naar triggers.

NEXT:
- RAPPORTFORMAAT: Implementeer output format bij stop.
- TESTSCENARIO TESTS: Automatiseer checks voor de testgevallen.
- PREVENTIEVE REGELEXECUTIE: Implementeer checks vóór elke actie, inclusief `AUDIT_ONLY` checks en scope-specifieke actieverboden.

LATER:
- GEAVANCEERDE PREVENTIE: Zelfcorrectie in 'planning' fase.
- INTEGRATIE: Koppeling met eventuele nieuwe user/system protocols.
***
