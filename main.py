import acoup
import insideofknoxville
import datetime

from newspaper import Newspaper

start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 2, 1)

newspaper = Newspaper()
newspaper = acoup.getArticles(newspaper, start_date, end_date)
#newspaper = insideofknoxville.getArticles(start_date, end_date)
for article in newspaper.articles:
    # Access the attributes of each article
    article_date = article.date
    article_title = article.title
    article_author = article.author
    article_content = article.content
    print(f"-\nTitle: {article_title}\n  Date: {article_date}\n    Author: {article_author}")
print("-")



