from project import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', weatherWidgetUrl='44d1215d23/zadar', locationLabel='zadar')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run()

# $env:FLASK_DEBUG=1
# $env:FLASK_APP="app.py"
