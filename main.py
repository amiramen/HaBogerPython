from flask import Flask
from flask import render_template
import bson.json_util

from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['MONGO_DBNAME'] = "test"
mongo = PyMongo(app)

@app.route('/')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/get_form_data/')
def get_form_data():
    query_result = mongo.db.restaurants.find().limit(5)
    json_serialized_response = bson.json_util.dumps(query_result)
    return json_serialized_response


if __name__ == "__main__":
    app.run()
