# META Platforms — DCF Valuation Report

**Date:** March 26, 2026
**Current Price:** $559.14
**Fair Value Estimate:** $750
**Verdict:** UNDERVALUED

---

## 1. Company Overview

Meta Platforms operates the world's largest social media ecosystem — Facebook, Instagram, WhatsApp, and Messenger — serving 3.3B+ daily active users. The company monetizes attention through digital advertising, generating 41%+ operating margins. Meta is in the midst of a massive AI infrastructure build-out ($70B capex in 2025), which depresses near-term free cash flow but positions the company for AI-driven ad targeting improvements and new product lines. Revenue grew from $28B (2016) to $201B (2025), a ~25% CAGR, while maintaining industry-leading profitability.

---

## 2. Financial Snapshot (FY 2025, in $M)

| Metric | Value | Notes |
|--------|-------|-------|
| Revenue | $200,966 | +22% YoY (from $164,501) |
| Operating Income | $83,276 | 41.4% margin |
| Net Income | $60,458 | Depressed by anomalous 29.6% tax rate |
| Diluted EPS | $23.49 | Down from $23.86 in 2024 despite higher revenue |
| Operating CF | $115,800 | +27% YoY |
| CapEx | $69,691 | Nearly doubled YoY ($37,256 in 2024) |
| D&A | $18,616 | |
| SBC | $20,427 | |

**CapEx / D&A = 3.74x** — extreme investment cycle (AI infrastructure). This is not maintenance capex.

**Free Cash Flow (three versions):**

| Version | Amount | Margin | Method |
|---------|--------|--------|--------|
| FCFF actual | $46,109 | 22.9% | OpCF − CapEx |
| FCFF normalized | $97,184 | 48.4% | OpCF − D&A (D&A as maint. capex proxy) |
| FCFF SBC-adjusted | $76,757 | 38.2% | OpCF − D&A − SBC |

Revenue DCF uses SBC-adjusted margin (38.2%) as starting point given capex/D&A >> 2x.

**Payout Ratio:**
- 2025: ($5,324 dividends + $26,248 buybacks) / $60,458 NI = **52.2%**
- 3-year average (2023-2025): **53.1%** → used in model

**Net Debt:** $85,081 debt − $81,592 cash = **$3,489M** (essentially zero leverage)

**ROIC:**
- NOPAT = $83,276 × (1 − 0.296) = $58,626M
- Invested Capital = $217,243 + $85,081 − $81,592 = $220,732M
- **ROIC = 26.6%** (>> 9.33% CAPM — growth creates significant value)

**WACC:**
- E/(E+D) = 94.3%, D/(E+D) = 5.7%
- WACC = 0.943 × 9.33% + 0.057 × 5.0% × (1 − 0.18) = **9.0%**
- Near CAPM since debt is negligible vs. $1.4T market cap

**Tax Rate Flag:** The 2025 effective tax rate of 29.6% is 12+ points above the historical median (~17-18%). The cash flow statement shows $18.7B in deferred income taxes, suggesting timing-related charges. This caused 2025 EPS ($23.49) to fall below 2024 ($23.86) despite a $14B increase in operating income. Starting EPS is conservatively depressed.

---

## 3. EPS & P/E History

```
EPS & P/E Analysis: META
Current shares outstanding: 2,187M (2.19B)
Share basis: year-specific diluted shares (from income statement)

  Year   Net Inc ($M)      EPS  Yr-End Price     P/E  EPS Gr%  P/E Gr%
----------------------------------------------------------------------
  2016 $      10,217 $  3.49 $     114.15   32.7x       --       --
  2017 $      15,934 $  5.39 $     175.09   32.5x    54.3%    -0.6%
  2018 $      22,112 $  7.57 $     130.07   17.2x    40.4%   -47.1%
  2019 $      18,485 $  6.43 $     203.65   31.7x   -15.1%    84.4%
  2020 $      29,146 $ 10.09 $     271.03   26.9x    57.0%   -15.2%
  2021 $      39,370 $ 13.77 $     333.73   24.2x    36.4%    -9.8%
  2022 $      23,200 $  8.59 $     119.40   13.9x   -37.6%   -42.6%
  2023 $      39,098 $ 14.87 $     351.20   23.6x    73.2%    69.8%
  2024 $      62,360 $ 23.86 $     583.17   24.4x    60.4%     3.5%
  2025 $      60,458 $ 23.49 $     659.53   28.1x    -1.5%    14.9%
----------------------------------------------------------------------

SUMMARY
----------------------------------------
EPS CAGR:                   23.6%
Avg YoY EPS Growth:         29.7%
Median YoY EPS Growth:      40.4%
EPS Growth Range:          -37.6% to 73.2%

Avg P/E:                    25.5x
Median P/E:                 25.7x
P/E Range:                  13.9x to 32.7x

Latest EPS:              $  23.49
Latest P/E:                 28.1x
```

