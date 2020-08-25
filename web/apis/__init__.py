from flask_restplus import Api
from myproject.web import app

api = Api(
	app,
	version='0.0.1',
	title='papers apis',
	description='网站API',
	# authorizations={} # 认证
	ui=True
)

from myproject.web.apis.papers import *
