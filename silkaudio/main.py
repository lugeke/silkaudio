from flask import Flask, render_template, send_file, abort
import os
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



@app.route("/audiobook/<path:filepath>")
def audiobook(filepath):
    """return the mp3 playlist file *.m3u8"""

    if filepath.endswith('.mp3'):
        return send_file(os.path.join('/Users/lugeke/Desktop/silkaudio/audiobook', filepath))
    fm3u8 = os.path.join('/Users/lugeke/Desktop/silkaudio/audiobook', filepath, 'prog_index.m3u8')
    print(filepath)
    print(fm3u8)
    if os.path.exists(fm3u8):
        return send_file(fm3u8, mimetype = 'application/x-mpegURL')
    else:
        abort(404)


