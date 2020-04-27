from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('password', __name__)

@bp.route('/')
def index():
    db = get_db()
    passwords = db.execute(
        'SELECT p.id, created, title, uname, upassword, url, notes'
        ' FROM password p JOIN user u ON p.user_id = {0}'
        ' ORDER BY created DESC'.format(g.user['id'])
    ).fetchall()
    return render_template('password/index.html', passwords = passwords)
