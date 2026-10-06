# Pairwise Paper Evaluator

A structured, evidence-linked AI-assisted workflow for comparing research papers and manuscripts.

## What it does

Pairwise Paper Evaluator helps researchers compare manuscripts more systematically, identify relative strengths and weaknesses, surface decision hinges, and prioritize revisions. Each comparison links its judgment to explicit evidence locations and a structured result.

## Why it may help researchers

Single overall assessments can hide which evidence drove a close judgment. Pairwise comparisons make the trade-offs between two manuscripts easier to inspect, discuss, and revisit. Evidence cards and explicit decision hinges help focus review; selected position reversals provide a stability check during development.

This is a research decision-support workflow, not a substitute for expert peer review.

## How it works

1. Define the comparison purpose and a fixed reference set.
2. Read each manuscript and freeze a concise evidence card.
3. Compare specified pairs under a shared rubric and record evidence locators.
4. Note the decision hinge, confidence, near-tie status, and any validity concern.
5. Reverse selected pairs as stability audits, then validate and summarize the structured results.

A reversal is an audit, not an additional vote. Aggregates summarize only the specified comparison set.

## Quick start

Requires Python 3.10+; no third-party packages are needed.

```bash
python scripts/validate_results.py examples/synthetic_example/results.json
python scripts/aggregate_results.py examples/synthetic_example/results.json
python -m unittest discover -s tests -v
```

For a real project, use manuscripts you may lawfully access, assign neutral IDs, record exact page/section/table locators, and retain source documents locally. See [Quickstart](docs/QUICKSTART.md).

## Explore the method and evidence

- [Method](docs/METHOD.md) — evidence cards, validity gate, pairwise edges, and audits.
- [Validation evidence](docs/VALIDATION.md) — observed stability checks and their scope.
- [Limitations](docs/LIMITATIONS.md) — known sensitivities and interpretation boundaries.

## Repository map

- `prompts/EVALUATOR_PROMPT.md` — reusable evaluator instruction.
- `schemas/pairwise_result.schema.json` — structured result schema.
- `scripts/` — dependency-free validation and aggregation utilities.
- `examples/synthetic_example/` — invented example data.
- `tests/` — local release tests.

## Citation and license

See [CITATION.cff](CITATION.cff). This release is licensed under the [MIT License](LICENSE).
