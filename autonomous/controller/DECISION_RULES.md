# DECISION RULES - NOA Opportunity Engine

Deze regels sturen de besluitvorming binnen de NOA Opportunity Engine, met Lexi als ultieme beslisser.

## 1. Lexi's Beslismomenten
Lexi's goedkeuring is vereist in de volgende gevallen:
- **Selectie van een kans voor experiment:** Na de scoring en kritische analyse, presenteert de Controller de beste kans(en) aan Lexi voor finale selectie om de builder de opdracht te geven.
- **Goedkeuring van Experiment Resultaten:** Na afronding van een experiment, met de verzamelde data en analyse, moet Lexi beslissen of het experiment succesvol is en verdere ontwikkeling (of opschaling) rechtvaardigt.
- **Afronding van een Kans:** Als een kans na onderzoek of experiment duidelijk niet levensvatbaar is (`no_valid_opportunity`), of juist zeer veelbelovend, is Lexi's akkoord nodig voor de volgende strategische stap (bv. stoppen, doorgaan).
- **Kritieke Systeemwijzigingen:** DevOps kan wijzigingen aan systemen monitoren of voorstellen, wat Lexi's goedkeuring vereist.

## 2. Agent-Specifieke Beslissingen (binnen richtlijnen)
- **Scout:** Identificeert kansen op basis van brede input. Kan zelfstandig filteren op basis van 'Hard rules'.
- **Researcher/Market:** Verzamelt informatie en analyseert data. Kan zelfstandig doorvragen indien bewijs onduidelijk is.
- **Monetization:** Onderzoekt geldroutes. Kan zelfstandig verschillende modellen simuleren binnen de kans.
- **Critic:** Heeft de macht om een kans te blokkeren op basis van de 'Hard rules' en de gedefinieerde scorecriteria. Een 'nee' van Critic is bindend voor de verdere doorloop van die specifieke kans.
- **Strategist:** Selecteert op basis van scores de beste kans(en) voor experiment. Maximaal één tegelijk.
- **Builder:** Definieert experimenten conform de geslecteerde kans. Kan geen volledige oplossingen bouwen.
- **Memory:** Slaat patronen en resultaten op.
- **DevOps:** Monitort systeemgezondheid en risico's. Kan proactief waarschuwen of actie ondernemen bij kritieke risico's (altijd loggen en aan Lexi rapporteren).

## 3. Score-gebaseerde Beslissingen
De Controller gebruikt de scores (demand, competition, buildability, monetization, Lexi_fit, speed_to_test) om kansen te rangschikken. Een kans moet minimaal een bepaalde drempelscore behalen in de meeste categorieën (gedefinieerd door Controller/Lexi) om door te gaan naar de Strategist fase.

## 4. 'Hard Rules' Precedent
De 'Hard rules' (bv. Kans zonder bron = score 0, geen geldclaim zonder bewijs) hebben altijd voorrang op andere scores. Een kans die een harde regel schendt, wordt direct afgewezen in de Critic/Scoring fase.

Dit protocol zorgt voor een duidelijke hiërarchie en controle, met Lexi als de finale autoriteit.