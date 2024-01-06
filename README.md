# History 

Saeed (one of my friends) has a sheet for his favorite movies and series. The lack of director names of each movie and serie in that list bothered him. So i create a scraper for Saeed as a birthday gift (sorry for latency).

# Files

**input.csv** is the input given by user. There are some examples in it. Follow the structure. Both fields `name` and `year` are obligatory.

**output.csv** is the output (result) given by app.

**main.py** is the app.

**requirements.txt** is the app's requirements.

**chromedriver** is Google Chrome driver.

# How to use:

1. Clone this repository.
2. Install requirements using `pip install -r requirements.txt`
3. File `chromedriver` should be the same version as your current chrome browser. This chromedriver's version is 120.0.6099, which is same as my chrome browser version. Hopefully, you can find your suitable chromedriver [HERE](https://googlechromelabs.github.io/chrome-for-testing/).
4. Update `input.csv` with the `name` and `year` of the movies which you want to know their directors.
5. Run the app. `python3 main.py`
6. Enjoy! `output.csv`

---
Author: **amyrmahdy**

Date: **13 Feb 2023 [v0]**

Date: **3 Jan 2024 [v1]**


