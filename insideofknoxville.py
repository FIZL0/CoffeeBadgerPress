#insideofknoxville.com
import requests
import dateparser
from bs4 import BeautifulSoup

def getArticles(startDate, endDate):
    startYear = startDate.year
    startMonth = startDate.month
    totalMonths = (endDate.year - startDate.year) * 12 + endDate.month - startDate.month + 1
    count = 0   #used to increment total months
    counter = 0 #used to increment month called in url
    pageNumber = 1
    print("Total Months: ", totalMonths)

    while(count < totalMonths):
        if((startMonth + counter) > 12):
            startMonth = 1
            counter = 0
            startYear = startYear + 1
        URL = f"https://insideofknoxville.com/{startYear}/{startMonth + counter}/page/{pageNumber}/"
        print(URL)
       
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("article")

        #this block checks for multiple days of articles
        pageSelector = soup.find("div", class_="pagination tipi-col tipi-xs-12 font-2")
        nextPage = pageSelector.find("a", class_="next page-numbers")
        if nextPage:
            print("YES")
        else:
            print("NO")

        while nextPage:

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
                            #for paragraph in content:  
                            #   print(paragraph.text)
                            print("\n\n")
            pageNumber = pageNumber + 1
            URL = f"https://insideofknoxville.com/{startYear}/{startMonth + counter}/page/{pageNumber}/"
            print(URL)
        
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all("article")    
            pageSelector = soup.find("div", class_="pagination tipi-col tipi-xs-12 font-2")
            nextPage = pageSelector.find("a", class_="next page-numbers")

        pageNumber = 1    
        count = count + 1
        counter = counter + 1