import csv
import time
import requests

# enrich a single IP address using the ip-api.com API
def enrichIP(ip):
    """
    return: a dictionary with country, city, ISP, etc.
    """
    # API for cleaner output
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,org,proxy,hosting,query"

    try:
        # GET request to ip-api
        response = requests.get(url, timeout=5)
        data = response.json()

        # API error handling
        if data["status"] != "success":
            return {"ip": ip, "error": data.get("message", "Unknown error")}
        
        # returning the enriched field
        return {
            "ip": data.get("query"),
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "isp": data.get("isp"),
            "org": data.get("org"),
            "is_proxy": data.get("proxy"),
            "is_hosting": data.get("hosting")
        }
    
    except Exception as e:
        # catching any unexpected errors (e.g., timeout, network failure)
        return {"ip": ip, "error": str(e)}
    

# encrich a CSV with raw IP logs
def enrichCSV(inputFile, outputFile):
    """
    writes the results to a new CSV
    """
    with open(inputFile, 'r', encoding='utf-8') as inpFile, open(outputFile, 'w', newline='', encoding='utf-8') as outFile:
        reader = csv.DictReader(inpFile)                                    # CSV readers

        reader.fieldnames = [field.strip() for field in reader.fieldnames]  # a clean up for all headers to remove hidden 
                                                                            # characters/spaces

        # Create a list of cleaned-up rows
        cleanedRows = []
        for row in reader:
            cleanedRow = {k.strip(): v.strip() for k, v in row.items()}
            cleanedRows.append(cleanedRow)
        
        # output columns we want to include
        fieldnames = [
            'ip', 
            'timestamp', 
            'user_agent', 
            'connection_type', 
            'country', 
            'region', 
            'city', 
            'isp', 
            'org', 
            'is_proxy', 
            'is_hosting', 'error'
        ]

        writer = csv.DictWriter(outFile, fieldnames=fieldnames)             # CSV writers
        writer.writeheader()

        for row in cleanedRows:
            ip = row.get("IP Address", "")
            enriched = enrichIP(ip)

            print("Writing Row For IP:", ip)
            print("Original values:", {
                'timestamp': row.get('Timestamp'),
                'user_agent': row.get('User Agent'),
                'connection_type': row.get('Connection Type')
            })

             # writing both the original and enriched data into the new file
            writer.writerow({
                'ip': ip,
                'timestamp': row.get('Timestamp', ''),
                'user_agent': row.get('User Agent', ''),
                'connection_type': row.get('Connection Type', ''),
                'country': enriched.get('country'),
                'region': enriched.get('region'),
                'city': enriched.get('city'),
                'isp': enriched.get('isp'),
                'org': enriched.get('org'),
                'is_proxy': enriched.get('is_proxy'),
                'is_hosting': enriched.get('is_hosting'),
                'error': enriched.get('error')
            })

            time.sleep(1)                                                     # throttles API requests to avoid hitting rate limits