## Overview
Forecast Scenario Sensitivity Analysis helps you quantify how changes in key drivers (price, volume, costs, FX, interest rates, churn, etc.) affect outcomes such as revenue, EBITDA, cash flow, and valuation. Use it to test scenarios, identify value drivers, and prioritize actions under uncertainty.

## Who should use this
- Financial analysts and FP&A teams building and stress-testing forecasts
- Corporate development and treasury evaluating valuation and liquidity risk
- Business partners comparing plans, risks, and upside cases

## Prerequisites
- Access to the forecasting model with edit rights
- A validated baseline forecast (assumptions, time horizon, currency)
- Defined target metrics (e.g., Revenue, EBITDA, FCF, NPV)
- Mapped drivers to model logic (no broken links or circular references)
- Historical data and driver ranges or distributions
- Version control or a workspace for scenario copies

## Steps
1. Clarify the objective
   - Define the question (e.g., “What drives variance in FY revenue?”).
   - Select output metrics (KPIs) and time buckets (monthly/quarterly/annual).

2. Set the baseline
   - Load the latest approved forecast.
   - Lock the version and note key baseline values for chosen KPIs.

3. Select drivers and ranges
   - Choose 3–10 drivers with clear causal links to outputs.
   - For each driver, set:
     - Type: deterministic (single value/range) or stochastic (distribution).
     - Range: min/base/max or confidence interval.
     - Constraints: floors/ceilings, integer-only, sign limits.

4. Create scenarios
   - Base Case: unchanged baseline.
   - Upside/Downside: apply coherent, business-justified changes across drivers.
   - Edge/Stress: apply extreme but plausible shocks to test resilience.

5. Run one-way sensitivity
   - Vary one driver across its range; hold others constant.
   - Capture output changes; produce a sensitivity curve for each KPI.

6. Run two-way sensitivity (optional)
   - Select two interacting drivers (e.g., price and volume).
   - Create a grid of combinations; visualize impact heatmap on KPIs.

7. Generate a tornado chart
   - Rank drivers by their marginal impact on a target KPI over the set range.
   - Identify top value/risk contributors.

8. Run Monte Carlo (if available)
   - Assign distributions (e.g., normal for demand error, triangular for cost).
   - Set trials (e.g., 5,000–20,000) and random seed for reproducibility.
   - Review percentile bands (P10/P50/P90), probability of loss/covenant breach.

9. Compare scenarios
   - Use side-by-side KPI tables and variance waterfalls vs. baseline.
   - Attribute variance by driver and by time period.

10. Validate and document
    - Sanity-check outputs (signs, magnitudes, timing).
    - Record assumptions, ranges, and rationale in scenario notes.

11. Export and share
    - Save scenario versions with clear names and dates.
    - Export charts/tables to your reporting pack.
    - Share links or schedule refreshes if supported.

12. Iterate
    - Refine ranges based on insights.
    - Narrow to the few drivers that explain most variance.
    - Align recommendations with risk appetite and target outcomes.

## Tips and best practices
- Start simple: test a small set of high-impact drivers before expanding.
- Use realistic ranges anchored in history, contracts, or market data.
- Separate correlation from causation; avoid double-counting related drivers.
- Keep time granularity consistent across inputs and outputs.
- Document every assumption; use versioned scenario names (e.g., FY27_Upside_v3).
- Stress liquidity first: include working capital, capex timing, and covenants.
- Standardize charts: tornado for drivers, fan charts for distributions, waterfalls for variance explanation.
- Calibrate distributions from forecasting errors or external benchmarks.
- Lock formulas and map drivers to single sources of truth to prevent drift.
- Backtest: run the method on prior periods to check realism.

## Troubleshooting
- Outputs do not change when drivers move
  - Cause: Driver not linked to model or overwritten by hardcode.
  - Fix: Trace dependencies; replace hardcodes with formulas; refresh links.

- Implausible or negative results
  - Cause: Missing floors/ceilings or unit mismatches.
  - Fix: Add constraints; align units (%, bps, currency); validate signs.

- Circular reference or calculation errors
  - Cause: Feedback loops (e.g., interest depends on cash, which depends on interest).
  - Fix: Use iterative calc with limits, or restructure to break loops.

- Monte Carlo runs are slow or unstable
  - Cause: Too many trials or volatile distributions.
  - Fix: Reduce trials, simplify model, set random seed, cap tails.

- Heatmaps/tornado charts look inconsistent
  - Cause: Mixed time horizons or different KPI definitions.
  - Fix: Standardize periods and KPI formulas across scenarios.

- Scenario names overwrite prior work
  - Cause: Duplicate naming.
  - Fix: Enforce naming convention with timestamps and owner tags.

- Exported results don’t match dashboard
  - Cause: Unsaved scenario or stale cache.
  - Fix: Save and recalc before export; clear cache; confirm filter context.

- Ranges exceed business constraints
  - Cause: Unbounded inputs.
  - Fix: Add business rules (e.g., churn ≤ 100%, price ≥ floor).

- Long run times after adding drivers
  - Cause: Over-parameterization.
  - Fix: Prioritize top drivers; aggregate less material lines; precompute lookups.

- Permission or access error
  - Cause: Insufficient rights to scenarios or drivers.
  - Fix: Request edit access; check workspace and role settings.