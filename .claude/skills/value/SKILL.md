---
name: value
description: Perform a full DCF valuation of a public company and produce a valuation report. Use when the user asks to value or analyze a stock ticker.
argument-hint: "[TICKER]"
allowed-tools: Bash, Read, Write, Glob, Grep
---

# Stock Valuation: $ARGUMENTS

Perform a full DCF valuation for **$ARGUMENTS** and produce `reports/$ARGUMENTS/valuation.md`.

## Tools

### Data Tools
| Tool | Command | Purpose |
|------|---------|---------|
| Three Statements | `.venv/bin/python company_info/three_statements.py --ticker $ARGUMENTS --years 10` | Income statement, cash flow, balance sheet from SEC EDGAR (10 years) |
| Market Data & CAPM | `.venv/bin/python company_info/market_data.py --ticker $ARGUMENTS` | Risk-free rate, beta, ERP, CAPM cost of equity, terminal growth ceiling |
| EPS & P/E History | `.venv/bin/python company_info/eps_pe.py --ticker $ARGUMENTS --net-income 'JSON'` | 10-year EPS, P/E, growth rates, averages from net income + yfinance prices |
| Analyst Estimates | `.venv/bin/python company_info/analyst_estimates.py --ticker $ARGUMENTS` | Consensus EPS, revenue, growth estimates, price targets (verification cross-check ONLY) |

### Calculator Tools
| Tool | Command | Purpose |
|------|---------|---------|
| EPS DCF | `.venv/bin/python calculators/eps_dcf.py --eps N --growth N --pe N --discount-rate N --terminal-growth N --payout-ratio N --years 10` | EPS exit-multiple valuation |
| Revenue DCF | `.venv/bin/python calculators/revenue_dcf.py --revenue N --revenue-growth N --wacc N --terminal-growth N --fcff-margin N --target-fcff-margin N --net-debt N --diluted-shares N --years 10` | Revenue/margin DCF → enterprise → equity value |
| Reverse DCF | `.venv/bin/python calculators/reverse_dcf.py --price N --eps N --pe N --discount-rate N --terminal-growth N --payout-ratio N --years 10` | Implied growth rate from current price (sanity check) |
| Sensitivity | `.venv/bin/python calculators/sensitivity.py --eps N --payout-ratio N --terminal-growth N --years 10 --axis "growth x pe" --growth "list" --pe "list" --discount-rate N` | Two-way sensitivity table for EPS DCF |

All CLI flags must be passed explicitly. The tools crash in non-interactive mode if flags are missing.

## Execution

### Phase 1: Gather Data

Run these tools (first two in parallel):

1. `.venv/bin/python company_info/three_statements.py --ticker $ARGUMENTS --years 10`
2. `.venv/bin/python company_info/market_data.py --ticker $ARGUMENTS`

Then read `reports/$ARGUMENTS/three_statements.txt` and extract net income for each year (from the income statement, in millions). Run:

3. `.venv/bin/python company_info/eps_pe.py --ticker $ARGUMENTS --net-income '{YEAR: NET_INCOME, ...}'`

If any tool fails, check the error. Common causes: missing .env SEC_IDENTITY, ticker not found, yfinance rate limit. Retry once, then work with what you have.

### Phase 2: ultrathink — Read and Analyze the Financial Statements

**This is the most important phase. Think deeply and carefully.**

Read `reports/$ARGUMENTS/three_statements.txt` and extract everything below. Do not rush this. Cross-reference numbers between statements to catch errors.

#### From the Income Statement:
- Revenue (latest year + trend over 10 years)
- Operating income and operating margin
- Net income
- Provision for income taxes and pretax income → effective tax rate
- Diluted EPS and diluted shares

**Tax rate check**: Compare the latest year's effective tax rate to prior years. If the latest year deviates more than 8 percentage points from the historical median, flag it — net income may be distorted by one-time tax items.

#### From the Cash Flow Statement:
- Net cash from operations (operating cash flow)
- Capital expenditure (purchases of property and equipment)
- Depreciation and amortization
- Stock-based compensation
- Dividends paid
- Share buybacks (repurchases of common stock)

#### From the Balance Sheet:
- Cash and cash equivalents (+ short-term investments/marketable securities if listed)
- Total debt (long-term debt + current portion + commercial paper if any)
- Stockholders' equity
- Shares outstanding

#### Compute These Derived Metrics:

**CapEx / D&A ratio:**
```
capex_to_da = Capital Expenditure / Depreciation & Amortization
```
This tells you if the company is in maintenance mode (~1x) or an investment cycle (>2x).

