from app import create_app
import click

app = create_app()

@app.cli.command("welcome")
@app.route("/")
def home():
    click.echo("We are at the video store!")

if __name__ == '__main__':
    print("Running from wsgi.py")
    app.run()
