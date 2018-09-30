import click
import os

from app import app, db
from app.models import Message
from flask_migrate import Migrate, upgrade

MIGRATION_DIR = os.path.join('app', 'migrations')

migrate = Migrate(app, db, directory=MIGRATION_DIR)


@app.cli.command()
@click.option("--drop", is_flag=True, help="create after drop.")
def initdb(drop):
    '''initialize database'''
    if drop:
       click.confirm("this action will delete the database, continue?", abort=True)
       db.drop_all()
       click.echo("Drop tables")
    db.create_all()
    click.echo("initialized database")


@app.cli.command()
@click.option("--count", default=20, help="Quantity of message with a default of 20")
def forge(count):
    """generate fake messages"""

    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo("generating messages..")

    for i in range(count):
        message = Message(name=fake.name(), body=fake.sentence(), timestamp=fake.date_time_this_year())
        db.session.add(message)
    db.session.commit()
    click.echo("created %d fake messages." % count)


@app.cli.command()
def deploy():
    """Run development tasks"""
    upgrade()
