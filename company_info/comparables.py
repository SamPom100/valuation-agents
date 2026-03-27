"""
Fetch valuation multiples for a list of tickers.

The agent selects the peer group. This tool fetches multiples from yfinance
and displays them in a comparison table with group statistics.

Usage:
    .venv/bin/python company_info/comparables.py --tickers "AAPL,MSFT,GOOG,META,AMZN"
"""

import argparse

import yfinance as yf


FIELDS = [
    ("trailingPE",                   "P/E(T)",    "x"),
    ("forwardPE",                    "P/E(F)",    "x"),
    ("enterpriseToEbitda",           "EV/EBITDA", "x"),
    ("priceToSalesTrailing12Months", "P/S",       "x"),
    ("enterpriseToRevenue",          "EV/Rev",    "x"),
]


def fetch(tickers):
    rows = []
    for symbol in tickers:
        info = yf.Ticker(symbol).info
        row = {"ticker": symbol.upper()}
        row["market_cap"] = info.get("marketCap")
        for yf_key, _, _ in FIELDS:
            row[yf_key] = info.get(yf_key)
        rows.append(row)

    # --- format ---
    lines = []
    lines.append("Comparable Company Multiples")
    lines.append("=" * 70)
    lines.append("")

    header = f"{'Ticker':<8} {'Mkt Cap':>10}"
    for _, label, _ in FIELDS:
        header += f" {label:>10}"
    lines.append(header)
    lines.append("-" * len(header))

    for r in rows:
        mc = r["market_cap"]
        mc_str = f"${mc / 1e9:>8,.0f}B" if mc else f"{'N/A':>10}"
        line = f"{r['ticker']:<8} {mc_str}"
        for yf_key, _, suffix in FIELDS:
            val = r[yf_key]
            if val and val > 0:
                line += f" {val:>9.1f}{suffix}"
            else:
                line += f" {'N/A':>10}"
        lines.append(line)

    lines.append("-" * len(header))
    lines.append("")
    lines.append("GROUP STATISTICS")
    lines.append("-" * 40)

    def median(lst):
        if not lst:
            return None
        s = sorted(lst)
        n = len(s)
        if n % 2 == 1:
            return s[n // 2]
        return (s[n // 2 - 1] + s[n // 2]) / 2

    for yf_key, label, suffix in FIELDS:
        vals = [r[yf_key] for r in rows if r.get(yf_key) and r[yf_key] > 0]
        if vals:
            med = median(vals)
            lo, hi = min(vals), max(vals)
            lines.append(f"  {label + ':':<16} Median {med:>6.1f}{suffix}   Range {lo:.1f}{suffix} - {hi:.1f}{suffix}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch comparable company multiples")
    parser.add_argument("--tickers", required=True,
                        help="Comma-separated ticker symbols")
    args = parser.parse_args()
    tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]
    print(fetch(tickers))


if __name__ == "__main__":
    main()
