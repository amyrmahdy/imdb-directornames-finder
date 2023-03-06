# History 

Saeed (one of my friends) has a sheet for his favorite movies and series. The lack of director names of each movie and serie in that list bothered him. So i create a scraper for Saeid as a birthday gift (sorry for latency).

# Code

**before.csv** is the sheet before adding directors names.

**after.csv** is the sheet after adding directors names. I added ULR for each movie and serie, too. Maybe he will use that someday!

**main_selenium.py** is the last version of this scraper. Existed some versions without selenium and only using request library but IMDB always blocked my ip, so I used selenium. The steps for this scraper are:

1 - Read all *names* of movies and series that we need to find director of them

2 - Open [imdb website](https://www.imdb.com/) in a chrome browser using selenium

3 - Use *names* in search bar to find the movie or serie

4 - Take first result of the search. Cause it is the most related movie or serie with the *name* that we searched. 

5 - Go to the credit page for the movie or serie.

6 - Take the director(s) name(s).

7 - Take the casts names.

8 - Take the url to imdb page for the movie or serie.

9 - Save the result.


### Author: amyrmahdy
### Date: 13 Feb 2023


