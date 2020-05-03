import flask
from flask import Flask
import wikipediaapi
import requests as rq
import json

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/')
def home():
    return flask.render_template("page_film.html.jinja2")


@app.route('/getStats/<movie>')
def get_stats(movie):
    omdb = get_omdb_data(movie)
    reponse ={ "Title": movie,
             "Image": omdb["Poster"],
             "Year": omdb["Year"],
             "Actors": omdb["Actors"],
             "Director": omdb["Director"],
             "Genre": omdb["Genre"],
             "Runtime": omdb["Runtime"],
             "Awards": omdb["Awards"],
             "Description": get_description(movie)
             }
    return json.dumps(reponse)


def get_description(movie):
    wiki = wikipediaapi.Wikipedia('fr')
    page = wiki.page(movie)
    return str(page.summary)


def get_omdb_data(movie):
    api_key = get_api_key()
    url = "http://www.omdbapi.com/?apikey={}&t={}".format(api_key, movie)
    r = rq.get(url)
    return r.json()


def get_api_key():
    with open("omdb_key.txt", "r") as f:
        return f.read().strip('\n')





if __name__ == "__main__":
    app.run(debug=True)
