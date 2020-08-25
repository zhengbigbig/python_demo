from flask_restplus import Resource
from flask import request

from myproject.web.apis import api
from myproject.web.models.papers import PaperModel


class PaperParsers(object):
	@staticmethod
	def getpaperlist():
		# 解析器
		parser = api.parser()
		parser.add_argument('index', type=int, help='第几页', required=True)
		parser.add_argument('count', type=int, help='一页包含多少数据', required=True)
		return parser

	@staticmethod
	def getpapersearch():
		# 解析器
		parser = api.parser()
		parser.add_argument('index', type=int, help='第几页', required=True)
		parser.add_argument('count', type=int, help='一页包含多少数据', required=True)
		parser.add_argument('author', type=str, help='论文作者', required=True)
		return parser


class PaperList(Resource):
	@api.expect(PaperParsers.getpaperlist())
	def get(self):
		index = int(request.values.get('index', 0))
		count = int(request.values.get('count', 0))
		papers, has_next = PaperModel.get_papers(index, count)
		return {
			'status': 200,
			'msg': 'success',
			'data': papers,
			'index': index,
			'count': count,
			'has_next': has_next
		}


class PaperAuthorSearch(Resource):
	@api.expect(PaperParsers.getpapersearch())
	def get(self):
		index = int(request.values.get('index', 0))
		count = int(request.values.get('count', 0))
		author = int(request.values.get('author', ''))
		papers, has_next = PaperModel.get_author_paper(index, count, author)
		return {
			'status': 200,
			'msg': 'success',
			'data': papers,
			'index': index,
			'count': count,
			'has_next': has_next
		}


ns = api.namespace('papers', description='论文接口')
ns.add_resource(PaperList, '', '/')
ns.add_resource(PaperAuthorSearch, '/author', '/author/')
