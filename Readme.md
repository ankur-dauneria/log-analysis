# Log Analysis

> This tool analyzes SQL logs to find useful insights. The project uses Flask framework, wherein a lightweight python web server is constructed to query the large Postgres SQL database (with over millions rows) to fetch the results. Results are then displayed on a bootstrap based frontend. In short, it's a reporting tool that queries the database to discover useful insights. Database used here contains newspaper articles, as well as the web server log for the site.

## Front end with output

[Preview image of frontend with output](img/log-analysis.png "Preview")

## Getting started

To use the database extract the `newsdata.sql` file from `newsdata.zip` and put it inside the repository folder, and follow below steps:

```SQL
psql -d news -f newsdata.sql
```

To clone and run the project, follow below steps:

``` python
    git clone <repository>
    cd <repository>
    python reportingtool.py
```

## Project structure

The project analyzes the SQL logs (newsdata.sql) to determine the answer to below queries.

 - What are the most popular three articles of all time?

 - Who are the most popular article authors of all time?

 - On which days did more than 1% of requests lead to errors?

A python web server based on Flask framework is built to query the postgres SQL database (with millions of rows), and display the results on the frontend.

#### Folders

 - `img`  contains prview image (front-end) of Log analysis reporting tool output

 - `templates`  contains HTML templates used by Flask framework

 - `static`  contains JS and CSS files used by Flask framework

 - `files`  contains sample textual output of the program

 `reportingtool.py` contains the web server code. It runs and uses the APIs to fetch the results of the queries.

 `reportingtooldb.py` contains APIs to connects to database, executes different SQLs queries and return the fetched data.

## SQL Queries

- What are the most popular three articles of all time?

``` SQL
create view most_popular_articles_view as select articles.title, count(log.ip) as num from articles left join log on log.path like concat('%', articles.slug, '%') group by articles.title order by num desc limit 3;
```

- Who are the most popular article authors of all time?

```SQL
create view most_popular_authors_view as select A.name, sum(B.num) as sumB from (select authors.id, authors.name, count(articles.title) as num from authors left join articles on authors.id = articles.author group by authors.id, authors.name order by num) as A left join (select articles.author, articles.title, count(log.ip) as num from articles left join log on log.path like concat('%', articles.slug, '%') group by articles.author, articles.title order by num desc) as B on A.id = B.author group by A.name order by sumB desc;
```

- On which days did more than 1% of requests lead to errors?

```SQL
create view most_erroneous_day_view as select * from (select A.dat, (A.num * 100 / B.num) as Percentage from (select log.time::timestamp::date as dat, count(log.status) as num from log where log.status like '404%' group by dat order by num) as A join (select log.time::timestamp::date as dat, count(log.status) as num from log group by dat order by num) as B on A.dat = B.dat) as F where F.percentage > 1;
```

## APIs

```python
def get_most_popular_articles() : Connects to DB, executes the SQL query (view) most_popular_articles_view and returns the results. most_popular_articles_view describes 3 most popular articles of all time.
```

```python
def get_most_popular_authors() : Connects to DB, executes the SQL query (view) most_popular_authors_view and returns the results. most_popular_authors_view describes most popular article authors of all time.
````

```python
def get_most_erroneous_day() : Connects to DB, executes the SQL query (view) most_erroneous_day_view and returns the results. most_erroneous_day_view describes days when total HTTP error > 1%.
```

## Built with

Backend: Python 3

Frontend: HTML5, CSS3, Bootstrap 3

Web framework: Flask

Database: Postgres SQL

Font: Google Fonts

## Found Issue/Report Bug

Please report it using the issues tab.

## Credit

Udacity for providing newsdata.sql

## License

This project uses [MIT](License.md) license.