**Free Cash Flow (three versions):**
```
FCFF actual     = Operating CF - CapEx
FCFF normalized = Operating CF - D&A        (D&A as maintenance capex proxy)
FCFF SBC-adj    = Operating CF - D&A - SBC  (true cash to equity holders)
```
Compute the margin for each: FCFF / Revenue x 100.

For the Revenue DCF starting margin:
- If capex/D&A is near 1x: use actual FCFF margin
- If capex/D&A is 1.5-2x: use average of actual and SBC-adjusted margins
- If capex/D&A is above 2x: use SBC-adjusted FCFF margin

**Payout ratio:**
```
payout_ratio = (Dividends Paid + Share Buybacks) / Net Income x 100
```
Compute for latest year and as a multi-year average.

**Net debt:**
```
net_debt = Total Debt - Cash & Investments
```
Negative = net cash position.

**ROIC:**
```
NOPAT = Operating Income x (1 - Tax Rate)
Invested Capital = Equity + Total Debt - Cash
ROIC = NOPAT / Invested Capital x 100
```
Compare ROIC to the CAPM discount rate. If ROIC >> discount rate, growth creates value.

#### Extraction Checkpoint

Before proceeding, verify your extractions:
- Does net income from the income statement match net income on the cash flow statement?
- Does operating CF - capex roughly equal the FCFF you computed?
- Do shares outstanding from the balance sheet roughly match diluted shares from eps_pe.py?
- Does total debt - cash roughly equal net debt?

If anything is off by more than 10%, re-read the statements and find the discrepancy.

### Phase 3: ultrathink — Set Assumptions

**Every assumption must trace to data from tool outputs or your Phase 2 analysis.**

Think carefully about what story the data tells. What is this business? Why does it earn what it earns? What could change?

#### Discount Rate
- Use the CAPM cost of equity from `market_data.py`
- Use the same rate for both EPS DCF (`--discount-rate`) and Revenue DCF (`--wacc`)

#### Terminal Growth Rate
- Must be strictly below the risk-free rate shown in `market_data.py`
- Typically 1-2 percentage points below the risk-free rate
- Same across all scenarios and both methods

#### Payout Ratio (for EPS DCF)
- Use the payout ratio you computed in Phase 2
- Same across all scenarios

#### FCFF Margin (for Revenue DCF)
- Use the appropriate margin from Phase 2 based on capex/D&A
- `target-fcff-margin`: where margins settle once investment normalizes — anchor to the SBC-adjusted FCFF margin

#### Other Inputs
- `eps`: latest EPS from `eps_pe.py`
- `revenue`, `net-debt`, `diluted-shares`: from Phase 2 (in millions)
- EPS/revenue growth: anchor to `eps_pe.py` CAGR/median and revenue trends
- Terminal P/E: anchor to the stock's own historical P/E from `eps_pe.py` (bear = low end of range, base = median, bull = high end)

#### Scenario Guidelines
- Bear = realistic downside ("if things go somewhat wrong")
- Bull = realistic upside ("if tailwinds persist")
- Base = honest best estimate, not split-the-difference
- If ROIC >> WACC, growth creates value — bear case should still reflect franchise value
- If tax rate is anomalous, consider adjusting starting EPS

### Phase 4: Run Reverse DCF (Sanity Check)

Before running forward DCFs, check what the market is pricing in:

```
calculators/reverse_dcf.py --price [CURRENT_PRICE] \
    --eps [LATEST_EPS] --pe [BASE_TERMINAL_PE] \
    --discount-rate [CAPM] --terminal-growth [TG] \
    --payout-ratio [PAYOUT] --years 10
```

This tells you the starting EPS growth rate the market implies. Compare to your base case growth:
- Implied ~ base → fairly valued
- Implied >> base → market expects more than you do
- Implied << base → market expects less than you do

This is a CHECK, not an input. Do not change your assumptions to match.

### Phase 5: Run Forward DCFs

Run **6 DCF calculations** (3 scenarios x 2 methods). Run in parallel.

### Phase 6: Run Sensitivity Table

```
calculators/sensitivity.py --eps [EPS] --payout-ratio [PAYOUT] \
    --terminal-growth [TG] --years 10 \
    --axis "growth x pe" \
    --growth "[range from bear to bull growth]" \
    --pe "[range from bear to bull P/E]" \
    --discount-rate [CAPM]
```

### Phase 7: ultrathink — Verify Everything

**Do not skip this. Go slow and check your work.**

1. **Arithmetic spot-check**: Pick the base case EPS DCF output.
   - Verify: Year 1 EPS = starting_eps x (1 + year_1_growth_rate). Does it match?
   - Verify: Terminal value = Year 10 EPS x terminal P/E. Does it match?
   - Verify: PV of terminal = terminal_value / (1 + discount_rate)^10. Does it match?
   - If ANY check fails, you have a data entry error. Find and fix it.

