from project import app,db
from flask import render_template , redirect , request , url_for , flash , abort
from flask_login import login_user , login_required , logout_user
from project.models import User
from project.forms import LoginForm , RegistrationForm , Calculator , Level


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/stepone')
def stepone():
    form=Level()
    if form.validate_on_submit():
        if form.beginner==NotImplemented and form.intermediate==NotImplemented:
            level=form.advanced
        if form.advanced==NotImplemented and form.beginner==NotImplemented:
            level=form.intermediate
        if form.intermediate==NotImplemented and form.advanced==NotImplemented:
            level=form.beginner
        return render_template("training_plan.html",level=level)
    return render_template("training_plan.html",form=form)

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/Register',methods=['GET','POST'])
def register():
    form2 = LoginForm()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,
        password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    if form2.validate_on_submit():
        user = User.query.filter_by(email=form2.email.data).first()
        if user is None:
            flash("The account is not valid!")
        elif user.check_password(form2.password.data) and user is not None:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('register.html',form=form,form2=form2)

@app.route("/calculator",methods=['GET','POST'])
def calculator():
    form = Calculator()
    if(form.validate_on_submit()):
        calories = 66.5+(13.75*form.weight.data)+(5.003*form.height.data)-(6.75*form.age.data)
        calories = int(calories)
        protein=form.weight.data*2

        return render_template("calculator.html",form=form,calories=calories,protein=protein)
    else:
        protein=140
        calories=2000
        return render_template("calculator.html",form=form,calories=calories,protein=protein)

@app.route("/steps")
def steps():
    return render_template("steps.html")
if __name__=='__main__':
    app.run(debug=True)