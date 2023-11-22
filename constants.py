import os
from dotenv import load_dotenv

load_dotenv()

if "POLYGON_API_KEY" not in os.environ:
    print("Please set your API key in the .env file")
    polygon_api_key = input("Enter your Polygon API key:")
    with open(".env", "a") as f:
        f.write(f"POLYGON_API_KEY={polygon_api_key}")
    load_dotenv()

POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY")
