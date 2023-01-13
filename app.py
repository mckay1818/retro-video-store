from app import create_app

app = create_app()

@app.route("/")
def home():
    return "We are at the video store!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')