"""
EPS DCF calculator with linear fade growth and exit multiple.

Usage:
    .venv/bin/python calculators/eps_dcf.py \
        --eps 13.71 --growth 15.0 --terminal-growth 2.8 \
        --pe 35.0 --discount-rate 8.58 --payout-ratio 48 --years 10
"""

import argparse


def calculate(eps, growth_pct, years, terminal_pe, discount_rate_pct, terminal_growth_pct, payout_ratio_pct):
    g_start = growth_pct / 100
    g_end = terminal_growth_pct / 100
    r = discount_rate_pct / 100
    payout = payout_ratio_pct / 100
    denom = max(years - 1, 1)

    rows = []
    pv_dist = 0.0
    proj = eps

    for yr in range(1, years + 1):
        g = g_start + (g_end - g_start) * (yr - 1) / denom
        proj *= (1 + g)
        dist = proj * payout
        pv = dist / (1 + r) ** yr
        pv_dist += pv
        rows.append((yr, g * 100, proj, dist, proj * terminal_pe, pv))

    tv = proj * terminal_pe
    tv_pv = tv / (1 + r) ** years
    iv = pv_dist + tv_pv
    tv_share = tv_pv / iv * 100 if iv > 0 else 0

    # --- format ---
    growth_label = f"{growth_pct:.1f}% \u2192 {terminal_growth_pct:.1f}%"
    col = f"\u2502 {'Year':>4} \u2502 {'Growth':>7} \u2502 {'Proj. EPS':>10} \u2502 {'Cash Dist.':>11} \u2502 {'EPS \u00d7 P/E':>10} \u2502 {'PV of Dist.':>12} \u2502"
    w = len(col) - 2
    R = lambda s: "\u2502" + s.ljust(w) + "\u2502"

    lines = [
        "\u250c" + "\u2500" * w + "\u2510",
        R(" EPS DCF \u2014 Exit Multiple Valuation"),
        "\u251c" + "\u2500" * w + "\u2524",
        R(f"  EPS: ${eps:.2f}  \u2502  Growth: {growth_label}"),
        R(f"  Terminal P/E: {terminal_pe:.1f}x  \u2502  Discount Rate: {discount_rate_pct:.1f}%  \u2502  Payout: {payout_ratio_pct:.1f}%"),
        "\u251c" + "\u2500" * w + "\u2524",
        col,
        "\u251c" + "\u2500" * w + "\u2524",
    ]

    for yr, g, e, d, p, pv in rows:
        lines.append(f"\u2502 {yr:>4} \u2502 {g:>6.1f}% \u2502 ${e:>9.2f} \u2502 ${d:>10.2f} \u2502 ${p:>9.2f} \u2502 ${pv:>11.2f} \u2502")

    lines += [
        "\u251c" + "\u2500" * w + "\u2524",
        R(f"  {'PV of Cash Distributions:':<34} ${pv_dist:>12.2f}"),
        R(f"  {'Terminal EPS (Year N):':<34} ${proj:>12.2f}"),
        R(f"  {'Terminal Value (EPS \u00d7 P/E):':<34} ${tv:>12.2f}"),
        R(f"  {'PV of Terminal Value:':<34} ${tv_pv:>12.2f}"),
        R(""),
        R(f"  {'>>> Intrinsic Value / Share:':<34} ${iv:>12.2f}"),
        R(f"  {'Terminal Value Share:':<34} {tv_share:>12.1f}%"),
        "\u2514" + "\u2500" * w + "\u2518",
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="EPS DCF calculator")
    p.add_argument("--eps", type=float, required=True)
    p.add_argument("--growth", type=float, required=True)
    p.add_argument("--pe", type=float, required=True)
    p.add_argument("--discount-rate", type=float, required=True)
    p.add_argument("--terminal-growth", type=float, required=True)
    p.add_argument("--payout-ratio", type=float, default=0.0)
    p.add_argument("--years", type=int, default=10)
    a = p.parse_args()
    print(calculate(a.eps, a.growth, a.years, a.pe, a.discount_rate, a.terminal_growth, a.payout_ratio))
