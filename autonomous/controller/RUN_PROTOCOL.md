# RUN PROTOCOL - NOA Opportunity Engine

Dit protocol beschrijft de stappen voor het uitvoeren van een run, van initiatie tot afronding.

## 1. Run Initiatie
- **Trigger:** Start van een nieuwe run door controller of timer.
- **Controller:** Leest `state.json` om de lopende fase en `next_action` te bepalen.
- **Log Start:** Maak een nieuwe entry aan in `runs/` met timestamp en run ID.

## 2. Scout Fase
- **Doel:** Genereren van ruwe kansen.
- **Input:** Algemene zoekcriteria, of specifiekere directieven van Controller (afhankelijk van `state.json`).
- **Actie:** Scout identificeert potentiele bijverdiensten of passieve inkomensmogelijkheden.
- **Output:** Ruwe kansen worden opgeslagen in `autonomous/opportunities/raw/`. Elk item krijgt een unieke ID.

## 3. Research & Market Analyse Fase
- **Doel:** Bewijs verzamelen, vraag & concurrentie analyseren.
- **Input:** Ruwe kansen uit `raw/`.
- **Actie:** Researcher verzamelt bewijs en bronnen (-> `evidence/sources/`, `evidence/notes/`). Market analyseert vraag en concurrentie.
- **Output:** Verrijkte kansen met bewijs en analyse opslaan in `autonomous/opportunities/researched/`.

## 4. Score & Critic Fase
- **Doel:** Objectieve score toekennen en kansen kritisch beoordelen.
- **Input:** Onderzochte kansen uit `researched/`.
- **Actie:** Critic analyseert grondig op betrouwbaarheid, risico's, en logische fouten. Scouters (demand, competition, buildability, monetization, Lexi_fit, speed_to_test) geven scores.
- **Output:** Gecorrigeerde/bevestigde scores worden opgeslagen in `autonomous/opportunities/scored/`. Kans die Critic niet doorstaat, wordt gemarkeerd als 'rejected'.

## 5. Strategist Fase
- **Doel:** Bepalen welke kans doorgaat naar experiment.
- **Input:** Gescoorde kansen uit `scored/`.
- **Actie:** Strategist selecteert maximaal één kans met de hoogste potentie en voldoet aan 'Hard Rules'.
- **Output:** Geselecteerde kans die doorgaat naar experiment wordt opgeslagen in `autonomous/opportunities/selected/`.

## 6. Builder Fase
- **Doel:** Een klein, testbaar experiment definiëren.
- **Input:** Geselecteerde kans uit `selected/`.
- **Actie:** Builder definieert de experiment-setup, hypothese, en testcriteria. NIET de volledige oplossing bouwen.
- **Output:** Experimentdefinitie opslaan in `autonomous/experiments/active/`.

## 7. Experiment Executie & Monitoring
- **Doel:** Het experiment uitvoeren en data verzamelen.
- **Input:** Experimentdefinitie uit `active/`.
- **Actie:** Controller initieert de test (simulatie of eenvoudige lokale trigger). Verzamel resultaten.
- **Output:** Experimentresultaten/data opslaan in `autonomous/experiments/completed/` of `autonomous/experiments/failed/`.

## 8. Afronding & Rapportage
- **Doel:** Run loggen, state updaten, en resultaten presenteren.
- **Controller:**
    - Compileert finale `run_log` entry met alle outputs en resultaten.
    - Update `state.json`: `runs_completed`, `last_run`, `accepted_opportunity`/`no_valid_opportunity`, `reasons`, `next_action`.
    - Schrijft definitieve `run_log` naar `runs/`.
- **DevOps:** Zorgt voor correcte logging en bestandshandling.

Dit protocol garandeert een gestructureerde en reproduceerbare uitvoering van elke kanszoek-cyclus.