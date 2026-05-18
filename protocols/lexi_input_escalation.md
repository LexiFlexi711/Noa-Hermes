# Protocol: lexi_input_escalation

## Doel
Dit protocol definieert de procedure voor wanneer de Agent Controller of een agent directe input, goedkeuring of beslissing van Lexi nodig heeft.

## Kernprincipes
1.  **Lexi is de Finale Beslisser:** Alle kritieke beslissingen, strategische richtingen, en potentieel risicovolle acties moeten uiteindelijk door Lexi worden goedgekeurd.
2.  **Gedefinieerde Escalatiepunten:** Er zijn specifieke momenten waarop Lexi's input VERPLICHT is.
3.  **Duidelijkheid in Vraagstelling:** De vraag aan Lexi moet helder, specifiek, en voorzien van alle nodige context zijn.
4.  **Traceerbaarheid:** Alle interacties met Lexi moeten worden gelogd door de Secretary.

## Escalatieprocedures

**1. Wanneer escalatie naar Lexi nodig is:**
*   **Strategische Beslissingen:**
    *   Goedkeuring van het algemene projectdoel of missie.
    *   Goedkeuring van grote workflowwijzigingen.
    *   Goedkeuring van nieuwe agentrollen die het team significant veranderen.
*   **Financiële Beslissingen:**
    *   Goedkeuring van kosten die buiten de vooraf gedefinieerde budgetten vallen.
    *   Goedkeuring van het activeren van betaalde API's of subscriptions.
*   **Risicovolle Acties:**
    *   Implementatie van wijzigingen die systeemstabiliteit kunnen beïnvloeden (bv. grote deployments).
    *   Goedkeuring van acties met potentieel significante impact (bv. 'push' naar productie, 'delete' van data).
*   **Onzekerheid/Ambiguïteit:**
    *   Wanneer `Lexi_fit` score onduidelijk is of expliciet Lexi's feedback vereist.
    *   Wanneer de Agent Controller de output niet kan valideren en de volgende stap onduidelijk is.
    *   Bij onverwachte fouten of onzekerheden die niet automatisch afgehandeld kunnen worden.
*   **Specifieke Agent Rollen:**
    *   `Critic` op `needs_lexi_input: true` voor kansen die een directere afstemming vereisen.
    *   `Experiment Strategist` bij selectie van experimenten die hoge investering of risico inhouden.
    *   `Agent Controller` wanneer een agent zijn contract breekt en dit niet automatisch kan worden afgehandeld.

**2. Proces van Escalatie:**
*   **Agent Rapporteert aan Controller:** Een agent (of de Controller zelf) identificeert een punt dat Lexi's input vereist.
*   **Controller Formuleert Vraag:** De Agent Controller stelt een duidelijke, bondige vraag met relevante context uit de huidige run/taak. Dit wordt genoteerd in de `lexi_report` van de Controller of direct aan Lexi gepresenteerd via het Hermes platform.
*   **Secretary Logt Escalatie:** De Secretary registreert de escalatie in de vergadernotulen.
*   **Lexi Beslist:** Lexi geeft haar feedback, goedkeuring of instructie.
*   **Controller Verwerkt Lexi's Input:** De Agent Controller integreert Lexi's beslissing in de workflow en stuurt de agents aan.
*   **Memory Keeper Slaat Op:** De beslissing en de context worden opgeslagen.

## Gedragsregels voor Escalatoren:
*   **Wees Concreet:** Vraag niet zomaar om feedback, maar specificeer wat je nodig hebt.
*   **Lever Context:** Geef alle relevante informatie mee om Lexi te helpen bij haar beslissing.
*   **Respecteer Tijd:** Escaleer alleen wanneer absoluut noodzakelijk.

## Toegestane Tools voor Escalatie:
*   Agent Controller: Gebruikt het Hermes platform om directe vragen aan Lexi te stellen.
*   Secretary: Logt escalatie in vergadernotulen.
*   Memory Keeper: Slaat beslissingen op.