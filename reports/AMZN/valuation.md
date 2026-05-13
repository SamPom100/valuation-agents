# Amazon.com, Inc. (AMZN) — DCF Valuation

**Valuation date:** April 20, 2026
**Current price:** $247.06
**Shares outstanding:** 10,754M (yfinance); FY25 diluted: 10,827M
**Market cap:** $2,657B

---

## 1. Company Overview

Amazon is a three-engine conglomerate: (1) North America & International retail (online and physical stores, third-party marketplace, subscriptions), (2) AWS — the leading cloud-infrastructure business with ~30%+ share of public cloud, and (3) advertising, a high-margin attached business now running at a ~$70B+ revenue annualized run-rate. FY25 revenue was $716.9B (+12.4% YoY), operating income $80.0B (11.2% margin — a record), and net income $77.7B ($7.17 diluted EPS). The business is in a heavy AI/AWS capacity investment cycle: 2025 capex hit $131.8B (2.0× D&A), pressuring free cash flow in the near term but building the revenue base for the next decade. The company has ~$123B cash and short-term investments against ~$66B long-term debt, so it holds a net cash position of ~$57B.

## 2. Financial Snapshot

All dollar amounts are in $M, from `reports/AMZN/three_statements.txt`.

### Revenue, Margin, Tax

| Metric | FY25 | FY24 | FY23 | FY22 | FY16 |
|---|---:|---:|---:|---:|---:|
| Revenue | 716,924 | 637,959 | 574,785 | 513,983 | 135,987 |
| Operating income | 79,975 | 68,593 | 36,852 | 12,248 | 4,186 |
| Operating margin | 11.15% | 10.75% | 6.41% | 2.38% | 3.08% |
| Net income | 77,670 | 59,248 | 30,425 | (2,722) | 2,371 |
| Pretax income | 97,311 | 68,614 | 37,557 | (5,936) | 3,892 |
| Effective tax rate | 19.6% | 13.5% | 19.0% | — | 36.6% |
| Diluted EPS | 7.17 | 5.53 | 2.90 | (0.27) | 4.90 (pre-split) |
| Diluted shares (M) | 10,827 | 10,721 | 10,492 | 10,189 | 484 (pre-split) |

- **Revenue 9-yr CAGR:** (716,924 / 135,987)^(1/9) − 1 = **20.3%**.
- **Operating margin** has climbed from 2% (2022) to **11.2%** (2025), driven by AWS share of mix and advertising scaling.
- **Tax rate check:** FY25 effective rate 19.6% is close to the 3-yr median (~17%). The only material anomaly is FY24 (13.5%, deferred-tax benefits) — less than the 8 pp flag threshold vs the 2023/2025 run-rate, so no normalization is required to starting EPS.

### Cash Flow & Capex Cycle

| ($M) | FY25 | FY24 | FY23 | FY22 | FY21 |
|---|---:|---:|---:|---:|---:|
| Operating cash flow | 139,514 | 115,877 | 84,946 | 46,752 | 46,327 |
| Capex (Purch. of PP&E) | 131,819 | 82,999 | 52,729 | 63,645 | 61,053 |
| D&A | 65,756 | 52,795 | 48,663 | 41,921 | 34,296 |
| Stock-based compensation | 19,467 | 22,011 | 24,023 | 19,621 | 12,757 |

- **Capex / D&A (FY25) = 131,819 / 65,756 = 2.00×** → investment supercycle (AI GPUs, data-center capacity).
- **FCFF actual = OCF − Capex = 139,514 − 131,819 = $7,695M → margin 1.07%**
- **FCFF normalized = OCF − D&A = 139,514 − 65,756 = $73,758M → margin 10.29%**
- **FCFF SBC-adjusted = OCF − D&A − SBC = 73,758 − 19,467 = $54,291M → margin 7.57%**

Per the skill guidance (capex/D&A ≈ 2×), the starting Revenue-DCF margin should anchor to the SBC-adjusted figure (~7.5%). Target margin should reflect where FCFF settles once the investment cycle normalizes and SBC decelerates — 13% base case, bracketed by 10% bear / 16% bull.

