import flask

app = flask.Flask(__name__)

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
