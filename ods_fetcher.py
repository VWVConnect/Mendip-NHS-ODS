# ods_fetcher.py
import requests

# Example: GP practice data (change URL for others)
url = "https://files.digital.nhs.uk/assets/ods/current/epraccur.csv"
save_as = "epraccur.csv"

r = requests.get(url)
with open(save_as, "wb") as f:
    f.write(r.content)

print("ODS data downloaded.")
