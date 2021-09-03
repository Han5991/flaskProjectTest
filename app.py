import os

from flask import Flask, render_template, request, redirect
from models import db, Fcuser

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = request.form.get("userid")
        username = request.form.get("username")
        userpw = request.form.get("userpw")
        re_userpw = request.form.get("re_userpw")
        if not (userid and username and userpw and re_userpw) and userpw == re_userpw:
            return render_template('register.html')

        fcuser = Fcuser()
        fcuser.userid = userid
        fcuser.username = username
        fcuser.password = userpw

        db.session.add(fcuser)
        db.session.commit()
        return redirect('/')
    return render_template('register.html')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbFile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbFile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='127.0.0.1', port=5000, debug=True)
