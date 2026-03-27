"""
Fetch market data and compute CAPM cost of equity.

Fetches from yfinance:
- 10Y Treasury yield (risk-free rate)
- Company beta, price, shares
- S&P 500 P/E (for equity risk premium)

Computes:
- Equity Risk Premium from market data (S&P 500 forward earnings yield)
- CAPM cost of equity with sensitivity table
- Terminal growth rate ceiling

Usage:
    .venv/bin/python company_info/market_data.py --ticker MSFT
"""

import argparse
import sys

import yfinance as yf


def fetch(ticker_symbol: str) -> str:
    # --- Risk-free rate from 10Y Treasury ---
    tnx = yf.Ticker("^TNX")
    tnx_hist = tnx.history(period="5d")
    if tnx_hist.empty or tnx_hist["Close"].dropna().empty:
        print("ERROR: Could not fetch 10Y Treasury yield (^TNX)", file=sys.stderr)
        sys.exit(1)
    risk_free_pct = float(tnx_hist["Close"].dropna().iloc[-1])
    risk_free = risk_free_pct / 100

    # --- Company data ---
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    beta = info.get("beta")
    price = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")
    shares = info.get("sharesOutstanding")
    market_cap = info.get("marketCap")

    # --- S&P 500 data for ERP ---
    spy = yf.Ticker("SPY")
    spy_info = spy.info
    spy_pe_trailing = spy_info.get("trailingPE")
    spy_pe_forward = spy_info.get("forwardPE")

    # ERP = S&P 500 forward earnings yield
    # Rationale: In equilibrium, expected stock return ≈ E/P + growth.
    # If growth ≈ Rf (nominal GDP ≈ nominal rate), then ERP = E/P + Rf - Rf = E/P.
    # So forward earnings yield is a market-implied ERP estimate.
    erp = None
    erp_source = None
    if spy_pe_forward and spy_pe_forward > 0:
        erp = 1.0 / spy_pe_forward
        erp_source = f"S&P 500 forward earnings yield (1 / {spy_pe_forward:.1f}x)"
    elif spy_pe_trailing and spy_pe_trailing > 0:
        erp = 1.0 / spy_pe_trailing
        erp_source = f"S&P 500 trailing earnings yield (1 / {spy_pe_trailing:.1f}x)"

    # --- CAPM ---
    capm = None
    if beta is not None and erp is not None:
        capm = risk_free + beta * erp

    # --- Output ---
    lines = []
    lines.append(f"Market Data & CAPM: {ticker_symbol.upper()}")
    lines.append("=" * 55)

    lines.append("")
    lines.append("RISK-FREE RATE")
    lines.append(f"  10Y Treasury Yield:        {risk_free_pct:.2f}%")

    lines.append("")
    lines.append("COMPANY")
    if beta is not None:
        lines.append(f"  Beta:                      {beta:.2f}")
    else:
        lines.append(f"  Beta:                      N/A")
    if price is not None:
        lines.append(f"  Current Price:             ${price:,.2f}")
    if shares is not None:
        lines.append(f"  Shares Outstanding:        {shares / 1e6:,.0f}M")
    if market_cap is not None:
        lines.append(f"  Market Cap:                ${market_cap / 1e9:,.0f}B")

    lines.append("")
    lines.append("S&P 500")
    if spy_pe_trailing:
        lines.append(f"  Trailing P/E:              {spy_pe_trailing:.1f}x  (earnings yield: {1/spy_pe_trailing*100:.2f}%)")
    if spy_pe_forward:
        lines.append(f"  Forward P/E:               {spy_pe_forward:.1f}x  (earnings yield: {1/spy_pe_forward*100:.2f}%)")

    lines.append("")
    lines.append("EQUITY RISK PREMIUM (market-implied)")
    if erp is not None:
        lines.append(f"  ERP:                       {erp * 100:.2f}%")
        lines.append(f"  Method:                    {erp_source}")
    else:
        lines.append("  ERP:                       Could not compute (S&P 500 P/E unavailable)")

    lines.append("")
    lines.append("CAPM COST OF EQUITY")
    if capm is not None:
        lines.append(f"  Formula:  Rf + Beta x ERP")
        lines.append(f"  Result:   {risk_free_pct:.2f}% + {beta:.2f} x {erp * 100:.2f}% = {capm * 100:.2f}%")
        lines.append("")
        lines.append("  Sensitivity (varying ERP):")
        for erp_delta in [-0.01, -0.005, 0, 0.005, 0.01, 0.015, 0.02]:
            adj_erp = erp + erp_delta
            adj_capm = risk_free + beta * adj_erp
            marker = "  <<<" if erp_delta == 0 else ""
            lines.append(f"    ERP {adj_erp * 100:>5.1f}%  →  CAPM = {adj_capm * 100:>5.1f}%{marker}")
    else:
        lines.append("  Could not compute (missing beta or ERP)")

    lines.append("")
    lines.append("TERMINAL GROWTH RATE")
    lines.append(f"  Ceiling (= 10Y Treasury):  {risk_free_pct:.2f}%")
    lines.append(f"  Terminal growth must be strictly below {risk_free_pct:.2f}%")
    lines.append(f"  (A company cannot grow faster than the economy forever)")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch market data and compute CAPM cost of equity")
    parser.add_argument("--ticker", required=True, help="Ticker symbol")
    args = parser.parse_args()
    print(fetch(args.ticker))


if __name__ == "__main__":
    main()
