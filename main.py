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
    try:
        a = mongo.db.restaurants.find_one()
        b = bson.json_util.dumps(a)
    except :
        print "hey"
        raise
    #json.loads(aJsonString, object_hook=json_util.object_hook)
    return b


if __name__ == "__main__":
    app.run()
