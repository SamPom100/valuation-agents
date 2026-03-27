# Cost of Capital — Damodaran's Framework

## Sources
- "Data Update 5 for 2026: Risk and Hurdle Rates" (February 2026)
  https://aswathdamodaran.blogspot.com/2026/02/data-update-5-for-2026-risk-and-hurdle.html
- "Data Update 7 for 2026: Debt and Taxes" (February 20, 2026)
  https://aswathdamodaran.blogspot.com/2026/02/data-update-7-for-2026-debt-and-taxes.html
- Blog search results on beta and regression (multiple posts, 2019-2025)

---

## Core Definition

Damodaran defines hurdle rates as opportunity costs — "the rate of return you can earn elsewhere in the market, on investments of equivalent risk." He emphasizes grounding calculations in first principles rather than mechanical formula application.

---

## WACC Components

### Risk-Free Rate
- US Treasury rates around 4% as the baseline (as of early 2026)
- Described as "normalized after 2022's shock period"

### Equity Risk Premium
- Uses "implied equity risk premium" — "model-agnostic and reflects what investors are pricing stocks to earn, on an annual basis"
- See `damodaran_erp.md` for full methodology
- January 2026 value: 4.23%

### Beta

**Damodaran's strong preference: bottom-up (industry average) betas over regression betas.**

From multiple data update posts, he calls regression beta "an extremely noisy measure of its risk" and states that "the averages...are significantly better at explaining differences in returns across stocks."

His recommended approach:
1. Find the average unlevered beta for the company's industry/sector
2. Relever for the company's specific capital structure:
```
Unlevered beta = Industry avg beta / (1 + (1-T) × D/E_industry)
Relevered beta = Unlevered beta × (1 + (1-T) × D/E_company)
```
3. For multi-business companies, use "the beta of their primary business"

He publishes industry betas on his website (pages.stern.nyu.edu/~adamodar/).

### Cost of Debt
- Should reflect default risk through the **interest coverage ratio** (EBIT / Interest Expense) as the most predictive metric of bond ratings and default probability
- Fairly-priced debt should reflect default risk
- Book value debt ratios are "analytically worthless" — market value metrics alone matter

---

## WACC Computation

Combines:
- Cost of equity (what equity investors expect at equivalent risk)
- Cost of debt (current borrowing costs for similarly-rated firms)
- Capital structure (debt and equity weights — must use market values)

He makes "simplifying assumptions" for consistency across the 48,156 firms he analyzes.

---

## Capital Structure and Tax Benefits

From Data Update 7:

### Debt vs. Equity
Three critical distinctions:
1. **Nature of claim:** Debt holders have contractual claims with specified payments; equity holders get residual claims
2. **Priority:** Debt holders have first claim on cash flows and liquidation proceeds
3. **Legal consequences:** Non-payment of dividends is fine; defaulting on debt can force bankruptcy

### Tax Shield
The primary advantage of debt: interest payments reduce taxable income, creating value. But:
- This benefit "is coming from taxpayers" — not operational improvement
- Tax benefits only materialize when companies generate taxable income
- Money-losing companies get no tax shield

### Optimal Capital Structure
Balances tax benefits against bankruptcy risk. Damodaran provides a cost-of-capital optimizer that minimizes WACC by testing different debt-to-equity mixes.

**Key critique:** "Debt is cheaper than equity" is misleading. If debt is fairly priced for risk, it doesn't reduce overall cost of capital without tax advantages. The only real benefit is the tax shield.

---

## Precision Limits

**Critical insight from Data Update 5:**

"80% of all US (global) companies have costs of capital between 5.26% (6.28%) and 9.88% (11.66%)."

Damodaran advocates using benchmark histograms as plausibility checks rather than treating WACC calculations as highly precise exercises. Spending excessive time refining cost-of-capital estimates is wasteful — the range is narrow enough that moderate errors don't dominate valuation outcomes.

---

## Implications for This Project

1. **Beta source.** The project uses `yfinance` regression beta. Damodaran would prefer industry-average bottom-up betas. For mega-caps (META, AAPL), regression betas are reasonably stable. For mid-caps with volatile histories (FICO), they can mislead.

2. **ERP method.** The project uses earnings yield. Should use implied ERP. See `damodaran_erp.md`.

3. **Cost of debt.** The project's WACC computation (in agent Phase 2) uses interest expense / total debt for cost of debt. This is roughly correct per Damodaran (interest coverage-based), though Damodaran would prefer using a synthetic rating from the coverage ratio mapped to default spreads.

4. **Market vs. book value weights.** The project uses market cap for equity weight, which is correct. The FICO report correctly uses market cap ($25B) not book equity (-$1.7B).

5. **Precision expectations.** Damodaran's 5.26%-9.88% range for 80% of US companies suggests that refinements beyond ±1% in WACC are noise. The project's CAPM sensitivity table (varying ERP) is a good practice per Damodaran.
