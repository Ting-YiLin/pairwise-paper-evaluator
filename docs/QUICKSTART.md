# Quickstart

This dependency-free workflow supports manual or AI-assisted comparisons. Use only manuscripts you are allowed to access; keep the documents on your own machine.

1. **Set the question.** Specify whether you are comparing full-text contribution, an editorial front door, a revision, or a target against a fixed reference set.
2. **Assign neutral IDs.** Store lawful source documents locally and use IDs such as P01 and P02 in the comparison file.
3. **Build evidence cards.** Read each paper, record the fields in [METHOD](METHOD.md), and freeze the cards before pairwise review.
4. **Evaluate edges.** Use the same rubric for each pair. Record the decision hinge, confidence, near-tie status, validity gate, and page/section/table locators. The prompt in `prompts/EVALUATOR_PROMPT.md` is a starting point.
5. **Audit selected reversals.** Swap left and right for selected low-confidence pairs. Preserve the pair ID and record `position_variant: reversed`.
6. **Validate and summarize.** Export JSON following the schema. Run:

   ```bash
   python scripts/validate_results.py path/to/results.json
   python scripts/aggregate_results.py path/to/results.json
   ```

The aggregate uses original edges only. Reversal audits check stability and are never additional votes. Review all output against the underlying evidence before using it in a decision.
