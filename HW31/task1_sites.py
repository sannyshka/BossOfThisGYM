import requests
import random

websites = ["google.com", "amazon.com", "facebook.com", "twitter.com", "apple.com"]

random_websites = random.choice(websites)

response = requests.get("https://" + random_websites)

print("Wesite: ", random_websites)
print("Status code: ", response.status_code)
print("HTML Length: ", len(response.text))
