from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models.resume import Resume

resume_bp = Blueprint("resume", __name__, url_prefix="/resume")


@resume_bp.get("/list")
@login_required
def resume_list():
    resumes = Resume.query.filter_by(user_id=current_user.id).order_by(Resume.updated_at.desc()).all()
    return render_template("resume/list.html", resumes=resumes)


@resume_bp.post("/create")
@login_required
def resume_create():
    resume = Resume(user_id=current_user.id, title="未命名简历")
    db.session.add(resume)
    db.session.commit()
    flash("简历已创建", "success")
    return redirect(url_for("resume.resume_edit", resume_id=resume.id))


@resume_bp.get("/<int:resume_id>/edit")
@login_required
def resume_edit(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user_id != current_user.id:
        flash("无权限访问该简历", "error")
        return redirect(url_for("resume.resume_list"))
    return render_template("resume/edit.html", resume=resume)


@resume_bp.post("/<int:resume_id>/delete")
@login_required
def resume_delete(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user_id != current_user.id:
        flash("无权限删除该简历", "error")
        return redirect(url_for("resume.resume_list"))

    db.session.delete(resume)
    db.session.commit()
    flash("简历已删除", "success")
    return redirect(url_for("resume.resume_list"))
