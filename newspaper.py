class Article:
    def __init__(self, date, title, link, content):
        self.date = date
        self.title = title
        self.link = link
        self.content = content

class Newspaper:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def display_articles(self):
        for idx, article in enumerate(self.articles, start=1):
            print(f"Article {idx}:")
            print(f"Date: {article.date}")
            print(f"Title: {article.title}")
            print(f"Link: {article.link}")
            print(f"Content: {article.content}")
            print()
    