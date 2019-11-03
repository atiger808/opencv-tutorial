# -*- coding: utf-8 -*-
'''
    @Time: 2018/5/14 0:30
    @Author: Ole211
'''
import traceback
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import formataddr

username = "594542251@qq.com"  # qq账户
authorization_code = "agokwajqivckbdhg"  # qq邮箱授权码
from_email = "594542251@qq.com"


def send_qq_plain_email(from_email, to_emails, title, content):
    """01发送文本邮件"""
    send_fail = []  # 发送出错邮箱列表
    for to_email in to_emails:
        # 构建邮箱
        message = MIMEText(content, "plain", "utf-8")
        message["Subject"] = "{}--邮箱测试".format(title)
        message["From"] = from_email
        message["To"] = to_email
        try:
            # 发送邮件
            s = smtplib.SMTP_SSL('smtp.qq.com', 465)
            s.login(username, authorization_code)
            s.sendmail(from_email, to_email, message.as_string())
            print(message.as_string())
            s.quit()
            print('发送成功')
        except smtplib.SMTPException as e:
            send_fail.append(to_email)
            print('发送个失败，%s' % e)
    return send_fail


def send_qq_html_email(from_email, to_emails, title, content):
    """02faso发送html邮件"""
    send_fail = []
    for to_email in to_emails:
        # 构建邮箱
        message = MIMEText(content, "html", 'utf-8')
        message['Subject'] = "{}--邮箱测试".format(title)
        message['From'] = from_email
        message['To'] = to_email
        try:
            # 创建发送邮箱对象
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(username, authorization_code)
            s.sendmail(from_email, to_email, message.as_string())
            print(message.as_string())
            s.quit()
            print('发送成功')
        except smtplib.SMTPException as e:
            send_fail.append(to_email)
            print("发送失败， %s" % e)
    return send_fail


def send_qq_attach_email(from_email, to_emails, title, content, attachs):
    """03发送带有附件的邮箱"""
    send_fail = []
    for to_email in to_emails:
        # 创建一个带有附件的邮箱
        message = MIMEMultipart()
        message.attach(MIMEText(content, "html", "utf-8"))
        message['Subject'] = "{}--邮箱测试".format(title)
        message['From'] = from_email
        message['To'] = to_email
        # 构造附件
        for f in attachs:
            attach = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
            attach["Content-Type"] = 'application/octet-stream'
            # filename 是邮件中显示的名字
            attach["Content-Disposition"] = 'attachment; filename={}'.format(f)
            message.attach(attach)
        try:
            # 创建发送邮箱对象
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(username, authorization_code)
            s.sendmail(from_email, to_email, message.as_string())
            print(message.as_string())
            s.quit()
            print("发送成功")
        except smtplib.SMTPException as e:
            send_fail.append(to_email)
            print('发送失败，%s' % e)
    return send_fail


def send_qq_img_email(from_email, to_emails, title, content, attachs, imgname):
    """04发送带有图片的html邮箱"""
    send_fail = []
    for to_email in to_emails:
        # 创建 一个带有图片的实例
        message = MIMEMultipart("reload")
        message['Subject'] = "{}--邮箱测试".format(title)
        message['From'] = from_email
        message['To'] = to_email
        message_alternative = MIMEMultipart('alternative')
        message.attach(message_alternative)
        message_alternative.attach(MIMEText(content, "html", "utf-8"))
        # 打开图片
        image = open(imgname, 'rb')
        msgImage = MIMEImage(image.read())
        image.close()
        # 定义图片id, 在html文本中引用
        msgImage.add_header('Content-ID', '<image_test>')
        message.attach(msgImage)
        # 构造附件
        for f in attachs:
            attach = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
            attach["Content-Type"] = 'application/octet-stream'
            # filename 是邮件中显示的名字
            attach["Content-Disposition"] = 'attachment; filename={}'.format(f)
            message.attach(attach)
            print('{}------sending'.format(f))
        try:
            # 创建发送邮件对象
            print('-------sendmail-------')
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(username, authorization_code)
            s.sendmail(from_email, to_email, message.as_string())
            s.quit()
            print('发送成功')
        except smtplib.SMTPException as e:
            send_fail.append(to_email)
            print("发送失败，%s" % e)
    return send_fail


