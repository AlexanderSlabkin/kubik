from flask_login import UserMixin

from egg_break import login, db


class User(UserMixin, db.Model):
    username = db.Column(db.String(16), primary_key=True)

    def __str__(self):
        return f'User: {self.username}'

    def get_id(self):
        return self.username


@login.user_loader
def load_user(username):
    print(f'USER is {User.query.get(str(username))}')
    return User.query.get(str(username))
