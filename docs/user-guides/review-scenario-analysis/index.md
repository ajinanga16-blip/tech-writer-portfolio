# Review Scenario Analysis User Guide

## Overview
Review Scenario Analysis is the process of evaluating and validating different forecast scenarios to understand their impact on financial outcomes. It involves comparing multiple scenarios, analyzing key variances, and assessing underlying assumptions to ensure accuracy and reliability. This step helps stakeholders identify risks, make informed decisions, and select the most appropriate forecast before final approval.

## Who should use this
- FP&A analysts and finance managers
- Business unit leaders and product owners
- Strategy and corporate development teams
- Risk management and treasury
- Executive reviewers and approvers

## Prerequisites
- Clearly defined scenarios (e.g., Base, Upside, Downside) with unique names or IDs
- A baseline or prior-approved forecast to compare against
- Access to the financial model or planning tool and required data sources
- Defined key performance indicators (KPIs) and reporting currency (e.g., revenue, gross margin, EBITDA, cash flow, headcount, CapEx)
- An assumptions register covering key drivers (pricing, volume, churn, FX, inflation, hiring, seasonality)
- Agreed fiscal calendar and time horizon (e.g., monthly/quarterly for 12–24 months)
- Variance thresholds and acceptance criteria (e.g., investigate any >5% or >$X variance)
- Version control plan and collaboration channels for stakeholder review

## Steps
1. Define scope and objectives
   - Clarify the decision to be supported (e.g., budget approval, investment, hiring plan).
   - Confirm the period, granularity, and KPIs to evaluate.

2. Assemble scenarios
   - Collect scenario files or versions from the planning tool.
   - Verify each scenario includes consistent timeframes and complete data for all KPIs.

3. Validate data integrity
   - Check for missing periods, duplicates, or broken links.
   - Reconcile totals to source systems where applicable.
   - Ensure currency, units, and calendars are consistent.

4. Set evaluation criteria and thresholds
   - Document quantitative thresholds for investigation (absolute and percentage).
   - Define qualitative criteria (e.g., plausibility of assumptions, alignment with strategy).

5. Normalize and run scenarios
   - Ensure common modeling settings (e.g., FX rates, calendar, accounting rules).
   - Recalculate or refresh all scenarios to eliminate stale outputs.

6. Compare scenarios using variance analysis
   - Calculate period-by-period and year-to-date variances vs. baseline and vs. each other.
   - Use absolute and percentage variances, plus contribution analysis by driver, product, or region.
   - Create bridges (waterfalls) to show sources of change between scenarios.

7. Examine key drivers and assumptions
   - Review the assumptions register for each scenario.
   - Test plausibility: source, date, owner, method, and historical back-testing.
   - Check dependencies (e.g., price-volume, headcount-productivity) for logical consistency.

8. Perform sensitivity and stress testing
   - Vary critical drivers within reasonable ranges to test robustness.
   - Run stress cases for tail risks (e.g., demand shock, supply constraint, FX swing).
   - Note breakpoints where results change materially.

9. Assess risks, mitigations, and contingencies
   - Identify top risks per scenario and quantify potential impact.
   - Document mitigations, trigger points, and contingency actions.

10. Document findings
   - Summarize key variances, drivers, and rationale for differences.
   - Highlight assumptions that most influence outcomes.
   - Provide a clear narrative and executive summary.

11. Review with stakeholders
   - Share results, methods, and assumptions for feedback.
   - Capture and resolve challenges, questions, and requested reruns.

12. Recommend and select a scenario
   - Evaluate scenarios against criteria and risk tolerance.
   - Provide a reasoned recommendation with sensitivities and caveats.
   - Obtain sign-off from approvers.

13. Finalize and archive
   - Lock the approved scenario in the planning tool with version tags.
   - Archive inputs, calculations, and documentation for auditability.
   - Record lessons learned for future cycles.

## Tips and best practices
- Establish a standard scenario taxonomy (e.g., Base, Conservative, Aggressive) and naming convention.
- Use a consistent KPI set and time buckets to ensure like-for-like comparisons.
- Apply materiality thresholds to focus analysis on impactful variances.
- Visualize results with bridges and trend charts to clarify drivers.
- Keep an up-to-date assumptions register with owners, sources, and timestamps.
- Perform quick sanity checks (unit economics, seasonality, cohort metrics) before deep dives.
- Involve cross-functional SMEs early (sales, ops, HR, supply chain) to validate realism.
- Differentiate structural vs. timing variances; flag one-offs and non-recurring items.
- Document unresolved uncertainties and define decision trigger points.
- Maintain version control; change-log any model or assumption updates.

## Troubleshooting
- Variances appear unrealistic or volatile
  - Check for inconsistent time granularity, calendar mismatches, or FX settings.
  - Recalculate scenarios and clear cached results.

- Scenarios use different assumptions unknowingly
  - Compare assumptions registers side-by-side.
  - Standardize global settings (inflation, FX, accounting rules) and rerun.

- Data gaps or broken links
  - Identify missing periods or entities; repair source connections.
  - Backfill with the latest actuals or approved proxies and document.

- Conflicting KPI movements (e.g., revenue up, margin unexpectedly down)
  - Decompose drivers (price, mix, discounting, COGS inflation).
  - Review dependencies and constraints in the model.

- Sensitivity tests produce unstable outputs
  - Reduce step sizes and test one driver at a time.
  - Inspect formulas for circular references or hardcoded overrides.

- Stakeholders challenge credibility
  - Provide traceability: sources, methods, and historical back-tests.
  - Share scenario bridges and sensitivity results; note limitations transparently.

- Approval delays due to unresolved questions
  - Log open issues with owners and due dates.
  - Propose interim decision criteria and escalation paths.