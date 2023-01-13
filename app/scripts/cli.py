import click

@click.group()
def main():
    #this will be run when cli.py is run as a script
    click.echo("Welcome welcome!")
    return 'Welllllll'

@click.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=5000, type=int)
def web(host: str, port: int):
    from wsgi import app
    app.run(host=host, port=port)

if __name__ == '__main__':
    print('Running from cli.py')
    web()