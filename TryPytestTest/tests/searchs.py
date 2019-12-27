#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

from flask import  Flask,request,jsonify,abort,make_response
from flask_restful import  Resource,Api

app = Flask(__name__)
api = Api(app=app)

books=[{
'id':1,
'author':'无涯',
'name':'Python自动化测试实战',
"done":True
}]

class BooksApi(Resource):

    def get(self):
        return jsonify(books)

    def post(self):
        if not request.json or not 'author' in request.json:
            abort(400)
        book = {
            'id': books[-1]['id'] + 1,
            'author': request.json.get('author'),
            'name': request.json.get('name'),
            'done': False
        }
        books.append(book)
        return jsonify({'status':1002,'msg':'添加成功','datas':book},201)

class BookApi(Resource):
    def get(self,book_id):
        book=list(filter(lambda t:t['id']==book_id,books))
        print(book)
        if len(book)==0:
            abort(400)
        else:
            return jsonify(book)

    def delete(self,book_id):
        book = list(filter(lambda t: t['id'] == book_id, books))
        if len(book)==0:
           abort(404)
        books.remove(book[0])
        return jsonify({'status':1001,'msg':'删除成功'})

api.add_resource(BooksApi, '/v1/api/books', endpoint='/v1/api/books')
api.add_resource(BookApi, '/v1/api/book/<int:book_id>')

if __name__ == '__main__':
   app.run(debug=True)
