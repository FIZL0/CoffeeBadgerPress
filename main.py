import acoup
import insideofknoxville
import datetime

from newspaper import Newspaper

start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 1, 28)

html_header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>CoffeeBadgerPress</title>
    <meta name="viewport" content="width=device-width">
    <style>
        body {
            font-family: 'Droid Serif', serif;
            font-size: 14px;
            color: #2f2f2f;
            background-color: #f9f7f1;
        }

        header {
            font-family: 'Playfair Display', serif;
            font-weight: 900;
            font-size: 80px;
            text-transform: uppercase;
            display: inline-block;
            line-height: 72px;
            margin-bottom: 20px;
        }

        p {
            margin-top: 0;
            margin-bottom: 20px;
        }

        .head {
            text-align: center;
            position: relative;
        }

        .subhead {
            text-transform: uppercase;
            border-bottom: 2px solid #2f2f2f;
            border-top: 2px solid #2f2f2f;
            padding: 12px 0 12px 0;
        }

        .weatherforcastbox {
            position: relative;
            width: 12%;
            left: 10px;
            border: 3px double #2f2f2f;
            padding: 10px 15px 10px 15px;
            line-height: 20px;
            display: inline-block;
            margin: 0 50px 20px -360px;
        }

        .content {
            font-size: 0;
            line-height: 0;
            word-spacing: -.31em;
            display: inline-block;
            margin: 30px 2% 0 2%;
        }

        .collumns {}

        .collumn {
            font-size: 14px;
            line-height: 20px;
            width: 31.2%;
            display: inline-block;
            padding: 0 1% 0 1%;
            vertical-align: top;
            margin-bottom: 50px;
            transition: all .7s;
        }

        .collumn+.collumn {
            border-left: 1px solid #2f2f2f;
        }

        .collumn .headline {
            text-align: center;
            line-height: normal;
            font-family: 'Playfair Display', serif;
            display: block;
            margin: 0 auto;
        }

        .collumn .headline.hl1 {
            font-weight: 700;
            font-size: 30px;
            text-transform: uppercase;
            padding: 10px 0 10px 0;
        }

        .collumn .headline.hl2 {
            font-weight: 400;
            font-style: italic;
            font-size: 24px;
            box-sizing: border-box;
            padding: 10px 0 10px 0;
        }
        /* Rest of your CSS styles */
    </style>
</head>
<body>
<div class="head">
    <div class="headerobjectswrapper">
        <header>Coffee Badger Press</header>
    </div>
    <div class="subhead">Knoxville, TN: start_date - end_date</div>
</div>
<div class="content">
    <!-- Your content here -->"""

html_end = """</div> </body> </html>"""

newspaper = Newspaper()
newspaper = acoup.getArticles(newspaper, start_date, end_date)
#newspaper = insideofknoxville.getArticles(start_date, end_date)
print("\nRESULTS:\n")
html_art = []
for article in newspaper.articles:
    # Access the attributes of each article
    article_date = article.date
    article_title = article.title
    article_author = article.author
    article_content = article.content
    html_art.append(f"""<div class="collumn">
            <div class="head"><span class="headline hl3">{article_title}</span><p><span class="headline hl4">by {article_author}</span></p></div>
            {article_content}</p></div>
        """)
    print(f"-\nTitle: {article_title}\n  Date: {article_date}\n    Author: {article_author}")
print("-")

html_art_string = ''.join(html_art)
html_content = html_header + html_art_string + html_end

# Specify the file path where you want to save the HTML file
file_path = "output.html"

# Open the file in write mode and write the HTML content to it
with open("output.html", "w", encoding="utf-8") as file:
    # Write the HTML content to the file
    file.write(html_content)


print("HTML file has been created successfully!")



