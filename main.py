import requests
from bs4 import BeautifulSoup


class JobInfo:

    def __init__(self, url, position, company, location, salary):
        self.url = f"https://remoteok.com{url}"
        self.position = position
        self.company = company
        self.location = location
        self.salary = salary

    def __str__(self):
        return f"Url: {self.url} \n Position: {self.position} \n Company: {self.company} \n Location: {self.location} \n Salary: {self.salary}"


class JobScraper:

    def __init__(self, keyword):
        self.url = f"https://remoteok.com/remote-{keyword}-jobs"
        self.headers = {
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.jobinfos = []

    def print_jobinfos(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        job_elements = soup.find_all("td", class_="company_and_position")[1:]

        for job_element in job_elements:
            url = job_element.find("a")["href"]
            position = job_element.find("h2", itemprop="title").text.strip()
            company = job_element.find("h3", itemprop="name").text.strip()
            class_location = job_element.find_all("div", class_="location")
            location = class_location[0].text.strip() if len(
                class_location) > 0 else ""
            salary = class_location[1].text.strip() if len(
                class_location) > 1 else ""
            jobinfo = JobInfo(url, position, company, location, salary)
            self.jobinfos.append(jobinfo)

        print("-" * 20 + f"{keyword}" + "-" * 20)
        for job in self.jobinfos:
            print(job)
        print("\n")


keywords = ["flutter", "python", "golang", "c-sharp", "javascript"]

for keyword in keywords:
    scraper = JobScraper(keyword)
    scraper.print_jobinfos()
