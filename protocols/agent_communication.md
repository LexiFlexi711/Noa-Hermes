# Protocol: agent_communication

## Doel
Dit protocol definieert reguliere communicatiepatronen en data-uitwisseling tussen agents, gecoördineerd door de Agent Controller.

## Kernprincipes
1. **Gestructureerde Communicatie:** Alle communicatie verloopt via de Agent Controller.
2. **Duidelijke Input/Output Schema's:** Agents ontvangen en produceren data die voldoen aan gedefinieerde JSON-schema's (gespecificeerd in hun `.md` definities).
3. **Traceerbaarheid:** Elke interactie moet traceerbaar zijn naar de `run_id` of `task_id` en de betrokken agents.
4. **Context Bewaring:** Relevante informatie moet worden doorgegeven via de Agent Controller, en opgeslagen door de Memory Keeper.

## Communicatieworkflow (Voorbeeld: Ideation Cycle)

Lexi -> **Agent Controller** (Missie Start)
    -> **Agent Controller** → Scout (Opdracht: Ruwe kansen genereren)
        → Scout Output → **Agent Controller**
            → **Agent Controller** → Web Researcher (Opdracht: Bronnen verzamelen voor kans X)
                → Web Researcher Output → **Agent Controller**
                    → **Agent Controller** → Market Validator (Opdracht: Marktdata analyseren)
                        → Market Validator Output → **Agent Controller**
                            → **Agent Controller** → Monetization Validator (Opdracht: Geldroutes onderzoeken)
                                → Monetization Validator Output → **Agent Controller**
                                    → **Agent Controller** → Critic (Opdracht: Validatie op risico's/feedback)
                                        → Critic Output → **Agent Controller**
                                            → **Agent Controller** → Strategist (Project selectie)
                                                → Strategist Output → **Agent Controller**
                                                    → **Agent Controller** → Builder (Bouw opdracht)
                                                        → Builder Output → **Agent Controller**
                                                            → **Agent Controller** → QA Agent (Verificatie Output)
                                                                → **Agent Controller** → DevOps Guard / Finance Guard (Veiligheids-/Kostenchecks)
                                                                    → **Agent Controller** (Finaliseert run, rapporteert aan Lexi/Memory)
                                                                        → Memory Keeper (Slaat learnings op)
                                                                        → Secretary (Logt alles)

## Gedragsregels voor Agenten
*   **Antwoord aan Controller:** Agents moeten binnen een redelijke tijd reageren op de Controller.
*   **Output Format:** Output moet strikt voldoen aan de input schema's gespecificeerd in de `.md` rolbestanden.
*   **Foutmeldingen:** Fouten moeten duidelijk worden gerapporteerd aan de Controller, inclusief context en oorzaak.
*   **Proactieve Communicatie:** Indien een agent een probleem ondervindt dat de workflow blokkeert, moet dit direct aan de Controller worden gemeld.

## Toegestane Tools voor Communicatie:
*   Agent Controller gebruikt `delegation` om taken te wijzen.
*   Agents sturen output terug aan de Controller via de Hermes framework-mechanismen.
*   Memory Keeper gebruikt `memory` tool voor opslag.
*   Secretary gebruikt `write_file` om verslagen te maken.