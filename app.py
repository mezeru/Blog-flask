from os import name
import flask
from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "Blog Post " + str(self.id)


@app.route('/posts/delete/<int:id>')
def delete(id):
    post = Card.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')


@app.route('/posts/edit/<int:id>', methods=["GET", "POSTS"])
def edit(id):
    post = Card.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')


@app.route('/posts', methods=["GET", "POST"])
def posts():

    if request.method == "POST":
        postName = request.form['name']
        postContent = request.form['content']
        newCard = Card(name=postName, content=postContent)
        db.session.add(newCard)
        db.session.commit()
        return redirect('/posts')

    else:
        allPosts = Card.query.order_by(Card.id.desc()).all()
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
