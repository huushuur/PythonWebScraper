from requests import get

websites = (
  "google.com",
  "https://httpstat.us/502",
  "https://httpstat.us/404",
  "https://httpstat.us/300",
  "https://httpstat.us/200",
  "https://httpstat.us/101"
)

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code >= 500:
    results[website] = "SERVER ERROR"
  elif response.status_code >= 400:
    results[website] = "CLIENT ERROR"
  elif response.status_code >= 300:
    results[website] = "REDIRECT"
  elif response.status_code >= 200:
    results[website] = "OK"
  elif response.status_code >= 100:
    results[website] = "INFORMATION"

print(results)
