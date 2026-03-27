"""
Compute historical EPS and P/E from net income + yfinance market data.

The agent reads net income from three_statements.txt and passes it in.
This tool fetches current diluted shares and historical year-end prices
from yfinance, then computes EPS and P/E.

If --diluted-shares is provided (JSON dict of year:shares_in_millions from the
income statement), each year uses its own diluted share count for accurate P/E.
Without it, all years use current shares — fine for growth rates, but P/E will
be understated for companies with significant buyback history.

Usage:
    .venv/bin/python company_info/eps_pe.py --ticker AAPL \
        --net-income '{"2025":112010,"2024":93736}' \
        --diluted-shares '{"2025":15115,"2024":15408}'
"""

import argparse
import json
import os
import sys
from typing import Dict

import yfinance as yf


def compute(ticker_symbol: str, net_income: Dict[str, float],
            diluted_shares: Dict[str, float] = None) -> str:
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info

    shares = info.get("sharesOutstanding")
    if shares is None:
        print("ERROR: could not get sharesOutstanding from yfinance", file=sys.stderr)
        sys.exit(1)

    shares_b = shares / 1e9
    shares_m = shares / 1e6

    # net_income values are in millions, get year-end prices
    history = ticker.history(period="max", interval="1d")
    if history.index.tz is not None:
        history.index = history.index.tz_localize(None)

    years = sorted(net_income.keys())

    rows = []
    prev_eps = None
    prev_pe = None

    using_historical_shares = diluted_shares is not None and len(diluted_shares) > 0

    for year in years:
        ni = net_income[year]
        year_shares = diluted_shares[year] if (using_historical_shares and year in diluted_shares) else shares_m
        eps = ni / year_shares  # net_income in millions, shares in millions

        # find last trading day of the year (or closest)
        year_int = int(year)
        year_prices = history[history.index.year == year_int]
        if year_prices.empty:
            # try year-end from prior december if fiscal year ends early
            price = None
        else:
            price = float(year_prices["Close"].iloc[-1])

        pe = price / eps if (price and eps and eps > 0) else None

        eps_growth = None
        if prev_eps and prev_eps > 0 and eps > 0:
            eps_growth = (eps - prev_eps) / prev_eps * 100

        pe_growth = None
        if prev_pe and prev_pe > 0 and pe and pe > 0:
            pe_growth = (pe - prev_pe) / prev_pe * 100

        rows.append({
            "year": year,
            "net_income_m": ni,
            "eps": eps,
            "price": price,
            "pe": pe,
            "eps_growth": eps_growth,
            "pe_growth": pe_growth,
        })

        prev_eps = eps
        prev_pe = pe

    # compute summary stats (skip first year for growth since no prior)
    eps_growths = [r["eps_growth"] for r in rows if r["eps_growth"] is not None]
    pe_growths = [r["pe_growth"] for r in rows if r["pe_growth"] is not None]
    eps_values = [r["eps"] for r in rows if r["eps"] is not None]
    pe_values = [r["pe"] for r in rows if r["pe"] is not None]

    def avg(lst):
        return sum(lst) / len(lst) if lst else None

    def median(lst):
        if not lst:
            return None
        s = sorted(lst)
        n = len(s)
        if n % 2 == 1:
            return s[n // 2]
        return (s[n // 2 - 1] + s[n // 2]) / 2

    # CAGR from first to last EPS
    eps_first = next((r["eps"] for r in rows if r["eps"] and r["eps"] > 0), None)
    eps_last = next((r["eps"] for r in reversed(rows) if r["eps"] and r["eps"] > 0), None)
    eps_cagr = None
    if eps_first and eps_last and len(rows) > 1:
        n_years = int(rows[-1]["year"]) - int(rows[0]["year"])
        if n_years > 0 and eps_first > 0 and eps_last > 0:
            eps_cagr = ((eps_last / eps_first) ** (1 / n_years) - 1) * 100

    # build output
    lines = []
    lines.append(f"EPS & P/E Analysis: {ticker_symbol.upper()}")
    lines.append(f"Current shares outstanding: {shares_m:,.0f}M ({shares_b:.2f}B)")
    if using_historical_shares:
        lines.append(f"Share basis: year-specific diluted shares (from income statement)")
    else:
        lines.append(f"Share basis: current shares for all years (split-consistent, P/E approximate if buybacks)")
    lines.append("")

    header = f"{'Year':>6} {'Net Inc ($M)':>14} {'EPS':>8} {'Yr-End Price':>13} {'P/E':>7} {'EPS Gr%':>8} {'P/E Gr%':>8}"
    lines.append(header)
    lines.append("-" * len(header))

    for r in rows:
        ni_str = f"${r['net_income_m']:>12,.0f}"
        eps_str = f"${r['eps']:>6.2f}" if r["eps"] is not None else f"{'N/A':>7}"
        price_str = f"${r['price']:>11.2f}" if r["price"] is not None else f"{'N/A':>12}"
        pe_str = f"{r['pe']:>6.1f}x" if r["pe"] is not None else f"{'N/A':>7}"
        eg_str = f"{r['eps_growth']:>7.1f}%" if r["eps_growth"] is not None else f"{'--':>8}"
        pg_str = f"{r['pe_growth']:>7.1f}%" if r["pe_growth"] is not None else f"{'--':>8}"
        lines.append(f"{r['year']:>6} {ni_str} {eps_str} {price_str} {pe_str} {eg_str} {pg_str}")

    lines.append("-" * len(header))
    lines.append("")
    lines.append("SUMMARY")
    lines.append("-" * 40)

    if eps_cagr is not None:
        lines.append(f"{'EPS CAGR:':<24} {eps_cagr:>7.1f}%")
    if eps_growths:
        lines.append(f"{'Avg YoY EPS Growth:':<24} {avg(eps_growths):>7.1f}%")
        lines.append(f"{'Median YoY EPS Growth:':<24} {median(eps_growths):>7.1f}%")
        lines.append(f"{'EPS Growth Range:':<24} {min(eps_growths):>7.1f}% to {max(eps_growths):.1f}%")
    lines.append("")
    if pe_values:
        lines.append(f"{'Avg P/E:':<24} {avg(pe_values):>7.1f}x")
        lines.append(f"{'Median P/E:':<24} {median(pe_values):>7.1f}x")
        lines.append(f"{'P/E Range:':<24} {min(pe_values):>7.1f}x to {max(pe_values):.1f}x")
    if pe_growths:
        lines.append(f"{'Avg YoY P/E Change:':<24} {avg(pe_growths):>7.1f}%")
        lines.append(f"{'Median YoY P/E Change:':<24} {median(pe_growths):>7.1f}%")
    lines.append("")
    if eps_values:
        lines.append(f"{'Latest EPS:':<24} ${eps_values[-1]:>7.2f}")
    if pe_values:
        lines.append(f"{'Latest P/E:':<24} {pe_values[-1]:>7.1f}x")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Compute EPS & P/E table from net income + yfinance"
    )
    parser.add_argument("--ticker", required=True, help="Ticker symbol")
    parser.add_argument(
        "--net-income", required=True,
        help='JSON dict of year:net_income_in_millions, e.g. \'{"2024":93736,"2023":96995}\''
    )
    parser.add_argument(
        "--diluted-shares", required=False, default=None,
        help='Optional JSON dict of year:diluted_shares_in_millions for accurate historical P/E'
    )
    args = parser.parse_args()

    net_income = json.loads(args.net_income)
    # ensure keys are strings and values are floats
    net_income = {str(k): float(v) for k, v in net_income.items()}

    diluted_shares = None
    if args.diluted_shares:
        diluted_shares = json.loads(args.diluted_shares)
        diluted_shares = {str(k): float(v) for k, v in diluted_shares.items()}

    output = compute(args.ticker, net_income, diluted_shares)
    print(output)

    out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", args.ticker.upper())
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "eps_pe.txt")
    with open(out_path, "w") as f:
        f.write(output + "\n")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
