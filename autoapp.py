from flask_migrate import Migrate
from silkaudio import create_app, db
from silkaudio.models import Audiobook, User, History
import os, click, json
from datetime import datetime
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.cli.command()
def create_all():
    """create all tables"""
    click.echo('create all tables')
    db.create_all()


@app.cli.command()
def clear_table():
    '''drop all tables'''
    click.echo('drop all tables')
    db.drop_all()
    db.create_all()



@app.cli.command()
@click.option('--startid', default=1, help='the id of audiobook')
def add_audiobook(startid):
    click.echo('add audiobook')
    click.echo(startid)
    dir = '/Users/lugeke/Desktop/frontEnd/silkaudio/public'
    from itertools import count
    import json 
    for i in count(startid):
        p = os.path.join(dir, str(i))
        if os.path.exists(p):
            with open(os.path.join(p, 'book.json')) as f:
                j = json.load(f)
            with open(os.path.join(p, 'chps.json')) as f:
                c = json.load(f)
            j['chapter'] = c
            ab = Audiobook.fromJSON(j)
            db.session.add(ab)
            db.session.commit()
            print(ab.id)
        else:
            break


