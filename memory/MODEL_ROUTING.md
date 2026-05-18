# Model Routing Plan

## Hoofdmodel (default)
deepseek/deepseek-v4-flash — OpenRouter

Heavy model (poortwachter): deepseek/deepseek-v4-pro — OpenRouter — enkel voor zware/riskante taken

## Heavy model — verplicht voor

| Agent | Reden |
|---|---|
| Agent Controller | Complexe governance, RUN_STATE, anti-loop |
| QA Agent | Outputvalidatie, contractbreuk detectie |
| Critic | Multi-factor go/no-go weging |
| Strategist | Experimentselectie uit gevalideerde data |
| Hermes Updater | Systeemonderzoek, bronnen vergelijken |
| Skills Agent | Foutclustering, protocolontwerp |
| Lexi-escalatie | Altijd heavy — menselijke beslispunten |

## Light model — toegestaan voor

| Agent | Reden |
|---|---|
| Secretary | Gestructureerd output, weinig redenering |
| Scout | Brainstorm, geen validatie |
| Researcher | Tools doen werk, model structureert |
| Market Validator | Checkt bronnen oppervlakkig |
| Monetization Validator | Checkt bestaande modellen |
| Builder | Uitvoerend, volgt exacte build_task |
| Producer | Creatief maar voorspelbaar |
| Memory Keeper | Registratie, geen oordeel |
| DevOps Guard | Alleen read-only checklist; heavy bij shell/write/service/git risico |
| Finance Guard | Alleen simpele kostenschatting; heavy bij providerkeuze, abonnement, recurring cost of betaalimpact |

## Nooit naar light model

- Systeemfile wijzigingen (configs, protocols, agents/)
- Secrets/tokens/env handling
- Git push/commit/delete
- Provider/model wijzigingen
- Install/apt/pip commando's
- Scope-overgang READ_ONLY → WRITE
- RUN_STATE wijzigingen
- Anti-loop override beslissingen
- Alles in WAITING_FOR_LEXI phase

## Bescherming light model

1. Scope-lock: light model → automatisch READ_ONLY of AUDIT_ONLY
2. Tool-filter: beperkte toolset, write alleen in allowed_paths
3. Anti-loop guard: action_count > 5 of repeated_tool_count → harde stop + escalatie naar heavy

## Model-router regels

```
IF task.scope in [SYSTEM_WRITE, CONFIG_CHANGE, SECRET_HANDLING, GIT_OPERATION]
  → heavy

IF task.agent in [controller, qa_agent, critic, strategist, hermes_updater, skills_agent]
  → heavy

IF task.agent in [secretary, scout, researcher, market, monetization, builder, producer, memory, devops, finance]
  → light (default)

IF task.evidence_required == true AND task.agent.model_tier == light
  → light mag uitvoeren, output door heavy QA gevalideerd

IF task.phase == WAITING_FOR_LEXI
  → geen enkel model, harde stop

IF run_state.loop_risk_triggered
  → heavy, ongeacht agent
```

## Te wijzigen config

- `~/.hermes/config.yaml` — model-mapping per agent
- `autonomous/agents/controller.md` — RUN_STATE veld `model_tier`
- `protocols/tool_usage_policy.md` — tool-restricties per model-tier
