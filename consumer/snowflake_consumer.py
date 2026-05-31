import json
import os

from kafka import KafkaConsumer
from dotenv import load_dotenv

import snowflake.connector

load_dotenv()

consumer = KafkaConsumer(
    'crypto_prices',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='crypto-group',
    value_deserializer=lambda x: json.loads(x.decode())
)

conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    role=os.getenv("SNOWFLAKE_ROLE")
)

cursor = conn.cursor()

for msg in consumer:

    data = msg.value

    for coin, values in data.items():

        if not isinstance(values, dict):
            continue

        if "usd" not in values:
            print("Skipping invalid message:", data)
            continue

        price = values["usd"]

        cursor.execute(
            """
            INSERT INTO CRYPTO_PRICES
            (COIN, PRICE, EVENT_TIME)
            VALUES (%s,%s,CURRENT_TIMESTAMP())
            """,
            (coin, price)
        )

        print(f"Inserted {coin} -> {price}")