import requests
import dateparser
import datetime
from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup
from newspaper import Article

def getArticles(newspaper, start_date, end_date):
    minimum_date = datetime.datetime(2019, 5 ,3).date()
    if(start_date < minimum_date):
        start_date = minimum_date
    current_date = start_date
    while(current_date < end_date): #+ relativedelta(months=1)
        URL = f"https://acoup.blog/{current_date.year}/{current_date.month}"
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
                        parsed_date = dateparser.parse(time_tag.text.strip()).date()
                        if parsed_date < start_date or parsed_date > end_date: # Check if the article is out of range
                            print("Article is not in date range given:", parsed_date) # temp
                            continue # Skip the article
                        print("Got Article, Date:", parsed_date) # need to change prints to put in a csv
                    newURL = link.get("href")
                    newPage = requests.get(newURL)
                    newSoup = BeautifulSoup(newPage.content, 'html.parser')
                    newArticle = newSoup.find("div", class_="entry-content")
                    author = soup.find('a', rel='author').text.strip()

                    paragraphs = newArticle.find_all("p")
                    images = newArticle.find_all("figure", class_="wp-block-image")
                    contents = []
                    # Iterate over paragraphs and images simultaneously
                    for paragraph, image in zip(paragraphs, images):
                        # Append paragraph text wrapped in <p> tags
                        contents.append(f'<p>{paragraph.text}</p>')
                        # Append image HTML
                        contents.append(str(image))

                    # If there are remaining paragraphs without images
                    if len(paragraphs) > len(images):
                        for paragraph in paragraphs[len(images):]:
                            contents.append(f'<p>{paragraph.text}</p>')

                    # If there are remaining images without paragraphs
                    elif len(images) > len(paragraphs):
                        for image in images[len(paragraphs):]:
                            contents.append(str(image))
                        
                new_article = Article(parsed_date, title.text.strip(), newURL, author, contents)
                newspaper.add_article(new_article)
        if(end_date > current_date):
            current_date += relativedelta(months=1)
    return newspaper