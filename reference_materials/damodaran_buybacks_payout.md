# Buybacks, Dividends, and Payout Policy — Damodaran's Framework

## Sources
- "Data Update 8 for 2026: Time for Harvesting - Dividends and Buybacks" (February 24, 2026)
  https://aswathdamodaran.blogspot.com/2026/02/data-update-8-for-2026-time-for.html
- "Stock Buybacks: They are big, they are back and they scare some people!" (September 22, 2014)
  https://aswathdamodaran.blogspot.com/2014/09/stock-buybacks-they-are-big-they-are.html

---

## Core Principle: Payout as Residual

From the 2026 Data Update 8 post:

Cash returns are the "third corporate finance decision" — after investment and financing choices. Damodaran defines the rational approach as **residual**: "dividends should reflect that status and, at least in principle, be set after investing and financing decisions have been made."

The governing metric is **Free Cash Flow to Equity (FCFE)** — cash available after taxes, reinvestment, and debt obligations. Companies should only return what FCFE permits; returning more requires depleting cash reserves or raising capital.

---

## Key Market Data (2025, from the 2026 post)

- US median dividend payout ratio: ~35%
- Global median dividend payout ratio: ~59%
- Less than 30% of US companies pay dividends
- Buybacks exceeded 60% of total US cash returns
- S&P 500 dividend yield represents under 15% of total expected return (down from ~50% in 1960)

---

## Dividend Dysfunction

Nearly 18% of money-losing companies paid dividends. Approximately 37% of cash-returning companies had negative FCFE. This systematic misalignment suggests dividend-focused strategies are problematic.

### Two dysfunction drivers:
1. **Inertia:** Companies set dividends on "auto pilot" — most years show unchanged payouts
2. **Peer pressure:** Firms adopt industry norms regardless of individual circumstances

This creates "dividend monsters" where maintaining dividends warps investment and financing decisions — leading to rejected good projects or excessive borrowing.

---

## Buyback Myths Damodaran Dismisses

From the 2014 post:

1. **"Buybacks destroy value if stock is overpriced":** Wrong. Buybacks transfer wealth between selling and remaining shareholders. They neither create nor destroy value at any price — wealth is merely redistributed.

2. **"Fewer shares always increases EPS":** Only true if the buyback doesn't reduce firm value proportionally. Leverage effects matter. The share count effect is "the red herring of buyback analysis, a number that looks profoundly meaningful at first sight but is useless in assessing the effect of a buyback."

3. **"Buybacks funded by debt are dangerous":** Aggregate debt ratios have *declined* despite rising buybacks. Buyback firms have lower leverage than non-buyback peers.

### Buybacks' Flexibility Advantage
Companies can reverse buybacks during downturns (as in 2008, 2020), whereas dividend cuts signal distress. This flexibility is a genuine economic benefit.

---

## Modeling Buybacks in DCF

From the 2014 post — Damodaran identifies a critical modeling error:

### Flawed Method
```
FCFE per share = (Cash from Ops - CapEx) / Current Share Count
```
...while simultaneously assuming the company will buy back shares. This double-counts: you're getting the cash flow benefit of buybacks without paying for them.

### Correct Methods

**Method A (Damodaran's preferred for FCFE models):**
Use total cash flows to equity holders (dividends + buybacks), don't reduce share count.
```
Cash to equity = Dividends + Buybacks
Value per share = PV of future cash to equity / Current shares
```

**Method B (if modeling share count explicitly):**
```
Adjusted FCFE = (Cash from Ops) - (CapEx) - (Cash used for buybacks)
Adjusted shares = Current shares - Cumulative shares repurchased
Value per share = PV of adjusted FCFE / Adjusted shares
```

Both give the same answer. You must not mix them (use Method A cash flows with Method B share counts).

### P/E Ratio Changes After Buybacks
Buybacks alter a firm's risk profile and should change its P/E ratio. Analysts often apply constant P/E multiples when projecting post-buyback prices — this is analytically incorrect. The P/E typically declines following a buyback because financial leverage changes.

### Net vs. Gross Buybacks
Always use net figures that deduct stock issuances (for employee compensation) from gross buybacks. Damodaran's data: net cash yield was 3.16% vs gross cash yield of 4.49% at end of 2013.

---

## Life Cycle Expectations for Payout

From the 2026 post:

- **Start-ups:** Negative FCFE; require equity infusions. No payout.
- **Young growth:** Self-funding but insufficient FCFE for dividends. No payout.
- **Mature growth:** Positive FCFE; prefer buybacks for flexibility.
- **Stable mature:** Ideal dividend payers; large predictable earnings, minimal reinvestment needs.

Companies refusing to "act their age" damage shareholders.

### Key Warning
"Any investing strategy built around cash return, whether dividends or buybacks, is likely to go off the tracks." Stocks aren't bonds.

---

## Implications for This Project

1. **Constant payout ratio is problematic.** The EPS DCF holds payout constant at, say, 53% for all 10 years. As growth fades from 15% to 3%, reinvestment needs decline and sustainable payout increases. Holding payout constant at 53% while growing at 3% means retaining 47% of earnings — implying extremely low ROIC on marginal capital, or an ever-growing cash pile.

2. **Revenue DCF share count.** The Revenue DCF divides equity value by current diluted shares. For aggressive repurchasers (FICO at 217% payout), future per-share value is significantly higher than today's share count implies. Damodaran would say: either model the declining share count (Method B), or use total equity cash flows without adjusting shares (Method A). The Revenue DCF does neither.

3. **Payout > 100% of net income.** FICO's 217% payout is debt-funded. Damodaran would say: payout should be bounded by FCFE, not net income. The project correctly identifies this as unsustainable and normalizes, but the formalization should reference FCFE as the constraint, not just net income.

4. **Net vs. gross buybacks.** The project uses gross buyback figures from the cash flow statement. Should ideally net out stock issuances for SBC.
