from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1de4d8a8d38166817d76bb768175f9c3'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)



if __name__ == '__main__':
    app.run(debug=True)