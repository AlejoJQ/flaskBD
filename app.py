from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<center><h1>JEREMY!!! BUENAS NOTICIAS MI BROOOO FUNCIONAAA!!!!</h1></center>"

if __name__ == "__main__":
    app.run()
