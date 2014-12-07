from flask import render_template, request, redirect, url_for
from app import app

@app.route('/', methods=['GET', 'POST'])
def tags_form():
    if request.method == 'POST':
        print repr(request.form)
        return redirect(url_for('tags_form'))
    return render_template("tag_form.html")


