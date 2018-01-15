from . import db
from flask import url_for
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
class Audiobook(db.Model):
    __tablename__ = 'audiobook'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.JSON, nullable=False)
    description = db.Column(db.Text, nullable=False)
    chapter = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return '<Audiobook id:{} title:{}>'.format(self.id, self.title)


    # def toJSON(self):
    #     jsonPost = {
    #         'id': self.id,
    #         'url': url_for('api.get_audiobooks', id=self.id, _external=True),
    #         'title': self.title,
    #         'author': self.author,
    #         'description': self.description,
    #         'chapter': self.chapter
    #     }
    #     return jsonPost

    @staticmethod
    def fromJSON(json):
        return Audiobook(
        title=json['title'], 
        author=json['author'], 
        description=json['description'],
        chapter= json['chapter'])



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    passwordHash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    memberSince = db.Column(db.DateTime, default=datetime.utcnow)
    histories = db.relationship('History', backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.passwordHash = generate_password_hash(password)

    def verifyPassword(self, password):
        return check_password_hash(self.passwordHash, password)

    def toJSON(self):
        jsonPost = {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'memberSince': self.memberSince,
            # 'histories': [h.toJSON() for h in self.histories.all()]
        }
        return jsonPost

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps({'id': self.id}).decode('ascii')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return '<User id:{} name:{}>'.format(self.id, self.username)


class History(db.Model):
    __tablename__ = 'history'
    userId = db.Column(db.Integer, db.ForeignKey('user.id'),
                        primary_key=True)
    audiobookId = db.Column(db.Integer, db.ForeignKey('audiobook.id'),
                             primary_key=True)
    chapterHistory = db.Column(db.JSON, nullable=False)
    recentListen = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<History userId:{} audiobookId:{}>'.format(self.userId, self.audiobookId)

    def toJSON(self):
        jsonPost = {
            'audiobook': Audiobook.query.get(id).toJSON(),
            'recentListen': self.recentListen,
            'chapterHistory': self.chapterHistory
        }
        return jsonPost

    
