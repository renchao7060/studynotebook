#闭包调用属性参数（数值）

#_*_coding:UTF-8_*_

def fun_100(val):
  passline=60
  if val>passline:
    print('pass')
  else:
    print('fail')
	
def fun_150(val):
  passline=90
  if val>passline:
    print('pass')
  else:
    print('fail')
	
fun_100(88)
fun_150(88)
	

	
	
def setpassline(passline):
  def cmp(val):
    if val>passline:
      print('pass')
    else:
      print('fail')
  return cmp
  
fun_100=setpassline(60)
fun_150=setpassline(90)
fun_100(88)
fun_150(88)