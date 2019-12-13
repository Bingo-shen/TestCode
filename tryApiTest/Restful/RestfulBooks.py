#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang
from flask import Flask,make_response,jsonify,abort,request
from flask_restful import Api,Resource
from flask_httpauth import HTTPBasicAuth

'''实例化Flask、Api、HTTPBasicAuth'''
app = Flask(__name__)
api = Api(app=app)
auth = HTTPBasicAuth()
'''解决jsonify中文显示乱码问题'''
app.config['JSON_AS_ASCII']=False
app.config['DEBUG']=True

'''鉴权和异常验证'''

@auth.get_password
def get_password(name):
    if name == "bingo-shen":
        return 'shenqiang'

@auth.error_handler
def authentication():
    return make_response(jsonify({'msg':'请认证'}),401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'msg':'this is page not found'}))

'''图书管理系统'''
books=[
    {'id':1,'author':'bingo','name':'自动化测试','done':True},
    {'id':2,'author':'bingo','name':'自动化测试','done':True}
]

'''函数调用登录鉴权'''
@app.route('/v1/api/books',methods=['GET'])
@auth.login_required
def get_books():
    return jsonify(books)

@app.route('/v1/api/books',methods=['POST'])
@auth.login_required
def create_books():
    if not request.json:
        abort(400)
    else:
        book = {
            'id':books[-1]['id'] + 1,
            'author': request.json.get('author'),
            'name':request.json.get('name'),
            'done':False
        }
        books.append(book)
        return jsonify({'msg':'create success'},201)

@app.route('/v1/api/books/<int:book_id>',methods=['GET'])
@auth.login_required
def get_book(book_id):
    book = list(filter(lambda t:t['id']==book_id,books))
    if len(book)==0:
        abort(404)
    else:
        return jsonify({'status':0,'msg':'success','data':book})

@app.route('/v1/api/books/<int:book_id>',methods=['DELETE'])
@auth.login_required
def delete_book(book_id):
    book = list(filter(lambda t:t['id']==book_id,books))
    if len(book)==0:
        abort(404)
    else:
        books.remove(book[0])
        return jsonify({'status':'1001','msg':'书籍的信息已经删除'})

@app.route('/v1/api/books/<int:book_id>',methods=['PUT'])
@auth.login_required
def put_book(book_id):
    book = list(filter(lambda t: t['id'] == book_id, books))
    if len(book)==0:
        abort(404)
    elif not  request.json:
        abort(400)
    elif 'author' not in request.json and 'name' not in request.json:
        abort(400)
    elif 'done' not in request.json and type(request.json['done']) is not bool:
        abort(400)
    else:
        book[0]['author'] = request.json.get('author',book[0]['author'])
        book[0]['name'] = request.json.get('name', book[0]['name'])
        book[0]['done'] = request.json.get('done', book[0]['done'])
        return jsonify({'statues':1002,'msg':'更新成功','data':book})

if __name__ == '__main__':
    app.run(debug=True)




