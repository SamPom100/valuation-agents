# Damodaran's Published Data Sources

## Sources
- All 2026 Data Update posts (January-February 2026)
- "The Price of Risk: An Equity Risk Premium Monologue!" (March 15, 2026)
  https://aswathdamodaran.blogspot.com/2026/03/the-price-of-risk-equity-risk-premium.html
- Various blog posts referencing his datasets

---

## Primary Website
pages.stern.nyu.edu/~adamodar/

Damodaran publishes comprehensive datasets updated annually (typically in January-February after year-end data is available).

---

## Key Datasets Relevant to This Project

### Implied Equity Risk Premium
- **Monthly data since September 2008**
- Location: pages.stern.nyu.edu/~adamodar/pc/implprem/ERPbymonth.xlsx
- Also: S&P 500 ERP computation spreadsheet (most recent noted: Feb 27, 2026)
- Contains: implied ERP, Treasury rates, expected returns, cash yields
- Updated monthly

### Industry Data
Damodaran maintains industry-level averages for ~100 industry groupings across:
- **Betas** (unlevered and levered, by industry)
- **Cost of capital / WACC** (by industry and region)
- **Debt ratios** (market value and book value)
- **Operating margins**
- **ROIC / ROE**
- **Revenue growth rates**
- **Payout ratios** (dividends and buybacks)
- **Effective tax rates**

These are computed from his sample of 48,156 publicly traded companies globally.

### Country Risk Premiums
- Country-specific ERPs for international valuations
- Referenced in multiple posts but specific URLs not captured from blog

---

## Data Methodology Notes (from Data Update 1, 2026)

- Damodaran uses **aggregated values** (total market cap / total net income) rather than simple averages of individual company ratios — avoids distortion from outliers
- Reports industry averages, not individual company data
- Adjusts debt ratios for lease capitalization per his methodology
- US dominance in dataset: $69.8 trillion market cap (46.8% of global total) out of 48,156 companies
- Historical returns data covers 1928-2025

---

## Key Numbers from 2026 Updates

| Metric | Value | Source Post |
|--------|-------|-------------|
| Implied ERP (Jan 1, 2026) | 4.23% | Data Update 2 |
| Expected stock return (Jan 1, 2026) | 8.41% | Data Update 2 |
| 10Y Treasury rate (Jan 1, 2026) | 4.18% | Data Update 2 |
| S&P 500 level (Jan 1, 2026) | 6,845.5 | Data Update 2 |
| Historical ERP (1928-2025) | 7.03% (SE: 2.05%) | Data Update 1 |
| US WACC range (80th percentile) | 5.26% - 9.88% | Data Update 5 |
| Global WACC range (80th percentile) | 6.28% - 11.66% | Data Update 5 |
| US median dividend payout ratio (2025) | ~35% | Data Update 8 |
| Global median dividend payout ratio (2025) | ~59% | Data Update 8 |
| Buybacks as % of US cash returns (2025) | >60% | Data Update 8 |
| % of global firms with ROE > CoE | 29% | Data Update 6 |
| % of global firms with ROIC > CoC | 28% | Data Update 6 |
| S&P 500 ROE (2022) | 19.73% | ERP Aug 2023 post |
| S&P 500 ROE (decade avg) | 17.04% | ERP Aug 2023 post |

---

## Update Schedule

Damodaran publishes a series of "Data Updates" each January/February covering:
1. Data overview and market summary
2. Equity returns and ERP
3. Bonds, currencies, gold, bitcoin
4. Global perspective
5. Risk and hurdle rates (WACC, betas)
6. Profitability (margins, ROIC, ROE)
7. Debt and taxes
8. Dividends and buybacks

He also publishes the implied ERP monthly and updates industry datasets annually.

---

## Potential Integration with This Project

The most impactful dataset to integrate would be the monthly implied ERP spreadsheet. Options:

1. **Direct fetch:** Download the Excel file programmatically and extract the latest monthly ERP. This would replace the earnings yield approach in `market_data.py`.

2. **Manual update:** Periodically check his website and update a local reference value. Less automated but simpler.

3. **Industry betas:** Could replace yfinance regression betas with Damodaran's industry averages. Would require the agent to know the company's industry classification (available from yfinance `info.sector`).

4. **WACC plausibility check:** Use the 5.26%-9.88% range for US companies as a sanity check on computed WACC.
