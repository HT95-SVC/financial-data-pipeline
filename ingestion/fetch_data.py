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
        recent_dividends = dividends.last("1Y")  # 최근 1년
        months = sorted(set(recent_dividends.index.month))
        print("배당 지급 월 :", months)
    else:
        print("배당 지급 이력 없음")

    print("-" * 40)

print("수집 종료")