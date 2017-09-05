#!/usr/bin/env python

# Import the components
from flask import Flask, request, redirect, url_for, render_template

# Import the database functions corresponding to queries
from reportingtooldb import (get_most_popular_articles,
                             get_most_popular_authors,
                             get_most_erroneous_day)

app = Flask(__name__)

# Render frontend at '/' and display the fetched data on the webpage


@app.route('/', methods=['GET'])
def main():
    """Get the SQL data into a HTML frontend"""
    fetched_1 = get_most_popular_articles()   # fetches results of query 1
    fetched_2 = get_most_popular_authors()    # fetches results of query 2
    fetched_3 = get_most_erroneous_day()      # fetches results of query 3
    return render_template('index.html',
                           fetched_1=fetched_1,
                           fetched_2=fetched_2,
                           fetched_3=fetched_3)

if __name__ == '__main__':
    app.secret_key = "SECRET KEY!"
    app.debug = True
    app.run(host='0.0.0.0', port=8000)  # starts the web server at 0.0.0.0:8000
