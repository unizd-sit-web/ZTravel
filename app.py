from project import app
from flask import render_template, session


@app.route('/')
def index():
    return render_template('index.html', email=session.get('email'), favorites=session.get('favorites'),
                           weatherWidgetUrl='44d1215d23/zadar', locationLabel='zadar')


@app.route('/contact')
def contact():
    return render_template('contact.html', email=session.get('email'))


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', email=session.get('email'))


if __name__ == '__main__':
    app.run()

# $env:FLASK_DEBUG=1
# $env:FLASK_APP="app.py"
