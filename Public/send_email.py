import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(file_path):
    smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
    smtp.login("15218475184@163.com", "xiaofeng.0418")

    smg = MIMEMultipart()
    text_smg = MIMEText("自动化测试执行完毕，执行结果请看附件！", "plain", "utf8")
    smg.attach(text_smg)

    file_msg = MIMEApplication(open(file_path, "rb").read())
    file_msg.add_header('content-disposition', 'attachment', filename='report.html')
    smg.attach(file_msg)

    smg["Subject"] = "菠萝包APPUI自动化测试报告"
    smg["From"] = "15218475184@163.com"
    smg["To"] = "1532456560@qq.com"
    smtp.send_message(smg, from_addr="15218475184@163.com", to_addrs="1532456560@qq.com")


if __name__ == '__main__':
    send_email(r"C:\pycharm\Boluobao\Report\23-03-12 14_02_37report.html")
    print("结束！")
