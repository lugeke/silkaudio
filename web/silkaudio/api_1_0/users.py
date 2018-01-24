from flask import jsonify, request, current_app, url_for
from . import api
from ..models import User


@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())

'''
{
    "email": "lugeke@outlook.com",
    "member_since": "Tue, 26 Dec 2017 16:47:08 GMT",
    "username": "lugeke"
}
'''


@api.route('/users/<int:id>/histories')
def get_user_histories(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.histories.order_by(histories.last_listen.desc())
    .paginate(
            page, per_page=current_app.config['AUDIOBOOKS_PER_PAGE'],
            error_out=False
        )
    histories = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_histories', page=page-1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_histories', page=page+1, _external=True)
    return jsonify({
        'histories': [h.to_json() for h in histories],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })