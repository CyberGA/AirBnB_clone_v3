#!/usr/bin/python3
"""A script to to return the status of your API"""
from models import storage
from api.v1.views import app_views
import os


app =  Flask(__name__)
app.register_blueprint(app_views)

host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
port = os.env.get('HBNB_API_PORT', 5000)

@app.teardown_appcontext
def close_storage(exception):
    """freeing up resources such as database connections"""
    storage.close()


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
