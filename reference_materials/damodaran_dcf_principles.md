# DCF Principles — Damodaran's Framework

## Sources
- "Discounted Cashflow Valuations (DCF): Academic Exercise, Sales Pitch or Investor Tool?" (February 1, 2015)
  https://aswathdamodaran.blogspot.com/2015/02/discounted-cashflow-valuations-dcf.html
- "DCF Myth 1: If you have a D(discount rate) and a CF (cash flow), you have a DCF!" (February 23, 2015)
  https://aswathdamodaran.blogspot.com/2015/02/dcf-myth-1-if-you-have-ddiscount-rate.html
- "Fairness Opinions: Fix them or Flush them!" (September 14, 2016)
  https://aswathdamodaran.blogspot.com/2016/09/fairness-opinions-fix-them-or-get-rid.html

---

## The Fundamental DCF Equation

"The present value of expected cash flows over its lifetime, adjusted for risk and time value of money." Damodaran emphasizes this requires no advanced mathematics — it's foundational finance.

---

## Four Essential Truths Often Overlooked

From the February 2015 post:

1. **Negative cash flows don't disqualify assets.** Valuable businesses can have negative cash flows for years if later cash flows justify the investment.

2. **DCF is agnostic about risk adjustment.** You don't need beta or modern portfolio theory. Creative alternatives exist. The method is the discounting framework, not any specific risk model.

3. **Asset life matters, not investor time horizon.** Valuations should span the asset's functional life, not your holding period.

4. **Estimates are inherently wrong.** Uncertainty is guaranteed. You're judged relative to other valuators, not by absolute accuracy.

---

## Three Consistency Tests for a Legitimate DCF

From DCF Myth 1 — a genuine DCF must pass all three:

### 1. Unit Consistency
All inputs must align across four dimensions:
- **Equity vs. Firm:** "If the cash flows are after debt payments...the discount rate used has to reflect the return required by those equity investors." FCFE → cost of equity. FCFF → WACC.
- **Nominal vs. Real:** Cash flows and discount rate must be in the same terms.
- **Pre-tax vs. Post-tax:** Alignment required throughout.
- **Currency:** All inputs in the same currency.

### 2. Input Consistency
The "valuation triangle" requires alignment between cash flows, growth expectations, and risk assumptions. High growth paired with low risk demands justification and is unusual.

### 3. Narrative Consistency
"A good DCF valuation has to follow the same principles and the numbers have to be consistent with the story that you are telling about a company's future."

---

## Seven Categories of Defective DCFs

From DCF Myth 1:

1. **Chimera DCF:** Mixing incompatible units — currencies, tax treatments, debt structures within the same model.

2. **Dreamstate DCF:** Unrealistic spreadsheet assumptions without competitive dynamics. Revenue grows forever, margins never compress, no competitive entry.

3. **Trojan Horse DCF:** Terminal value derived from market multiples, disguising pricing as valuation. Damodaran identifies this as one of the most common failures. The model looks like a DCF but the terminal value is really just a relative valuation in disguise.

4. **Robo DCF:** Purely mechanical models lacking analytical judgment. No narrative, just formula outputs.

(Three additional categories were referenced but not detailed in the post.)

**Core distinction:** True intrinsic valuation derives from fundamental cash flow principles. Pricing involves market-based multiples. Many Wall Street models blur this line, using DCF frameworks primarily for defensibility rather than honest value discovery.

---

## On Exit Multiples as Terminal Value

From the Fairness Opinions post:
- Damodaran explicitly warns: "And please, no more terminal values estimated from EBITDA multiples!"
- He advocates for appraisers using multiples more transparently rather than disguising them inside DCFs
- He suggests appraisers must "justify their use of multiples (both in terms of the specific multiple used, as well as the value for that multiple)"

---

## Common DCF Mistakes

### Over-Complication
"Layers of detail" often serve to intimidate rather than clarify. Sometimes intentionally obscuring key assumptions. Essential details improve estimates; unnecessary ones create false precision.

### Over-Selling
Analysts frequently use DCF models as sales tools rather than analytical devices, backing predetermined recommendations.

### Over-Sanitizing
Hiding uncertainties embedded in valuations, downplaying the storytelling inherent in any valuation exercise.

---

## Implications for This Project

1. **Trojan Horse DCF:** The EPS DCF uses P/E as terminal value. Per Damodaran, this is a Trojan Horse — market pricing disguised as intrinsic valuation. The Revenue DCF uses Gordon Growth, which is the "proper" approach. Having both is actually a strength, but the report should acknowledge the EPS DCF is a hybrid model.

2. **Unit Consistency (FCFE vs FCFF):** The project computes "FCFF" as Operating CF - CapEx, but OCF starts from net income (after interest). This is FCFE, not FCFF. The Revenue DCF then discounts at WACC. Per Damodaran's unit consistency test, this is a mismatch: FCFE should be discounted at cost of equity, FCFF at WACC. For low-debt companies the error is small. For leveraged companies it's real.

3. **Narrative Consistency:** The project's narrative-first assumption setting (Phase 3) aligns well with Damodaran's emphasis on story-number consistency.
