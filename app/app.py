from flask import Flask, render_template, send_from_directory
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
    
    return doc.to_html()

#http://127.0.0.1:5000/audio/Pink_Floyd_Time.mp3
@app.route('/audio/<path:Pink_Floyd_Time>')
def serve_floyd(Pink_Floyd_Time):
        return send_from_directory('static/audio', Pink_Floyd_Time)

if __name__ == '__main__':
    app.run()