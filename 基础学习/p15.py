#_*_coding:UTF-8_*_

#统一登陆门户，为各网页统一添加认证方式
username=input('username:')
password=input('password:')
user='renchao'
passw='123'

def deco(auth):
  def func(fun):
    def wrapper(*args,**kwargs):
      if auth=='local':
        if username==user and password==passw:
          print('local auth ok!')
          f=fun(*args,**kwargs)###方式1
          print('after auth')
          return f#不返回函数的话index()/home()函数中return返回为None,而非‘from index’/'from bbs'
        else:
          print('local auth fail')
      elif auth=='ldap':
        if username==user and password==passw:
          print('ldap auth ok!')
          return fun(*args,**kwargs)#方式2 不返回函数的话bbs()函数中return返回为None,而非‘from bbs’
        else:
          print('ldap auth fail')
      else:
        print('auth-type invaid')
      #return fun(*args,**kwargs)
    return wrapper
  return func


@deco(auth='local')#等价于index=deco(auth='local')(index)
def index():
  print('in index')
  return 'from index'
  
@deco(auth='local')
def home():
  print('in home')
  return 'from home'
  
@deco(auth='ldap')
def bbs():
  print('in bbs')
  return 'from bbs'
  
index()
print()
print(home())
print()
print(bbs())

