from setuptools import setup, find_packages

setup(
    name='applehttp2push',
    version='0.0.1',
    description='一个基于python2和http2的苹果推送SDK 基于yubang的修改',
    author='geyouwen',
    author_email='690591423@qq.com',
    url='https://github.com/yubang/applepush',
    packages=find_packages(),
    install_requires=['hyper', ],
)