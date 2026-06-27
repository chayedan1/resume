from flask import Blueprint, render_template, redirect, url_for, flash, request, make_response
from flask_login import login_user, logout_user, login_required
from app import db
from app.models.user import User
from app.forms.auth import RegisterForm, LoginForm

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.get("/register")
def register_form():
    form = RegisterForm()
    return render_template("auth/register.html", form=form)


@auth_bp.post("/register")
def register_submit():
    form = RegisterForm()
    if not form.validate_on_submit():
        for field, errs in form.errors.items():
            flash(f"{field}: {', '.join(errs)}", "error")
        resp = make_response(render_template("auth/register.html", form=form))
        resp.status_code = 400
        return resp

    if User.query.filter((User.email == form.email.data) | (User.username == form.username.data)).first():
        flash("鐢ㄦ埛鍚嶆垨閭宸茶娉ㄥ唽", "error")
        return render_template("auth/register.html", form=form), 409

    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()

    flash("娉ㄥ唽鎴愬姛锛岃鐧诲綍", "success")
    return redirect(url_for("auth.login_form"))


@auth_bp.get("/login")
def login_form():
    form = LoginForm()
    return render_template("auth/login.html", form=form)


@auth_bp.post("/login")
def login_submit():
    form = LoginForm()
    if not form.validate_on_submit():
        for field, errs in form.errors.items():
            flash(f"{field}: {', '.join(errs)}", "error")
        resp = make_response(render_template("auth/login.html", form=form))
        resp.status_code = 400
        return resp

    user = User.query.filter_by(email=form.email.data).first()
    if not user or not user.check_password(form.password.data):
        flash("閭鎴栧瘑鐮侀敊璇?, "error")
        resp = make_response(render_template("auth/login.html", form=form))
        resp.status_code = 401
        return resp

    login_user(user)
    flash("鐧诲綍鎴愬姛", "success")
    next_url = request.args.get("next") or url_for("resume.resume_list")
    return redirect(next_url)


@auth_bp.get("/logout")
@login_required
def logout():
    logout_user()
    flash("宸查€€鍑虹櫥褰?, "success")
    return redirect(url_for("auth.login_form"))