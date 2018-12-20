from email.mime.text import MIMEText
import smtplib

def send_email(email, height,weight,average_weight, average_height, count,bmiIndex,bmiCat):
    from_email="force.abhijeet@gmail.com"
    from_password="Hazard@10"
    to_email=email

    subject="Height data"
    message="Hey there!<Br> Your height is <strong>%s</strong>.<Br> Your weight is <strong>%s</strong>.<Br> Your Body Mass Index is <strong>%s</strong>.<Br> Your Body Mass index category is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong>.<br> Average Weight of all is <strong>%s</strong>.<br>Total participants of the survey are <strong>%s</strong> people. <br> Thanks!" % (height,weight,bmiIndex,bmiCat, average_height,average_weight, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