---

## 4. Discount Rate

```
CAPM COST OF EQUITY
  Formula:  Rf + Beta x ERP
  Result:   4.38% + 1.28 x 3.87% = 9.33%
```

CAPM of 9.33% is used for the EPS DCF (cost of equity for equity cash flows). WACC of 9.0% is used for the Revenue DCF (enterprise-level FCFF). The two are nearly identical since META's debt-to-capital ratio is only 5.7%.

---

## 5. Reverse DCF — What the Market Implies

```
Reverse DCF — Implied EPS Growth
Price: $559.14 | EPS: $23.49 | Terminal P/E: 24.0x | Discount: 9.3% | Terminal Growth: 3.0% | Payout: 53%

>>> Implied Starting Growth: 10.48% (fading to 3.0%)

  Year   Growth    Proj. EPS    EPS x P/E  PV of Dist.
------------------------------------------------------
     1    10.5% $     25.95 $    622.85 $     12.58
     2     9.7% $     28.46 $    682.97 $     12.62
     3     8.8% $     30.97 $    743.20 $     12.56
     4     8.0% $     33.44 $    802.57 $     12.40
     5     7.2% $     35.83 $    860.01 $     12.16
     6     6.3% $     38.10 $    914.41 $     11.82
     7     5.5% $     40.19 $    964.64 $     11.41
     8     4.7% $     42.07 $   1009.62 $     10.92
     9     3.8% $     43.68 $   1048.31 $     10.37
    10     3.0% $     44.99 $   1079.75 $      9.77
------------------------------------------------------
PV of Distributions:           $      116.62
Terminal Value (EPS x P/E):    $     1079.75
PV of Terminal:                $      442.52
Rebuilt Intrinsic Value:       $      559.14
```

The market prices in **10.5% starting EPS growth** fading to 3%. My base case assumes 15% — I believe the market underestimates META's ability to monetize its AI investments and maintain ad pricing power. The gap is meaningful but not extreme. Note that starting EPS is depressed by the anomalous 29.6% tax rate; if the tax rate normalizes, EPS growth will partially come from tax normalization alone.

---

## 6. Assumptions Table

| Parameter | Bear | Base | Bull | Source |
|-----------|------|------|------|--------|
| Starting EPS | $23.49 | $23.49 | $23.49 | eps_pe.py (FY 2025 diluted) |
| EPS Growth (starting) | 8% | 15% | 22% | CAGR 23.6%; discounted for scale/maturation |
| Terminal P/E | 20x | 24x | 28x | Historical median 25.7x, range 13.9-32.7x |
| Discount Rate (CAPM) | 9.33% | 9.33% | 9.33% | market_data.py |
| Terminal Growth | 3.0% | 3.0% | 3.0% | Below Rf 4.38% |
| Payout Ratio | 53% | 53% | 53% | 3-year average (dividends + buybacks) |
| Starting Revenue | $200,966M | $200,966M | $200,966M | FY 2025 income statement |
| Revenue Growth (starting) | 8% | 14% | 20% | Revenue CAGR ~15% (2016-2025) |
| WACC | 9.0% | 9.0% | 9.0% | Phase 2 computation |
| Starting FCFF Margin | 38.2% | 38.2% | 38.2% | SBC-adjusted (capex/D&A = 3.74x) |
| Target FCFF Margin | 33% | 38% | 42% | Bear: ad margin pressure; Bull: AI scale leverage |
| Net Debt | $3,489M | $3,489M | $3,489M | Debt $85,081 − Cash $81,592 |
| Diluted Shares | 2,574M | 2,574M | 2,574M | FY 2025 diluted shares |

