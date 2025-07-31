from flask import render_template
from app import app
from app.forms import LoginForm


#In this example there are two decorators, which associate the URLs / and /index to this function. This means that when a web browser requests either of these two URLs, Flask is going to invoke this function and pass its return value back to the browser as a response.

@app.route('/')
@app.route('/index')
def index():
     user = {'username': 'Rahul'}
     return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
      form = LoginForm()
      if form.validate_on_submit():
         flash('Login requested for user {}, remember_me={}'.format(
              form.username.data, form.remember_me.data))
         return redirect(url_for('index'))
      return render_template('login.html', title='Sign In', form=form)
