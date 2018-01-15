from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Audiobook, User

@api.route('/audiobooks/')
def get_audiobooks():    
    page = request.args.get('page', 1, type=int)
    pagination = Audiobook.query.order_by(Audiobook.title.desc()).paginate(
        page, per_page=current_app.config['AUDIOBOOKS_PER_PAGE'], error_out=False
    )
    audiobooks = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_audiobooks', page=page-1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_audiobooks', page=page+1, _external=True)
    # return jsonify({
    #     'audiobooks': [ab.toJSON() for ab in audiobooks],
    #     'prev': prev,
    #     'next': next,
    #     'count': pagination.total
    # })
    return jsonify([{
            'audiobook': ab,
            'progress': {
                "recentChapter": ab.chapter[0],
                "all": {
                    ab.chapter[0]: 0
                }
            },
            "recentListen": 0
} for ab in audiobooks])



#  "progress": {
#             "recentChapter": "05 - Ch01 - The Habit Loop; How Habits Work - Part 03",
#             "all": {
#                 "11 - Ch02 - The Craving Brain; How To Create New Habits - Part 05": 45,
#                 "05 - Ch01 - The Habit Loop; How Habits Work - Part 03": 90
#             }
#         },
#         "recentListen": 1515386324335

@api.route('/audiobooks/<int:id>')
def get_audiobook(id):
    ab = Audiobook.query.get_or_404(id)
    return jsonify(ab.toJSON())


@api.route('/audiobooks/<int:id>/')
def get_audiobook_res(id):
    if filepath.endswith('.mp3'):
        return send_file(os.path.join('/Users/lugeke/Desktop/silkaudio/audiobook', filepath))
    fm3u8 = os.path.join('/Users/lugeke/Desktop/silkaudio/audiobook', filepath, 'prog_index.m3u8')
    print(filepath)
    print(fm3u8)
    if os.path.exists(fm3u8):
        return send_file(fm3u8, mimetype = 'application/x-mpegURL')
    else:
        abort(404)

    