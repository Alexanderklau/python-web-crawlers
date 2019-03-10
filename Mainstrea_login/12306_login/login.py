# coding: utf-8

__author__ = "lau.wenbo"

# _*_coding:utf-8_*_

import requests
from PIL import Image
from json import loads
import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class LoginTic(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }
        # 创建一个网络请求session实现登录验证
        self.session = requests.session()

    # 获取验证码图片
    def getImg(self):
        url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"
        response = self.session.get(url=url, headers=self.headers, verify=False)
        # 把验证码图片保存到本地
        with open('img.jpg', 'wb') as f:
            f.write(response.content)
        # 用pillow模块打开并解析验证码,这里是假的，自动解析以后学会了再实现
        try:
            im = Image.open('img.jpg')
            # 展示验证码图片，会调用系统自带的图片浏览器打开图片，线程阻塞
            im.show()
            # 关闭，只是代码关闭，实际上图片浏览器没有关闭，但是终端已经可以进行交互了(结束阻塞)
            im.close()
        except:
            print(u'请输入验证码')
        # =======================================================================
        # 根据打开的图片识别验证码后手动输入，输入正确验证码对应的位置，例如：2,5
        # ---------------------------------------
        #         |         |         |
        #    0    |    1    |    2    |     3
        #         |         |         |
        # ---------------------------------------
        #         |         |         |
        #    4    |    5    |    6    |     7
        #         |         |         |
        # ---------------------------------------
        # =======================================================================
        captcha_solution = input('请输入验证码位置，以","分割[例如2,5]:')
        return captcha_solution

    # 验证结果
    def checkYanZheng(self, solution):
        # 分割用户输入的验证码位置
        soList = solution.split(',')
        # 由于12306官方验证码是验证正确验证码的坐标范围,我们取每个验证码中点的坐标(大约值)
        yanSol = ['35,35', '105,35', '175,35', '245,35', '35,105', '105,105', '175,105', '245,105']
        yanList = []
        for item in soList:
            print
            item
            yanList.append(yanSol[int(item)])
        # 正确验证码的坐标拼接成字符串，作为网络请求时的参数
        yanStr = ','.join(yanList)
        checkUrl = "https://kyfw.12306.cn/passport/captcha/captcha-check"
        data = {
            'login_site': 'E',  # 固定的
            'rand': 'sjrand',  # 固定的
            'answer': yanStr  # 验证码对应的坐标，两个为一组，跟选择顺序有关,有几个正确的，输入几个
        }
        # 发送验证
        cont = self.session.post(url=checkUrl, data=data, headers=self.headers, verify=False)
        # 返回json格式的字符串，用json模块解析
        dic = loads(cont.content)
        code = dic['result_code']
        # 取出验证结果，4：成功  5：验证失败  7：过期
        if str(code) == '4':
            return True
        else:
            return False

    # 发送登录请求的方法
    def loginTo(self):
        # 用户输入用户名，这里可以直接给定字符串
        userName = input('Please input your userName:')
        # 用户输入密码，这里也可以直接给定
        # pwd = raw_input('Please input your password:')
        # 输入的内容不显示，但是会接收，一般用于密码隐藏
        pwd = getpass.getpass('Please input your password:')
        loginUrl = "https://kyfw.12306.cn/passport/web/login"
        data = {
            'username': userName,
            'password': pwd,
            'appid': 'otn'
        }
        result = self.session.post(url=loginUrl, data=data, headers=self.headers, verify=False)
        dic = loads(result.content)
        print (result.content)
        mes = dic['result_message']
        # 结果的编码方式是Unicode编码，所以对比的时候字符串前面加u,或者mes.encode('utf-8') == '登录成功'进行判断，否则报错
        if mes == u'登录成功':
            print('恭喜你，登录成功，可以购票!')
        else:
            print('对不起，登录失败，请检查登录信息!')


if __name__ == '__main__':
    # checkYanZheng('0,3')
    login = LoginTic()
    yan = login.getImg()
    chek = False
    # 只有验证成功后才能执行登录操作
    while not chek:
        chek = login.checkYanZheng(yan)
        if chek:
            print('验证通过!')
        else:
            print('验证失败，请重新验证!')
    login.loginTo()