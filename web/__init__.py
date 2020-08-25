from flask import Flask
from flask_bootstrap import Bootstrap

# 初始化flask
app = Flask(__name__,
            template_folder='./templates',
            static_folder='./templates/static')
bootstrap = Bootstrap(app)

from myproject.web.apis import *
from myproject.web.views import *