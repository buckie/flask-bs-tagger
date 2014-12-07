from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def tags_form():
    if request.method == 'POST':
        print repr(request.form)
        return redirect(url_for('tags_form'))
    return render_template("tag_form.html")


if __name__ == '__main__':
    app.run(debug=True)
