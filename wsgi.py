from app import create_app

app = create_app()

@app.route("/")
def home():
    return "We are at the video store!"

if __name__ == '__main__':
    print("Running from wsgi.py")
    app.run()
