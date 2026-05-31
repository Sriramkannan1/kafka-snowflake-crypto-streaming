# 🚀 Real-Time Cryptocurrency Streaming Pipeline using Kafka & Snowflake

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Kafka](https://img.shields.io/badge/Apache_Kafka-Streaming-black?style=for-the-badge\&logo=apachekafka)
![Snowflake](https://img.shields.io/badge/Snowflake-Cloud_Data_Warehouse-29B5E8?style=for-the-badge\&logo=snowflake)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge\&logo=docker)

## 📌 Project Overview

This project demonstrates a **real-time data streaming pipeline** that ingests live cryptocurrency market data, publishes it to Apache Kafka, consumes the streaming events, and stores them in Snowflake for analytics and reporting.

The system is designed using modern data engineering principles and simulates a real-world streaming architecture used in financial analytics platforms.

---

## 🏗️ Architecture

```text
┌─────────────────────┐
│ Cryptocurrency API  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Kafka Producer      │
│ (Python)            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Apache Kafka Topic  │
│ crypto_prices       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Kafka Consumer      │
│ (Python)            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Snowflake           │
│ Cloud Warehouse     │
└─────────────────────┘
```

---

## 🎯 Key Features

* Real-time cryptocurrency data ingestion
* Apache Kafka event streaming
* Fault-tolerant producer-consumer architecture
* Snowflake cloud data warehouse integration
* Dockerized Kafka and ZooKeeper deployment
* Continuous data ingestion pipeline
* Scalable event-driven architecture
* Analytics-ready storage layer

---

## 🛠️ Tech Stack

| Technology   | Purpose                         |
| ------------ | ------------------------------- |
| Python       | Producer & Consumer Development |
| Apache Kafka | Event Streaming Platform        |
| ZooKeeper    | Kafka Coordination              |
| Snowflake    | Cloud Data Warehouse            |
| Docker       | Containerization                |
| REST API     | Real-Time Data Source           |

---

## 📂 Project Structure

```text
crypto-streaming-project/
│
├── producer/
│   └── crypto_producer.py
│
├── consumer/
│   └── snowflake_consumer.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Snowflake Table Schema

```sql
CREATE TABLE CRYPTO_PRICES (
    ID NUMBER AUTOINCREMENT,
    COIN STRING,
    PRICE FLOAT,
    EVENT_TIME TIMESTAMP
);
```

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/kafka-snowflake-crypto-streaming.git

cd kafka-snowflake-crypto-streaming
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file:

```env
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=CRYPTO_DB
SNOWFLAKE_SCHEMA=STREAMING
SNOWFLAKE_ROLE=ACCOUNTADMIN
```

---

### 4️⃣ Start Kafka Infrastructure

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

---

### 5️⃣ Run Producer

```bash
python producer/crypto_producer.py
```

Example Output:

```text
Sent:
{
  "bitcoin": {
    "usd": 73560
  }
}
```

---

### 6️⃣ Run Consumer

```bash
python consumer/snowflake_consumer.py
```

Example Output:

```text
Inserted bitcoin -> 73560
Inserted ethereum -> 2000
Inserted solana -> 81
```

---

## 📊 Verify Data in Snowflake

```sql
SELECT *
FROM CRYPTO_PRICES
ORDER BY EVENT_TIME DESC;
```

---

## 📈 Future Enhancements

* Snowpipe Integration
* dbt Transformations
* Real-Time Dashboards
* Power BI Reporting
* Streamlit Monitoring Dashboard
* Alerting & Notifications
* Data Quality Validation
* Multi-Topic Kafka Architecture

---

## 💡 Learning Outcomes

This project demonstrates practical experience with:

* Event-Driven Architecture
* Real-Time Data Processing
* Apache Kafka Fundamentals
* Cloud Data Warehousing
* Docker-Based Deployment
* Data Pipeline Development
* Streaming Analytics

---

## 👨‍💻 Author

**Sriram K**

Data Engineering | Cloud Computing | Full Stack Development | AI Applications

GitHub: https://github.com/Sriramkannan1

LinkedIn: https://www.linkedin.com/in/sriram-kannan-btech-ai/

---

## ⭐ If you found this project useful

Consider giving the repository a star to support future improvements and open-source contributions.
