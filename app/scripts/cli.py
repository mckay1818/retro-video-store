import click

@click.group()
def main():
    click.echo("Welcome welcome!")

@click.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=5000, type=int)
def web(host: str, port: int):
    from app import create_app
    app = create_app()
    app.run(host=host, port=port)

if __name__ == '__main__':
    print("made it")
    click.echo("OR DID I")
    main()