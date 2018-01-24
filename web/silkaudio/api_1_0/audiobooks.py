from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Audiobook, User
from silkaudio import db


@api.route('/audiobooks/')
def get_audiobooks():
    page = request.args.get('page', 1, type=int)
    pagination = Audiobook.query.order_by(Audiobook.title.desc()).paginate(
        page, per_page=current_app.config['AUDIOBOOKS_PER_PAGE'],
        error_out=False
    )
    audiobooks = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_audiobooks', page=page-1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_audiobooks', page=page+1, _external=True)
    return jsonify({
        'audiobooks': [ab for ab in audiobooks],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/audiobook/<int:id>')
def get_audiobook(id):
    ab = Audiobook.query.get_or_404(id)
    return jsonify(ab)


@api.route('/audiobook', methods=['GET', 'POST'])
def audiobook():
    if request.method == 'POST':
        book = request.get_json()
        # modify
        if 'id' in book:
            ab = Audiobook.query.get_or_404(book['id'])
            if 'title' in book:
                ab.title = book['title']
            if 'description' in book:
                ab.description = book['description']
            if 'author' in book:
                ab.author = book['author']
            db.session.add(ab)
            db.session.commit()
            return jsonify({'success': True})
        # add
        else:
            if 'chapter' not in book:
                book['chapter'] = []
            if not ('title' in book and 'author' in book and
                    'description' in book):
                return jsonify({'success': False, 'message':
                                'title,author,description can\'t be empty'})
            ab = Audiobook.fromJSON(book)
            db.session.add(ab)
            db.session.commit()
            return jsonify({
              'success': True,
              'id': ab.id
            })


@api.route('/audiobooks/search/')
def search_audiobooks():
    title = request.args.get('title')
    author = request.args.get('author')
    return '123'

