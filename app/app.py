from flask import Flask
from justhtml import JustHTML
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/player')
def player_page():
    doc = JustHTML("<html><body><p class='intro'>Hello!</p></body></html>")

    # Query with CSS selectors
    for p in doc.query("p.intro"):
        print(p.name)        # "p"
        print(p.attrs)       # {"class": "intro"}
        print(p.to_html())   # <p class="intro">Hello!</p>
    return doc.query("p.intro")[0].to_html()

if __name__ == '__main__':
    app.run()