2. **Input consistency**:
   - EPS from eps_pe.py x shares from Phase 2 should approximate net income from the statements
   - Net debt from Phase 2 should match total debt - cash from the balance sheet
   - Revenue used in Revenue DCF should match the latest year from the income statement

3. **Cross-method check**: If EPS DCF and Revenue DCF base cases diverge by more than 50%:
   - Is FCFF margin properly adjusted for the capex cycle?
   - Is payout ratio correct and non-zero?
   - Are all Revenue DCF inputs in millions (not raw dollars or billions)?
   - Explain the divergence in the report

4. **Reasonableness**:
   - Year 10 projected EPS x terminal P/E = implied future stock price. Could this company actually trade there?
   - Year 10 revenue in Revenue DCF: is it plausible given the company's market?
   - If fair value is less than 25% of current price, or more than 400%, double-check all inputs before proceeding

5. **Bias check**: Re-read your assumptions.
   - Are you being systematically conservative (low growth, low P/E, high discount rate)?
   - Are you being systematically aggressive (high growth, high P/E, low discount rate)?
   - Does the reverse DCF implied growth confirm your assumptions are in a reasonable range?

6. **Analyst consensus cross-check**: Run the analyst estimates tool:
   ```
   .venv/bin/python company_info/analyst_estimates.py --ticker $ARGUMENTS
   ```
   **This is a CHECK, not an input. Do not revise your assumptions to match consensus.**
   - Compare your base-case EPS growth to the Street's next-5Y growth estimate
   - Compare your base-case revenue trajectory to consensus revenue estimates
   - Compare your fair value range to analyst price targets
   - If your assumptions diverge significantly from consensus, that's fine — but explain WHY in the report (you may see something the Street doesn't, or vice versa)
   - If consensus data is unavailable for this ticker, skip this step

### Phase 8: Write the Report

Create `reports/$ARGUMENTS/valuation.md` with these sections:

1. **Company Overview** (3-5 sentences)
2. **Financial Snapshot** — key data from the statements: revenue trend, margins, capex/D&A, FCFF margins (all three versions), payout ratio, net debt, ROIC. Show your arithmetic.
3. **EPS & P/E History** — paste eps_pe.py output in code fence
4. **Discount Rate** — paste market_data.py CAPM section, one sentence on why it's appropriate
5. **Reverse DCF** — paste output, compare implied growth to your base case
6. **Assumptions Table** — every parameter, every scenario, with source

| Parameter | Bear | Base | Bull | Source |
|-----------|------|------|------|--------|
| ... | ... | ... | ... | (tool or computation) |

7. **EPS DCF Results** — bear/base/bull in code fences
8. **Revenue DCF Results** — bear/base/bull in code fences
9. **Sensitivity Table** — in code fence
10. **Analyst Consensus Cross-Check** — if data was available, show: consensus next-5Y growth vs your base case, consensus revenue vs your projections, price target range vs your fair value range. One paragraph on where you agree/disagree with the Street and why. If no data, omit this section.
11. **Valuation Summary**

For method weighting: explain your reasoning based on capex/D&A and SBC. Investment supercycle with high SBC → lean on EPS DCF. Maintenance mode with low SBC → weight equally.

For probability weighting: use 25% bear / 50% base / 25% bull, or justify a different split.

| Scenario | EPS DCF | Revenue DCF | Weighted |
|----------|---------|-------------|----------|
| Bear     | $X      | $X          | $X       |
| Base     | $X      | $X          | $X       |
| Bull     | $X      | $X          | $X       |

12. **Verdict** — UNDERVALUED (>25% upside) / FAIRLY VALUED (within 25%) / OVERVALUED (>25% downside)
    - 3-5 sentence explanation
    - Upside risks (2-3 specific)
    - Downside risks (2-3 specific)
    - Conviction: High / Medium / Low

## Rules

- All outputs go in `reports/$ARGUMENTS/` — three_statements.txt and eps_pe.txt are auto-generated, you write valuation.md
- All dollar amounts from the three statements are in **millions**
- Revenue DCF inputs (`revenue`, `net-debt`, `diluted-shares`) must all be in millions
- EPS DCF inputs are per-share — no unit conversion needed
- **Every number must trace to a tool output or your own arithmetic.** If you can't cite it, don't use it
- Do NOT hallucinate financial data
- Preserve box-drawing calculator output in code fences
- Do NOT tune assumptions to reach a predetermined conclusion — set assumptions from data, then see where value lands
- The report must be self-contained — a reader understands the full analysis without running tools
- **Do not skip the verification phase.** If checks fail, fix inputs before writing the report
