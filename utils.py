# import datetime
from polygon import RESTClient
from constants import POLYGON_API_KEY

client = RESTClient(api_key=POLYGON_API_KEY)


def get_percentage_change(ticker: str, end_date: str, start_date: str) -> float:
    """
    Get the percentage change of a stock from one year ago to today.

    :param ticker: The ticker symbol of the stock.
    :param end_date: The end date of the time period.
    :param start_date: The start date of the time period.
    :return: The percentage change of the stock from one year ago to today.
    """

    # ticker = "AMD"
    # end_date = datetime.datetime.utcnow().date()
    # start_date = end_date - datetime.timedelta(days=365)

    print(f"One Year Before: {start_date}")
    price_before_one_year = client.get_daily_open_close_agg(
        ticker=ticker, date=start_date, adjusted=False
    ).close
    print(f"Price Before One Year: {price_before_one_year}")

    print(f"Current Date: {end_date}")
    # commented out because it will work if market is closed for current day
    # otherwise it returns None for close value
    # current_price = client.get_daily_open_close_agg(
    #     ticker=ticker, date=end_date - datetime.timedelta(days=1), adjusted=False
    # )
    aggs = [
        a
        for a in client.list_aggs(
            ticker=ticker,
            multiplier=1,
            timespan="day",
            from_=end_date,
            to=end_date,
        )
    ]
    current_price = aggs[-1].close
    print(f"Current Price: {current_price}")

    percentage_change = (
        (current_price - price_before_one_year) / price_before_one_year
    ) * 100

    print(f"Percentage Change: {percentage_change}")
    return round(percentage_change, 2)
