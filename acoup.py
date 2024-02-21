import requests
import dateparser

from bs4 import BeautifulSoup

def getArticles(start_date, end_date):
    URL = "https://acoup.blog/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    articles = soup.find_all("article")
    for article in articles:
        title = article.find("h1", class_="entry-title")
        if title:
            # Find the link within the title
            link = title.find("a")
            if link:
                # Get time the article was published
                time_tag = article.find("time", class_="entry-date published updated")
                if time_tag is None:
                    time_tag = article.find("time", class_="entry-date published")

                if time_tag:
                    # Print the content of the time tag
                    parsed_date = dateparser.parse(time_tag.text.strip())
                    if parsed_date < start_date or parsed_date > end_date: # Check if the article is out of range
                        print("Article is not in date range given:", parsed_date)
                        continue # Skip the article
                    print("Date:", parsed_date) # need to change prints to put in a csv
                newURL = link.get("href")
                print("Link:", newURL)
                newPage = requests.get(newURL)
                newSoup = BeautifulSoup(newPage.content, 'html.parser')
                newArticle = newSoup.find("div", class_="entry-content")

                paragraphs = newArticle.find_all("p")
                print("Title:", title.text.strip())
                for paragraph in paragraphs:
                    print(paragraph.text,"\n")
    return