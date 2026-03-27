"""
Revenue DCF calculator with linear fade growth, margin fade, and Gordon terminal.

Usage:
    .venv/bin/python calculators/revenue_dcf.py \
        --revenue 281724 --revenue-growth 12.0 --terminal-growth 2.8 \
        --fcff-margin 29.0 --target-fcff-margin 32.0 \
        --wacc 8.58 --net-debt -51414 --diluted-shares 7426 --years 10
"""

import argparse


def calculate(revenue, revenue_growth_pct, years, wacc_pct, terminal_growth_pct,
              fcff_margin_pct, target_fcff_margin_pct, net_debt, diluted_shares):
    g_start = revenue_growth_pct / 100
    g_end = terminal_growth_pct / 100
    m_start = fcff_margin_pct / 100
    m_end = target_fcff_margin_pct / 100
    wacc = wacc_pct / 100
    denom = max(years - 1, 1)

    rows = []
    pv_sum = 0.0
    rev = revenue

    for yr in range(1, years + 1):
        g = g_start + (g_end - g_start) * (yr - 1) / denom
        m = m_start + (m_end - m_start) * (yr - 1) / denom
        rev *= (1 + g)
        fcff = rev * m
        pv = fcff / (1 + wacc) ** yr
        pv_sum += pv
        rows.append((yr, g * 100, m * 100, rev, fcff, pv))

    tv_rev = rev * (1 + g_end)
    tv_fcff = tv_rev * m  # use final year margin
    if wacc <= g_end:
        return (f"ERROR: WACC ({wacc_pct:.1f}%) must exceed terminal growth ({terminal_growth_pct:.1f}%) "
                f"for the Gordon Growth Model to produce a finite terminal value.")
    tv = tv_fcff / (wacc - g_end)
    tv_pv = tv / (1 + wacc) ** years
    ev = pv_sum + tv_pv
    equity = ev - net_debt
    per_share = equity / diluted_shares
    tv_share = tv_pv / ev * 100 if ev > 0 else 0

    # --- format ---
    gl = f"{revenue_growth_pct:.1f}% \u2192 {terminal_growth_pct:.1f}%"
    ml = f"{fcff_margin_pct:.1f}% \u2192 {target_fcff_margin_pct:.1f}%"
    col = f"\u2502 {'Year':>4} \u2502 {'Rev Gr':>7} \u2502 {'FCFF Mgn':>8} \u2502 {'Revenue':>14} \u2502 {'FCFF':>14} \u2502 {'PV':>14} \u2502"
    w = len(col) - 2
    R = lambda s: "\u2502" + s.ljust(w) + "\u2502"

    lines = [
        "\u250c" + "\u2500" * w + "\u2510",
        R(" Revenue DCF \u2014 Enterprise to Equity Value"),
        "\u251c" + "\u2500" * w + "\u2524",
        R(f"  Revenue: ${revenue:,.0f}M  \u2502  Growth: {gl}  \u2502  FCFF Margin: {ml}"),
        R(f"  WACC: {wacc_pct:.1f}%  \u2502  Net Debt: ${net_debt:,.0f}M  \u2502  Shares: {diluted_shares:,.0f}M"),
        "\u251c" + "\u2500" * w + "\u2524",
        col,
        "\u251c" + "\u2500" * w + "\u2524",
    ]

    for yr, g, m, r, f, pv in rows:
        lines.append(f"\u2502 {yr:>4} \u2502 {g:>6.1f}% \u2502 {m:>7.1f}% \u2502 ${r:>13,.0f} \u2502 ${f:>13,.0f} \u2502 ${pv:>13,.0f} \u2502")

    lines += [
        "\u251c" + "\u2500" * w + "\u2524",
        R(f"  {'PV of FCFF Stream (Stage 1):':<36} ${pv_sum:>14,.0f}"),
        R(f"  {'Terminal Revenue (Year N+1):':<36} ${tv_rev:>14,.0f}"),
        R(f"  {'Terminal FCFF (Year N+1):':<36} ${tv_fcff:>14,.0f}"),
        R(f"  {'Terminal Value (Gordon Growth):':<36} ${tv:>14,.0f}"),
        R(f"  {'PV of Terminal Value:':<36} ${tv_pv:>14,.0f}"),
        R(""),
        R(f"  {'Enterprise Value:':<36} ${ev:>14,.0f}"),
        R(f"  {'Net Debt (debt \u2212 cash):':<36} ${net_debt:>14,.0f}"),
        R(f"  {'Equity Value:':<36} ${equity:>14,.0f}"),
        R(f"  {'Diluted Shares:':<36} {diluted_shares:>14,.0f}M"),
        R(""),
        R(f"  {'>>> Intrinsic Value / Share:':<36} ${per_share:>14.2f}"),
        R(f"  {'Terminal Value Share:':<36} {tv_share:>13.1f}%"),
        "\u2514" + "\u2500" * w + "\u2518",
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Revenue DCF calculator")
    p.add_argument("--revenue", type=float, required=True)
    p.add_argument("--revenue-growth", type=float, required=True)
    p.add_argument("--years", type=int, default=10)
    p.add_argument("--wacc", type=float, required=True)
    p.add_argument("--terminal-growth", type=float, required=True)
    p.add_argument("--fcff-margin", type=float, required=True)
    p.add_argument("--target-fcff-margin", type=float, required=True)
    p.add_argument("--net-debt", type=float, required=True)
    p.add_argument("--diluted-shares", type=float, required=True)
    a = p.parse_args()
    print(calculate(a.revenue, a.revenue_growth, a.years, a.wacc, a.terminal_growth,
                    a.fcff_margin, a.target_fcff_margin, a.net_debt, a.diluted_shares))
