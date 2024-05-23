import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


mail_template = """
<h2 style="color:red">我的Python教程，官方微信公众号：wdPython</h2>
<p>这是一个简单的HTML</p>
<h2 style="color:red">我的Python教程，官方微信公众号：wdPython</h2>
<p>这是一个简单的HTML</p>
<p>刘亦菲的图片</p>
<center>点击下方我的Python教程历史博文集合</center>
<a href='https://mp.weixin.qq.com/s/LwaDH9PFLowLl8sIzaE6_w'>Python博文精选</a>
"""


class EMail:
    def __init__(self):
        self.from_addr = "huaqiwill@qq.com"
        self.subject = "测试邮件"
        self.password = "nhrdvawdinovdeba"
        self.to_addr = "3173484026@qq.com"
        self.content = mail_template

    def send_email(self):
        # 创建邮件对象
        msg = MIMEMultipart()

        # 设置邮件标题
        msg["Subject"] = Header(self.subject, "utf-8").encode()

        # 设置邮件发送者
        msg["From"] = f"{self.from_addr} <{self.from_addr}>"

        # 设置邮件接受者
        msg["To"] = self.to_addr

        # 2.添加发送内容
        # 添加HTML

        msg.attach(MIMEText(self.content, "html", "utf-8"))

        # 3.发送邮件
        smtp = smtplib.SMTP_SSL(f"smtp.qq.com", 465)

        # 登录邮箱(如果是qq邮箱需要账号和授权码，其他的邮箱账号密码登入即可)
        smtp.login(self.from_addr, self.password)
        smtp.sendmail(self.from_addr, self.to_addr, msg.as_string())
        smtp.quit()


if __name__ == "__main__":
    # 发件人是qq邮箱
    EMail().send_email()
    print("邮件已经发送完成！！")
