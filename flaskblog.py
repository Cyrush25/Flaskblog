from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date posted': 'April 20, 2018'
    },
    {
        'author': 'Aarush Chandna',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date posted': 'May 20, 2023'
    }
]

@app.route('/')
def hello():
    # return '<h1>Helelo Nigalala</h1>'
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    # return '<h1>This is the About Page</h1>'
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)