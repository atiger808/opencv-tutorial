# _*_ coding: utf-8 _*_
# @Time     : 2019/9/22 4:56
# @Author   : Ole211
# @Site     : 
# @File     : send_163_text_email.py
# @Software : PyCharm

def send_163_email(subject, message):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    sender = '监控预警<atiger0614@163.com>'
    receiver = 'atiger0614@163.com'
    smtpserver = 'smtp.163.com'
    username = 'atiger0614@163.com'
    password = 'poo001'

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
    smtp.quit()

if __name__ == '__main__':
    send_163_email(subject='Warning', message='出事了！')