# Protocol: path_management

## Doel
Dit protocol definieert de regels en procedures voor het hanteren van bestandspaden binnen het Noa Agent Company, met de nadruk op veiligheid, traceerbaarheid en consistentie.

## Kernprincipes
1.  **Absolute Paden Overal:** Standaard moeten alle bestandspaden absoluut zijn, specifiek binnen de gedefinieerde projectstructuur `/home/sjoe/Noa-Hermes/`.
2.  **Traceerbaarheid:** Elke operatie op bestanden moet traceerbaar zijn naar de agent, taak, en run-ID.
3.  **Limiteer Scope:** Toegang tot bestanden moet beperkt blijven tot wat strikt noodzakelijk is voor de agent's rol en taak.

## Regels voor Padgebruik

**1. Standaard Pad Gebruik:**
*   **Absolute Paden:** Alle bestandspaden voor `read_file`, `write_file`, `search_files`, `patch` commando's MOETEN absolute paden zijn die beginnen met `/home/sjoe/Noa-Hermes/`.
*   **Projectspecifieke Mappen:** Gebruik specifieke mappen zoals `autonomous/agents/`, `autonomous/meetings/`, `autonomous/experiments/active/`, `projects/`, `dataLexi/` etc., zoals gedefinieerd in de agentrollen.

**2. Relatieve Paden:**
*   **Voorwaardelijk Gebruik:** Relatieve paden zijn alleen toegestaan als de huidige werkdirectory (`pwd`) door de Agent Controller expliciet is geverifieerd als stabiel en binnen de veilige context van de taak.
*   **Verificatie:** De Agent Controller moet de `pwd` controleren en loggen voordat relatieve paden worden gebruikt.

**3. Verboden Pad Fallbacks:**
*   **Geen Fallback naar `/tmp` of `/home/sjoe/`:** Deze algemene mappen mogen NIET worden gebruikt voor operationele bestanden, tenzij expliciet gespecificeerd als tijdelijke scratch space voor een specifieke, gelogde reden. Deze ruimte moet na gebruik worden opgeschoond.
*   **Niet-Project Mappen:** Paden die buiten de `/home/sjoe/Noa-Hermes/` structuur liggen, zijn verboden voor alle agenten, tenzij expliciet goedgekeurd door Lexi via de Agent Controller.

**4. Foutafhandeling bij Bestandsoperaties:**
*   **`File not found` / `Permission denied`:**
    *   De agent die de operatie uitvoert, moet dit direct melden als `failed` aan de Agent Controller.
    *   De Agent Controller initieert, indien nodig, een diagnose:
        1.  Controleer het pad op typfouten en correcte absolute/relatieve status.
        2.  Gebruik `terminal` om `ls -lah <parent_directory>` te draaien om de inhoud van de map te inspecteren.
        3.  Indien het bestand structureel lijkt te ontbreken na deze controles, markeer de taak als `failed` en escaleer naar Lexi.
*   **Loggen:** Alle pad-gerelateerde fouten en diagnose-stappen moeten worden gelogd door de Secretary.

## Gedragsregels voor Agents
*   **Altijd Absolute Paden:** Houd de standaard aan.
*   **Context Vragen:** Indien de toegestane paden onduidelijk zijn, vraag de Agent Controller om verduidelijking.
*   **Rapporteer Afwijkingen:** Meld onmiddellijk problemen met paden of bestandsoperaties.

## Toegestane Tools voor Pad Management
*   `read_file`, `write_file`, `search_files`, `patch` (alleen met absolute paden).
*   `terminal` (voor `pwd`, `ls -lah`, `find` commando's conform protocol).
*   `code_execution` (voor path manipulatie in scripts, met logging).
*   `Agent Controller` (voor het afdwingen van deze regels en het bieden van context).