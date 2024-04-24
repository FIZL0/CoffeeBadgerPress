#insideofknoxville.com
import requests
import dateparser
from bs4 import BeautifulSoup
from newspaper import Article

def getArticles(newspaper, startDate, endDate):
    startYear = startDate.year
    startMonth = startDate.month

    totalMonths = (endDate.year - startDate.year) * 12 + endDate.month - startDate.month + 1    #total months within date range

    count = 0       #used to increment total months
    counter = 0     #used to increment month called in url
    pageNumber = 1
    print("Total Months: ", totalMonths)
    
    #loop for number of months within date range
    while(count < totalMonths):
        if((startMonth + counter) > 12):    #keep month counter 1-12
            startMonth = 1
            counter = 0
            startYear = startYear + 1
        URL = f"https://insideofknoxville.com/{startYear}/{startMonth + counter}/page/{pageNumber}/"
        print(URL)
       
        #beautifulsoup
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("div", id="main")
        articles = results.find_all("article")

        while True:
            #identifying whether there's a second page of articles
            pageSelector = soup.find("div", class_="pagination tipi-col tipi-xs-12 font-2")
            nextPage = pageSelector.find("a", class_="next page-numbers")

            #grabbing all articles
            for article in articles:
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
                            parsedDate = dateparser.parse(date, settings={'DATE_ORDER': 'YMD'}).date()
                            if parsedDate > endDate or parsedDate < startDate:      #only grabbing articles within date range
                                print("Article out of date range: ", parsedDate)
                                continue
                            print("Got Article: ", parsedDate)

                            articleBody = nResults.find("div", class_="entry-content-wrap")
                            content =  articleBody.find_all(["p", "figure", "ul"])      #will only grab text, images, and list items
                            articleData = []

                            for item in content:
                                if str(item).startswith("<figure class=\"gallery-item\""):  #excluding gallery item images
                                    continue
                                elif str(item).startswith("<figure"):   #appending images and captions
                                    articleData.append(str(item))
                                elif str(item).startswith("<ul>"):  #appending list items 
                                    articleData.append(str(item))
                                else:
                                    articleData.append(f'<p>{item.text}</p>')   #appending paragraphs

                            newArticle = Article(parsedDate, title, nURL, author, articleData)
                            newspaper.add_article(newArticle)

            if nextPage == None:    #if no next page, break the loop
                break
            
            #incrementing the month in the URL and rerunning
            pageNumber = pageNumber + 1
            URL = f"https://insideofknoxville.com/{startYear}/{startMonth + counter}/page/{pageNumber}/"     
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find("div", id="main")
            articles = results.find_all("article")    
            
        pageNumber = 1    
        count = count + 1
        counter = counter + 1
    return newspaper