import connexion
import os
import database
from dotenv import load_dotenv
from pages.home import page_home

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Creating Flask app
app = connexion.FlaskApp(__name__, specification_dir=".")

db_connection_string = os.getenv("DATABASE_URL")

app.app.config["SQLALCHEMY_DATABASE_URI"] = db_connection_string
app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

# Add Website UI pages
app.app.register_blueprint(page_home)

database.db.init_app(app.app)
with app.app.app_context():
    database.db.create_all()

# Running app
app.add_api(os.getenv("API_FILE"))
port = os.getenv("VIRTUAL_PORT")
app.run(port=port)