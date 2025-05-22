# SafeStreet VPN Analyzer 🚀

## 📌 Problem
Detect VPN traffic from anonymized IP data to help strengthen cybersecurity infrastructure and prevent abuse.

## 🧪 Solution
This app uses an ML-driven backend pipeline to analyze patterns in IP-level data and classify potential VPN usage.

## 💻 Tech Stack
Python · Flask · HTML/CSS · scikit-learn · Pandas · NumPy

## 🎯 Key Contributions (Krish Shetty)
- Engineered ML model to detect VPN activity from IP metadata
- Built data preprocessor and handled feature engineering
- Collaborated on API/backend integration and deployment

## 🔗 Original Repo
Project was originally developed as a team effort:
> https://github.com/DeepNandre/SafeStreet-IP-Analyzer

This version is recreated and maintained by Krish Shetty for personal use, documentation, and portfolio visibility.

# 📌 Phase 1 – Data Enrichment Pipeline
In this phase, the goal was to simulate a real-world security system where raw IP logs are enhanced with contextual intelligence before being analyzed or classified.

✅ Objective:
To convert raw IP-level traffic data into enriched records containing location, ISP, and risk-related metadata using external threat intelligence APIs.

🛠️ What We Did:
Created a mock dataset (ip_logs_raw.csv) containing:

IP address

Timestamp

User agent

Connection type

Developed an enrichment module (enrich.py) that:

Uses the ip-api.com service to retrieve metadata for each IP address

Extracts fields like country, city, ISP, proxy usage, and hosting flags

Gracefully handles API failures and malformed data

Generated a new enriched dataset (enriched_logs.csv) with both original and augmented features

🧠 Why It Matters:
Enriched data provides context critical for downstream ML models to make informed predictions.

This mimics what real cybersecurity platforms do when correlating IP traffic with third-party intelligence sources.

The enrichment logic is modular, reusable, and ready for production integration in real-time pipelines.

📂 Output:
data/
├── ip_logs_raw.csv           # Raw IP traffic logs (mock)
└── enriched_logs.csv         # Enriched records with threat context
backend/
└── enrich.py                 # Reusable Python enrichment pipeline
