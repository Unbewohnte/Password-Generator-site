from flask import Flask,render_template, request,redirect,url_for
from forms import PasswordGenerationForm,PasswordGenerationFormRu
from password_generator import generate


application = Flask(__name__)
application.config['SECRET_KEY'] = '' #Generate your own



@application.route("/",methods=['POST','GET'])
def redir():
	return redirect(url_for('enpage'),code=302)


@application.route("/en", methods= ['POST','GET'])
def enpage():
    form = PasswordGenerationForm()
    if form.validate_on_submit():
        form.valid = True
        Checkbox_values = [{'checkbox':'Upper_reg','value':request.form.get('Upper_register_field')},
                        {'checkbox':'Digits','value':request.form.get('Digits_field')},
                        {'checkbox':'Punctuation','value':request.form.get('Punctuation_field')}]
        len = int(request.form['length'])
        how_many = int(request.form['how_many_passwords'])
        form.password = generate(len,how_many=how_many,flags=Checkbox_values)
    else:
        form.valid = False
        print('Something went wrong')
    return render_template("homeen.html", form = form)


@application.route("/ru", methods= ['POST','GET'])
def rupage():
    form = PasswordGenerationFormRu()
    if form.validate_on_submit():
        form.valid = True
        Checkbox_values = [{'checkbox':'Upper_reg','value':request.form.get('Upper_register_field')},
                        {'checkbox':'Digits','value':request.form.get('Digits_field')},
                        {'checkbox':'Punctuation','value':request.form.get('Punctuation_field')}]
        len = int(request.form['length'])
        how_many = int(request.form['how_many_passwords'])
        form.password = generate(len,how_many=how_many,flags=Checkbox_values)
    else:
        form.valid = False
        print('Something went wrong')
    return render_template("homeru.html", form = form)

@application.errorhandler(404)
def not_found(error):
    return render_template('not_found404.html',error = error)


# Run Flask as Python script without any foreign commands
if __name__ == '__main__':
    application.run(debug = False)
