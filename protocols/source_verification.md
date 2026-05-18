# Protocol: source_verification

## Doel
Dit protocol dwingt de verplichting af voor agents om alle claims, data en resultaten te onderbouwen met verifieerbare bronnen.

## Kernprincipes
1.  **Bewijs is Koning:** Alle output die feitelijke claims bevat, MOET een expliciete, werkende referentie naar de bron hebben.
2.  **Traceerbaarheid:** De bron moet direct leiden naar de data of informatie waarop de claim is gebaseerd.
3.  **Validatie:** Bronnen moeten gecontroleerd worden op relevantie en betrouwbaarheid.

## Regels voor Bronverificatie

**1. Verplichte Bronnen:**
*   **Onderzoek & Marktvalidatie:** Agents zoals `Web Researcher`, `Market Validator`, `Monetization Validator` en `Critic` MOETEN voor elke claim, score of conclusie een directe, werkende URL of pad naar het bewijsstuk leveren. Dit kan zijn:
    *   `web_search` resultaat URL.
    *   Directe link naar een artikel, rapport, of document.
    *   Pad naar een lokaal bestand (`read_file` bron).
*   **Claims zonder Bron:** Elke claim zonder expliciete, verifieerbare bron wordt beschouwd als speculatie.

**2. Score Bepaling:**
*   **`web_search` / `web_extract` Resultaten:** Als een `web_search` query geen resultaten oplevert, of als `web_extract` faalt, wordt de betreffende taak gemarkeerd als `failed` voor de `Web Researcher`. De `Monetization Validator` en `Market Validator` mogen geen score toekennen op basis van deze mislukte zoekopdrachten.
*   **`Monetization Validator`:**
    *   Bij het voorstellen van `monetization_options`, elke optie MOET een `evidence` veld hebben met werkende URL's.
    *   Indien geen bewijs beschikbaar is voor een substantiële geldroute, wordt de kans met die route als `rejected` beschouwd voor die specifieke optie.
*   **`Critic`:**
    *   `evidence_quality` score is direct gekoppeld aan de volledigheid en betrouwbaarheid van de bronnen geleverd door `Web Researcher` en `Market Validator`.
    *   Een score van 0 voor `evidence_quality` kan leiden tot een `rejected` beslissing.

**3. "Geen bron = Score 0":**
*   Dit principe geldt voor alle agents die claims doen die uit externe bronnen moeten komen. Dit omvat ook claims over markttrends, concurrentie, of potentiële inkomstenbronnen.

**4. Rapportage van Bron Kwaliteit:**
*   **`Web Researcher`:** Moet de relevantie van de gevonden bronnen beoordelen en rapporteren.
*   **`Critic`:** Moet de kwaliteit en betrouwbaarheid van de bronnen specifiek meewegen in de `evidence_quality` score.

## Gedragsregels voor Agents
*   **Altijd Bronnen Vermelden:** Dit is geen optie, maar een vereiste voor alle claims.
*   **Confronteer Ontbrekende Bronnen:** Agents die input ontvangen zonder bronnen moeten dit markeren en escaleren aan de Agent Controller.
*   **Niet Speculeren:** Vermijd claims zonder direct bewijs.

## Toegestane Tools voor Bronverificatie:
*   `web` (primair voor zoeken en toegang)
*   `browser` (fallback)
*   `read_file` (voor lokale bronnen)
*   `search_files` (voor lokale datasets)
*   `Agent Controller` (voor routing en validatie)
*   `QA Agent` (voor het controleren van naleving van dit protocol)