import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os
import os.path

# smtpserver='smtp.163.com'

user='zhqg23@163.com'
password='zhuqiuge23'

sender='zhqg23@163.com'
reciver='qiuge.zhu@autodesk.com'
subject='python email test'

#发送的附件
result_dir='F:\\Gigi\\pageobject\\TestReport'
lists=os.listdir(result_dir)
lists.sort()
file=os.path.join(result_dir,lists[-1])
file_name=os.path.basename(file)
print(file_name)
sendfile=open(file,'rb').read()

att=MIMEText(sendfile,'html','utf-8')
att["Content-Type"]='application/octet-stream'
att["Content-Disposition"]='attachment;filename="%s"'%file_name

msg=MIMEMultipart('related')
#msg=MIMEText('<html><h1>你好,这是一个测试python发送邮件带有附件</h1></html>','html','utf-8')
msg['Subject']=subject
msg['From']=sender
msg['To']=reciver
msg.attach(att)


smtp=smtplib.SMTP_SSL('smtp.163.com', 465)
smtp.login(user, password)
smtp.sendmail(sender,reciver,msg.as_string())
smtp.close()