**Scenario Narratives:**
- **Bear (8%):** Ad market slows, regulatory restrictions on data collection reduce targeting effectiveness, Reality Labs/AI capex yields subpar returns. Margins compress as competition intensifies.
- **Base (15%):** Continued ad dominance with AI-enhanced targeting driving pricing power. Capex cycle peaks and begins normalizing. Modest new revenue from AI products.
- **Bull (22%):** AI revolution in ad targeting drives outsized monetization gains. Business messaging, Meta AI, and new products open meaningful revenue streams. Capex efficiency improves as infrastructure scales.

---

## 7. EPS DCF Results

### Bear Case
```
┌───────────────────────────────────────────────────────────────────────┐
│ EPS DCF — Exit Multiple Valuation                                     │
├───────────────────────────────────────────────────────────────────────┤
│  EPS: $23.49  │  Growth: 8.0% → 3.0%                                  │
│  Terminal P/E: 20.0x  │  Discount Rate: 9.3%  │  Payout: 53.0%        │
├───────────────────────────────────────────────────────────────────────┤
│ Year │  Growth │  Proj. EPS │  Cash Dist. │  EPS × P/E │  PV of Dist. │
├───────────────────────────────────────────────────────────────────────┤
│    1 │    8.0% │ $    25.37 │ $     13.45 │ $   507.38 │ $      12.30 │
│    2 │    7.4% │ $    27.26 │ $     14.45 │ $   545.16 │ $      12.09 │
│    3 │    6.9% │ $    29.14 │ $     15.44 │ $   582.71 │ $      11.82 │
│    4 │    6.3% │ $    30.98 │ $     16.42 │ $   619.62 │ $      11.49 │
│    5 │    5.8% │ $    32.77 │ $     17.37 │ $   655.42 │ $      11.12 │
│    6 │    5.2% │ $    34.48 │ $     18.28 │ $   689.64 │ $      10.70 │
│    7 │    4.7% │ $    36.09 │ $     19.13 │ $   721.83 │ $      10.24 │
│    8 │    4.1% │ $    37.58 │ $     19.91 │ $   751.50 │ $       9.76 │
│    9 │    3.6% │ $    38.91 │ $     20.62 │ $   778.22 │ $       9.24 │
│   10 │    3.0% │ $    40.08 │ $     21.24 │ $   801.57 │ $       8.71 │
├───────────────────────────────────────────────────────────────────────┤
│  PV of Cash Distributions:          $      107.46                     │
│  Terminal EPS (Year N):             $       40.08                     │
│  Terminal Value (EPS × P/E):        $      801.57                     │
│  PV of Terminal Value:              $      328.51                     │
│                                                                       │
│  >>> Intrinsic Value / Share:       $      435.97                     │
│  Terminal Value Share:                      75.4%                     │
└───────────────────────────────────────────────────────────────────────┘
```

