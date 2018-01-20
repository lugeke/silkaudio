from silkaudio import create_app, db
from silkaudio.models import Audiobook, User, History
import os, click, json, subprocess, shlex
from datetime import datetime
from flask import url_for
from flask.json import JSONEncoder

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Audiobook):
            return {
            'id': obj.id,
            'url': url_for('api.get_audiobook', id=obj.id, _external=True),
            'title': obj.title,
            'author': obj.author,
            'description': obj.description,
            'chapter': obj.chapter
        }
        return super().default(obj)
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.json_encoder = MyJSONEncoder

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
@click.option('--host', default='', help='the id of audiobook')
@click.option('--no-debugger', help='the id of audiobook')
def add_audiobook(host, no_debugger):
    click.echo('add audiobook')
    audioPath = os.environ.get('AUDIO_PATH') or r'/Users/lugeke/Desktop/audiobook'

    dirs = [f for f in os.listdir(audioPath) if os.path.isdir(os.path.join(audioPath, f))]
    try:
        for d in dirs:
            d = os.path.join(audioPath, d)
            with open(os.path.join(d, 'book.json')) as f:
                j = json.load(f)
            # with open(os.path.join(d, 'chps.json')) as f:
            #     c = json.load(f)
            # j['chapter'] = c
            ab = Audiobook.fromJSON(j)
            db.session.add(ab)
            db.session.commit()
    except Exception as e:
        print(e)


@app.cli.command()
# @click.option('--host', default='', help='the id of audiobook')
# @click.option('--no-debugger', help='the id of audiobook')
# def generateSoftLnk(host, no_debugger):
def generateSoftLnk():
    click.echo('generateSoftLnk')
    audioPath = os.environ.get('AUDIO_PATH') or r'/Users/lugeke/Desktop/audiobook'

    for ab in Audiobook.query.all():
        sourceFile = os.path.join(audioPath, ab.title.replace(' ', '_'))
        targetFile = os.path.join(audioPath, str(ab.id))
        if os.path.exists(targetFile):
            print('target file {} exist'.format(targetFile))
            continue
        elif not os.path.exists(sourceFile):
            print('source file {} not exist'.format(sourceFile))
            continue
        elif subprocess.call(['ln', '-s', '{}'.format(sourceFile), targetFile]) != 0:
            print('create link error {} {}'.format(ab.id, ab.title))
        else:
            print('create link success {} {}'.format(ab.id, ab.title))