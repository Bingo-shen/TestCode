#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

from flask import Flask,make_response,jsonify
from flask_restful import  Resource,Api,reqparse
from flask_httpauth import HTTPBasicAuth

'''实例化Flask这个类'''
app = Flask(__name__)
'''调用flask Restful'''
api = Api(app=app)
'''调用鉴权'''
auth = HTTPBasicAuth()
'''解决jsonify中文显示乱码问题'''
app.config['JSON_AS_ASCII']=False
app.config['DEBUG']=True

'''输入账号密码认证，否者报错提示请认证'''
@auth.get_password
def get_password(username):
    if username == 'shenqiang':
        return 'admin'

@auth.error_handler
def authorized():
    return make_response(jsonify({'msg':'你好，请认证'}),401)

'''页面报错404的友好提示'''
@app.errorhandler(404)
def notFound(error):
    '''函数必须添加：error'''
    return make_response(jsonify({'error':'this page is not found'}),404)

'''页面报错405的友好提示'''
@app.errorhandler(405)
def notFound(error):
    '''函数必须添加：error'''
    return make_response(jsonify({'error':'该请求方法错误'}),405)

'''配置index路由器'''
'''添加登录鉴权资源'''
@app.route('/index')
@auth.login_required
def index():
    return jsonify({'status':0,'msg':'success','datas':{'userid':1003,'name':'shenqiang','age':'18'}})


# '''配置login路由器'''
# class LoginView(Resource):
#     def get(self):
#         return jsonify({'status':0,'msg':'success','datas':{}})
#
#     def post(self):
#         '''简单的数据约束和校验'''
#         parser = reqparse.RequestParser()
#         parser.add_argument('username',type=str,help='您的用户参数不能为空',required=True)
#         parser.add_argument('password',type=str)
#         parser.add_argument('age',type=int,help='您的年龄必须为整型')
#         return jsonify(parser.parse_args())
#
# '''添加请求地址：包含API，视图的路由地址'''
# api.add_resource(LoginView,'/login',endpoint='login')

if __name__ == '__main__':
    app.run(debug=True)