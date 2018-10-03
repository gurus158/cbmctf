from services import user_service,tasks_service,comments_service
import os as os
from gevent.pywsgi import WSGIServer
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer,SignatureExpired
from flask import render_template,jsonify, request, url_for, Flask,session,abort,flash,redirect,json

app=Flask(__name__)
app.config.from_pyfile('static/config.cfg')
mail=Mail(app)
s= URLSafeTimedSerializer("cbm_ctf_by_cbm")


@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect("/login")
    else:
        return  render_template('home.html')

@app.route('/getusername')
def getusername():
    if session.get('logged_in'):
        return jsonify(session['username'])
    else:
        return jsonify("please login first")

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST' :
        login_details = request.form
        if user_service.login_check(login_details):
            login_msg = 'username or password is incorrect'
        else:
            login_msg = ''

        if login_msg != '':
            #flash("wrong username or password")
            return render_template('login.html', username=login_details['username'], password=login_details['password'],login_msg=login_msg)
        else:
            session['logged_in'] = True
            session['username']=login_details['username']

        return redirect("/")

    return  render_template('login.html')


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        signup_detail = request.form
        if user_service.check_username(signup_detail['username']) == False :
            username_msg = 'username already exist!!'
        else:
            username_msg = ''

        if user_service.check_email(signup_detail['email']) == False:
            email_msg='email already exist!!'
        else:
            email_msg=''


        if username_msg == '' and email_msg == '':
            email=signup_detail['email']
            token=s.dumps(email,salt='email_confirmed')
            msg=Message('Email Confirmation CBM CTF',sender='divya.dulyan8@gmail.com',
                        recipients=[email])
            #link= url_for('confirm_email', token=token,_external=True)
            link= "localhost:5001/confirm_email/"+token
            msg.body='email Confirmation link is {}'.format(link)
            mail.send(msg)

            user_service.signup_user(user_service.create_user(signup_detail))
            return "<h1>confirmation mail is send please confirm email for access acount.</h1>"

        else:
            return render_template('signup.html', username_msg=username_msg, email_msg=email_msg,
                                   firstname=signup_detail['firstname']
                                   , email=signup_detail['email'], username=signup_detail['username'])

    return render_template('signup.html')

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email=s.loads(token,salt='email_confirmed',max_age=3600)
    except SignatureExpired:
        return "<h1>Token is expired!!</h1>"
    print email
    user_service.confirm_email(email)
    return '<h1>The token works!</h1>'

@app.route('/submitflag/<username>',methods=['POST'])
def submitflag(username):
    req_data=json.loads(request.data)

    user_flag=req_data['user_flag']
    task_name=req_data['task_name']
    res="wrong flag!! Try Again."
    if user_service.check_task_name(task_name):
        return jsonify("task_not_exist")
    else:
        if user_service.already_solved(username,task_name):
            res="you already solved it!! now solve other problems."

        elif user_service.submit_flag(username,user_flag,task_name):
            res="congrats!! correct flag."

    return jsonify(res)

@app.route('/leaderboard')
def leaderboard():
    leaderboard=user_service.get_leaderboard()
    return jsonify(leaderboard)

@app.route('/logout')
def logout():
    session.pop('user',None)
    session['logged_in']=False
    flash("successfully Logged out")
    return redirect('/login')

@app.route('/gettaskdetail/<taskname>')
def gettaskdetail(taskname):
    taskdetails=tasks_service.get_task_details(taskname)
    return jsonify(taskdetails)

@app.route('/addcomment',methods=['POST'])
def addcomment():
    comment_detail=request.form
    print comment_detail['username']
    comments_service.add_comment(comment_detail)
    return redirect('/')


@app.route('/comments/<taskname>')
def getComments(taskname):
    comment_list=comments_service.get_comments(taskname)
    return jsonify(comment_list)


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response



if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    http_server = WSGIServer(('0.0.0.0', 5002), app)
    http_server.serve_forever()
