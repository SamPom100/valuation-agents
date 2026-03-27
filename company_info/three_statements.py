import argparse
import os
from rich import print
from rich.console import Console

from edgar import Company, Financials, set_identity, MultiFinancials
set_identity(os.getenv("SEC_IDENTITY", "your.name@example.com"))

def fetch(ticker, years):
    company = Company(ticker)
    filings = company.get_filings(form="10-K", amendments=False).head(years)
    multi = MultiFinancials.extract(filings)

    income = multi.income_statement()
    cash_flow = multi.cash_flow_statement()
    balance = multi.balance_sheet()

    income.max_periods = years
    cash_flow.max_periods = years
    balance.max_periods = years

    out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", ticker.upper())
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "three_statements.txt")

    with open(out_path, "w") as f:
        console = Console(file=f, width=300)
        console.print(income)
        console.print("\n")
        console.print(cash_flow)
        console.print("\n")
        console.print(balance)

    print(f"Wrote {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch income statement data using Edgar")
    parser.add_argument("--ticker", type=str, required=True, help="Ticker symbol, e.g. META")
    parser.add_argument("--years", type=int, default=10, help="Number of years to pull")
    args = parser.parse_args()
    fetch(args.ticker, args.years)


if __name__ == "__main__":
    main()
