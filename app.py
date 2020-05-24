from flask import Flask, render_template, request, redirect
from datetime import datetime
from model import RegForm
from flask_bootstrap import Bootstrap
import smtplib


app = Flask(__name__)
if app.config['ENV'] == "production":
    app.config.from_object("config.ProductionConfig")

elif app.config['ENV'] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")
Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    current_time = datetime.now().minute

    return render_template('index.html', time=current_time)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = RegForm(request.form)
    inbox_email = app.config['MAIL_NAME_INBOX']

    if request.method == 'POST' and form.validate_on_submit():
        content_email = request.form['email']
        content_name = request.form['name']
        content_inquiry = request.form['inquiry']
        message = '{}, {}, {}'.format(
            content_email, content_name, content_inquiry)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(app.config['MAIL_ACCOUNT'], app.config['MAIL_PASSWORD'])
        server.sendmail(app.config['MAIL_ACCOUNT'],
                        inbox_email, message)
        return redirect('/')
    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
