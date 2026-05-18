# Protocol: tool_usage_policy

## Doel
Dit protocol definieert de regels en beperkingen voor het gebruik van tools door agents, om veiligheid, efficiëntie en correctheid te waarborgen.

## Kernprincipes
1.  **Strikte Tool Selectie:** Elke agent gebruikt alleen de tools die expliciet in zijn rolcontract (`.md` bestand) zijn toegestaan.
2.  **Correcte Tool Context:** Tools worden gebruikt met de juiste parameters en binnen de gespecificeerde scope.
3.  **Geluimitreerd Gebruik:** Agents mogen tools niet misbruiken of buiten hun bedoelde functie gebruiken.
4.  **Transparantie & Logging:** Alle tool calls moeten logbaar zijn en de output moet correct worden verwerkt.

## Regels voor Tool Gebruik

**1. Algemene Tool Selectie & Routing:**
*   **Agent Controller's Rol:** De Agent Controller is primair verantwoordelijk voor het kiezen van de juiste tool voor een gegeven taak, gebaseerd op de agent's rolcontract en protocolvereisten.
*   **Strikte Scheiding:**
    *   `terminal` is voor shell-commando's, diagnose, & controle. Nooit voor actieve wijzigingen (tenzij expliciet de `DevOps Guard`rol dit vereist met approval).
    *   `execute_code` is voor het uitvoeren van Python scripts/codeblokken, niet voor algemene command-line taken die `terminal` vereisen.
*   **Fallback Mechanisme:** Bij twijfel over toolselectie, moet de Agent Controller eerst de `qa_agent` consulteren of direct escaleren naar Lexi.

**2. Specifieke Tool Beperkingen & Vereisten:**
*   **`web` & `browser`:**
    *   `web_search` / `web_extract` mag pas na succesvolle plugin-check/initialisatie.
    *   `browser` is enkel een fallback indien `web` faalt.
*   **`read_file`, `write_file`, `search_files`, `patch`:**
    *   Mogen alleen opereren op absolute paden binnen `/home/sjoe/Noa-Hermes/` (conform `path_management.md`).
    *   `patch` is enkel voor kleine edits op bewezen bestanden. `write_file` is voor nieuwe of volledige content.
*   **`terminal`:**
    *   Gebruik beperkt tot controle/diagnose (`pwd`, `ls`, `git status` etc.). Geen modifica/install/delete commando's zonder explicit goedgekeurde workflow en approval.
*   **`code_execution`:**
    *   Exclusief voor analyse, structurering, validatie van data (bv. JSON), of het uitvoeren van een *door Builder gegenereerd script* voor experimentdoeleinden. **NIET** voor het *creëren* van scripts zonder expliciete `build_task`.
*   **`memory`:**
    *   Gebruikt voor persistente opslag van learnings, status, voorkeuren. Enkel via de `Memory Keeper` agent of direct door Controller voor meta-informatie.

**3. Foutafhandeling:**
*   **`File not found`, `permission denied`:** Moet leiden tot `failed` status en escalatie naar Controller. Controller moet diagnostische stappen ondernemen (zoals gedefinieerd in `path_management.md`).
*   **`NameError` / `ImportError` in `code_execution`:** Indicatie van verkeerde tool selectie of misconfiguratie. Moet leiden tot `failed` status.
*   **Tool Output:** Output moet volledig ontvangen en verwerkt worden, niet samengevat, tenzij de taak dit expliciet vereist en gevalideerd is door QA.

## Gedragsregels voor Agents
*   **Ken je Tools:** Weet welke tools je hebt en hoe ze correct te gebruiken.
*   **Escalleer Bij Twijfel:** Als de juiste tool of het exacte gebruik onduidelijk is, vraag de Agent Controller.
*   **Log Toolgebruik:** Elke tool call moet gelogd worden voor traceerbaarheid.

## Toegestane Tools voor dit Protocol:
*   `Agent Controller` (aansturing en validatie)
*   `QA Agent` (verificatie van naleving)
*   `Hermes Updater` (voor onderzoek naar nieuwe/verbeterde tools)
*   `Secretary` (voor logging van tool calls en output)