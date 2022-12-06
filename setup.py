from setuptools import setup

setup(name='restful_api_examples',
      version='0.1',
      description='Examples for using REST APIs With Flask, Connexion, and SQLAlchemy',
      author='Changjie Lin',
      license='MIT',
      packages=['webapp'],
      install_requires=[
            'connexion[swagger-ui]==2.14.1',
            'Flask==2.2.2',
            'flask-marshmallow[sqlalchemy]==0.14.0'],
      python_requires='>=3.9')
