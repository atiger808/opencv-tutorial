# _*_ coding: utf-8 _*_
# @Time     : 2019/9/22 4:56
# @Author   : Ole211
# @Site     :
# @File     : send_163_text_email.py
# @Software : PyCharm

def send_qq_email(subject, message):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    sender = '王先森<594542251@qq.com>'
    receiver = 'ole211@qq.com'
    smtpserver = 'smtp.qq.com'
    username = '594542251@qq.com'
    password = "agokwajqivckbdhg"  # qq邮箱授权码

    msg = MIMEText(str(message), 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['To'] = receiver
    msg['From'] = sender

    smtp = smtplib.SMTP()
    try:
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        print('邮件发送成功')
    except Exception as e:
        print(e)
        print('邮件发送失败')
    smtp.quit()

if __name__ == '__main__':
    send_qq_email(subject='测试', message='Thanks！')