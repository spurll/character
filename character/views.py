from flask import render_template, flash, redirect, session, url_for, request

from character import app
from character.forms import LoginForm, TemplateForm
from character.models import User, Object


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for("view"))


@app.route('/view')
@login_required
def view_objects():
    """
    Views objects.
    """
    user = current_user
    objects = user.objects

    form = TemplateForm()

    if not objects:
        flash("You don't have any objects.")

    return render_template(
        "view.html", title="View", user=user, links=None, form=form,
        objects=objects
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Logs the user in using LDAP authentication.
    """
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', title="Log In", form=form)

    if form.validate_on_submit():
        user = authenticate(form.username.data, form.password.data)

        if not user:
            flash('Login failed.')
            return render_template('login.html', title="Log In", form=form)

        if user and user.is_authenticated:
            db_user = User.query.get(user.id)
            if db_user is None:
                db.session.add(user)
                db.session.commit()

            login_user(user, remember=form.remember.data)

            return redirect(request.args.get('next') or url_for('index'))

    return render_template('login.html', title="Log In", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@lm.user_loader
def load_user(id):
    return User.query.get(id)
