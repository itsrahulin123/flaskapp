from flask import Flask

# The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is
# used.

app = Flask(__name__)
app.config.from_object(Config)

# The app package is defined by the app directory and the __init__.py script, and is referenced in the from app import routes statement.
# The app variable is defined as an instance of class Flask in the __init__.py script, which makes it a member of the app package.

from app import routes


# So what goes in the routes module? The routes handle the different URLs that the application supports. In Flask, handlers for the application routes are written as Python functions, called view functions. View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests a given URL.