### Capital Returns (Payout Ratio)

Amazon pays no dividend and does only sporadic buybacks. Cumulative 2020–2025:

| ($M) | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **Total** |
|---|---:|---:|---:|---:|---:|---:|---:|
| Dividends | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Buybacks | 0 | 0 | 6,000 | 0 | 0 | 0 | 6,000 |
| Net income | 21,331 | 33,364 | (2,722) | 30,425 | 59,248 | 77,670 | 219,316 |

**6-yr payout ratio = 6,000 / 219,316 = 2.7%** → use **3%** in the EPS DCF. Payout is negligible, so DCF value is dominated by the terminal multiple (confirmed by >98% terminal-value share in EPS DCF outputs).

### Balance Sheet & Net Debt (FY25)

| ($M) | FY25 |
|---|---:|
| Cash & equivalents | 86,810 |
| Marketable securities | 36,219 |
| **Cash + investments** | **123,029** |
| Long-term debt | 65,648 |
| Total stockholders' equity | 411,065 |

**Net debt = 65,648 − 123,029 = −$57,381M** (net cash).

### ROIC vs WACC

- NOPAT = 79,975 × (1 − 0.196) = **$64,300M**
- Invested capital = 411,065 + 65,648 − 123,029 = **$353,684M**
- **ROIC = 64,300 / 353,684 = 18.2%**
- WACC (CAPM) = **9.2%** → ROIC ≈ **2× WACC**: growth creates substantial value, which justifies a premium terminal multiple and keeps even the bear case above liquidation-style valuations.

### Consistency checks

- Net income on IS ($77,670M) matches CF statement first line ($77,670M). ✓
- OCF − Capex = 139,514 − 131,819 = $7,695M ≈ our FCFF_actual. ✓
- Balance-sheet equity common stock count shows 10,593M outstanding; yfinance reports 10,754M; FY25 diluted 10,827M — all within ~2%. ✓
- Total debt − (cash + investments) = −$57,381M = our net-debt. ✓

## 3. EPS & P/E History

```
EPS & P/E Analysis: AMZN
Current shares outstanding: 10,754M (10.75B)
Share basis: year-specific diluted shares (from income statement — split-adjusted)

  Year   Net Inc ($M)      EPS  Yr-End Price     P/E  EPS Gr%  P/E Gr%
----------------------------------------------------------------------
  2016 $       2,371 $  0.24 $      37.49  153.1x       --       --
  2017 $       3,033 $  0.31 $      58.47  190.1x    25.6%    24.2%
  2018 $      10,073 $  1.01 $      75.10   74.6x   227.5%   -60.8%
  2019 $      11,588 $  1.15 $      92.39   80.4x    14.1%     7.8%
  2020 $      21,331 $  2.09 $     162.85   77.9x    81.9%    -3.1%
  2021 $      33,364 $  3.24 $     166.72   51.5x    54.9%   -33.9%
  2022 $      -2,722 $ -0.27 $      84.00     N/A       --       --
  2023 $      30,425 $  2.90 $     151.94   52.4x       --       --
  2024 $      59,248 $  5.53 $     219.39   39.7x    90.6%   -24.2%
  2025 $      77,670 $  7.17 $     230.82   32.2x    29.8%   -19.0%
----------------------------------------------------------------------

SUMMARY
EPS CAGR (9yr):          45.5%
Avg YoY EPS Growth:      74.9%
Median YoY EPS Growth:   54.9%
EPS Growth Range:        14.1% to 227.5%

Avg P/E:                 83.5x
Median P/E:              74.6x
P/E Range:               32.2x to 190.1x   (multi-year compression)

Latest EPS:            $ 7.17
Latest P/E:             32.2x
```

P/E has structurally compressed from >70× (pre-earnings-maturity) toward a low-30s multiple as the denominator (EPS) has grown faster than the stock price. The "stock's own" P/E history isn't a clean anchor because the business transformed around 2018–2020. I therefore anchor terminal P/E to the **recent steady-state P/E** plus a premium/discount for the scenario: 22× bear / 30× base / 38× bull. The base 30× is slightly below the 2024 P/E of 39.7× and close to the S&P's high-quality growth basket.

