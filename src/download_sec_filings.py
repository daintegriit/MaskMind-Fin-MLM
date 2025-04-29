import os
import requests
import time

HEADERS = {
    "User-Agent": "Darryl Carpenter - Research Bot",
    "Accept-Encoding": "gzip, deflate",
    "Host": "www.sec.gov"
}

BASE_INDEX_URL = "https://data.sec.gov/submissions/CIK{CIK}.json"
BASE_ARCHIVE_URL = "https://www.sec.gov/Archives"

def download_sec_filings(cik, company_name, save_dir="data/domain_corpus/sec_filings/", filing_type="10-K", count=3):
    cik_padded = cik if len(cik) == 10 else cik.zfill(10)
    url = BASE_INDEX_URL.format(CIK=cik_padded)
    res = requests.get(url, headers=HEADERS)

    if res.status_code != 200:
        print(f"❌ Error fetching filings: {res.status_code}")
        return

    filings = res.json().get("filings", {}).get("recent", {})
    form_list = filings.get("form", [])
    accession_numbers = filings.get("accessionNumber", [])

    os.makedirs(save_dir, exist_ok=True)

    downloaded = 0
    for form, acc_num in zip(form_list, accession_numbers):
        if form != filing_type:
            continue

        acc_num_clean = acc_num.replace("-", "")
        txt_file_name = f"{acc_num_clean}.txt"
        doc_url = f"{BASE_ARCHIVE_URL}/edgar/data/{cik_padded}/{acc_num_clean}/{txt_file_name}"
        print(f"🔗 Fetching: {doc_url}")
        res = requests.get(doc_url, headers=HEADERS)

        if res.status_code == 200:
            file_path = os.path.join(save_dir, f"{company_name}_{filing_type}_{downloaded+1}.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(res.text)
            print(f"✅ Saved: {file_path}")
            downloaded += 1
        else:
            print(f"⚠️ Could not fetch: {doc_url}")

        time.sleep(1)
        if downloaded >= count:
            break

    if downloaded == 0:
        print("⚠️ No filings downloaded.")
    else:
        print(f"🎉 Downloaded {downloaded} {filing_type} filings for {company_name}.")

# Try it!
download_sec_filings("0000320193", "Apple")
