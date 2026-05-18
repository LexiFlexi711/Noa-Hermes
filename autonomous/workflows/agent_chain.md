# Workflow: agent_chain

## Doel

Definieert de standaard ketting van agents voor kansvalidatie en experimentuitvoering.
De Agent Controller volgt deze ketting tenzij Lexi een andere volgorde opgeeft.

## Primaire ketting — Kansvalidatie

```
Scout → Researcher → Market Validator → Monetization Validator → Critic → Strategist → Builder → QA Agent
```

### Per stap

| Stap | Agent | Input van | Output naar | Doel |
|---|---|---|---|---|
| 1 | Scout | Controller | Researcher | Ruwe kansen genereren |
| 2 | Researcher | Scout | Market Validator | Kansen onderbouwen met bronnen |
| 3 | Market Validator | Researcher | Monetization Validator | Vraag & concurrentie valideren |
| 4 | Monetization Validator | Market Validator | Critic | Geldroutes onderzoeken |
| 5 | Critic | Monetization Validator | Strategist | Totaalvalidatie & go/no-go |
| 6 | Strategist | Critic | Builder | Max 1 experiment selecteren |
| 7 | Builder | Strategist | QA Agent | Minimale assets bouwen |
| 8 | QA Agent | Builder | Controller | Output valideren |

### Stopcondities in de ketting

- Elke agent mag output markeren als `failed` → Controller escaleert naar Lexi.
- Critic mag `no_go` adviseren → ketting stopt, Controller rapporteert aan Lexi.
- Strategist mag besluiten: geen geldig experiment → ketting stopt.
- Bij `LOOP_RISK` trigger → Controller stopt de hele run (zie `autonomous/protocols/anti_loop_protocol.md`).

## Ondersteunende agents (parallel, op afroep)

| Agent | Rol | Wanneer ingeschakeld |
|---|---|---|
| Secretary | Notulist | Tijdens meetings, op vraag van Controller |
| Memory Keeper | Leerregistratie | Na elke run, bij fouten |
| DevOps Guard | Veiligheidscheck | Voor elke write/push/install |
| Finance Guard | Kostencheck | Bij API-gebruik, tokens, credits |
| Python Mentor | Leercoach | Op vraag van Lexi |
| Hermes Updater | Systeemverbetering | Periodiek, op vraag van Lexi |
| Skills Agent | Protocol/skill beheer | Bij herhaalde fouten, op vraag van Lexi |
| Producer | Content creatie | Na goedgekeurd experimentplan |

## Protocollen per fase

- **Alle fases**: `autonomous/protocols/anti_loop_protocol.md`
- **Toolgebruik**: `protocols/tool_usage_policy.md`
- **Bronplicht**: `protocols/source_verification.md`
- **Padbeheer**: `protocols/path_management.md`
- **Outputvalidatie**: `protocols/output_validation.md`
- **Agentcommunicatie**: `protocols/agent_communication.md`
- **Escalatie naar Lexi**: `protocols/lexi_input_escalation.md`
