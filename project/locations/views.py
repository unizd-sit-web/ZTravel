from flask import Blueprint, render_template, session

locations_blueprint = Blueprint('locations',
                                __name__,
                                template_folder='templates/locations')


@locations_blueprint.route('/plitvicka_jezera')
def plitvicka_jezera():
    return render_template('plitvicka_jezera.html', locationId=1, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='44d8815d62/plitvicka-jezera', locationLabel='plitvička jezera')


@locations_blueprint.route('/krka')
def krka():
    return render_template('krka.html', locationId=2, favorites=session.get('favorites'), email=session.get('email'),
                           weatherWidgetUrl='45d0314d58/krk', locationLabel='krka')


@locations_blueprint.route('/kudin')
def kudin():
    return render_template('kudin.html', locationId=3, favorites=session.get('favorites'), email=session.get('email'),
                           weatherWidgetUrl='44d2015d82/golubic', locationLabel='golubić')


@locations_blueprint.route('/vransko_jezero')
def vransko_jezero():
    return render_template('vransko_jezero.html', locationId=4, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='43d9515d57/lake-vrana-dalmatia', locationLabel='vrana')


@locations_blueprint.route('/mars_trail')
def mars_trail():
    return render_template('mars_trail.html', locationId=5, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='44d4415d06/pag', locationLabel='pag')


@locations_blueprint.route('/tulove_grede')
def tulove_grede():
    return render_template('tulove_grede.html', locationId=6, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='44d2315d57/jasenice-zadar-county', locationLabel='tulove grede')


@locations_blueprint.route('/grabovaca')
def grabovaca():
    return render_template('grabovaca.html', locationId=7, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='44d9715d65/grabovac', locationLabel='grabovac')


@locations_blueprint.route('/kornati')
def kornati():
    return render_template('kornati.html', locationId=8, favorites=session.get('favorites'), email=session.get('email'),
                           weatherWidgetUrl='43d8115d31/kornati', locationLabel='kornati')


@locations_blueprint.route('/una')
def una():
    return render_template('una.html', locationId=9, favorites=session.get('favorites'), email=session.get('email'),
                           weatherWidgetUrl='43d5816d60/dugopolje', locationLabel='dugopolje')


@locations_blueprint.route('/velebit')
def velebit():
    return render_template('velebit.html', locationId=10, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='44d8215d05/krasno', locationLabel='velebit')


@locations_blueprint.route('/paklenica')
def paklenica():
    return render_template('paklenica.html', locationId=11, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='45d3217d02/paklenica', locationLabel='paklenica')


@locations_blueprint.route('/zrmanja')
def zrmanja():
    return render_template('zrmanja_rafting.html', locationId=12, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='44d1916d06/zrmanja-vrelo', locationLabel='zrmanja vrelo')


@locations_blueprint.route('/cetina_spring')
def cetina_spring():
    return render_template('cetina_spring.html', locationId=13, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='43d4416d69/omis', locationLabel='omiš')


@locations_blueprint.route('/cetina_rafting')
def cetina_rafting():
    return render_template('cetina_rafting.html', locationId=14, favorites=session.get('favorites'),
                           email=session.get('email'),
                           weatherWidgetUrl='43d4416d69/omis', locationLabel='omiš')


@locations_blueprint.route('/silba')
def silba():
    return render_template('silba.html', locationId=15, favorites=session.get('favorites'), email=session.get('email'),
                           weatherWidgetUrl='44d3814d69/silba', locationLabel='silba')