## 4. Discount Rate

```
Market Data & CAPM: AMZN
RISK-FREE RATE
  10Y Treasury Yield:        4.26%

COMPANY
  Beta:                      1.38

EQUITY RISK PREMIUM (market-implied)
  ERP:                       3.56%
  Method:                    S&P 500 trailing earnings yield (1 / 28.1x)

CAPM COST OF EQUITY
  Formula:  Rf + Beta x ERP
  Result:   4.26% + 1.38 x 3.56% = 9.19%

TERMINAL GROWTH RATE
  Ceiling (= 10Y Treasury):  4.26%   (terminal growth must be < 4.26%)
```

**Use 9.19% as both the equity-DCF discount rate and the revenue-DCF WACC.** Beta 1.38 reflects AMZN's sensitivity to consumer cyclicality + cloud capex cycles. The net-cash position would slightly lower WACC vs cost of equity alone, but the impact is <20bps, and the tool convention of using CAPM cost-of-equity for both DCFs is an acceptable simplification (especially since revenue-DCF equity value already adds back the net cash).

**Terminal growth = 2.5%** (below the 4.26% risk-free ceiling, above long-run US real GDP).

## 5. Reverse DCF — What Is the Market Pricing In?

```
Reverse DCF — Implied EPS Growth
Price: $247.06 | EPS: $7.17 | Terminal P/E: 28.0x | Discount: 9.2%
Terminal Growth: 2.5% | Payout: 3%

>>> Implied Starting Growth: 20.50% (fading to 2.5%)
```

At a 28× terminal multiple, the market is pricing in a **~20.5% starting EPS growth rate fading linearly to 2.5% over 10 years**. For context:

- AMZN's own EPS CAGR (2016–25, 9 yrs): **45.5%**
- Most-recent 2-yr EPS growth: 90.6% → 29.8% (still in a rebound from the 2022 loss-year)
- Consensus +1y EPS growth (below): **21.5%**
- Analyst LTG: N/A

**My base-case starting growth is 18%**, slightly below the 20.5% market implied — suggesting the market is mildly more optimistic than my base case, but not wildly so. That is broadly consistent with AMZN trading near fair value rather than at extremes.

## 6. Assumptions Table

| Parameter | Bear | Base | Bull | Source |
|---|---:|---:|---:|---|
| Starting EPS | $7.17 | $7.17 | $7.17 | eps_pe.py |
| EPS growth (Yr 1, fades to terminal) | 12% | 18% | 24% | Bracket around 20.5% market-implied; below 9-yr CAGR (45.5%) and 2-yr avg (~60%) — reflects growth-law-of-large-numbers |
| Terminal P/E | 22× | 30× | 38× | Anchored near FY25 P/E 32.2× (base); FY24 P/E 39.7× (bull); historic low 32.2× minus compression (bear) |
| Discount rate / WACC | 9.19% | 9.19% | 9.19% | CAPM from market_data.py |
| Terminal growth | 2.5% | 2.5% | 2.5% | Below 4.26% Rf ceiling |
| Payout ratio | 3% | 3% | 3% | 6-yr avg: $6B / $219B NI |
| Starting revenue | $716,924M | $716,924M | $716,924M | IS FY25 |
| Revenue growth (Yr 1, fades) | 8% | 11% | 14% | FY25 YoY 12.4%; 9-yr CAGR 20.3% (moderating) |
| Starting FCFF margin | 6% | 7.5% | 8% | SBC-adj 7.57% is anchor; bear penalizes persistent capex |
| Target FCFF margin (Yr 10) | 10% | 13% | 16% | Normalized FCFF margin 10.3% = floor; capex normalization lifts toward 13–16% |
| Net debt | −$57,381M | −$57,381M | −$57,381M | BS: debt 65,648 − (cash 86,810 + mkt sec 36,219) |
| Diluted shares | 10,827M | 10,827M | 10,827M | IS FY25 |

## 7. EPS DCF Results