### Base Case
```
┌───────────────────────────────────────────────────────────────────────┐
│ EPS DCF — Exit Multiple Valuation                                     │
├───────────────────────────────────────────────────────────────────────┤
│  EPS: $23.49  │  Growth: 15.0% → 3.0%                                 │
│  Terminal P/E: 24.0x  │  Discount Rate: 9.3%  │  Payout: 53.0%        │
├───────────────────────────────────────────────────────────────────────┤
│ Year │  Growth │  Proj. EPS │  Cash Dist. │  EPS × P/E │  PV of Dist. │
├───────────────────────────────────────────────────────────────────────┤
│    1 │   15.0% │ $    27.01 │ $     14.32 │ $   648.32 │ $      13.10 │
│    2 │   13.7% │ $    30.71 │ $     16.27 │ $   736.93 │ $      13.61 │
│    3 │   12.3% │ $    34.49 │ $     18.28 │ $   827.82 │ $      13.99 │
│    4 │   11.0% │ $    38.29 │ $     20.29 │ $   918.88 │ $      14.20 │
│    5 │    9.7% │ $    41.99 │ $     22.25 │ $  1007.70 │ $      14.25 │
│    6 │    8.3% │ $    45.49 │ $     24.11 │ $  1091.68 │ $      14.12 │
│    7 │    7.0% │ $    48.67 │ $     25.80 │ $  1168.09 │ $      13.82 │
│    8 │    5.7% │ $    51.43 │ $     27.26 │ $  1234.28 │ $      13.35 │
│    9 │    4.3% │ $    53.66 │ $     28.44 │ $  1287.77 │ $      12.74 │
│   10 │    3.0% │ $    55.27 │ $     29.29 │ $  1326.40 │ $      12.00 │
├───────────────────────────────────────────────────────────────────────┤
│  PV of Cash Distributions:          $      135.18                     │
│  Terminal EPS (Year N):             $       55.27                     │
│  Terminal Value (EPS × P/E):        $     1326.40                     │
│  PV of Terminal Value:              $      543.60                     │
│                                                                       │
│  >>> Intrinsic Value / Share:       $      678.78                     │
│  Terminal Value Share:                      80.1%                     │
└───────────────────────────────────────────────────────────────────────┘
```

### Bull Case
```
┌───────────────────────────────────────────────────────────────────────┐
│ EPS DCF — Exit Multiple Valuation                                     │
├───────────────────────────────────────────────────────────────────────┤
│  EPS: $23.49  │  Growth: 22.0% → 3.0%                                 │
│  Terminal P/E: 28.0x  │  Discount Rate: 9.3%  │  Payout: 53.0%        │
├───────────────────────────────────────────────────────────────────────┤
│ Year │  Growth │  Proj. EPS │  Cash Dist. │  EPS × P/E │  PV of Dist. │
├───────────────────────────────────────────────────────────────────────┤
│    1 │   22.0% │ $    28.66 │ $     15.19 │ $   802.42 │ $      13.89 │
│    2 │   19.9% │ $    34.36 │ $     18.21 │ $   962.01 │ $      15.23 │
│    3 │   17.8% │ $    40.47 │ $     21.45 │ $  1133.03 │ $      16.41 │
│    4 │   15.7% │ $    46.81 │ $     24.81 │ $  1310.54 │ $      17.36 │
│    5 │   13.6% │ $    53.15 │ $     28.17 │ $  1488.19 │ $      18.03 │
│    6 │   11.4% │ $    59.23 │ $     31.39 │ $  1658.51 │ $      18.38 │
│    7 │    9.3% │ $    64.76 │ $     34.32 │ $  1813.30 │ $      18.38 │
│    8 │    7.2% │ $    69.44 │ $     36.80 │ $  1944.27 │ $      18.03 │
│    9 │    5.1% │ $    72.99 │ $     38.68 │ $  2043.64 │ $      17.33 │
│   10 │    3.0% │ $    75.18 │ $     39.84 │ $  2104.95 │ $      16.33 │
├───────────────────────────────────────────────────────────────────────┤
│  PV of Cash Distributions:          $      169.39                     │
│  Terminal EPS (Year N):             $       75.18                     │
│  Terminal Value (EPS × P/E):        $     2104.95                     │
│  PV of Terminal Value:              $      862.68                     │
│                                                                       │
│  >>> Intrinsic Value / Share:       $     1032.07                     │
│  Terminal Value Share:                      83.6%                     │
└───────────────────────────────────────────────────────────────────────┘
```

---

## 8. Revenue DCF Results

