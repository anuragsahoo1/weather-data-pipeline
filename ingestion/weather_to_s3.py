import os
import json
import logging
import requests
import boto3
from datetime import datetime
from dotenv import load_dotenv

# Load env variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
BUCKET = os.getenv("S3_BUCKET")
REGION = os.getenv("AWS_REGION")

CITIES = ["Bhubaneswar", "Delhi", "Mumbai"]

logging.basicConfig(level=logging.INFO)

# S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=REGION
)

def fetch_weather(city):
    import pandas as pd	
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def upload_to_s3(data, city):
    now = datetime.utcnow()

    key = f"raw/city={city}/year={now.year}/month={now.month:02d}/day={now.day:02d}/hour={now.hour:02d}/{now.minute}_{now.second}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(data)
    )

    logging.info(f"Uploaded: {key}")

def main():
    for city in CITIES:
        try:
            data = fetch_weather(city)

            record = {
                "city": city,
                "timestamp": datetime.utcnow().isoformat(),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"]
            }

            upload_to_s3(record, city)

        except Exception as e:
            logging.error(f"Error for {city}: {e}")

if __name__ == "__main__":
    main()
