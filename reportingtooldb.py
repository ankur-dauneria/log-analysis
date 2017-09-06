# Import the Postgres SQL component
import psycopg2


def dbconnect(database_name="news"):
    """Connects to database and returns the db connection handle and cursor

    Attributes: database name (news as default value)
    Returns: DB connection handle, cursor
    """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Error: Database connect failed!")


def get_most_popular_articles():
    """Connects to DB, executes the SQL query (view) most_popular_articles_view
       and returns the results. most_popular_articles_view describes 3 most
       popular articles of all time.

       Attributes: None
       Returns: Set of rows
    """
    db, cursor = dbconnect()
    query = "select * from most_popular_articles_view"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


def get_most_popular_authors():
    """Connects to DB, executes the SQL query (view) most_popular_authors_view
       and returns the results. most_popular_authors_view describes most
       popular article authors of all time.

       Attributes: None
       Returns: Set of rows
    """
    db, cursor = dbconnect()
    query = "select * from most_popular_authors_view"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


def get_most_erroneous_day():
    """Connects to DB, executes the SQL query (view) most_erroneous_day_view
       and returns the results. most_erroneous_day_view describes days when
       total HTTP error > 1%.

       Attributes: None
       Returns: Set of rows
    """
    db, cursor = dbconnect()
    query = "select * from most_erroneous_day_view"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results
