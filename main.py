from flask import Flask, render_template, request
import requests
import smtplib
BLOG_ENDPOINT='https://api.npoint.io/9dd7cb66e29c10f32d83'
app = Flask(__name__)
response = requests.get(BLOG_ENDPOINT)
blogs = response.json()
@app.route('/')
def home():
    return render_template("index.html",blogs=blogs)

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        message=request.form['msg']
        mail_stat=send_mail(name,email,phone,message)
        print(mail_stat)
        return render_template('contact.html',mail_st=mail_stat)
    else:
        return render_template('contact.html',mail_st=False)
def send_mail(name,email,phone,message):
    email_message=f"Subject:New user got enrolled to your blog\n\n Name: {name}\n Email: {email}\n phone:{phone}\nmessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        try:
            connection.login('your email','youremail password')
            send=connection.sendmail('your email','your email',email_message)
            return True
        except:
            return False

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:index>')
def show_post(index):
    requested_post=None
    for blog in blogs:
        print(blog)
        if blog['id']==index:
            requested_post=blog
    return render_template('post.html',post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
