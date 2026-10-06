# Pairwise Paper Evaluator

A reproducible, AI-assisted workflow for structured comparisons between research manuscripts. It uses evidence cards, a scientific-validity gate, explicit pairwise decisions, and selected position-reversal audits to make review judgments easier to inspect and discuss.

This is a research and calibration aid. It does not measure objective paper quality, predict journal acceptance, or establish a universal ranking.

## What the workflow does

For each comparison, reviewers state which manuscript is stronger under a declared purpose and rubric, record the decision hinge and evidence locations, and note confidence and near-tie status. A separate validity gate records whether a central scientific concern limits the comparison. Reversing manuscript positions can audit whether the direction survives; it is an audit, not an extra vote.

## Five-step view

1. Define the comparison purpose and a fixed reference set.
2. Read each manuscript and freeze a concise evidence card.
3. Compare specified pairs using the same rubric and record locators.
4. Reverse selected low-confidence pairs as stability audits.
5. Validate the JSON and summarize only the local comparison set.

## Observed project evidence

In the frozen project records, 14 recorded position-reversal audits preserved the substantive direction (0 observed flips). These audits were not probability-sampled and do not estimate a general positional-bias rate. The project also recorded a meaningful cross-model disagreement on a boundary comparison, showing that near-tie judgments can depend on evaluator family.

## What this does not establish

- No human-expert ground truth or external criterion validity.
- No objective true-quality measure, universal ranking, journal percentile, or acceptance probability.
- No general positional-bias rate from the recorded audits.
- No independence among AI reviewers; correlated errors remain possible.
- Local aggregate summaries can depend on the reference set and grouping.

## Quickstart

Requires Python 3.10+; no third-party packages are needed.

```bash
python scripts/validate_results.py examples/synthetic_example/results.json
python scripts/aggregate_results.py examples/synthetic_example/results.json
python -m unittest discover -s tests -v
```

For a real project, use only manuscripts you may lawfully access, assign neutral IDs, record exact page/section/table locators, and retain source files locally. Start with [Quickstart](docs/QUICKSTART.md).

## Repository map

- `docs/METHOD.md` — comparison method and validity gate.
- `docs/VALIDATION.md` — evidence levels and current observations.
- `docs/LIMITATIONS.md` — scope and known failure modes.
- `prompts/EVALUATOR_PROMPT.md` — reusable evaluator instruction.
- `schemas/pairwise_result.schema.json` — result structure.
- `scripts/` — dependency-free validation and aggregation.
- `examples/synthetic_example/` — invented example data.

## Citation and license

See [CITATION.cff](CITATION.cff). The license is pending an owner decision; see [LICENSE_PENDING.md](LICENSE_PENDING.md).
