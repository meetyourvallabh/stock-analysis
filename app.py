import datetime
from flask import Flask, request, jsonify
from utils import get_percentage_change
from flasgger import Swagger
from constants import POLYGON_API_KEY

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/")
def index():
    """
    This is the index route to check is app is running or not
    ---
    responses:
        200:
            description: A simple message to check if app is running
    """
    return jsonify({"status": True, "message": "App is running"})


@app.route("/percentage_change")
def percentage_change():
    """
    This is the percentage_change route to get the percentage change of a stock from start to end date, if start and end date is not specified then default is one year ago to today
    ---
    parameters:
        - name: ticker
          in: query
          type: string
          required: true
          default: AAPL
        - name: start_date
          in: query
          type: string
          required: false
          default: One year ago
        - name: end_date
          in: query
          type: string
          required: false
          default: Today
    responses:
        200:
            description: The percentage change of the stock from start to end date
            schema:
                id: percentage_change response
                properties:
                    ticker:
                        type: string
                        default: AAPL
                    percentage_change:
                        type: float
                        default: 100.0
                    start_date:
                        type: string
                        default: 2020-01-01
                    end_date:
                        type: string
                        default: 2021-01-01
                    status:
                        type: boolean
                        default: True
            examples:
                {
                    "ticker": "AAPL",
                    "percentage_change": 100.0,
                    "start_date": "2020-01-01",
                    "end_date": "2021-01-01",
                    "status": True
                    }
    """
    ticker = request.args.get("ticker", "AAPL", type=str)
    end_date = request.args.get(
        "end_date", str(datetime.datetime.utcnow().date()), type=str
    )
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    start_date = request.args.get(
        "start_date", end_date - datetime.timedelta(days=365), type=str
    )
    print(f"ticker: {ticker}")
    print(f"end_date: {end_date}")
    print(f"start_date: {start_date}")
    percentage_change = get_percentage_change(ticker, end_date, start_date)
    return (
        jsonify(
            {
                "ticker": ticker,
                "percentage_change": percentage_change,
                "start_date": start_date,
                "end_date": end_date,
                "status": True,
            }
        ),
        200,
    )


@app.route("/percentage_change_one_year")
def percentage_change_one_year():
    """
    This is the percentage_change_one_year route to get the percentage change of a stock from one year ago to today
    ---
    parameters:
        - name: ticker
          in: query
          type: string
          required: true
          default: AAPL
    responses:
        200:
            description: The percentage change of the stock from one year ago to today
            schema:
                id: percentage_change_one_year response
                properties:
                    ticker:
                        type: string
                        default: AAPL
                    percentage_change:
                        type: float
                        default: 100.0
                    start_date:
                        type: string
                        default: 2020-01-01
                    end_date:
                        type: string
                        default: 2021-01-01
                    status:
                        type: boolean
                        default: True
            examples:
                {
                    "ticker": "AAPL",
                    "percentage_change": 100.0,
                    "start_date": "2020-01-01",
                    "end_date": "2021-01-01",
                    "status": True
                    }
    """
    ticker = request.args.get("ticker", "AAPL", type=str)
    end_date = datetime.datetime.utcnow().date()
    start_date = end_date - datetime.timedelta(days=365)
    print(f"ticker: {ticker}")
    print(f"end_date: {end_date}")
    print(f"start_date: {start_date}")
    percentage_change = get_percentage_change(ticker, end_date, start_date)
    return (
        jsonify(
            {
                "ticker": ticker,
                "percentage_change": percentage_change,
                "start_date": start_date,
                "end_date": end_date,
                "status": True,
            }
        ),
        200,
    )


if __name__ == "__main__":
    if POLYGON_API_KEY == "":
        raise ValueError("Please set your Polygon.io API key in the .env file")
    app.run(debug=True, host="0.0.0.0")
