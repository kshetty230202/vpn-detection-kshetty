from backend.enrich import enrichCSV

if __name__ == "__main__":
    enrichCSV("data/ip_logs_raw.csv", "data/enriched_logs.csv")