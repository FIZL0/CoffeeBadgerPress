class Article:
    def __init__(self, date, title, link, author, content):
        self.date = date
        self.title = title
        self.link = link
        self.author = author
        self.content = content

class Newspaper:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    
    