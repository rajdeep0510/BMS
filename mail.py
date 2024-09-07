from email.message import EmailMessage
import ssl
import smtplib

#email_reciver = 'rajdeepvala10@gmail.com'
#email_password = 'ncyv vcee qzgd yyek'



def security_mail(email_reciver):

    email_sender = 'fakebankmail@gmail.com'
    email_password = 'ncyv vcee qzgd yyek'

    subject = '!!!  fack account in danger  !!!'
    body = '''
    Your fake account is in danger someone is trying to stral money from your fack account. 
    May god help you because wee can't.
    '''

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciver, em.as_string())

