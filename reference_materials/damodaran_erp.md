# Equity Risk Premium — Damodaran's Framework

## Sources
- "The Price of Risk: An Equity Risk Premium Monologue!" (March 15, 2026)
  https://aswathdamodaran.blogspot.com/2026/03/the-price-of-risk-equity-risk-premium.html
- "The Price of Risk: With Equity Risk Premiums, Caveat Emptor!" (August 5, 2023)
  https://aswathdamodaran.blogspot.com/2023/08/the-price-of-risk-with-equity-risk.html
- "Data Update 2 for 2026: Equities get tested and pass again!" (January 2026)
  https://aswathdamodaran.blogspot.com/2026/01/data-update-2-for-2026-equities-get.html

---

## The Three Approaches

### 1. Historical ERP (Damodaran rejects this for forward-looking use)
- Look at actual stock returns vs bond returns over a long period
- US historical ERP: 7.03% with standard error of 2.05% (1928-2025)
- Problems Damodaran identifies:
  - Yields estimates between 5.5% and 14.5% depending on time period and methodology
  - "Allows bias to easily creep in" through choice of time window
  - Moves "in the wrong direction, falling during crises" — when the 2008 crisis hit, historical ERP declined because realized returns were poor, even though forward-looking risk was higher
  - Inverse correlation with subsequent stock returns over 10-year periods (i.e., it has negative predictive power)

### 2. Earnings Yield / Fed Model (Damodaran explicitly rejects this)

**This is what our project currently uses: ERP = 1 / S&P 500 forward PE**

Damodaran's critique from the August 2023 post — three specific problems:

1. **Assumes zero earnings growth.** The formula ERP = E/P - Rf only works if earnings never grow. US stocks have delivered positive earnings growth every decade for the past century.

2. **Assumes 100% payout ratio.** The formula treats all earnings as if they're paid out as dividends. In reality, companies retain ~50%+ of earnings for reinvestment, and two-thirds of cash returns are buybacks, not dividends.

3. **Ignores excess returns.** ROE for S&P 500 companies substantially exceeds cost of equity historically:
   - 2022: ROE 19.73%
   - Last decade average: 17.04%
   - Even 2008 (worst case): 9.35%
   - The Fed Model ignores this entire spread

**Result:** Earnings yield approach produced:
- 0.41% ERP in August 2023 (Damodaran's implied method gave 4.44% at the same time)
- Negative ERPs during multiple historical periods (1980s-1990s)
- Damodaran calls these results "useless" for valuation

### 3. Implied ERP (Damodaran's preferred method)

Backed out from current market prices and expected cash flows. At start of 2026: **4.23%** (expected stock return 8.41% minus 4.18% Treasury bond rate).

**How it works:**
- Takes the current S&P 500 index level (6,845.5 at Jan 1, 2026)
- Uses **augmented dividends**: dividends + buybacks (not dividends alone) as cash flows to equity
- Incorporates **near-term growth**: analyst consensus earnings growth estimates for the aggregate index (NOT individual company bottom-up estimates)
- Allows ROE to differ from cost of equity (excess returns)
- Solves for the internal rate of return (IRR) that equates cash flows to the current price
- Subtracts risk-free rate to isolate ERP

**Key advantages Damodaran identifies:**
- "Entirely a market-driven number and is model-agnostic"
- More precise than historical estimates
- Responsive to market sentiment changes
- Rises during crises (opposite of historical premiums) — during 2008, his daily ERP estimates rose from 4.2% to nearly double over two months
- Strong positive correlation with subsequent 10-year stock returns (i.e., actually predictive)

**Interpreting the number:**
- If you think the market's implied ERP is too low → stocks are overpriced
- If you think the implied ERP is too high → stocks are underpriced
- If you're a non-market-timer → the implied ERP "is, in fact, the right ERP for the market"

**Sensitivity:** Index value ranges dramatically by ERP assumption — from 14,834 at 2% ERP to 4,790 at 6% ERP.

**Historical context:** 4.23% sits near the 1960-2025 average. Not bubble territory (1999 was 2.05%). Not crisis territory (2008 peaked near 8%).

## Damodaran's Published Data
- Monthly implied ERP since September 2008
- Published at: pages.stern.nyu.edu/~adamodar/pc/implprem/ERPbymonth.xlsx
- S&P 500 computation spreadsheet (most recent: Feb 27, 2026)
- Updated monthly on his website

## Three Lessons (from March 2026 post)
1. ERPs are dynamic; using outdated premiums conflates company and market valuations
2. Implied ERP incorporates interest rates, growth expectations, and cash payouts more completely than dividend/earnings yields alone
3. Limited academic resources exist on this topic; Damodaran maintains a 153-page annual paper on determinants, historical data, country applications, and predictive efficacy

---

## Implications for This Project

The project's `market_data.py` computes ERP as `1 / spy_pe_forward`. This is the Fed Model that Damodaran explicitly rejects. The CAPM discount rate — which drives every DCF in the project — is built on this foundation.

Options to fix:
1. Fetch Damodaran's monthly implied ERP from his spreadsheet (best: his methodology, his data)
2. Compute an implied ERP using his methodology from yfinance data (harder to replicate exactly)
3. At minimum, use a hardcoded recent value from his published data and update periodically
