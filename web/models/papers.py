from myproject.web.models.mysql import db


class PaperModel(object):
	@staticmethod
	def get_papers(index, count):
		sql = f'''
		select id,title,url from papers
		where is_deleted=0
		limit {(index - 1) * count},{count + 1}
		'''

		result = db.query(sql)
		if not result:
			return [], 0
		if len(result) == count + 1:
			result.pop()
			has_next = 1  # 是否有下一页
		else:
			has_next = 0
		return result, has_next

	@staticmethod
	def get_author_paper(index, count, author):
		author = db.escape_string(author)

		sql = '''
			SELECT id,title,url
			FROM papers
			WHERE authors like '%{author}%' and is_deleted=0
			limit {(index - 1) * count},{count + 1}
		'''

		result = db.query(sql)
		if not result:
			return [], 0
		if len(result) == count + 1:
			result.pop()
			has_next = 1  # 是否有下一页
		else:
			has_next = 0
		return result, has_next
