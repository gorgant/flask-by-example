# Here we created a table to store the results of the word counts.

# We first import the database connection that we created in our 
# app.py file as well as JSON from SQLAlchemys PostgreSQL dialects.
# JSON columns are fairly new to Postgres and are not available in
# every database supported by SQLAlchemy so we need to import it
# specifically.

# Next we created a Result() class and assigned it a table name of
# results. We then set the attributes that we want to store for a
# result-

# - the id of the result we stored
# - the url that we counted the words from
# - a full list of words that we counted
# - a list of words that we counted minus stop words (more on this later)

# We then created an __init__() method that will run the first time we 
# create a new result and, finally, a __repr__() method to represent
# the object when we query for it.


from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)