# coding:utf-8

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '21732181'
API_KEY = 'XCQT4EcaOLxCZwvC6xY7ALQh'
SECRET_KEY = 'sHPAwmEmFdlrp4ibAOmZMWLmQ1SGTFSS'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
s = '皮皮真，你是傻屌'
result = client.synthesis(s, 'zh', 1, {
	'vol': 5,  # 音量，取值0-15，默认5中音量
	'per': 3,
	'spd': 6,  # 语速，取值0-9，默认为5中语速
	'pit': 3,  # 音调，取值0-9，默认为5中语调
})
print(result)
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
	with open('auido.mp3', 'wb') as f:
		f.write(result)