### Bear

```
┌───────────────────────────────────────────────────────────────────────┐
│ EPS DCF — Exit Multiple Valuation                                     │
│  EPS: $7.17  │  Growth: 12.0% → 2.5%                                  │
│  Terminal P/E: 22.0x  │  Discount Rate: 9.2%  │  Payout: 3.0%         │
├───────────────────────────────────────────────────────────────────────┤
│ Year │  Growth │  Proj. EPS │  Cash Dist. │  EPS × P/E │  PV of Dist. │
│    1 │   12.0% │ $     8.03 │ $      0.24 │ $   176.67 │ $       0.22 │
│    5 │    7.8% │ $    11.48 │ $      0.34 │ $   252.64 │ $       0.22 │
│   10 │    2.5% │ $    14.38 │ $      0.43 │ $   316.36 │ $       0.18 │
├───────────────────────────────────────────────────────────────────────┤
│  PV of Distributions:   $   2.12   Terminal PV:  $131.33              │
│  >>> Intrinsic Value / Share:       $      133.44                     │
│  Terminal Value Share:                      98.4%                     │
└───────────────────────────────────────────────────────────────────────┘
```

### Base

```
┌───────────────────────────────────────────────────────────────────────┐
│ EPS DCF — Exit Multiple Valuation                                     │
│  EPS: $7.17  │  Growth: 18.0% → 2.5%                                  │
│  Terminal P/E: 30.0x  │  Discount Rate: 9.2%  │  Payout: 3.0%         │
├───────────────────────────────────────────────────────────────────────┤
│ Year │  Growth │  Proj. EPS │  Cash Dist. │  EPS × P/E │  PV of Dist. │
│    1 │   18.0% │ $     8.46 │ $      0.25 │ $   253.82 │ $       0.23 │
│    5 │   11.1% │ $    14.13 │ $      0.42 │ $   423.87 │ $       0.27 │
│   10 │    2.5% │ $    18.83 │ $      0.56 │ $   565.00 │ $       0.23 │
├───────────────────────────────────────────────────────────────────────┤
│  PV of Distributions:   $   2.57   Terminal PV:  $234.54              │
│  >>> Intrinsic Value / Share:       $      237.11                     │
│  Terminal Value Share:                      98.9%                     │
└───────────────────────────────────────────────────────────────────────┘
```

### Bull

```
┌───────────────────────────────────────────────────────────────────────┐
│ EPS DCF — Exit Multiple Valuation                                     │
│  EPS: $7.17  │  Growth: 24.0% → 2.5%                                  │
│  Terminal P/E: 38.0x  │  Discount Rate: 9.2%  │  Payout: 3.0%         │
├───────────────────────────────────────────────────────────────────────┤
│ Year │  Growth │  Proj. EPS │  Cash Dist. │  EPS × P/E │  PV of Dist. │
│    1 │   24.0% │ $     8.89 │ $      0.27 │ $   337.85 │ $       0.24 │
│    5 │   14.4% │ $    17.24 │ $      0.52 │ $   654.96 │ $       0.33 │
│   10 │    2.5% │ $    24.43 │ $      0.73 │ $   928.30 │ $       0.30 │
├───────────────────────────────────────────────────────────────────────┤
│  PV of Distributions:   $   3.12   Terminal PV:  $385.35              │
│  >>> Intrinsic Value / Share:       $      388.47                     │
│  Terminal Value Share:                      99.2%                     │
└───────────────────────────────────────────────────────────────────────┘
```

## 8. Revenue DCF Results

