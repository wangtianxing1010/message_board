from flask import flash, render_template, url_for, redirect

from app import app, db
from app.forms import MessageOnBoardForm
from app.models import Message


@app.route('/', methods=['POST','GET'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = MessageOnBoardForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('Your message has been posted!')
        return redirect(url_for("index"))
    return render_template('index.html', form=form, messages=messages)