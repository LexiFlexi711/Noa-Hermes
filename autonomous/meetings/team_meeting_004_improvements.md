# TEAM MEETING 004 — VERBETERPUNTEN & SKILL-GOVERNANCE

## Doel
Analyseer het huidige agententeam, hun rollen, workflows en identificeer verbeterpunten die kunnen leiden tot hogere betrouwbaarheid en efficiëntie. Stel concrete acties voor voor de Agents Controller en Lexi.

## Aanwezige Rollen (Huidige Staat)

**1. Direct onder Lexi:**
*   **Agent Controller (Noa):** Orchestreert het team, monitort workflow, verdeelt taken, controleert output, popt gevaarlijke acties, schakelt QA/DevOps/Finance Guards in, rapporteert aan Lexi.
*   **Hermes Updater:** Onderzoekt systeemverbeteringen, verzamelt bronnen, analyseert procedures, stelt verbeteracties voor.
*   **Skills Agent:** Monitort structurele fouten, herhaalt problemen, rommelige workflows en onbetrouwbare rapportage. Converteert dit naar voorstellen voor skills, checklists of protocollen.

**2. Uitvoerend Team (onder Agent Controller):
*   **Secretary:** Leidt vergaderingen, bewaakt agenda, noteert gesprekken, beslissingen, conflicten, actiepunten. Maakt verslagen (MD/JSON).
*   **Scout (idea_scout):** Zoekt ruwe kansen, ideeën, signalen.
*   **Web Researcher (web_researcher):** Verzamelt feitelijke bronnen met absolute paden/URL's.
*   **Market Validator (market_validator):** Valideert vraag, concurrentie op basis van bronnen.
*   **Monetization Validator (monetization_validator):** Onderzoekt geldroutes met bewijs, benoemt risico's.
*   **Critic (critic):** Valideert kansen op zwaktes, risico's, bronkwaliteit, haalbaarheid. Geeft scores & go/no-go advies. Rapporteert `needs_lexi_input`.
*   **Experiment Strategist (experiment_strategist):** Kiest max 1 tesetbaar experiment uit gevalideerde input, definieert plan.
*   **Builder (builder):** Bouwt minimale assets voor experiment conform plan en `allowed_paths`.
*   **QA Agent (qa_agent):** Controleert agent-output op kwaliteit, schema, rolgrenzen, bronplicht, veiligheid, bruikbaarheid. Verifieert toolgebruik en paden.
*   **Python Mentor (python_mentor):** Begeleidt Lexi in Python leren, koppelt kennis aan projecten.
*   **Memory Keeper (memory_keeper):** Bewaart lessen, patronen, beslissingen, fouten. Traceert data naar bronnen.
*   **DevOps Guard (devops_guard):** Bewaakt systeem-, Git-, pad-, secret-risico's. Blokkeert risicovolle acties.
*   **Finance Guard (finance_guard):** Bewaakt kosten, verbruik, financiële risico's.

---