"""
Fetch analyst consensus estimates from yfinance.

Returns EPS estimates, revenue estimates, growth estimates, and price targets.
Designed as a post-assumption cross-check — the agent should only see this
AFTER setting its own assumptions to avoid anchoring bias.

Usage:
    .venv/bin/python company_info/analyst_estimates.py --ticker AAPL
"""

import argparse
import sys

import yfinance as yf


def fetch(ticker_symbol: str) -> str:
    ticker = yf.Ticker(ticker_symbol)

    lines = []
    lines.append(f"Analyst Consensus Estimates: {ticker_symbol.upper()}")
    lines.append("=" * 55)
    lines.append("")
    lines.append("NOTE: This is a cross-check, not an input.")
    lines.append("Do not revise assumptions to match consensus.")
    lines.append("")

    # --- Price Targets ---
    lines.append("PRICE TARGETS")
    lines.append("-" * 40)
    try:
        pt = ticker.analyst_price_targets
        if pt is not None and not (hasattr(pt, "empty") and pt.empty):
            for key in ["low", "current", "mean", "median", "high"]:
                val = pt.get(key) if isinstance(pt, dict) else getattr(pt, key, None)
                if val is not None:
                    lines.append(f"  {key.capitalize():<10} ${val:>10,.2f}")
        else:
            lines.append("  No price target data available")
    except Exception:
        lines.append("  No price target data available")
    lines.append("")

    # --- EPS Estimates ---
    lines.append("EPS ESTIMATES")
    lines.append("-" * 40)
    try:
        ee = ticker.earnings_estimate
        if ee is not None and not ee.empty:
            periods = ee.columns.tolist()
            header = f"  {'':>20}"
            for p in periods:
                header += f" {str(p):>12}"
            lines.append(header)
            for row_label in ["avg", "low", "high", "numberOfAnalysts"]:
                if row_label in ee.index:
                    display = {
                        "avg": "Avg EPS",
                        "low": "Low EPS",
                        "high": "High EPS",
                        "numberOfAnalysts": "# Analysts",
                    }.get(row_label, row_label)
                    row_str = f"  {display:>20}"
                    for p in periods:
                        val = ee.loc[row_label, p]
                        if val is not None and str(val) != "nan":
                            if row_label == "numberOfAnalysts":
                                row_str += f" {int(val):>12}"
                            else:
                                row_str += f" ${float(val):>11.2f}"
                        else:
                            row_str += f" {'N/A':>12}"
                    lines.append(row_str)
        else:
            lines.append("  No EPS estimate data available")
    except Exception:
        lines.append("  No EPS estimate data available")
    lines.append("")

    # --- Revenue Estimates ---
    lines.append("REVENUE ESTIMATES")
    lines.append("-" * 40)
    try:
        re_ = ticker.revenue_estimate
        if re_ is not None and not re_.empty:
            periods = re_.columns.tolist()
            header = f"  {'':>20}"
            for p in periods:
                header += f" {str(p):>14}"
            lines.append(header)
            for row_label in ["avg", "low", "high", "numberOfAnalysts"]:
                if row_label in re_.index:
                    display = {
                        "avg": "Avg Revenue",
                        "low": "Low Revenue",
                        "high": "High Revenue",
                        "numberOfAnalysts": "# Analysts",
                    }.get(row_label, row_label)
                    row_str = f"  {display:>20}"
                    for p in periods:
                        val = re_.loc[row_label, p]
                        if val is not None and str(val) != "nan":
                            if row_label == "numberOfAnalysts":
                                row_str += f" {int(val):>14}"
                            else:
                                row_str += f" ${float(val)/1e9:>13.1f}B"
                        else:
                            row_str += f" {'N/A':>14}"
                    lines.append(row_str)
        else:
            lines.append("  No revenue estimate data available")
    except Exception:
        lines.append("  No revenue estimate data available")
    lines.append("")

    # --- Growth Estimates ---
    lines.append("GROWTH ESTIMATES")
    lines.append("-" * 40)
    try:
        ge = ticker.growth_estimates
        if ge is not None and not ge.empty:
            # growth_estimates is a DataFrame with index = periods, columns = tickers + S&P 500
            # We want the column matching our ticker or the first column
            col = None
            for c in ge.columns:
                if ticker_symbol.upper() in str(c).upper():
                    col = c
                    break
            if col is None and len(ge.columns) > 0:
                col = ge.columns[0]

            if col is not None:
                for idx in ge.index:
                    val = ge.loc[idx, col]
                    if val is not None and str(val) != "nan":
                        lines.append(f"  {str(idx):<28} {float(val)*100:>7.1f}%")
                    else:
                        lines.append(f"  {str(idx):<28} {'N/A':>8}")

                # Also show S&P 500 column if present for comparison
                sp_col = None
                for c in ge.columns:
                    if "S&P" in str(c) or "500" in str(c) or "sp500" in str(c).lower():
                        sp_col = c
                        break
                if sp_col is not None:
                    lines.append("")
                    lines.append(f"  S&P 500 comparison:")
                    for idx in ge.index:
                        val = ge.loc[idx, sp_col]
                        if val is not None and str(val) != "nan":
                            lines.append(f"  {str(idx):<28} {float(val)*100:>7.1f}%")
        else:
            lines.append("  No growth estimate data available")
    except Exception:
        lines.append("  No growth estimate data available")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch analyst consensus estimates (cross-check tool)"
    )
    parser.add_argument("--ticker", required=True, help="Ticker symbol")
    args = parser.parse_args()
    print(fetch(args.ticker))


if __name__ == "__main__":
    main()