### Bear Case
```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Revenue DCF — Enterprise to Equity Value                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│  Revenue: $200,966M  │  Growth: 8.0% → 3.0%  │  FCFF Margin: 38.2% → 33.0%   │
│  WACC: 9.0%  │  Net Debt: $3,489M  │  Shares: 2,574M                         │
├──────────────────────────────────────────────────────────────────────────────┤
│ Year │  Rev Gr │ FCFF Mgn │        Revenue │           FCFF │             PV │
├──────────────────────────────────────────────────────────────────────────────┤
│    1 │    8.0% │    38.2% │ $      217,043 │ $       82,911 │ $       76,065 │
│    2 │    7.4% │    37.6% │ $      233,201 │ $       87,735 │ $       73,845 │
│    3 │    6.9% │    37.0% │ $      249,266 │ $       92,339 │ $       71,303 │
│    4 │    6.3% │    36.5% │ $      265,053 │ $       96,656 │ $       68,473 │
│    5 │    5.8% │    35.9% │ $      280,367 │ $      100,621 │ $       65,396 │
│    6 │    5.2% │    35.3% │ $      295,008 │ $      104,171 │ $       62,114 │
│    7 │    4.7% │    34.7% │ $      308,775 │ $      107,248 │ $       58,668 │
│    8 │    4.1% │    34.2% │ $      321,469 │ $      109,800 │ $       55,105 │
│    9 │    3.6% │    33.6% │ $      332,899 │ $      111,780 │ $       51,467 │
│   10 │    3.0% │    33.0% │ $      342,886 │ $      113,153 │ $       47,797 │
├──────────────────────────────────────────────────────────────────────────────┤
│  PV of FCFF Stream (Stage 1):         $       630,233                        │
│  Terminal Revenue (Year N+1):         $       353,173                        │
│  Terminal FCFF (Year N+1):            $       116,547                        │
│  Terminal Value (Gordon Growth):      $     1,942,452                        │
│  PV of Terminal Value:                $       820,513                        │
│                                                                              │
│  Enterprise Value:                    $     1,450,745                        │
│  Net Debt (debt − cash):              $         3,489                        │
│  Equity Value:                        $     1,447,256                        │
│  Diluted Shares:                               2,574M                        │
│                                                                              │
│  >>> Intrinsic Value / Share:         $        562.26                        │
│  Terminal Value Share:                         56.6%                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Base Case
```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Revenue DCF — Enterprise to Equity Value                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│  Revenue: $200,966M  │  Growth: 14.0% → 3.0%  │  FCFF Margin: 38.2% → 38.0%  │
│  WACC: 9.0%  │  Net Debt: $3,489M  │  Shares: 2,574M                         │
├──────────────────────────────────────────────────────────────────────────────┤
│ Year │  Rev Gr │ FCFF Mgn │        Revenue │           FCFF │             PV │
├──────────────────────────────────────────────────────────────────────────────┤
│    1 │   14.0% │    38.2% │ $      229,101 │ $       87,517 │ $       80,291 │
│    2 │   12.8% │    38.2% │ $      258,375 │ $       98,642 │ $       83,025 │
│    3 │   11.6% │    38.2% │ $      288,232 │ $      109,977 │ $       84,922 │
│    4 │   10.3% │    38.1% │ $      318,016 │ $      121,270 │ $       85,911 │
│    5 │    9.1% │    38.1% │ $      346,991 │ $      132,242 │ $       85,948 │
│    6 │    7.9% │    38.1% │ $      374,364 │ $      142,591 │ $       85,023 │
│    7 │    6.7% │    38.1% │ $      399,322 │ $      152,009 │ $       83,154 │
│    8 │    5.4% │    38.0% │ $      421,063 │ $      160,191 │ $       80,394 │
│    9 │    4.2% │    38.0% │ $      438,841 │ $      166,857 │ $       76,826 │
│   10 │    3.0% │    38.0% │ $      452,006 │ $      171,762 │ $       72,554 │
├──────────────────────────────────────────────────────────────────────────────┤
│  PV of FCFF Stream (Stage 1):         $       818,047                        │
│  Terminal Revenue (Year N+1):         $       465,567                        │
│  Terminal FCFF (Year N+1):            $       176,915                        │
│  Terminal Value (Gordon Growth):      $     2,948,588                        │
│  PV of Terminal Value:                $     1,245,516                        │
│                                                                              │
│  Enterprise Value:                    $     2,063,563                        │
│  Net Debt (debt − cash):              $         3,489                        │
│  Equity Value:                        $     2,060,074                        │
│  Diluted Shares:                               2,574M                        │
│                                                                              │
│  >>> Intrinsic Value / Share:         $        800.34                        │
│  Terminal Value Share:                         60.4%                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Bull Case
```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Revenue DCF — Enterprise to Equity Value                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│  Revenue: $200,966M  │  Growth: 20.0% → 3.0%  │  FCFF Margin: 38.2% → 42.0%  │
│  WACC: 9.0%  │  Net Debt: $3,489M  │  Shares: 2,574M                         │
├──────────────────────────────────────────────────────────────────────────────┤
│ Year │  Rev Gr │ FCFF Mgn │        Revenue │           FCFF │             PV │
├──────────────────────────────────────────────────────────────────────────────┤
│    1 │   20.0% │    38.2% │ $      241,159 │ $       92,123 │ $       84,516 │
│    2 │   18.1% │    38.6% │ $      284,836 │ $      110,010 │ $       92,593 │
│    3 │   16.2% │    39.0% │ $      331,043 │ $      129,254 │ $       99,808 │
│    4 │   14.3% │    39.5% │ $      378,492 │ $      149,378 │ $      105,823 │
│    5 │   12.4% │    39.9% │ $      425,593 │ $      169,764 │ $      110,335 │
│    6 │   10.6% │    40.3% │ $      470,517 │ $      189,671 │ $      113,094 │
│    7 │    8.7% │    40.7% │ $      511,295 │ $      208,267 │ $      113,929 │
│    8 │    6.8% │    41.2% │ $      545,949 │ $      224,689 │ $      112,764 │
│    9 │    4.9% │    41.6% │ $      572,640 │ $      238,091 │ $      109,624 │
│   10 │    3.0% │    42.0% │ $      589,820 │ $      247,724 │ $      104,641 │
├──────────────────────────────────────────────────────────────────────────────┤
│  PV of FCFF Stream (Stage 1):         $     1,047,128                        │
│  Terminal Revenue (Year N+1):         $       607,514                        │
│  Terminal FCFF (Year N+1):            $       255,156                        │
│  Terminal Value (Gordon Growth):      $     4,252,599                        │
│  PV of Terminal Value:                $     1,796,344                        │
│                                                                              │
│  Enterprise Value:                    $     2,843,472                        │
│  Net Debt (debt − cash):              $         3,489                        │
│  Equity Value:                        $     2,839,983                        │
│  Diluted Shares:                               2,574M                        │
│                                                                              │
│  >>> Intrinsic Value / Share:         $       1103.33                        │
│  Terminal Value Share:                         63.2%                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 9. Sensitivity Table

EPS DCF intrinsic value across growth rate (rows) and terminal P/E (columns):

```
Sensitivity Table: EPS DCF Intrinsic Value
EPS: $23.49 | Payout: 53% | Terminal Growth: 3.0% | Discount Rate: 9.3%

