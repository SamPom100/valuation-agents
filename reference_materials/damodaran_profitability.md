# Profitability, ROIC, and Value Creation — Damodaran's Framework

## Sources
- "Data Update 6 for 2026: In Search of Profitability" (February 2026)
  https://aswathdamodaran.blogspot.com/2026/02/data-update-6-for-2026-in-search-of.html
- "Myth 5.3: Growth is good, more growth is better!" (November 30, 2016)
  https://aswathdamodaran.blogspot.com/2016/11/myth-53-growth-is-good-more-growth-is.html
- "The Corporate Life Cycle: Managing, Valuation and Investing Implications!" (August 19, 2024)
  https://aswathdamodaran.blogspot.com/2024/08/the-corporate-life-cycle-corporate.html

---

## Three Profit Metrics

From Data Update 6:

1. **Gross Margin** — reflects "unit economics"
2. **Operating Margin** — reflects "economies of scale"
3. **Net Margin** — reflects effects of "taxes" plus "debt choices"

2025 aggregate data:
- Global firms: $6.2 trillion net income on $72.4 trillion revenue
- US firms: $2.2 trillion net income on $22.7 trillion revenue

---

## Return Metrics: ROE and ROIC

Damodaran emphasizes that profitability alone (margins) sets the bar too low. Accounting returns — ROE and ROIC — measure whether capital is being used well.

### The Fundamental Value Creation Principle
"Value creation requires a business to generate a return on its equity (capital) that exceeds its cost of equity (capital)."

**Excess returns** = difference between accounting returns and their corresponding cost of capital.

### How Rare Value Creation Is (2025 data)
- Only 29% of global firms earn ROE exceeding their cost of equity
- Only 28% generate ROIC above their cost of capital
- When raising the threshold to 5%+ excess returns: only 19% (ROE) and 17% (ROIC)

Most companies do NOT create value through growth.

### Limitations of Accounting Returns
- Can be "skewed not just by accounting inconsistencies" but also by write-offs
- Damodaran acknowledges an extensive paper detailing "how accounting returns deviate from reality"
- Negative book equity (e.g., FICO) makes ROIC calculations less meaningful

---

## Competitive Advantages and Moats

From Data Update 6:
- Competitive advantages (moats) determine whether companies sustain excess returns
- "Moats have crumbled" over four decades due to global competition and disruption
- Investors should assume margin compression when projecting future cash flows

This directly impacts terminal value: if moats erode, terminal ROIC should converge toward WACC, not stay elevated.

---

## Corporate Life Cycle and Valuation

From the August 2024 post:

Damodaran views valuation as "a bridge between stories and numbers" where "the balance between stories and numbers will shift, as you move through the life cycle."

### Young/Growth Companies
- Growth rates: very high but highly uncertain (story-driven)
- Profitability: often negative or minimal
- Reinvestment: substantial, with negative free cash flows
- Valuation challenge: absent historical data, narratives drive valuations more than fundamental models

### Mature Companies
- Growth rates: lower, grounded in demonstrated performance
- Margins: established and more predictable
- Reinvestment: declining relative to revenues
- Analyst strength: "number-crunchers" comfortable with accounting ratios excel here

### Declining Companies
- Terminal value: becomes critical since long-term growth assumptions are pessimistic
- Focus: cash return policy dominates valuation considerations
- Pricing metrics: book value multiples become more common
- Management quality should match stage: "pragmatism and mercantilism" — disciplined asset management and cash harvesting

Key distinction: "pricing an asset can give you a very different number than valuing that asset"

---

## Growth and Reinvestment Linkage

From Myth 5.3 (also referenced in terminal_value.md):

```
Sustainable Growth Rate = Reinvestment Rate × ROIC
```

Implications for terminal value modeling:
- If terminal growth = 3% and ROIC = 15%, then reinvestment rate = 3/15 = 20%
- If terminal growth = 3% and ROIC = 8%, then reinvestment rate = 3/8 = 37.5%
- A company with ROIC = WACC creates zero value from growth — the growth exactly funds reinvestment
- Only excess returns (ROIC > WACC) create value through growth

---

## Implications for This Project

1. **ROIC check is correct.** The project computes ROIC and compares to WACC. This aligns with Damodaran's emphasis on excess returns as the value creation metric.

2. **Terminal ROIC should decay.** For the Revenue DCF's Gordon Growth terminal value, the agent should consider whether terminal ROIC remains elevated or converges toward WACC. For companies like FICO (67% ROIC), some convergence is prudent — even great moats erode per Damodaran.

3. **Life cycle awareness.** The project treats all companies with the same model (10-year fade). Damodaran would adjust methodology by stage — young growth companies need longer growth periods, declining companies need negative growth capability, and mature companies are ideal for the current model.

4. **Only 28% of companies create value through growth.** This should inform the agent's skepticism when setting growth assumptions — high growth only creates value if ROIC > WACC is sustained.
