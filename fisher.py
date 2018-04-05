# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
from app import create_app

__author__ = 'Alimazing'

app = create_app()
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3001)