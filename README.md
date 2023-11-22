# stock-analysis

## Overview of Project
This projects helps in performing basic stock analysis. It uses polygon.io internal API to fetch the stock data. 

## Requirements
- Python 3.11
- Polygon.io API key

## Usage
- Clone the repository
- Install the requirements using `pip install -r requirements.txt`
- Run the `app.py` file using `python app.py`
- Enter the API key when prompted or add it in the .env file as `POLYGON_API_KEY`
- Open the browser and go to `http://localhost:5000/apidocs` for API documentation or you can use the postman collection in the repository `stock-analysis.postman_collection`

## Docker usage
- Clone the repository
- Build the docker image using `docker build -t stock-analysis .`
- Run the docker container using `docker run -d --name stock-analysis-container -p 5000:5000 stock-analysis`
- Open the browser and go to `http://localhost:5000/apidocs` for API documentation or you can use the postman collection in the repository `stock-analysis.postman_collection`
