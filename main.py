import acoup
import insideofknoxville
import datetime
from newspaper import Newspaper
import htmlHeader

def runMain(firstDate, secondDate, sinceLastButton):
    start_date: datetime.date = firstDate
    end_date: datetime.date = secondDate
    since_last_button: bool = sinceLastButton   #if button pressed, will be true

    html_header = htmlHeader.htmlHeader     #html header and styling
    html_header2 = f"""     
    <body>
    <div class="head">
        <div class="headerobjectswrapper">
            <header>Coffee Badger Press</header>
        </div>
        <div class="subhead">Knoxville, TN: {start_date.strftime("%m/%d/%Y")} - {end_date.strftime("%m/%d/%Y")}</div>
    </div>
    <div class="content">
    """

    html_end = "</div> </body> </html>"

    #building the newspaper and populating with articles using the web scrapers
    newspaper = Newspaper()
    newspaper = acoup.getArticles(newspaper, start_date, end_date)
    newspaper = insideofknoxville.getArticles(newspaper, start_date, end_date)
    html_art = []   #articles
    for article in newspaper.articles:
        # Access the attributes of each article
        article_date = article.date
        article_title = article.title
        article_author = article.author
        article_content = article.content
        html_art.append(f"""<div class="column">
            <div class="head"><span class="headline hl3">
            {article_title}</span><p><span class="headline hl4">
            by {article_author}</span></p></div>
            {''.join(article_content)}
        </div>""")

    html_art_string = ''.join(html_art)
    html_content = html_header + html_header2 + html_art_string + html_end

    # Specify the file path where you want to save the HTML file
    file_path = "output.html"

    # Open the file in write mode and write the HTML content to it
    with open("output.html", "w", encoding="utf-8") as file:
        # Write the HTML content to the file
        file.write(html_content)
    print("HTML file has been created successfully!")

    #will update variable in lastRun.py if first button is pressed, updateing to current date
    if (since_last_button):
        lastRunPath = "app&output/lastRun.py"
        lastRunDate = f"\"{end_date}\""
        with open(lastRunPath, "w", encoding="utf-8") as file:
            file.write(lastRunDate)
