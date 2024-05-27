import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import configparser
import os
import asyncio


mail_template = """
<h2 style="color:red">{content}</h2>
<p>{content}</p>
"""


class EMail:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.getcwd(), "config.ini"), encoding="utf8")
        mail_config = config["mail"]

        self.from_addr = mail_config["from_addr"]
        self.subject = mail_config["subject"]
        self.password = mail_config["password"]
        self.to_addr = mail_config["to_addr"]
        self.content = mail_template

        self.host = mail_config["host"]
        self.port = int(mail_config["port"])

    def send_email(
        self,
        content,
        subject,
        to_addr,
    ):
        self.content = self.content.replace("{content}", content)
        self.to_addr = to_addr
        self.subject = subject
        
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
        smtp = smtplib.SMTP_SSL(self.host, self.port)

        # 登录邮箱(如果是qq邮箱需要账号和授权码，其他的邮箱账号密码登入即可)
        smtp.login(self.from_addr, self.password)
        smtp.sendmail(self.from_addr, self.to_addr, msg.as_string())
        smtp.quit()

    def send_email_sync(self, content):
        asyncio.create_task(self.send_email(content))


if __name__ == "__main__":
    # 发件人是qq邮箱
    EMail().send_email()
    print("邮件已经发送完成！！")
