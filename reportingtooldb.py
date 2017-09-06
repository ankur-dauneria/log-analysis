# Import the Postgres SQL component
import psycopg2

DBNAME = "news"           # database name
DBUSER = "vagrant"        # database user name
DBPASSWORD = "vagrant"    # database user password


def get_most_popular_articles():
    """Connects to DB, executes the SQL query (view) most_popular_articles_view
       and returns the results. most_popular_articles_view describes 3 most
       popular articles of all time.

       Attributes: None
       Returns: Set of rows
    """
    db = psycopg2.connect(database=DBNAME, user=DBUSER, password=DBPASSWORD)
    c = db.cursor()
    c.execute("select * from most_popular_articles_view")
    results = c.fetchall()
    db.close()
    return results


def get_most_popular_authors():
    """Connects to DB, executes the SQL query (view) most_popular_authors_view
       and returns the results. most_popular_authors_view describes most
       popular article authors of all time.

       Attributes: None
       Returns: Set of rows
    """
    db = psycopg2.connect(database=DBNAME, user=DBUSER, password=DBPASSWORD)
    c = db.cursor()
    c.execute("select * from most_popular_authors_view")
    results = c.fetchall()
    db.close()
    return results


def get_most_erroneous_day():
    """Connects to DB, executes the SQL query (view) most_erroneous_day_view
       and returns the results. most_erroneous_day_view describes days when
       total HTTP error > 1%.

       Attributes: None
       Returns: Set of rows
    """
    db = psycopg2.connect(database=DBNAME, user=DBUSER, password=DBPASSWORD)
    c = db.cursor()
    c.execute("select * from most_erroneous_day_view")
    results = c.fetchall()
    db.close()
    return results
