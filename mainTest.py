#ignore this. Just using it for testing

import insideofknoxville
import datetime

from newspaper import Newspaper

start_date = datetime.datetime(2024, 2, 1)
end_date = datetime.datetime(2024, 3, 2)

insideofknoxville.getArticles(start_date, end_date)