Lexi's doelen & voorkeuren:
- Ultieme doel: Noa autonoom maken als een JARVIS-achtige agent (voice, proactief, smart home, visuele input).
- Wil Python leren via hands-on mentoring, project-gebaseerd, geen schoolse cursus.
- GitHub: username is LexiFlexi711 (NIET LexiMaatje), repo Noa-Hermes wordt het thuis voor Noa's brein.

Hermes baseline:
- Hermes draait met deepseek/deepseek-v4-pro als hoofdmodel, OpenRouter als provider.
- Ollama Cloud faalt met gemma3:4b als Hermes-agentmodel (HTTP 500 bij volledige context).
- OpenRouter blijft hoofdroute voor Hermes.
§
OpenClaw model-quirk: deepseek/deepseek-chat-v3-0324 op OpenRouter geeft letterlijk "NO_REPLY" (5 output tokens) terug na tool calls in OpenClaw-agentcontext. Rechtstreekse API-calls naar het model werken wel, maar zodra OpenClaw context/system prompt meestuurt met tool history, weigert het model. NIET opnieuw proberen als OpenClaw-model. Gemini-flash-lite werkt wel. Vervangen op 2026-05-14.
§
Server power fix: lightdm suspend-pogingen gestopt door gsd-power plugin te disablen via Hidden=true in XDG autostart. Suspend.target blijft gemasked als vangnet.
§
NOA-Reign (Lexi's AI-agent werkplaats):
- GitHub: LexiFlexi711/NOA-reign (private), LexiFlexi711/Noa-Hermes (public, ~/Noa-Hermes)
- Lokale NTFS kopie: /mnt/otherdrive1/dataLexi/LexiProjects/NOA-Reign
- GitHub clone: /tmp/NOA-reign (voor inspectie)
- Crypto tradebot: 59 Python files, candle_battle_reader.py (2410 regels) als kern
- Filosofie: "candles are the primary truth" — geen indicatoren, elke candle als buyer/seller battle
- Deceptive detection: body color zegt niks, close position bepaalt winnaar
- 4 tijdskaders: 1D (macro), 4H (structuur), 1H (setup), 15M (battle)
- Trading bible PDF als basis. Lexi bedacht theorie, ChatGPT prompts, Claude Code schreef code
- Validatie: bot output vs echte charts (112 screenshots), iteratief fouten herstellen
- Lexi's prioriteit: eerst output 100% correct naar haar gevoel, dan pas cijfers/monetisatie
- Paper-only, Kraken exchange, ETH/EUR focus
§
The main persistent path for the crypto tradebot code is /mnt/otherdrive1/dataLexi/LexiProjects/NOA-Reign/projects/crypto-tradebot/.
§
ECGT was mentioned during the Git/Second Brain workflow, but Lexi has not yet approved a final meaning or usage rule. Do not use ECGT automatically until Lexi explicitly defines it.
§
Initiating self-improvement process: Analyzing current task flow against defined roles (Claude Code: delegates, Hermes: executes, Lexi: Owner/Final Decision Maker). Goal is to identify specific areas for optimization to ensure strict adherence to the principle "Claude Code delegates. Hermes executes. Lexi decides." This plan and findings will be documented with the "ECGT" tag.
§
User emphasizes the 'ECGT' principle (Eerst Controleren, Daarna Garanderen, Transparant Afhandelen) as a core operational standard for all commitments and actions, ensuring reliability and transparency.
§
User expects adherence to the defined agent roles of Director (Claude Code), Executor (Hermes), and Owner/Final Decision Maker (Lexi). The principle 'Claude Code delegates. Hermes executes. Lexi decides.' must guide task execution and interaction.