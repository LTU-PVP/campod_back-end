from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Collection, db
from routes import bp
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///podcasts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MEDIA_FOLDER'] = './media_test'  # Folder for your MP3 files


UPLOAD_FOLDER = './media_test'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



db.init_app(app)

app.register_blueprint(bp)


# Optional: root route for testing
@app.route('/')
def index():
    return "Podcast API running. Try /shows or /episodes"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Collection.query.filter_by(name="Default Podcast").first():
            default_show = Collection(name="Default Podcast", description="Fallback show for uncategorized episodes")
            db.session.add(default_show)
            db.session.commit()
            print("Default show created with ID:", default_show.id)
    app.run(debug=True, host='localhost', port=5000)

