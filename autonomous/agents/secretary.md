# TEAM MEETING 002 — Teamanalyse

## Doel
Analyseer of het team logisch, bruikbaar en veilig is opgebouwd.

## Aanwezige rollen
Maak onderscheid tussen:
1. Direct onder Lexi:
   - Agent Controller
   - Hermes Updater

2. Uitvoerend team:
   - Secretary
   - Scout
   - Researcher
   - Market Validator
   - Monetization Validator
   - Critic
   - Strategist
   - Builder
   - QA Agent
   - Python Mentor
   - Memory Keeper
   - DevOps Guard
   - Finance Guard

## Iteratie 1 — Wat doet elke agent?

Om het team te analyseren, beschrijft elke agent hier zijn rol, verantwoordelijkheden, beperkingen en samenwerkingen. Deze zijn gebaseerd op de `.md` bestanden die we eerder hebben aangemaakt en mogelijk nog moeten verfijnen.

**Agent Controller:**
*   **Bestandsnaam:** `/home/sjoe/Noa-Hermes/autonomous/agents/controller.md`
*   **Bedrijfsrol:** Operational Lead / Team Controller / Agent Orchestrator.
*   **Hoofdtaak:** Orchestreert, monitort en optimaliseert het agententeam.
*   **Mag doen:** Taken verdelen, output beoordelen, agents blokkeren, runs stoppen, verbeteringen voorstellen, Lexi om beslissing vragen, rapporten schrijven.
*   **Mag niet:** Finaal beslissen, business-runs starten zonder opdracht, content maken, geldclaims, code bouwen, webresultaten verzinnen, tools installeren, provider/model wijzigen, Git push, delete, secrets openen, publicatie, trading.
*   **Input:** Missie van Lexi, teamstatus, learnings, agent-outputs, Lexi context.
*   **Output:** Taken-delegatie, rapporten aan Lexi.
*   **Samenwerking:** Coördineert alle agents, werkt met Secretary en Memory Keeper, escaleert naar Lexi.

**Hermes Updater:**
*   **Bedrijfsrol:** Internal Agent Improvement Researcher / Hermes Improvement Officer.
*   **Hoofdtaak:** Zoekt naar verbeteringen voor Hermes, Noa-Hermes en het agent-team.
*   **Mag doen:** Verbeteringen zoeken, bronnen verzamelen, workflows vergelijken, problemen koppelen aan oplossingen, voorstellen doen.
*   **Mag niet:** Code aanpassen, config wijzigen, tools installeren, secrets openen, Git push, etc. (enkel adviseren).
*   **Input:** `research_question`, `target_system`, `sources_to_scan`, `known_problem`.
*   **Output:** Verbeteringsvoorstellen, risico's, implementatiecomplexiteit.
*   **Samenwerking:** Werkt onder Lexi's opdracht, rapporteert aan Controller.

**Secretary:**
*   **Bestandsnaam:** `/home/sjoe/Noa-Hermes/autonomous/agents/secretary.md`
*   **Bedrijfsrol:** Meeting Secretary / Notulist / Vergaderleider.
*   **Hoofdtaak:** Leidt vergaderingen, bewaakt agenda, noteert gesprekken, beslissingen, actiepunten.
*   **Mag doen:** Structureren, spreekvolgorde, vragen herhalen, antwoorden samenvatten, onvolledige antwoorden markeren, actiepunten/beslissingen/open vragen noteren, verslag schrijven (MD/JSON).
*   **Mag niet:** Kansen kiezen, research doen, strategie bepalen, geldroutes voorstellen, bouwen, agents verbeteren, finale beslissingen nemen, discussie manipuleren, inhoud verzinnen.
*   **Input:** `meeting_id`, `meeting_title`, `output` voor Lexi.
*   **Output:** Leesbaar verslag (MD), machineleesbare notulen (JSON).
*   **Samenwerking:** Werkt onder Agent Controller tijdens vergaderingen.

**Scout Agent:**
*   **Bedrijfsrol:** Idea Generator / Opportunity Identifier.
*   **Hoofdtaak:** Zoekt ruwe kansen, ideeën en signalen.
*   **Mag doen:** Genereert ruwe kansen, groepeert per type, markeert vermoedens, stuurt door naar Researcher.
*   **Mag niet:** Kans goedkeuren, geldclaim, ROI, content maken, experiment kiezen, bouwen, publiceren.
*   **Input:** `mission`, `constraints`.
*   **Output:** Ruwe kansen.
*   **Samenwerking:** Stuurt input naar Agent Controller voor routing naar Researcher.