┌────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
         │     18x │     20x │     22x │     24x │     26x │     28x │
├────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
      8% │ $   403 │ $   436 │ $   469 │ $   502 │ $   535 │ $   567 │
     10% │ $   439 │ $   475 │ $   511 │ $   548 │ $   584 │ $   620 │
     12% │ $   478 │ $   518 │ $   558 │ $   597 │ $   637 │ $   676 │
     15% │ $   543 │ $   588 │ $   633 │ $   679 │ $   724 │ $   769 │
     18% │ $   615 │ $   667 │ $   718 │ $   770 │ $   822 │ $   874 │
     22% │ $   724 │ $   786 │ $   847 │ $   909 │ $   970 │ $ 1,032 │
└────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

Current price of $559 corresponds roughly to the 10% growth / 26x P/E cell ($584) or the 12% growth / 22x P/E cell ($558), confirming the reverse DCF finding that the market prices in ~10-12% growth.

---

## 10. Comparable Multiples

```
Comparable Company Multiples
======================================================================

Ticker      Mkt Cap     P/E(T)     P/E(F)  EV/EBITDA        P/S     EV/Rev
--------------------------------------------------------------------------
META     $   1,414B      23.8x      15.6x      14.8x       7.0x       7.5x
GOOGL    $   3,452B      26.4x      21.3x      23.0x       8.6x       8.6x
SNAP     $       7B        N/A       7.0x        N/A       1.2x       1.5x
PINS     $      12B      30.0x       8.3x      29.6x       2.9x       2.4x
TTD      $      10B      24.4x       9.2x      13.9x       3.6x       3.3x
AMZN     $   2,280B      29.6x      22.6x      16.0x       3.2x       3.2x
--------------------------------------------------------------------------

GROUP STATISTICS
----------------------------------------
  P/E(T):          Median   26.4x   Range 23.8x - 30.0x
  P/E(F):          Median   12.4x   Range 7.0x - 22.6x
  EV/EBITDA:       Median   16.0x   Range 13.9x - 29.6x
  P/S:             Median    3.4x   Range 1.2x - 8.6x
  EV/Rev:          Median    3.3x   Range 1.5x - 8.6x
```

