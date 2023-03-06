import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Read
df = pd.read_csv("before.csv")
df["Year"].astype(int)
all_movies = df.loc[:,"Name"].values.tolist()

# Test
# all_movies = ["Oceans 8","Joker","This Is Us"]
# all_movies = ["Joker"]

# Definition
base_url = "https://www.imdb.com/"
d_path = "./chromedriver"


# Function that takes movie_serie_name and gives movie_url
def find_movie_serie_url(movie_serie_name,driver):
    global base_url
    search_movie_serie = base_url + "find/?q=" + movie_serie_name
    
    driver.get(url = search_movie_serie)
    class_movies_serie = 'ipc-metadata-list-summary-item__t'
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    movies_serie = soup.find('a', attrs = {'class': class_movies_serie })
    movies_serie_url = movies_serie["href"]
    return movies_serie_url

# Function that takes movie_url and gives the soup
def get_soup(movie_url,driver):
    global base_url
    movie_credit_url = movie_url.split("/?")[0] + "/fullcredits/"
    search_director = base_url + movie_credit_url
    driver.get(url = search_director)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    return soup

# Function that takes the soup and gives the directors
def find_movie_directors(soup):
    all_credit = soup.findAll('table', attrs = {'class': "simpleTable simpleCreditsTable"})
    directors = all_credit[0]
    the_directors = []
    for director in directors.findAll("tr"):
        the_directors.append(director.find("td",attrs = {'class' : "name"}).text.strip())
    return ', '.join(the_directors)

# Function that takes the soup and gives the casts
def find_cast(soup):
    all_credit = soup.findAll('table', attrs = {'class': "cast_list"})
    casts_html = all_credit[0]
    the_casts = []
    trs = casts_html.findAll("tr")[1:]
    for tr in trs:
        try:
            name = tr.findAll("td")[1].text.strip()
            the_casts.append(name)
        except:
            print("error")
            break
    return ', '.join(the_casts)



# Body
all_movie_serie_urls = []
all_directors = []
all_casts = []
count = 0
driver = webdriver.Chrome(executable_path = d_path)
for movie_name in all_movies:
    print(movie_name)
    movie_serie_url = find_movie_serie_url(movie_name,driver)
    all_movie_serie_urls.append(base_url + movie_serie_url)
    the_soup = get_soup(movie_serie_url,driver)
    directors = find_movie_directors(the_soup)
    casts = find_cast(the_soup)
    all_directors.append(directors)
    all_casts.append(casts)
    if count == 100:
        count = 0
        driver.quit()
        driver = webdriver.Chrome(executable_path = d_path)
    else:
        count += 1

if driver is not None:
    driver.quit()


# Print results
print(all_directors)
print("--------")
print(all_casts)
print("-------")
print(all_movie_serie_urls)

# # Save only directors and URL
# df_temp = pd.DataFrame({
#     "Director" : all_directors,
#     "URL" : all_movie_serie_urls
# })
# df_temp.to_csv("director_url.csv", index = False)

# Save results
df.loc[:,"Director"] = all_directors
df["URL"] = all_movie_serie_urls
df["Casts"] = all_casts
df.to_csv("after.csv", index = False)


# Author: amyrmahdy
# Date: 13 Feb 2023
