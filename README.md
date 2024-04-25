## Application Summary
Coffee Badger Press is a content aggregator, aimed at presenting articles from predetermined
websites provided by the client.

## Specifications
The application will present the articles in a format thematic of a classic newspaper, able to be
printed out if needed. The user will be able to specify a desired date range, which the
application will pull all articles within this range. The application will also provide an “all recent
articles” function that will present all articles that have been published since the last time the
application had been run. At a minimum, articles will be pulled from acoup.blog and
insideofknoxville.com.

## Running The Application
The app can be run in one of two ways:

### 1. Download the entire repository
The entire package can be downloaded and unzipped, or the repository cloned. If doing this, the required modules will need to be installed, which can be found in the requirements.txt file, along with their versions. The app can then be run through CBPApp.py in your chosen IDE, or through terminal. When running the application, once the newspaper has been generated, you can find the output in the output.html file.

### 2. Download the app&output folder Only
The app&output folder is a distributable, which includes the CBPApp.exe and ascii-art.png. The executable has be run within the app&output folder. The first time the application is run and the newspaper has been generated, an output.html file will populate within the folder. Anytime the app is re-run, this output file will overwrite with a new newspaper. If you want to save a sepcific generated newspaper, make sure to save a copy elsewhere.
