from flask import Flask
import wikipediaapi
import requests as rq

app = Flask(__name__)

@app.route('/')
def hello_world():
    return get_omdb_data("Inception")


def get_description(movie):
    wiki = wikipediaapi.Wikipedia('fr')
    page = wiki.page(movie)
    return str(page.summary)


def get_omdb_data(movie):
    api_key = get_api_key()
    url = "http://www.omdbapi.com/?apikey={}&t={}".format(api_key, movie)
    r = rq.get(url)
    desc = r.json()["Ratings"][0]["Value"]
    return desc


def get_api_key():
    with open("omdb_key.txt", "r") as f:
        return f.read().strip('\n')



if __name__ == "__main__":
    app.run(debug=True)
