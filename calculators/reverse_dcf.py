"""
Reverse DCF — solve for the EPS growth rate implied by the current price.

Given a stock price, computes what starting EPS growth rate would produce
that price under an EPS exit-multiple DCF with fading growth.

Usage:
    .venv/bin/python calculators/reverse_dcf.py \
        --price 371.04 --eps 13.71 --pe 35.0 \
        --discount-rate 8.58 --terminal-growth 2.8 \
        --payout-ratio 48 --years 10
"""

import argparse


def _eps_dcf_value(eps, growth_pct, years, pe, discount_rate_pct, terminal_growth_pct, payout_ratio_pct):
    """Compute intrinsic value from an EPS exit-multiple DCF with linear fade."""
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


def solve(price, eps, years, pe, discount_rate_pct, terminal_growth_pct, payout_ratio_pct):
    """Bisect to find the starting growth rate that produces the target price."""
    low = terminal_growth_pct  # can't be below terminal in fade mode
    high = 100.0

    for _ in range(200):
        mid = (low + high) / 2
        val = _eps_dcf_value(eps, mid, years, pe, discount_rate_pct, terminal_growth_pct, payout_ratio_pct)
        if val < price:
            low = mid
        else:
            high = mid
        if abs(high - low) < 1e-6:
            break

    return (low + high) / 2


def main():
    parser = argparse.ArgumentParser(description="Reverse DCF — implied EPS growth from current price")
    parser.add_argument("--price", type=float, required=True, help="Current share price")
    parser.add_argument("--eps", type=float, required=True, help="Current or normalized EPS")
    parser.add_argument("--pe", type=float, required=True, help="Terminal P/E multiple")
    parser.add_argument("--discount-rate", type=float, required=True, help="Discount rate in percent")
    parser.add_argument("--terminal-growth", type=float, required=True, help="Terminal growth rate in percent")
    parser.add_argument("--payout-ratio", type=float, default=0.0, help="Payout ratio in percent")
    parser.add_argument("--years", type=int, default=10, help="Forecast period")
    args = parser.parse_args()

    implied = solve(args.price, args.eps, args.years, args.pe,
                    args.discount_rate, args.terminal_growth, args.payout_ratio)

    # Show the projection at the implied rate
    g_start = implied / 100
    g_end = args.terminal_growth / 100
    r = args.discount_rate / 100
    payout = args.payout_ratio / 100
    denom = max(args.years - 1, 1)

    print(f"Reverse DCF — Implied EPS Growth")
    print(f"Price: ${args.price:.2f} | EPS: ${args.eps:.2f} | Terminal P/E: {args.pe:.1f}x | "
          f"Discount: {args.discount_rate:.1f}% | Terminal Growth: {args.terminal_growth:.1f}% | "
          f"Payout: {args.payout_ratio:.0f}%")
    print(f"")
    print(f">>> Implied Starting Growth: {implied:.2f}% (fading to {args.terminal_growth:.1f}%)")
    print(f"")

    header = f"{'Year':>6} {'Growth':>8} {'Proj. EPS':>12} {'EPS x P/E':>12} {'PV of Dist.':>12}"
    print(header)
    print("-" * len(header))

    proj = args.eps
    total_pv_dist = 0.0
    for yr in range(1, args.years + 1):
        g = g_start + (g_end - g_start) * (yr - 1) / denom
        proj *= (1 + g)
        dist_pv = (proj * payout) / (1 + r) ** yr
        total_pv_dist += dist_pv
        print(f"{yr:>6} {g*100:>7.1f}% ${proj:>10.2f} ${proj*args.pe:>10.2f} ${dist_pv:>10.2f}")

    terminal_pv = (proj * args.pe) / (1 + r) ** args.years
    rebuilt = total_pv_dist + terminal_pv

    print("-" * len(header))
    print(f"{'PV of Distributions:':<30} ${total_pv_dist:>12.2f}")
    print(f"{'Terminal Value (EPS x P/E):':<30} ${proj * args.pe:>12.2f}")
    print(f"{'PV of Terminal:':<30} ${terminal_pv:>12.2f}")
    print(f"{'Rebuilt Intrinsic Value:':<30} ${rebuilt:>12.2f}")
    print(f"{'Target Price:':<30} ${args.price:>12.2f}")


if __name__ == "__main__":
    main()