**Web Researcher:**
*   **Bedrijfsrol:** Factual Source Collector.
*   **Hoofdtaak:** Verzamelt feitelijke bronnen (web, lokale bestanden) voor kansen.
*   **Mag doen:** Zoekt live bronnen, laadt plugins, geeft bronnen met details, controleert aansluiting, rapporteert webfalen.
*   **Mag niet:** Geldclaims, content maken, strategie kiezen, bron verzinnen.
*   **Input:** `research_id`, `query`, `required_sources`.
*   **Output:** Feitelijke bronnen met details.
*   **Samenwerking:** Ontvangt opdracht van Controller, levert output aan Market Validator/Critic.

**Market Validator:**
*   **Bedrijfsrol:** Market Intelligence Analyst.
*   **Hoofdtaak:** Valideert vraag, concurrentie, marktsignalen op basis van bronnen.
*   **Mag doen:** Onderzoekt vraag/concurrentie, scoort met bewijs, geeft score 0 bij ontbrekende bronnen.
*   **Mag niet:** Kans kiezen, monetization routes verzinnen, ROI, aannames als feiten.
*   **Input:** `opportunity_id`, `title`, `description`, `target_audience`, `research_sources`.
*   **Output:** Marktvalidatie met scores.
*   **Samenwerking:** Gebruikt output van Researcher.

**Monetization Validator:**
*   **Bedrijfsrol:** Business Model Analyst.
*   **Hoofdtaak:** Onderzoekt concrete geldroutes voor een kans. Vereist bewijs, benoemt risico's.
*   **Mag doen:** Zoekt hoe geld verdiend kan worden, vereist bewijs, onderscheidt directe/indirecte monetization.
*   **Mag niet:** ROI-percentages, omzetvoorspelling, aankopen, abonnementen, trading.
*   **Input:** `opportunity_id`, `title`, `description`, `market_evidence`.
*   **Output:** Geldroutes, risico’s, afhankelijkheden.
*   **Samenwerking:** Gebruikt input van Market Validator.

**Critic:**
*   **Bedrijfsrol:** Risk Assessor / Validation Specialist.
*   **Hoofdtaak:** Valideert kansen op zwaktes, risico’s, bronkwaliteit, haalbaarheid.
*   **Mag doen:** Fouten detecteren, afkeuren bij ontbrekende bronnen, scores geven, risico’s benoemen, go/no-go advies geven.
*   **Mag niet:** Kansen kiezen, monetization routes bedenken (enkel reviewen), experimenten kiezen, bouwen, finale beslissingen nemen.
*   **Input:** Outputs van voorgaande validatie agents.
*   **Output:** `status`, `decision_advice`, `scores`, `needs_lexi_input` (incl. Lexi_fit details), `failure_reasons`, `risks`, `monetization_option_reviewed`, `critic_notes`.
*   **Samenwerking:** Ontvangt input van Market, Monetization, Researcher. Geeft output aan Strategist. Gebruikt Lexi_fit input via Controller.

**Experiment Strategist:**
*   **Bedrijfsrol:** Product Manager / Experiment Designer.
*   **Hoofdtaak:** Kiest max 1 testbaar experiment uit gevalideerde input. Zet info om naar testplan.
*   **Mag doen:** Leest outputs (Scout, Researcher, Market, Monetization, Critic); kiest max 1 experiment; definieert doel/succesmeting/asset; bepaalt volgende agent.
*   **Mag niet:** Eigen bronnen verzinnen, content maken, code bouwen, publicatie, ROI, meerdere experimenten, investering zonder Lexi.
*   **Input:** Gevallideerde kansen, outputs.
*   **Output:** Experimentplan.
*   **Samenwerking:** Ontvangt input van Critic; stuurt output naar Builder.

**Builder:**
*   **Bedrijfsrol:** Minimal Viable Asset Creator.
*   **Hoofdtaak:** Ontwerpt/definieert experiment conform Strategist. Bouwt minimale assets.
*   **Mag doen:** Bestanden aanmaken (binnen mappen), scripts/templates/assets maken, technische haalbaarheid melden, output loggen.
*   **Mag niet:** Kansen kiezen, experimenten definiëren, geldclaim, publiceren, pushen, buiten scope werken.
*   **Input:** `experiment_id`, `opportunity_id`, `build_task`, `allowed_paths`, `forbidden_actions`, `expected_output`.
*   **Output:** Status, files_written, missing_requirements, risks, next_action.
*   **Samenwerking:** Ontvangt input van Strategist.

