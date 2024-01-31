from flask import Flask,render_template,request,redirect,url_for,session
from flask_mail import Mail,Message
import os,random

import pyodbc



app=Flask(__name__)
app.secret_key = '28janrandom'
app.secret_key = os.urandom(24)  

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] =587 #465 #$587
app.config['MAIL_USERNAME'] = 'bbonzana@gmail.com'
app.config['MAIL_PASSWORD'] = 'eojchcxcrdozgnkb'
app.config['MAIL_USE_TLS'] = True #False #true
app.config['MAIL_USE_SSL'] = False #True #false
mail=Mail(app)

#database connector
# server = 'server29janpraneet'
# database = 'db29jan'
# username = 'dbadmin'
# password = 'Localhost@1234567'

# #creating own connection string
# conn_str = 'Driver={SQL Server};Server=tcp:server29janpraneet.database.windows.net,1433;Database=db29jan;Uid=dbadmin;Pwd={Localhost@1234567};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

# # Create a connection string
# #conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# # Establish a connection
# conn = pyodbc.connect(conn_str)


otp_storage=[11234,33243,43554,66765,76558,87575,64646,87876,12343,54366]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['emailname']
        otp = random.choice(otp_storage)
        session['otp'] = otp

        msg = Message("Your OTP", sender='bbonzana@gmail.com', recipients=[email])
        msg.body = f"Your OTP is: {otp}"
        mail.send(msg)

        return redirect(url_for('verify_otp'))
    return render_template('index.html')


@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if 'otp' in session:
        if request.method == 'POST':
            entered_otp = int(request.form['otpname'])
            stored_otp = session['otp']
            if entered_otp == stored_otp:
                return 'OTP verified. You are logged in!'
            else:
                return 'Invalid OTP. Please try again.'
        else:
            return render_template('verify_otp.html')
    else:
        return redirect(url_for('index'))





# def home():
#     if request.method=='POST':
#         if 'send_otp' in request.form:
#             email=request.form['emailname']
#             otp=random.choice(otp_storage)
#             session['otp']=otp

#             msg=Message("Your OTP",sender='bbonzana@gmail.com',
#                         recipients=[email])
#             msg.body=f"Your OTP is: {otp}"
#             mail.send(msg)
#             # return "sent email"
#             return render_template('verify_otp.html', email=email)
#         elif 'verify_otp' in request.form:
#             entered_otp = int(request.form['otpname'])
#             if 'otp' in session:
#                 stored_otp=session['otp']
#                 if entered_otp==stored_otp:
#                     return 'otp verified'
#                 else:
#                     return "invalid otp"
#             else:
#                 return 'otp session expired'
            
#     return render_template('index.html')

# conn.close()


if __name__ == '__main__':
    app.run(debug=True)
