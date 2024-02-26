import acoup
import datetime

from newspaper import Newspaper
acoup_minimum_start_date = datetime.datetime(2019, 5, 1)
start_date = datetime.datetime(2019, 5, 1)
end_date = datetime.datetime(2024, 1, 15)

newspaper = Newspaper()
newspaper = acoup.getArticles(newspaper, start_date, end_date)

for article in newspaper.articles:
    # Access the attributes of each article
    article_date = article.date
    article_title = article.title
    article_content = article.content
    #print(article_date,article_title,article_content)


