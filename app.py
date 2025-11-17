from api import create_app
from api.config import HOST, PORT


app = create_app()


if __name__ == '__main__':
    app.run(debug=False, host=HOST, port=PORT)