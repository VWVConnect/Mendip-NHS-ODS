# ods_fetcher.py
import requests
import os

url = "https://files.digital.nhs.uk/assets/ods/current/epraccur.csv"
filename = "epraccur.csv"

r = requests.get(url)
r.raise_for_status()

with open(filename, "wb") as f:
    f.write(r.content)

print(f"Downloaded: {filename} ({os.path.getsize(filename)} bytes)")
