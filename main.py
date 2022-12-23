######################################################################

#       __        _               ___            _  _                #
#    /\ \ \ ___  (_) ____        / __\ ___    __| |(_) _ __    __ _  #
#   /  \/ // _ \ | ||_  /_____  / /   / _ \  / _` || || '_ \  / _` | #
#  / /\  /| (_) || | / /|_____|/ /___| (_) || (_| || || | | || (_| | #
#  \_\ \/  \___/ |_|/___|      \____/ \___/  \__,_||_||_| |_| \__, | #
#                                                             |___/  #

######################################################################

from bs4 import BeautifulSoup
import requests
import os
import platform

clear = "clear"

if platform.system() == "Windows":
    clear = "cls"

os.system(clear)

genres = []
url_dict = {}
genres = ["Action", "Adventure",
             "Animation", "Biography",
             "Comedy", "Crime",
             "Drama", "Family",
             "Fantasy", "Film-Noir",
             "History", "Horror",
             "Music", "Musical",
             "Mystery", "Romance",
             "Sci-Fi", "Sport",
             "Thriller", "War",
             "Western"]

def chGenre():
    global input_genre

    while True:
        input_genre = input("Genre: ")
        if not input_genre in genres:
            print("No such genre.")
        else:
            break

    get_links()

def get_links():

    for genre in genres:
        url = "https://www.imdb.com/search/title/?genres={}&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=N97GEQS6R7J9EV7V770D&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_16"
        formated_url = url.format(genre) 
        url_dict[genre] = formated_url

    return url_dict

def get_movies():
    global movies, ratings
    
    movies = []
    ratings = []

    url = url_dict[input_genre]
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    lister_list = soup.find("div", class_="lister-list")
    titles = lister_list.find_all("h3", class_="lister-item-header")

    for title in titles:
        movies.append(title.text)

    rating_bar = lister_list.find_all("div", class_="ratings-bar")
    for star in rating_bar:
        stars = star.find("strong")
        ratings.append(stars.text)

    create_dict()

def create_dict():
    global movies_stars
    movies_stars = {}

    for i in range(len(movies)):
        movies_stars[movies[i]] = ratings[i]

    return movies_stars

def show():
    for key,value in movies_stars.items():
        print(f"{key} : rating:{value}")
        print("-" * len(key + value))

chGenre()
get_movies()
show()

######################################################################

#       __        _               ___            _  _                #
#    /\ \ \ ___  (_) ____        / __\ ___    __| |(_) _ __    __ _  #
#   /  \/ // _ \ | ||_  /_____  / /   / _ \  / _` || || '_ \  / _` | #
#  / /\  /| (_) || | / /|_____|/ /___| (_) || (_| || || | | || (_| | #
#  \_\ \/  \___/ |_|/___|      \____/ \___/  \__,_||_||_| |_| \__, | #
#                                                             |___/  #

######################################################################
