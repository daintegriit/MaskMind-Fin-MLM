import os
import requests

# Known Apple 10-K for 2023
url = "https://www.sec.gov/Archives/edgar/data/320193/000032019323000034/0000320193-23-000034.txt"
save_path = "data/domain_corpus/sec_filings/Apple_10-K_2023.txt"

headers = {
    "User-Agent": "Darryl Carpenter - Research Bot",
    "Accept-Encoding": "gzip, deflate",
    "Host": "www.sec.gov"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"✅ Saved: {save_path}")
else:
    print(f"❌ Error: {response.status_code}")