**QA Agent:**
*   **Bedrijfsrol:** Quality Assurance / Output Contract Checker.
*   **Hoofdtaak:** Controleert agent-output op kwaliteit, schema, rolgrenzen, bronplicht, veiligheid, bruikbaarheid.
*   **Mag doen:** Output afkeuren, schemafouten markeren, ontbrekende bronnen markeren, rolbreuk markeren, onbruikbare output markeren, verbeterpunten rapporteren.
*   **Mag niet:** Strategie kiezen, kansen kiezen, experiment selecteren, code bouwen, content maken, monetization route kiezen, systeemwijziging, finale beslissingen nemen.
*   **Input:** `target_agent_output`, `agent_type`, `expected_output_schema`, `role_contract`, `source_requirements`, `quality_requirements`.
*   **Output:** `qa_score`, `assessment_timestamp`, `passed`, `discrepancies`, `recommendations`, `next_step_advice`.
*   **Samenwerking:** Controleert output van alle output-genererende agents.

**Python Mentor:**
*   **Bedrijfsrol:** Technical Mentor / Learning Coach voor Lexi.
*   **Hoofdtaak:** Begeleidt Lexi in Python-leren, koppelt aan projecten.
*   **Mag doen:** Leerpaden ontwerpen, concepten demonstreren, feedback geven op code, linken aan projecten, helpen bij begrip, kansen voor toepassing identificeren.
*   **Mag niet:** Zelf code bouwen voor Lexi, projecten overnemen, financieel advies, tools laten installeren zonder noodzaak.
*   **Input:** `lexi_learning_goal`, `current_project_context`, `lexi_code_snippet`, `lexi_questions`.
*   **Output:** Leerplan, codefeedback, uitleg, volgende stap, progress note.
*   **Samenwerking:** Werkt direct met Lexi, rapporteert aan Controller.

**Memory Keeper:**
*   **Bedrijfsrol:** Knowledge Steward / Pattern Repository.
*   **Hoofdtaak:** Slaat lessen, patronen, beslissingen en fouten op.
*   **Mag doen:** Schrijft lessons learned, winning/rejected patterns, faalrecords, brongebruik, state-update suggesties, gebruikersvoorkeuren bijhouden. Traceerbaarheid garanderen.
*   **Mag niet:** Feiten verzinnen, conclusies zonder bron, oude fouten overschrijven, secrets opslaan, publiceren, Git push.
*   **Input:** `run_id`, `agent_outputs`, `accepted_patterns`, `rejected_patterns`, `failures`, `state_update_request`.
*   **Output:** Gestructureerde opslag van learnings en voorkeuren.
*   **Samenwerking:** Alle agents leveren input. Controller gebruikt output voor teamoptimalisatie.

**DevOps Guard:**
*   **Bedrijfsrol:** Security & Compliance Officer.
*   **Hooodtaak:** Bewaakt systeem-, Git-, pad-, secret-risico's. Controleert of acties veilig zijn.
*   **Mag doen:** Git-status checken, buiten paden controleren, secrets detecteren, risicovolle acties blokkeren, rapporteren.
*   **Mag niet:** Productiewijzigingen, push/delete/install/publicatie/trading, secrets tonen, .env/tokens kopiëren, Docker/Caddy/serverconfig wijzigen zonder Lexi.
*   **Input:** `task_id`, `proposed_action`, `target_paths`, `files_to_write`, `files_to_read`, `risk_context`.
*   **Output:** Veilig/onveilig rapport, blokkades.
*   **Samenwerking:** Controleert acties van de Controller en Builder.

**Finance Guard:**
*   **Bedrijfsrol:** Cost Analyst / Budget Monitor.
*   **Hoofdtaak:** Bewaakt kosten, verbruik, financiële risico's.
*   **Mag doen:** Controleren of actie geld kost, betaalde API's checken, kostenrisico inschatten, onbekende kosten markeren, Lexi's toestemming vragen.
*   **Mag niet:** Aankopen, abonnement activeren, API-key wijzigen, trading, omzet voorspellen, ROI-percentages, fake revenue.
*   **Input:** `task_id`, `proposed_action`, `providers`, `expected_usage`, `known_costs`, `unknown_costs`.
*   **Output:** Kosten- en budgetimpact rapport.
*   **Samenwerking:** Controleert acties die kosten met zich meebrengen.
