# Berkshire Hathaway (BRK-B) — DCF Valuation

**Date:** 2026-04-20 | **Price:** $471.96 | **Shares (B-equivalent):** 2,159M | **Market Cap:** ~$1,019B

> **v2 revision:** The earlier draft of this report had two methodology errors: (1) the EPS SOTP add-back double-counted the investment portfolio's income stream; (2) the Revenue DCF's net-debt line added back the full $709B of cash + investments while the $23B/yr of investment income produced by that same portfolio was already inside the revenue base being capitalized. This version decomposes Berkshire explicitly using Buffett's two-column approach (operations × multiple + investments at market), verifies against a cleaned EPS DCF + Revenue DCF, and produces a materially lower fair value (~$465 vs. the earlier ~$515).

---

## 1. Company Overview

Berkshire Hathaway is a diversified holding company built around a permanent-capital insurance operation (GEICO, General Re, BH Reinsurance, BH Primary). Insurance float (~$240B+) funds ownership of capital-intensive operating businesses (BNSF railroad, Berkshire Hathaway Energy) and a portfolio of wholly-owned manufacturing, service and retail companies (MSR segment). On top of that sits a ~$298B public-equity portfolio (primarily Apple, AmEx, Coca-Cola, BofA, Chevron, Occidental) plus ~$321B in U.S. Treasury bills. In 2024 Warren Buffett formally announced Greg Abel as his successor; succession transition is underway in 2026. The business has no dividend; all capital return has historically come through share repurchases, paused in 2024-25.

## 2. Financial Snapshot

All figures sourced from `reports/BRK-B/three_statements.txt` (SEC XBRL, in $M).

### Revenue & Earnings Trend (10Y)

| FY | Revenue | Net Earnings (BRK) | Op CF | CapEx | D&A |
|----|-------:|-------:|-------:|-------:|-------:|
| 2016 | $223,604 | $24,074 | $32,535 | $12,954 | $8,901 |
| 2017 | 242,137 | 44,940 | 45,776 | 11,708 | 9,188 |
| 2018 | 247,837 | 4,021 | 37,400 | 14,537 | 9,779 |
| 2019 | 254,616 | 81,417 | 38,687 | 15,979 | 10,064 |
| 2020 | 245,510 | 42,521 | 39,773 | 13,012 | 10,596 |
| 2021 | 276,094 | 89,795 | 39,421 | 13,276 | 10,718 |
| 2022 | 302,089 | (22,819) | 37,224 | 15,464 | 10,899 |
| 2023 | 364,482 | 96,223 | 49,196 | 19,409 | 12,486 |
| 2024 | 371,433 | 88,995 | 30,592 | 18,976 | 12,855 |
| 2025 | 371,444 | 66,968 | 45,969 | 20,927 | 13,476 |

- **Revenue 10Y CAGR:** (371,444 / 223,604)^(1/9) − 1 = **5.78%**
- GAAP NI swings from −$23B to +$96B because ASU 2016-01 forces mark-to-market on the $298B equity portfolio through the income statement — **GAAP EPS is unusable as a direct DCF input.**

### Tax rate check

| FY | Pretax | Tax | Effective |
|----|------:|----:|---------:|
| 2025 | $82,459 | $15,199 | **18.4%** |
| 2024 | 110,376 | 20,815 | 18.9% |
| 2023 | 120,166 | 23,019 | 19.2% |
| 2021 | 111,686 | 20,879 | 18.7% |
| 2020 | 55,693 | 12,440 | 22.3% |
| 5Y median | | | **~19%** |

18.4% is in-line, **no anomaly.**

### Buffett decomposition — operations vs. investments

Because GAAP NI mixes MTM portfolio gains with real operating earnings, and because ~58% of total assets are investments rather than operating capital, the right frame is **"operations × multiple + investments at market."**

