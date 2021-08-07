import flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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


all_posts = [
    {
        'name': 'First',
        'content': 'This is content of post one'
    },
    {
        'name': 'Second',
        'content': 'This is content of post two'
    }
]


@app.route('/posts')
def posts():
    return(
        flask.render_template('posts.html', posts=all_posts)
    )


@app.route("/")
def index():
    return(
        flask.render_template('index.html')
    )


if __name__ == '__main__':
    app.run(debug=True)
