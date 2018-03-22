import smtplib
import logging

gmail_user = "johnfoconnoriii@gmail.com"
gmail_pwd  =  "FILLMEIN"

def send_email(user, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)  
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
        server_ssl.sendmail(FROM, TO, message)
        #server_ssl.quit()
        server_ssl.close()
        logging.debug('successfully sent the mail')
    except:
        logging.debug("failed to send mail")


FROM = "johnfoconnoriii@gmail.com"
TO   = "johnnyoc3@gmail.com"

from datetime import datetime
import time

def get_formatted_time(aDatetime):
    return aDatetime.strftime("%a, %d %b %Y %H:%M:%S +0000")


def trigger(aDateTime):
    send_email("catfeeder", ['johnnyoc3@gmail.com', 'paige.sweetin@gmail.com'], "Fed the cat on {}".format(get_formatted_time(aDateTime)), "")

