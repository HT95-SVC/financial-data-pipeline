import yfinance as yf
import pandas as pd
import os

tickers = ["AVGO", "NVDA", "VRT", "ETN", "ARCC", "ENB"]

print("확인중인 종목의 수 :", len(tickers))

for ticker in tickers:

    print("수집 시작 :", ticker)

    stock = yf.Ticker(ticker)
    info = stock.info

    price = info.get("currentPrice")
    dividend = info.get("dividendRate")
    dividend_yield = info.get("dividendYield")

    print("현재가 :", price)
    print("연간 배당금 :", dividend)

    if dividend_yield is not None:
        print("배당수익률 :", round(dividend_yield * 100, 2), "%")
    else:
        print("배당수익률 : 없음")

    # 🔹 배당 지급 월 계산
    dividends = stock.dividends

    if not dividends.empty:
        one_year_ago = pd.Timestamp.today() - pd.DateOffset(years=1)
        recent_dividends = dividends[dividends.index >= one_year_ago]
        months = sorted(set(recent_dividends.index.month))
        print("배당 지급 월 :", months)
    else:
        print("배당 지급 이력 없음")
    row = {
        "ticker": ticker,
        "price": price,
        "dividend": dividend,
        "dividend_yield": dividend_yield,
        "dividend_months": months if not dividends.empty else None
    }

    df = pd.DataFrame([row])

    file_path = f"data/raw/{ticker}.csv"

    df.to_csv(file_path, index=False)
    print("-" * 40)

print("수집 종료")