### Bear

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Revenue DCF — Enterprise to Equity Value                                     │
│  Revenue: $716,924M  │  Growth: 8.0% → 2.5%  │  FCFF Margin: 6.0% → 10.0%    │
│  WACC: 9.2%  │  Net Debt: $-57,381M  │  Shares: 10,827M                      │
├──────────────────────────────────────────────────────────────────────────────┤
│   10 │    2.5% │    10.0% │ $    1,194,236 │ $      119,424 │ $       49,575 │
│  PV of FCFF Stream (Stage 1):   $   485,635                                  │
│  Terminal Value (Gordon):        $ 1,829,733      PV:       $   759,555      │
│  Enterprise Value:               $ 1,245,190                                 │
│  Equity Value:                   $ 1,302,571                                 │
│  >>> Intrinsic Value / Share:    $       120.31                              │
│  Terminal Value Share:           61.0%                                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Base

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Revenue DCF — Enterprise to Equity Value                                     │
│  Revenue: $716,924M  │  Growth: 11.0% → 2.5%  │  FCFF Margin: 7.5% → 13.0%   │
│  WACC: 9.2%  │  Net Debt: $-57,381M  │  Shares: 10,827M                      │
├──────────────────────────────────────────────────────────────────────────────┤
│   10 │    2.5% │    13.0% │ $    1,373,248 │ $      178,522 │ $       74,108 │
│  PV of FCFF Stream (Stage 1):   $   690,220                                  │
│  Terminal Value (Gordon):        $ 2,735,206      PV:       $ 1,135,433      │
│  Enterprise Value:               $ 1,825,652                                 │
│  Equity Value:                   $ 1,883,033                                 │
│  >>> Intrinsic Value / Share:    $       173.92                              │
│  Terminal Value Share:           62.2%                                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Bull

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Revenue DCF — Enterprise to Equity Value                                     │
│  Revenue: $716,924M  │  Growth: 14.0% → 2.5%  │  FCFF Margin: 8.0% → 16.0%   │
│  WACC: 9.2%  │  Net Debt: $-57,381M  │  Shares: 10,827M                      │
├──────────────────────────────────────────────────────────────────────────────┤
│   10 │    2.5% │    16.0% │ $    1,574,902 │ $      251,984 │ $      104,603 │
│  PV of FCFF Stream (Stage 1):   $   895,184                                  │
│  Terminal Value (Gordon):        $ 3,860,746      PV:       $ 1,602,664      │
│  Enterprise Value:               $ 2,497,848                                 │
│  Equity Value:                   $ 2,555,229                                 │
│  >>> Intrinsic Value / Share:    $       236.01                              │
│  Terminal Value Share:           64.2%                                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Cross-method divergence (base):** EPS DCF $237 vs Revenue DCF $174 = ~36% gap. The EPS DCF is higher because (a) reported earnings include non-operating income (FY25 had $17.3B of non-op income from equity-investment marks — Rivian, etc.), (b) net interest income on the cash pile adds ~0.5 pp to EPS that isn't in FCFF, and (c) SBC gets "added back" in operating income but is subtracted from our FCFF. The EPS DCF therefore over-credits non-recurring gains, while the Revenue DCF is conservative on capex normalization. Real value likely sits between the two.

## 9. Sensitivity Table (EPS DCF Base, varying Growth × P/E)

```
EPS: $7.17 | Payout: 3% | Terminal Growth: 2.5% | Discount: 9.19%

             18x     22x     26x     30x     34x     38x
---------------------------------------------------------
   10%    $  100   $  122   $  144   $  165   $  187   $  209
   14%    $  120   $  146   $  172   $  198   $  225   $  251
   18%    $  143   $  175   $  206   $  237   $  268   $  300
   22%    $  170   $  208   $  245   $  282   $  319   $  357
   26%    $  202   $  246   $  290   $  334   $  379   $  423
```

At the current price of $247, the market is sitting roughly on the 18%-growth / 30×-P/E cell — which is my base case.

## 10. Analyst Consensus Cross-Check

```
PRICE TARGETS
  Low        $175.00
  Mean       $281.18
  Median     $285.00
  High       $360.00
  (Current:  $247.06)

GROWTH ESTIMATES
  +1y                             21.5%
  LTG                             N/A
```

