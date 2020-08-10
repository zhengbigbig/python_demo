from removebg import RemoveBg
import os

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')
rmbg = RemoveBg("DuU5fYvDaiYyt8Ya3466666", "error.log")
path = 'images'


def remove_bg(img_path):
	rmbg.remove_background_from_img_file(img_path)
