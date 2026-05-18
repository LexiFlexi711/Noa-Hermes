# Protocol: output_validation

## Doel
Dit protocol definieert de standaarden en procedures voor het valideren van de output van agents om te verzekeren dat deze bruikbaar, correct en conforme is.

## Kernprincipes
1.  **Schema Conformiteit:** Alle gestructureerde output (JSON, YAML, specifieke MD-formaten) MOET voldoen aan het gedefinieerde schema.
2.  **Rol Integriteit:** Output MOET consistent zijn met de gedefinieerde rol en beperkingen van de agent.
3.  **Volledigheid & Correctheid:** Output MOET alle vereiste velden bevatten en correcte data tonen.
4.  **Traceerbaarheid:** Output MOET linken naar de input en de oorspronkelijke taak/run_id.

## Validatieprocedures

**1. Schema Validatie:**
*   **Standaard:** Alle outputs in JSON-formaat MOETEN syntactisch correct zijn en passen binnen het `expected_schema` van de agent.
*   **Tooling:** `code_execution` tool mag gebruikt worden voor JSON-schema validatie.
*   **Foutafhandeling:** Ongeldige JSON wordt gemarkeerd als `failed` output.

**2. Rol & Contract Integriteit:**
*   **Verificatie:** QA Agent controleert of de output van een agent in lijn is met zijn `role_contract` (bv. `.md` definitie) en 'Mag wel'/'Mag niet' lijsten.
*   **Voorbeeld:** Critic mag geen monetization optie *kiezen*, alleen reviewen. Builder mag geen productiecode bouwen.

**3. Bronplicht & Correctheid:**
*   **Verificatie:** QA Agent controleert of bronnen (URL's, paden) correct zijn vermeld waar vereist (`source_requirements`).
*   **Compleetheid:** Controleren of alle vereiste velden in de output aanwezig zijn. `File not found` of `permission denied` bij het schrijven van log/verslagbestanden door Secretary resulteert in `failed`.

**4. Workflow Bruikbaarheid:**
*   **Overgangscontrole:** Output moet bruikbaar zijn als input voor de volgende agent in de workflow (bv. correct formaat, vereiste velden aanwezig).
*   **`next_action` veld:** Indien aanwezig, moet dit een valide volgende stap aanduiden.

**5. Secretary Verslag Validatie:**
*   **Verificatie:** QA Agent controleert of de `.md` en `.json` verslagen van de Secretary daadwerkelijk op disk staan (`write_file` succesvol) en traceerbaar zijn naar de `meeting_id`.

## Gedragsregels voor Agents
*   **Output is Contractieel:** De output van een agent bindt deze. Fouten hierin kunnen leiden tot `failed` status of `needs_revision`.
*   **Vraag Verduidelijking:** Indien input of schema onduidelijk is, vraag de Agent Controller om verduidelijking vóór het produceren van output.

## Toegestane Tools voor Validatie
*   `code_execution` (voor JSON/schema validatie).
*   `read_file`, `search_files` (om output bestanden te controleren).
*   `terminal` (voor basis bestands/directory checks).
*   `Agent Controller` (voor coördinatie en escalatie).
*   `QA Agent` (voor de uiteindelijke controle).