- **Consensus +1y EPS growth of 21.5% vs my 18% base Yr-1 growth.** The Street is a touch more bullish than I am — consistent with the reverse-DCF implied 20.5%. My base is deliberately a hair more conservative because the 21.5% assumes continued margin expansion that may face wage / AI-infrastructure cost headwinds.
- **Consensus price-target range ($175–$360, mean $281) almost exactly straddles my valuation range** ($133 bear / $237 EPS DCF base / $388 EPS DCF bull). Consensus mean sits between my EPS DCF base ($237) and bull ($388), which is sensible given the Street tends to model the bull case implicitly through peak-cycle margins.
- Divergence is modest and not a red flag — if anything, it suggests my base is slightly conservative, which I accept deliberately given (a) the capex supercycle introduces margin-return risk and (b) regulatory overhang on both retail (antitrust) and AWS (pricing investigations) remains a real discount factor.

## 11. Valuation Summary

### Method weighting

Capex/D&A is 2.0× (investment supercycle) and SBC is ~$19.5B on $80B operating income (~24% of OI). Per the skill's guidance, heavy investment + high SBC → **lean on EPS DCF**. Additionally, the Revenue DCF is dragged down by the near-term FCFF margin compression that is the *point* of the capex cycle (it's an accounting, not an economic, problem). I use **70% EPS DCF / 30% Revenue DCF**.

### Probability weighting

Standard **25% bear / 50% base / 25% bull**. No unusual information to justify skewing.

| Scenario | EPS DCF | Revenue DCF | Method-Weighted (70/30) |
|---|---:|---:|---:|
| Bear | $133.44 | $120.31 | **$129.50** |
| Base | $237.11 | $173.92 | **$218.15** |
| Bull | $388.47 | $236.01 | **$342.73** |

**Probability-weighted fair value**
= 0.25 × $129.50 + 0.50 × $218.15 + 0.25 × $342.73
= $32.38 + $109.08 + $85.68
= **$227.13**

| Metric | Value |
|---|---|
| Current price | **$247.06** |
| Probability-weighted fair value | **$227.13** |
| Upside/(Downside) | **(8.1%)** |
| Range (method-weighted bear → bull) | $130 – $343 |

## 12. Verdict

**FAIRLY VALUED** — 8% downside at current prices is inside the ±25% band.

The market is pricing AMZN near (mildly above) intrinsic value on a probability-weighted basis. The reverse-DCF implied growth of 20.5% is marginally above my 18% base and roughly equal to consensus +1y growth — i.e., the market and the Street are roughly in sync, and I agree with that view within a tight margin. The stock isn't obviously cheap, but a franchise compounding earnings with 18%+ ROIC at ~2× WACC is worth owning near fair value, especially if the AWS / AI investment cycle pays off on the capex base being laid today.

### Upside risks (2–3)
1. **AI/AWS revenue acceleration**: if AI-cloud demand keeps AWS growing 20%+ (vs recent 19%) with margin expansion, both growth and margin assumptions go higher — bull case ($343) becomes plausible.
2. **Advertising scale**: ads are now a ~$70B run-rate business at segment-like 50%+ margins; continued share shift from linear/TV lifts blended operating margin well above 11%.
3. **Capex cycle ends**: if capex/D&A normalizes to 1.2–1.4× by 2028, FCFF margin jumps 4–6 pp and Revenue DCF value rerates sharply toward the EPS DCF value — closing the method gap to the upside.

### Downside risks (2–3)
1. **Capex overbuild**: $132B of 2025 capex is a bet on AI-compute demand. If cloud customers pause, depreciation drags operating margin 200–400 bps (the bear $130 case).
2. **Regulatory / antitrust**: ongoing FTC suit on retail, AWS pricing inquiries, and EU DMA obligations could force structural remedies — pressure on the blended take-rate and ad attach.
3. **Consumer weakness**: retail is ~50% of revenue; a prolonged US consumer slowdown (already some signs in durables) hits the denominator of the flywheel.

### Conviction

**Medium.** The valuation range is wide ($130 to $343 method-weighted) because so much of EPS DCF value sits in the terminal multiple (>98% terminal share) — a structural feature of a low-payout growth compounder. The reverse-DCF, analyst consensus, and my base case all cluster near the current price, giving reasonable confidence that we're near fair value, but small changes in terminal P/E or Year-1 growth move fair value by $50+. This is not a high-conviction mispricing in either direction.
