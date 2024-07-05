import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    response = requests.get(url)

    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )

    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

    for job in jobs:
        title = job.find("span", class_="title").text
        job_info = job.find_all("span", class_="company")
        company = job_info[0].text if len(job_info) > 0 else ""
        position = job_info[1].text if len(job_info) > 1 else ""
        region = job_info[2].text if len(job_info) > 2 else ""
        try:
            url = job.find("div",
                           class_="tooltip--flag-logo").next_sibling["href"]
        except KeyError:
            url = "You need log-in"
        job_data = {
            "title": title,
            "company": company,
            "position": position,
            "region": region,
            "url": f"https://weworkremotely.com{url}"
        }
        all_jobs.append(job_data)

def get_pages(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    return len(
        soup.find("div", class_="pagination").find_all("span", class_="page"))

total_pages = get_pages(
    "https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)


