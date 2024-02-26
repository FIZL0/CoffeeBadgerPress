#insideofknoxville.com
import requests
import dateparser
from bs4 import BeautifulSoup

def getArticles(startDate, endDate):
    URL = "https://insideofknoxville.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("article")

    for article in results:
        nURL = article.find("a").get("href")
        nPage = requests.get(nURL)
        nSoup = BeautifulSoup(nPage.content, "html.parser")
        nResults = nSoup.find("article")

        title = nResults.find("h1", class_="title")
        
        if title:
            title = title.text.strip()
            author = nResults.find("span", class_="author")        
            if author:
                author = author.text.strip()
                date = nResults.find("span", class_="date")            
                if date:
                    date = date.text.strip()
                    parsedDate = dateparser.parse(date, settings={'DATE_ORDER': 'YMD'})

                    if parsedDate > endDate or parsedDate < startDate:
                        print("Article out of date range: ", parsedDate)
                        continue

                    content = nResults.find_all("p")

                    print(title)
                    print(author)
                    print(parsedDate)
                    for paragraph in content:  
                        print(paragraph.text)
                    print("\n\n")