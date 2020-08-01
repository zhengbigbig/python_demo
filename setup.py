import setuptools
import os

# 配置路径
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
# 读取文件并作为描述
with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='zbb',
    version='0.0.1',
    author='zbb',
    author_email='780357902@qq.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    py_modules=['langspeak'],
    packages=setuptools.find_packages(),  # 配置路径
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
