# Terminal Value — Damodaran's Framework

## Sources
- "Myth 5.5: The Terminal Value ate my DCF!" (November 30, 2016)
  https://aswathdamodaran.blogspot.com/2016/11/myth-55-terminal-value-ate-my-dcf.html
- "Myth 5.3: Growth is good, more growth is better!" (November 30, 2016)
  https://aswathdamodaran.blogspot.com/2016/11/myth-53-growth-is-good-more-growth-is.html
- "Myth 5.2: As g-> r...To Infinity and Beyond!" (November 30, 2016)
  https://aswathdamodaran.blogspot.com/2016/11/myth-52-as-g-rto-infinity-and-beyond.html
- "Myth 5.4: Negative Growth Rates forever? Impossible!" (November 30, 2016)
  https://aswathdamodaran.blogspot.com/2016/11/myth-54-negative-growth-rates-forever.html

---

## Terminal Value as % of Total Value

Damodaran argues high terminal value proportions are **normal and healthy**, not a flaw.

From Myth 5.5:
- "you should not be surprised to see the terminal value in your DCF account for a high percentage of value"
- "it is when it does NOT account for the bulk of the value that you should be wary"
- Historical data (1928-2015): approximately 67-70% of US stock returns came from price appreciation rather than dividends — so terminal value naturally dominates

**How terminal value % varies:**
- 0% excess growth, ROE = CoE: terminal value ≈ 75% of total value
- 10% excess growth, ROE = CoE: terminal value ≈ 122% (can exceed 100%)
- Higher reinvestment needs → lower/negative early cash flows → higher TV %
- Growth companies with low/negative early cash flows can have TV > 100% — this is fine

**Critical insight:** Higher terminal value % means you should pay MORE attention to growth period assumptions, not less. Terminal value is determined by Year N earnings (end of growth period) and the returns earned during high growth. Changing growth period assumptions significantly impacts the terminal year baseline.

---

## Terminal Growth Rate Constraints

From Myth 5.2 — the growth cap is "not a debatable assumption, since it is mathematical, not one that owes its presence to economic theory."

### The Cap
Terminal growth cannot exceed the economy's growth rate. When g approaches r, valuations approach infinity — "Buzz Lightyear valuations."

### Three Factors for Setting the Cap

1. **Geographic scope:** Use domestic economy growth for domestic operators; global growth for international companies. Emerging markets converge toward global averages (~2%) over time.

2. **Real vs. nominal:** Growth must match cash flow terms. Real cash flows need real growth caps; nominal cash flows need nominal caps.

3. **Currency:** High-inflation currencies can justify higher nominal perpetual growth.

### Risk-Free Rate as Proxy

Rather than forecasting GDP growth, Damodaran recommends the risk-free rate as the cap:

**Empirical evidence:** Historical US data (1954-2015): nominal GDP growth averaged 0.74% above the 10-year Treasury rate. They are "closely tied" over long periods.

**Consistency rationale:** Using a low risk-free rate (2% or lower) while assuming high nominal growth (5-6%) creates dangerous mismatches. "That is a recipe for disaster" when central banks suppress rates artificially.

**Self-control rationale:** Terminal growth rate offers maximum leverage for analyst bias. Anchoring to an observable market rate removes "the most potent vehicle for bias in valuation."

**Practical guidance:**
- Never allow perpetual growth to exceed the risk-free rate in your chosen currency
- A more permissive variant allows growth **up to 1% above the risk-free rate**, but not beyond
- Ignoring the growth cap "represents one of the greatest perils in valuation"

**Note:** Damodaran is actually more permissive than our project. He allows terminal growth UP TO the risk-free rate (or even 1% above). Our SKILL.md says "strictly below" and "typically 1-2 percentage points below." Our approach is more conservative, which is fine but not required by Damodaran.

---

## Growth, ROIC, and Value Creation

From Myth 5.3 — the fundamental relationship:

### The Core Formula
```
Growth Rate = Reinvestment Rate × Return on Invested Capital (ROIC)
```

You cannot increase growth while holding cash flows constant — higher growth demands more reinvestment, which reduces available cash flows.

### When Growth Creates vs. Destroys Value
Increasing growth from 0% to 3%:
- **Decreases value** when ROIC < cost of capital
- **Unchanged value** when ROIC = cost of capital
- **Increases value** only when ROIC > cost of capital

"It is not the growth rate per se, but the excess returns (the difference between return on invested capital and the cost of capital) that drives value."

### Two Critical Errors in DCF Practice

**Error 1: Growing Year-N Cash Flow Linearly**
Simply extending the final year's cash flow at a terminal growth rate locks in an incompatible reinvestment rate. Damodaran showed this approach undervalued a company by roughly 50% compared to properly recalculating terminal year cash flows.

**Correct approach for terminal value:**
```
Terminal reinvestment rate = terminal growth / terminal ROIC
Terminal FCFF = Terminal NOPAT × (1 - terminal reinvestment rate)
Terminal Value = Terminal FCFF / (WACC - g)
```

**Error 2: Zero Reinvestment in Stable Growth**
Assuming capex = depreciation with positive growth rates is mathematically inconsistent. It produces ROIC approaching infinity, which is nonsensical. If you grow, you must reinvest.

### Practical Modeling

For terminal value, reinvestment must reflect the sustainable growth rate. Damodaran recommends assuming excess returns gradually decline toward zero for mature companies, with adjustments based on competitive advantages.

---

## Negative Growth

From Myth 5.4:
- ~40% of all companies (US and global) saw revenues decline in 2015
- ~25% experienced declining revenues over 2006-2015
- Sectors with high decline rates: publishing, computers, consumer electronics, steel

The perpetual growth formula remains valid with negative growth rates. Terminal value with negative growth depends critically on asset liquidation — if assets can be divested above continuing-operation value, negative growth can actually increase firm value.

Refusing to model negative growth biases valuations upward.

---

## Implications for This Project

1. **Terminal reinvestment consistency:** The Revenue DCF (`revenue_dcf.py`) takes Year 10 FCFF and grows it by terminal growth without recalculating reinvestment. Per Damodaran, this can undervalue by ~50%. The fix: compute terminal reinvestment rate = g / ROIC, then terminal FCFF = terminal NOPAT × (1 - RR).

2. **Terminal value %:** The project reports TV share (e.g., META 80.1%). Per Damodaran, this is completely normal. The SKILL.md should note that TV > 70% is expected, and TV > 100% is possible for high-growth companies with heavy reinvestment.

3. **Growth cap:** The project's cap (below Rf) is more conservative than Damodaran requires (up to Rf, or even Rf + 1%). This creates a conservative bias but is defensible.

4. **Negative growth:** The project can't model declining companies. The reverse DCF lower bound is terminal growth — can't solve for implied growth below terminal. The linear fade model only goes high → low.
