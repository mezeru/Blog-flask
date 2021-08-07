from os import name
import flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy(app)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "Blog Post " + str(self.id)


@app.route('/posts')
def posts():

    if request.method == "POST":
        postName = request.form['name']
        postContent = request.form['content']
        newCard = Card(name=postName, content=postContent)
        db.session.add(newCard)
        return redirect('/posts')
    else:
        allPosts = Card.query.order_by(Card.id).all()
        return(
            flask.render_template('posts.html', posts=allPosts)
        )


@app.route("/")
def index():
    return(
        flask.render_template('index.html')
    )


if __name__ == '__main__':
    app.run(debug=True)
