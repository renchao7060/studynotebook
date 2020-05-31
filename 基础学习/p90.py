'''
12306自动登录系统
1、检查验证码
2、检查密码
3、登录
https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand #get 校验图片地址
https://kyfw.12306.cn/passport/captcha/captcha-check #post校验码
answer	33,46
login_site	E
rand	sjrand
https://kyfw.12306.cn/passport/web/login #post登录地址
username	renchao7060
password	xxxxxxxx
appid	otn
'''
import requests

r=requests.session()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/62.0.3202.94 Safari/537.36'}
def sigin():
    #获取验证码图片
    response=r.get('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand',headers=headers)
    with open('code.png','wb') as f:
        f.write(response.content)
    codestring=input('请输入验证码坐标值')
    #验证码校验
    data = {'answer': codestring, 'login_site': 'E', 'rand': 'sjrand' }
    response=r.post('https://kyfw.12306.cn/passport/captcha/captcha-check',data=data,headers=headers)
    result=response.json()
    if result['result_code']=="4":
        print('验证码校验成功')
    else:
        print('验证码校验失败')
        sigin()
        return
    #登录
    data={'username':'renchao7060','password':'987321Aa','appid':'otn'}
    response=r.post('https://kyfw.12306.cn/passport/web/login',data=data,headers=headers)
    print(response.text)

if __name__=='__main__':
    sigin()