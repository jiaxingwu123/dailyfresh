# coding=utf-8
from django.http import HttpResponseRedirect

# 如果登录则转到登录页面
def islogin(func):
    def login_fun(request,*args,**kwargs):
        # 登录成功时写拉一个session信息
        if request.session.get('user_id'):
            # 如果有user_id则执行装施器所装是的函数
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            # url为键，后面的为值
            red.set_cookie('url',request.get_full_path)
            return red
    return login_fun
'''
http://127.0.0.1:8080/200/?type=10
request.path:表示当前路径，为/200/
request.get_full_path():表示完整的路经 为/200/？type=10
'''