**Cross-check vs. DCF-implied multiples (base case):**
- DCF base value $727 / EPS $23.49 = **implied 30.9x P/E** — above peer median (26.4x) but within the range. META deserves a premium given its 41% operating margin and 26.6% ROIC, both best-in-class among the peer group.
- META currently trades at 23.8x trailing P/E, the lowest in the peer group — below GOOGL (26.4x), PINS (30.0x), and AMZN (29.6x) despite superior profitability. This supports the undervaluation thesis.
- Forward P/E of 15.6x is notably above the small-cap ad-tech peers (SNAP, PINS, TTD) but below mega-cap peers GOOGL (21.3x) and AMZN (22.6x).

---

## 11. Valuation Summary

**Method Weighting:** Given the extreme investment supercycle (capex/D&A = 3.74x) and substantial SBC ($20.4B), the Revenue DCF's SBC-adjusted starting margin may overstate normalized free cash flow. Leaning **60% EPS DCF / 40% Revenue DCF**.

**Probability Weighting:** 25% Bear / 50% Base / 25% Bull.

| Scenario | EPS DCF | Revenue DCF | Weighted (60/40) |
|----------|---------|-------------|-------------------|
| Bear     | $436    | $562        | $486              |
| Base     | $679    | $800        | $727              |
| Bull     | $1,032  | $1,103      | $1,061            |

**Probability-Weighted Fair Value:**

| Scenario | Weight | Value | Contribution |
|----------|--------|-------|-------------|
| Bear     | 25%    | $486  | $122        |
| Base     | 50%    | $727  | $364        |
| Bull     | 25%    | $1,061| $265        |
| **Fair Value** | | | **$750** |

**Current Price:** $559.14
**Upside to Fair Value:** +34%

---

## 12. Verdict: UNDERVALUED

Meta trades at a meaningful discount to intrinsic value. The market prices in ~10.5% EPS growth, which underestimates the company's ability to monetize its dominant social media platforms through AI-enhanced advertising. The 2025 starting EPS of $23.49 is artificially depressed by an anomalous 29.6% effective tax rate (vs. historical ~17-18%), meaning even modest tax normalization provides an EPS tailwind. With 26.6% ROIC far exceeding the 9.33% cost of equity, every dollar of growth creates substantial value.

**Upside Risks:**
1. Tax rate normalization to historical ~18% levels would immediately boost EPS by ~15% to ~$27, compressing the forward P/E
2. AI-driven ad targeting improvements drive revenue-per-user acceleration beyond base case
3. New revenue streams (business messaging monetization, Meta AI subscriptions, licensing) provide optionality not captured in the base case

**Downside Risks:**
1. Continued massive capex ($70B+ annually) with uncertain returns, particularly Reality Labs and AI infrastructure — destroys value if ROIC declines
2. Regulatory restrictions on data collection/targeted advertising (EU DMA, US privacy legislation) could structurally impair the ad business
3. Competition from TikTok/ByteDance or emerging platforms erodes user engagement and ad pricing power

**Conviction: Medium-High.** The valuation gap is supported by both methods, confirmed by peer comparables (lowest trailing P/E in the group despite best margins), and anchored by a conservatively depressed starting EPS. The primary uncertainty is whether the massive capex program will generate adequate returns.