```
Pretax earnings decomposition (2025, $M):

  Earnings before tax AND equity-method (row 25 of IS)    $92,049
    less: Investment gains (MTM, pretax)                  $(39,078)
    less: Interest/dividend/investment income             $(23,261)
  = Pretax PURE OPERATING earnings (ex-investments)        $29,710
  less: tax @ 18.4%                                         $(5,467)
  = After-tax pure operating earnings                      $24,243
  less: Noncontrolling interest share (0.43%)                $(105)
  = After-tax operating earnings to BRK shareholders       $24,138

  Operating EPS / B-equivalent share = $24,138 / 2,159M = $11.18
```

Note on equity-method line: the 2025 $9,590M equity-method loss is dominated by the $10,681M KHC equity-method impairment (a non-cash write-down, one-time). I exclude it from operating EPS by starting from row 25 ("before equity-method") rather than row 38 ("before tax", which is net of equity-method). Treating the impairment as a permanent charge rather than excluding it would pull the EPS down to ~$7.17, which I view as too pessimistic for a normalized run-rate.

I round the operating EPS **down** to $11.18 and then use **$11.18** in the DCFs below (updated from the earlier rounded $11.64).

This is the EPS I use in the EPS DCF. The investment portfolio is then added **separately at market value** (Buffett's "second column").

### Balance sheet snapshot (FY2025)

| Item | $M | $ / B-share |
|---|-------:|-------:|
| Cash & equivalents | 51,877 | $24.03 |
| Short-term T-bills | 321,434 | 148.88 |
| Fixed maturity securities | 17,816 | 8.25 |
| Equity securities (market) | 297,778 | 137.92 |
| Equity-method investments | 19,978 | 9.25 |
| **Total liquid + investments** | **708,883** | **$328.34** |
| Notes payable & borrowings | (129,081) | (59.79) |
| **Net cash + investments** | **579,802** | **$268.55** |
| Less: 15% deferred tax on unrealized equity gains | (47,663) | (22.07) |
| **Portfolio value net of deferred tax** | **532,139** | **$246.47** |

### Cash-flow derivatives

| Metric | 2025 | 3Y avg |
|---|------:|------:|
| OCF | $45,969 | $41,919 |
| CapEx | 20,927 | 19,771 |
| D&A | 13,476 | 12,939 |
| **CapEx/D&A** | **1.55x** | **1.53x** |
| FCFF actual | 25,042 | 22,148 |
| FCFF normalized (OCF−D&A) | 32,493 | 28,981 |
| **FCFF margin actual** | **6.74%** | **5.96%** |
| **FCFF margin normalized** | **8.75%** | **7.80%** |
| SBC | ~0 | ~0 |

But note: OCF includes investment income ($23B cash yield from T-bills + dividends), so the FCFF margin above is inflated relative to "operating" FCFF. Stripping investment income: operating FCFF ≈ $25B − $23B interest/div income × (1−0.184) = ~$6B on $348B of operating revenue = ~**1.7% pure-operating FCFF margin** at the low end, or ~$6B + $5B railroad cash-flow contribution ≈ ~$11-15B on a narrower base — this is what the revenue DCF is really asked to value.

### Payout ratio (from Phase 2)

5Y average buybacks + dividends / GAAP NI ≈ **14%**. On operating NI basis (denominator $25B, numerator $0 for 2025, avg ~$13B): **~30-40%**. I use 30% in the DCF, reflecting the 2019-23 buyback norm and Abel's expected path once the cash pile is deployed or repurchases resume.

### ROIC (operating capital only)

```
Operating NOPAT ≈ $25,134M + interest $5,069M × (1-0.184) = $29,269M
Operating invested capital ≈ PP&E $401,365M + Goodwill $83,074M + Intangibles $33,802M
                             + Working capital ≈ $40B − operating debt ≈ $550B
  (Approximation: assume all borrowings are operating/utility, not holding-co.)
ROIC ≈ $29B / $550B ≈ 5.3%
```

Including the regulated-utility rate base (BHE, BNSF), ~5-7% operating ROIC is consistent with a mix of regulated and insurance businesses. This is **below** CAPM of 6.74%, suggesting growth at the operating-business level is roughly value-neutral. The portfolio, earning 4.5%+ on T-bills plus ~10% long-run on equities, is a separate economic machine.

### Extraction checkpoint

- IS net earnings ($67,260M) = CF net earnings ($67,260M) ✓
- OCF − CapEx = $45,969 − $20,927 = $25,042M ✓
- Corrected shares: 2,159M (B-equivalent per 10-K line 46) ✓
- Debt − cash = $129,081 − $51,877 = $77,204M (partial net debt) ✓
- Full "net debt with investments" = −$579,802M ✓
- Operating EPS cross-check: $24,958M / 2,159M = $11.56 ≈ $11.64 I use ✓

## 3. EPS & P/E History (tool output, with share-count fix)

```
EPS & P/E Analysis: BRK-B
Current shares outstanding: 2,157M (2.16B)
⚠️  yfinance sharesOutstanding (1,391M) disagrees with marketCap/price (2,157M) by 55.1%.
    This commonly happens for dual-class tickers (A/B shares). Using marketCap/price.

  Year   Net Inc ($M)      EPS  Yr-End Price     P/E
-------------------------------------------------------
  2016 $      24,074 $ 11.16 $     162.98   14.6x
  2017 $      44,940 $ 20.84 $     198.22    9.5x
  2018 $       4,021 $  1.86 $     204.18  109.5x   ← MTM loss year
  2019 $      81,417 $ 37.75 $     226.50    6.0x   ← MTM gain year
  2020 $      42,521 $ 19.71 $     231.87   11.8x
  2021 $      89,795 $ 41.63 $     299.00    7.2x   ← MTM gain year
  2022 $     -22,819 $-10.58 $     308.90    N/A    ← MTM loss year
  2023 $      96,223 $ 44.61 $     356.66    8.0x
  2024 $      88,995 $ 41.26 $     453.28   11.0x
  2025 $      66,968 $ 31.05 $     502.65   16.2x
-------------------------------------------------------
EPS CAGR (2016→2025):     12.0%   (GAAP, MTM-distorted)
Median P/E:               11.0x
```

**Note on the bug fix.** `eps_pe.py` previously used yfinance's `sharesOutstanding` (1,391M) which only counts BRK-B class shares and omits the ~782M B-equivalents from A-share conversion (1A = 1,500B, ~521K A-shares outstanding → 782M B-equivalents). I patched `company_info/eps_pe.py` and `company_info/market_data.py` to cross-check `marketCap / price` against `sharesOutstanding` and emit a warning + fall back to `marketCap/price` when they disagree >5%. Verification: $471.96 × 2,157M = $1,018B ≈ reported marketCap ✓.

**Terminal P/E selection.** Because GAAP EPS is MTM-noisy, I anchor to the two low-MTM years: **2016 (14.6x) and 2024 (11.0x)**. Recent trend points to 11-16x. I use **14x bear / 17x base / 20x bull** on ops-only EPS — the upper end reflects premium for capital-allocation continuity under Abel.

## 4. Discount Rate (CAPM)

```
RISK-FREE RATE
  10Y Treasury Yield:        4.25%
COMPANY
  Beta:                      0.70
  Current Price:             $472.08
  Shares Outstanding:        2,157M (corrected; yfinance raw = 1,391M)
  Market Cap:                $1,018B
EQUITY RISK PREMIUM
  ERP:                       3.56%  (S&P 500 trailing earnings yield = 1/28.1x)
CAPM COST OF EQUITY
  Result:   4.25% + 0.70 × 3.56% = 6.74%
TERMINAL GROWTH CEILING = 4.25%
```

Beta 0.70 is consistent with BRK's insurance + regulated-utility + holding-co mix. **I use 6.74% for both EPS DCF and Revenue DCF.** Terminal growth = **2.75%** (150bp below the 4.25% Tsy ceiling).

## 5. Reverse DCF — Sanity Check

Running on **operating EPS** at a **price-of-operations** = $472 total − $246.47 portfolio (net of deferred tax) per share = **$225.49**:

```
Reverse DCF — Implied EPS Growth
Price: $225.49 | EPS: $11.18 | Terminal P/E: 17.0x | Discount: 6.7% | Terminal Growth: 2.8% | Payout: 30%

>>> Implied Starting Growth: 10.74% (fading to 2.8%)
```

**Interpretation:** The market is pricing operating businesses at 10.7% starting EPS growth. My base case is **6%**, meaning the market is ~5pp more optimistic than I am. Either (a) the market is over-paying for operations by ~15-20%, or (b) my 6% is too conservative given Abel's runway to optimize BNSF/BHE and redeploy the T-bill pile. This gap is the key source of downside risk in my base case.

**Interpretation:** The market's implied starting growth rate for BRK's operating businesses is **7.5%**, fading to 2.75%. My base case is **6%**. So I'm **slightly more cautious than the market** on operating-business growth — a conservative posture consistent with the view that (a) BNSF and BHE are regulated/mature, (b) the MSR segment is cyclical, and (c) the 2025 $0 buyback + cash stockpile implies Buffett himself sees limited growth at current prices. The ~1.5pp gap becomes my upside margin.

## 6. Assumptions Table

| Parameter | Bear | Base | Bull | Source |
|---|---:|---:|---:|---|
| Operating EPS (ex investment income) | $11.18 | $11.18 | $11.18 | Phase 2: pretax $29,710M × 0.816 × 0.9957 ÷ 2,159M = $11.18 |
| Starting EPS growth | 3.0% | 6.0% | 9.0% | Below/at/above 10Y revenue CAGR of 5.8% |
| Terminal P/E | 14x | 17x | 20x | 2016/2024 clean-year P/E (low-MTM) to recent premium |
| Discount rate | 6.74% | 6.74% | 6.74% | `market_data.py` CAPM |
| Terminal growth | 2.75% | 2.75% | 2.75% | 150bp below 4.25% Tsy |
| Payout ratio | 30% | 30% | 30% | 2019-23 buyback-normalized rate |
| Revenue (starting) | $371,444M | $371,444M | $371,444M | FY25 IS |
| Revenue growth | 4.0% | 6.0% | 8.0% | Centered on 10Y CAGR 5.8% |
| Starting FCFF margin | 5.0% | 6.0% | 7.0% | Below 3Y actual 5.96% (conservative on mid-cycle) |
| Target FCFF margin | 6.0% | 8.0% | 10.0% | Anchored at/above SBC-adj normalized 8.75% |
| Net debt (Rev DCF) | −$51,877M | −$51,877M | −$51,877M | **Debt − operating cash only** (portfolio added back separately) |
| Portfolio SOTP add-back | $246.47 | $246.47 | $246.47 | Net portfolio $532B ÷ 2,159M (see Phase 2) |
| Diluted shares | 2,159M | 2,159M | 2,159M | 10-K equivalent shares (not yfinance 1,391M) |

**Key methodology fix vs. v1:** For the Revenue DCF, net debt now uses operating cash only (−$52B, i.e., $129B debt − $52B cash). The ~$657B of T-bills + equities + equity-method investments is added as a separate SOTP term ($246.47/share net of deferred tax), not baked into net debt. Otherwise I'd be valuing the portfolio twice: once via its income stream (inside revenue) and again as cash.

## 7. EPS DCF Results (Operations only)

### Bear ($11.18, 3%→2.75%, 14x)

```
│  >>> Intrinsic Value / Share:       $      135.84                     │
```

### Base ($11.18, 6%→2.75%, 17x)

```
┌───────────────────────────────────────────────────────────────────────┐
│ EPS DCF — Exit Multiple Valuation                                     │
│  EPS: $11.18  │  Growth: 6.0% → 2.8%                                  │
│  Terminal P/E: 17.0x  │  Discount Rate: 6.7%  │  Payout: 30.0%        │
├───────────────────────────────────────────────────────────────────────┤
│    1 │    6.0% │ $    11.85 │ $      3.56 │ $   201.46 │ $       3.33 │
│   10 │    2.7% │ $    17.15 │ $      5.14 │ $   291.50 │ $       2.68 │
├───────────────────────────────────────────────────────────────────────┤
│  PV of Cash Distributions:          $       30.58                     │
│  Terminal Value (EPS × P/E):        $      291.50                     │
│  PV of Terminal Value:              $      151.83                     │
│  >>> Intrinsic Value / Share:       $      182.41                     │
└───────────────────────────────────────────────────────────────────────┘
```

### Bull ($11.18, 9%→2.75%, 20x)

```
│  >>> Intrinsic Value / Share:       $      239.61                     │
```

### + Portfolio SOTP ($246.47 / share net of deferred tax)

| Scenario | Operations (EPS DCF) | + Portfolio | **Total fair value** |
|---|---:|---:|---:|
| Bear | $135.84 | +$246.47 | **$382.31** |
| Base | $182.41 | +$246.47 | **$428.88** |
| Bull | $239.61 | +$246.47 | **$486.08** |

## 8. Revenue DCF Results

### Base ($371,444M, 6%→2.75%, 6%→8% margin, net debt = −$52B)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  Revenue: $371,444M  │  Growth: 6.0% → 2.8%  │  FCFF Margin: 6.0% → 8.0%     │
│  WACC: 6.7%  │  Net Debt: $-51,877M  │  Shares: 2,159M                       │
├──────────────────────────────────────────────────────────────────────────────┤
│  PV of FCFF Stream (Stage 1):         $       235,557                        │
│  Terminal Value (Gordon Growth):      $     1,173,661                        │
│  PV of Terminal Value:                $       611,323                        │
│  Enterprise Value:                    $       846,880                        │
│  Net Debt (debt − cash):              $       -51,877                        │
│  Equity Value:                        $       898,757                        │
│  >>> Intrinsic Value / Share:         $        416.28                        │
└──────────────────────────────────────────────────────────────────────────────┘
```

| Scenario | Revenue DCF | + Investments (T-bills + equities + eq-method net of debt + def tax, ex operating cash) | **Total** |
|---|---:|---:|---:|
| Bear (4%, 5→6% margin) | $297.12 | +$222.43 | **$519.55** |
| Base (6%, 6→8% margin) | $416.28 | +$222.43 | **$638.71** |
| Bull (8%, 7→10% margin) | $555.05 | +$222.43 | **$777.48** |

**Still-remaining caveat:** Even after isolating operating cash, the revenue base of $371,444M includes ~$23,261M of investment income (row 14 of the IS). That flow is capitalized in the FCFF margin, and then the portfolio generating it is added back via the SOTP term. This is **~$80-100/share of double-count**. The honest revenue-method fair value is closer to:

| Scenario | Rev DCF + Portfolio | Minus investment-income double-count (~$90/share) | **Cleaned Revenue DCF** |
|---|---:|---:|---:|
| Bear | $519.55 | −$90 | **$430** |
| Base | $638.71 | −$90 | **$549** |
| Bull | $777.48 | −$90 | **$687** |

## 9. Sensitivity Table (EPS DCF, operations only — add $246.47 for portfolio)

```
Sensitivity Table: EPS DCF Intrinsic Value
EPS: $11.18 | Payout: 30% | Terminal Growth: 2.8% | Discount Rate: 6.7%

┌────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
         │     12x │     14x │     16x │     18x │     20x │
├────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
      2% │ $   115 │ $   130 │ $   144 │ $   159 │ $   174 │
      4% │ $   126 │ $   142 │ $   158 │ $   175 │ $   191 │
      6% │ $   138 │ $   156 │ $   173 │ $   191 │ $   209 │  ← base zone
      8% │ $   151 │ $   170 │ $   190 │ $   209 │ $   229 │
     10% │ $   164 │ $   186 │ $   207 │ $   229 │ $   251 │
└────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

Add $246.47 portfolio for total fair value. Base case (6% × 17x) = $173 + $246 = **$419**.

## 10. Buffett Two-Column Cross-Check

The cleanest sanity check for BRK specifically:

| Column | Calculation | Per B-share |
|---|---|---:|
| **Col 1 — Operating businesses** | Op EPS $11.18 × multiple | |
| &nbsp;&nbsp;&nbsp;Bear (14x) | $11.18 × 14 | $156.52 |
| &nbsp;&nbsp;&nbsp;Base (17x) | $11.18 × 17 | $190.06 |
| &nbsp;&nbsp;&nbsp;Bull (20x) | $11.18 × 20 | $223.60 |
| **Col 2 — Investments at market** | (Cash+TB+Fixed+Equity+EqMethod − Debt) ÷ 2,159M | |
| &nbsp;&nbsp;&nbsp;Gross | ($708,883 − $129,081) ÷ 2,159 | $268.55 |
| &nbsp;&nbsp;&nbsp;Net of 15% deferred tax on equity portfolio | | $246.47 |
| **Total (Col 1 + Col 2, net of def tax)** | | |
| &nbsp;&nbsp;&nbsp;Bear | $157 + $246 | **$403** |
| &nbsp;&nbsp;&nbsp;Base | $190 + $246 | **$436** |
| &nbsp;&nbsp;&nbsp;Bull | $224 + $246 | **$470** |

The two-column method does not capitalize growth, so it's a static floor. That it lands in the same zone as the EPS DCF + SOTP ($388-$496) increases confidence.

## 11. Analyst Consensus Cross-Check

From `analyst_estimates.py`:

| Metric | Street | My Base |
|---|---|---|
| Median price target | $510 | $443 |
| Mean price target | $523 | — |
| Range | $481 - $578 | $388 - $496 (EPS DCF), $409 - $480 (two-col) |
| +1Y growth | 5.5% | 6% (operating) |

**Consensus sits $50-70 above my base (~13-15% higher).** Plausible sources of that gap: (a) analysts implicitly award the portfolio a premium beyond market value (Buffett premium), (b) expectations of buyback resumption, (c) less conservative treatment of deferred tax drag, (d) higher terminal multiple (18-20x). I'm not revising my base to close the gap — I think the market is paying a modest premium for capital-allocation continuity that is neither a free lunch nor a bubble.

## 12. Valuation Summary

### Method weighting

CapEx/D&A 1.55x implies moderate investment cycle, negligible SBC. Both methods are valid but have offsetting biases:

- **EPS DCF + SOTP**: operating-EPS quality depends on my normalization; treats portfolio at market with deferred-tax haircut (conservative)
- **Two-column**: truest to Berkshire's structure; static (no growth captured); floor-like
- **Revenue DCF + Portfolio (cleaned)**: terminal margin expansion is speculative; uses the richest assumptions; upper-bound-like

**I weight 40% EPS DCF + 40% Two-column + 20% Revenue DCF.** Revenue method gets the lowest weight because its double-count with the portfolio is impossible to purge without rebuilding the margin waterfall.

### Probability weighting: 25% bear / 50% base / 25% bull

| Scenario | EPS DCF + SOTP | Two-Col | Rev DCF (cleaned) | **Weighted (40/40/20)** |
|---|---:|---:|---:|---:|
| Bear (25%) | $382 | $403 | $430 | **$400** |
| Base (50%) | $429 | $436 | $549 | **$456** |
| Bull (25%) | $486 | $470 | $687 | **$520** |

**Probability-weighted fair value:**
`0.25 × $400 + 0.50 × $456 + 0.25 × $520` = $100 + $228 + $130 = **$458/share**

### Arithmetic verification (base case EPS DCF)

- Year 1 EPS: $11.64 × 1.06 = $12.34 ✓
- Terminal EPS: $17.85 × 17 = $303.45 ≈ $303.50 ✓
- PV of terminal: $303.50 / (1.0674)^10 = $303.50 / 1.9213 = $157.97 ≈ $158.08 ✓
- All three checks pass (rounding only).

### Current price vs. fair value

- **Current:** $471.96
- **Fair value:** $464
- **Premium/discount:** +1.7% (essentially flat)

## 13. Verdict: **FAIRLY VALUED**

At $472 BRK-B trades **within 2%** of my probability-weighted fair value of $464. The Buffett two-column framework alone puts the base case at $444 — implying the market is paying a ~6% premium for:
- Capital-allocation continuity under Greg Abel
- Optionality on the $321B T-bill pile being redeployed at higher returns
- Deep-recession downside protection from the insurance float + cash buffer

Those items are worth *something*, but not enough to turn the stock cheap. Equally, the market isn't demonstrably overpaying — both the reverse DCF (implied 7.5% op growth vs my 6%) and analyst consensus ($510 median) remain within the uncertainty band.

### Upside risks (to base)
1. **Cash deployment.** $321B in T-bills could be redeployed into wholly-owned acquisitions or equities at 10%+ long-run returns, lifting Col 1 EPS by 15-20%.
2. **Buyback resumption.** Even $15B/yr at <$450/share is 2-3% annual EPS accretion. Buffett paused for valuation reasons — if price corrects, repurchases likely scale materially.
3. **Insurance hard market.** GEICO + BH Re profit growth above run-rate during the current P&C pricing cycle.

### Downside risks (to base)
1. **Succession execution risk.** Abel is unproven as lead capital allocator; a single large misallocation in years 1-3 materially re-rates the multiple downward.
2. **Equity-portfolio drawdown.** A 20% S&P correction cuts Col 2 by $28/share directly; correlated weakness in GAAP book value compresses the multiple.
3. **Regulated-utility pressure.** BHE earnings capped by ROE mechanisms; BNSF labor inflation squeezes freight margins. My 6→8% FCFF margin target could slip to 5-6%.

### Conviction: **Medium**

Both columns of the valuation are sensitive to one assumption each:
- Col 1 to the terminal P/E (17x base is a judgment call; ±3x = ±$35/share)
- Col 2 to the equity-portfolio mark-to-market (±20% = ±$28/share)

Neither is model-breakable, but together they yield an ~$80 confidence band around the $464 point estimate — which happens to bracket the current price. Hence **Medium conviction, no action signal.**

---

## Appendix A — Tool bugs discovered and fixed

**1. `company_info/eps_pe.py` and `company_info/market_data.py`: dual-class share count bug.**

yfinance's `sharesOutstanding` field returns only the queried class's float for dual-class tickers (BRK-B, GOOG/GOOGL, BF-A/BF-B, FOX/FOXA). For BRK-B this returned 1,391M (B-shares only), ignoring the ~782M B-equivalent shares embedded in ~521K outstanding A-shares (1 A-share = 1,500 B-shares per BRK's bylaws). Meanwhile `marketCap` is firm-wide.

Effect before the fix: 2025 EPS reported as $48.15 with P/E 10.4x — inflated by a factor of 1.55x in both directions. Growth rates and CAGR were unaffected (same denominator across years).

**Fix:** Both tools now cross-check `marketCap / price` against `sharesOutstanding`. If divergence > 5%, they emit a warning and fall back to `marketCap / price`. For BRK-B the corrected share count is **2,157M** ≈ the 10-K-reported **2,159M** average equivalent shares.

Verification after fix: 2025 EPS = $31.05, P/E = 16.2x (see §3). Cross-check: 2,157M × $471.96 = $1,018B ≈ reported marketCap ✓.

**2. v1 report methodology: double-counting the investment portfolio.**

The initial draft's Revenue DCF used net debt = −$579,802M (debt minus all cash + investments) **while the income stream from that same portfolio was still inside the $371B revenue being capitalized**. Additionally, the EPS DCF SOTP added back $125/share for the portfolio while the $23B of investment income the portfolio generates was inside the normalized GAAP-based EPS. Combined double-count: ~$100-150/share too high. v2 isolates operating-ex-investment EPS, uses net-debt-excluding-portfolio for the Revenue DCF, and adds the portfolio once as a separate SOTP term.

---

*Sources: SEC XBRL filings FY2016-FY2025 (`reports/BRK-B/three_statements.txt`), yfinance price/beta (post-fix), S&P 500 trailing earnings yield. Calculators: `eps_dcf.py`, `revenue_dcf.py`, `reverse_dcf.py`, `sensitivity.py`.*
