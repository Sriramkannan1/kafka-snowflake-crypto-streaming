import json
import time
import requests

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

TOPIC = "crypto_prices"

while True:

    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={
            "ids": "bitcoin,ethereum,solana",
            "vs_currencies": "usd"
        }
    )

    data = response.json()

    producer.send(TOPIC, data)

    producer.flush()

    print("Sent:", data)

    time.sleep(10)