if __name__ == '__main__':
    #  #发送邮箱的内容
    #  content = """
    #          <p>html邮件格式练习</p>
    #          <p><a href="http://www.baidu.com">百度链接</a></p>
    #  """
    #  #收件人的邮箱地址
    to_email = ['1197773452@qq.com']
    #
    #邮件附件文件名， 打开的是本目录文件
    attachs = []
    file_path = 'd://send-email//'
    attachs = [file_path + i for i in attachs]
    files = [os.path.join(file_path, i) for i in os.listdir(file_path)]
    for i in files:
        if os.path.isfile(os.path.join(file_path, i)):
            attachs.append(i)

    # 发送带图片的文件内容
    img_content = """
            <p>html邮件格式练习</p>
            <p><a href="http://www.baidu.com">百度链接</a></p>
            <p><img style="width: 100px; height: 100px;" src="cid:image_test"></p>
            
    """
    # 图片名称
    imgname = 'd://img//close.jpg'
    imgnames = []
    # 测试发送文本邮件
    # send_fail = send_qq_plain_email("594542251@qq.com", to_email, "文本文件", content)
    # 发送带有html的邮件
    # send_fail = send_qq_html_email("594542251@qq.com", to_email, "html文件", content)
    # 发送带有附件的邮件
    # send_fail = send_qq_attach_email("594542251@qq.com", to_email, "带附件的文件", content, attachs)
    # 发送带有图片和附件的邮件
    send_fail = send_qq_img_email("594542251@qq.com", to_email, "带图片和附件", img_content, attachs, imgname)
# print(send_fail)

# 发送邮件的请求信息
"""
发送html邮箱内容：
Content-Type: text/html; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Subject: 第一课--作业回复
From: 3002832062@qq.com
To: 3002832062@qq.com

CiAgICAgICAgPHA+aHRtbOmCruS7tuagvOW8j+e7g+S5oDwvcD4KICAgICAgICA8cD48YSBocmVm
PSJodHRwOi8vd3d3LmJhaWR1LmNvbSI+55m+5bqm6ZO+5o6lPC9hPjwvcD4KICAgIA==

发送成功

"""

"""
发送html，带附件的邮箱内容：
Content-Type: text/base64; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="send_email.py"

I2NvZGluZz11dGYtOA0KDQppbXBvcnQgc210cGxpYg0KZnJvbSBlbWFpbC5taW1lLnRleHQgaW1w
......
DQpQU0pvZEhSd09pOHZkM2QzTG1KaGFXUjFMbU52YlNJKzU1bSs1YnFtNlpPKzVvNmxQQzloUGp3
dmNENEtJQ0FnSUE9PQ0KDQrlj5HpgIHmiJDlip8NCg0KIiIiDQoNCg0KDQoNCg0KDQo=

--===============8800341415687636184==--

发送成功

"""

"""
发送有图片的html，并带附件的邮箱内容：
Content-Type: multipart/related;
 boundary="===============2776155673590694152=="
MIME-Version: 1.0
Subject: 第一课--作业回复
From: 3002832062@qq.com
To: 3002832062@qq.com

--===============2776155673590694152==
Content-Type: multipart/alternative;
 boundary="===============8121511135129254006=="
MIME-Version: 1.0

--===============8121511135129254006==
Content-Type: text/html; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64

CiAgICAgICAgPHA+aHRtbOmCruS7tuagvOW8j+e7g+S5oDwvcD4KICAgICAgICA8cD48YSBocmVm
PSJodHRwOi8vd3d3LmJhaWR1LmNvbSI+55m+5bqm6ZO+5o6lPC9hPjwvcD4KICAgICAgICA8cD48
aW1nIHN0eWxlPSJ3aWR0aDogMTAwcHg7aGVpZ2h0OiAxMDBweCIgc3JjPSJjaWQ6aW1hZ2VfdGVz
dCI+PC9wPgogICAg

--===============8121511135129254006==--

--===============2776155673590694152==
Content-Type: image/png
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-ID: <image_test>

iVBORw0KGgoAAAANSUhEUgAAAJ8AAACfCAYAAADnGwvgAAAACXBIWXMAAAsTAAALEwEAmpwYAABF
y2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0w
......
rTpn7e5OjIT29b755q8xTSNFTu7XEqOkVa3IFsjHc/SfOrXrK1sw5Dyz4fmhc+cejbR22vpvy/I3
bf7JvUwBxv3/PSmQLxq2XrWakmdmegBj1P/Wm69Hajt7jhz+E6YotHjjpixYILivwiFAgLDyCRDI
J0CAQD4BAvkECBDIJ4C3+L8BABEmsKs/76ERAAAAAElFTkSuQmCC
--===============2776155673590694152==
Content-Type: text/base64; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-Type: application/octet-stream
Content-Disposition: attachment; filename=send_email.py

I2NvZGluZz11dGYtOA0KDQppbXBvcnQgc210cGxpYg0KZnJvbSBlbWFpbC5taW1lLnRleHQgaW1w
b3J0IE1JTUVUZXh0DQpmcm9tIGVtYWlsLm1pbWUubXVsdGlwYXJ0IGltcG9ydCBNSU1FTXVsdGlw
......
aXA4TkNnMEtJaUlpRFFvTkNnMEtEUW9OQ2cwS0RRbz0NCg0KLS09PT09PT09PT09PT09PT04ODAw
MzQxNDE1Njg3NjM2MTg0PT0tLQ0KDQrlj5HpgIHmiJDlip8NCg0KIiIiDQoNCg0KDQoNCg0KDQo=

--===============2776155673590694152==--
"""
