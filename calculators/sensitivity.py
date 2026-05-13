"""
Two-way sensitivity table for EPS DCF valuation.

Varies two parameters across a grid and shows intrinsic value at each
combination. Supports: growth x pe, growth x discount, pe x discount.

Usage:
    .venv/bin/python calculators/sensitivity.py \
        --eps 27.64 --payout-ratio 53 --terminal-growth 3.0 --years 10 \
        --axis "growth x pe" \
        --growth "6,8,10,12,14,16,18,20" \
        --pe "14,16,18,20,22,24,26" \
        --discount-rate 9.24
"""

import argparse


def _eps_dcf_value(eps, growth_pct, years, pe, discount_rate_pct, terminal_growth_pct, payout_ratio_pct):
    """EPS exit-multiple DCF with linear fade. Returns intrinsic value."""
    g_start = growth_pct / 100
    g_end = terminal_growth_pct / 100
    r = discount_rate_pct / 100
    payout = payout_ratio_pct / 100
    denom = max(years - 1, 1)

    pv_dist = 0.0
    proj = eps
    for yr in range(1, years + 1):
        g = g_start + (g_end - g_start) * (yr - 1) / denom
        proj *= (1 + g)
        pv_dist += (proj * payout) / (1 + r) ** yr

    return pv_dist + (proj * pe) / (1 + r) ** years


def main():
    parser = argparse.ArgumentParser(description="Two-way sensitivity table for EPS DCF")
    parser.add_argument("--eps", type=float, required=True)
    parser.add_argument("--payout-ratio", type=float, required=True)
    parser.add_argument("--terminal-growth", type=float, required=True)
    parser.add_argument("--years", type=int, default=10)
    parser.add_argument("--axis", required=True,
                        choices=["growth x pe", "growth x discount", "pe x discount"],
                        help="Which two parameters to vary")
    parser.add_argument("--growth", type=str, required=True, help="Comma-separated growth rates (%%)")
    parser.add_argument("--pe", type=str, required=True, help="Comma-separated P/E values or single value")
    parser.add_argument("--discount-rate", type=str, required=True, help="Comma-separated discount rates or single value")
    args = parser.parse_args()

    def parse(s):
        return [float(x.strip()) for x in s.split(",")] if s else None

    growth_vals = parse(args.growth)
    pe_vals = parse(args.pe)
    dr_vals = parse(args.discount_rate)

    axes = [a.strip().lower() for a in args.axis.split("x")]

    # Determine row/col axes and the fixed parameter
    if axes == ["growth", "pe"]:
        row_vals, col_vals, fixed = growth_vals, pe_vals, dr_vals[0]
        row_fmt, col_fmt = lambda v: f"{v:>.0f}%", lambda v: f"{v:>.0f}x"
        cell = lambda r, c: _eps_dcf_value(args.eps, r, args.years, c, fixed, args.terminal_growth, args.payout_ratio)
        fixed_desc = f"Discount Rate: {fixed:.1f}%"
    elif axes == ["growth", "discount"]:
        row_vals, col_vals, fixed = growth_vals, dr_vals, pe_vals[0]
        row_fmt, col_fmt = lambda v: f"{v:>.0f}%", lambda v: f"{v:>.1f}%"
        cell = lambda r, c: _eps_dcf_value(args.eps, r, args.years, fixed, c, args.terminal_growth, args.payout_ratio)
        fixed_desc = f"Terminal P/E: {fixed:.1f}x"
    elif axes == ["pe", "discount"]:
        row_vals, col_vals, fixed = pe_vals, dr_vals, growth_vals[0]
        row_fmt, col_fmt = lambda v: f"{v:>.0f}x", lambda v: f"{v:>.1f}%"
        cell = lambda r, c: _eps_dcf_value(args.eps, fixed, args.years, r, c, args.terminal_growth, args.payout_ratio)
        fixed_desc = f"EPS Growth: {fixed:.1f}%"
    # Print table
    cw = 9  # column width
    rw = 8  # row label width

    print(f"Sensitivity Table: EPS DCF Intrinsic Value")
    print(f"EPS: ${args.eps:.2f} | Payout: {args.payout_ratio:.0f}% | "
          f"Terminal Growth: {args.terminal_growth:.1f}% | {fixed_desc}")
    print()

    # Header
    print("┌" + "─" * rw + "┬" + ("─" * cw + "┬") * (len(col_vals) - 1) + "─" * cw + "┐")
    print(f"{'':>{rw}} │" + "".join(f" {col_fmt(c):>{cw-2}} │" for c in col_vals))
    print("├" + "─" * rw + "┼" + ("─" * cw + "┼") * (len(col_vals) - 1) + "─" * cw + "┤")

    # Rows
    for r in row_vals:
        print(f"{row_fmt(r):>{rw}} │" + "".join(f" ${cell(r, c):>{cw-3},.0f} │" for c in col_vals))

    print("└" + "─" * rw + "┴" + ("─" * cw + "┴") * (len(col_vals) - 1) + "─" * cw + "┘")


if __name__ == "__main__":
    main()
