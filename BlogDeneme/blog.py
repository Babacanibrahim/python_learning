from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

#Kullanıcı kayıt formu
class RegisterForm(Form):
    name = StringField("İsim : ",validators=[validators.Length(min=4,max=20)])
    username = StringField("* Kullanıcı Adı : ",validators=[validators.Length(min=5,max=25),validators.DataRequired()])
    email = StringField("E-posta : ",validators=[validators.Length(min=10,max=30),validators.Email(message="Geçersiz e posta girdiniz.")])
    password = PasswordField("* Parolanız : ",validators=[validators.Length(min=8,max=20),validators.DataRequired(),validators.EqualTo("confirm",message="Parolalar uyuşmuyor")])
    confirm = PasswordField("* Parolanız tekrar :")

#Kullanıcı giriş formu
class LoginForm(Form):
    username = StringField("Kullanıcı Adı : ",validators=[validators.DataRequired()])
    password = PasswordField("* Parolanız : ",validators=[validators.DataRequired()])

#Makale ekleme formu
class AddArticleForm(Form):
    title=StringField("Makale başlığı",validators=[validators.DataRequired(),validators.Length(max=50)])
    content=TextAreaField("Makaleniz",validators=[validators.DataRequired(),validators.Length(max=750)])

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için yetkiniz yok. Lütfen giriş yapın.","danger")
            return redirect(url_for("login"))
    return decorated_function

app =Flask(__name__)
app.secret_key="ibblog"

app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"]= "root1234."
app.config["MYSQL_DB"]= "ibblog"
app.config["MYSQL_CURSORCLASS"]= "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/articles")
def articles():
    cursor=mysql.connection.cursor()

    query="SELECT * FROM articles"

    result=cursor.execute(query)
    

    if result >0:
        articles=cursor.fetchall()
        cursor.close()
        return render_template("articles.html",articles=articles)
    else:
        cursor.close()
        return render_template("articles.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register",methods=["GET","POST"])
def register():
    form=RegisterForm(request.form)

    if request.method=="POST" and form.validate():
        name=form.name.data
        username=form.username.data
        email=form.email.data
        password=sha256_crypt.hash(form.password.data)

        cursor=mysql.connection.cursor()

        query="INSERT INTO users (name,email,username,password) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        flash("Başarıyla kayıt oluşturuldu.","success")
        return redirect(url_for("login"))
    else:
        return render_template("register.html",form=form)
    
@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm(request.form)

    if request.method=="POST" and form.validate():
        username=form.username.data
        password_entered=form.password.data

        cursor=mysql.connection.cursor()

        query="SELECT * FROM users WHERE username=%s"
        result=cursor.execute(query,(username,))
        if result > 0:
            data=cursor.fetchone()
            real_password=data["password"]
            cursor.close()
            if sha256_crypt.verify(password_entered,real_password):
                session["logged_in"]=True
                session["username"]=username
                
                flash("Giriş başarılı.","success")
                return redirect(url_for("index"))
            else:
                flash("Parolanızı yanlış girdiniz.","danger")
                return redirect(url_for("login"))
        else:
            cursor.close()
            flash("Böyle bir kullanıcı adı bulunamadı.","danger")
            return redirect(url_for("login"))
    return render_template("login.html",form=form)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
@login_required
def dashboard():
    cursor=mysql.connection.cursor()

    query="SELECT * FROM articles WHERE author =%s"
    result=cursor.execute(query,(session["username"],))

    if result>0:
        author_articles=cursor.fetchall()
        return render_template("dashboard.html",author_articles=author_articles)
    else:
        cursor.close()
        return render_template("dashboard.html")

@app.route("/addarticle",methods=["GET","POST"])
def add_article():
    form=AddArticleForm(request.form)
    if request.method=="POST" and form.validate():
        cursor=mysql.connection.cursor()
        title=form.title.data
        content=form.content.data

        query="INSERT INTO articles (title,author,content) VALUES (%s,%s,%s)"
        cursor.execute(query,(title,session["username"],content))
        mysql.connection.commit()

        cursor.close()
        flash("Makaleniz başarıyla eklendi.","success")
        return redirect(url_for("dashboard"))
    return render_template("addarticle.html",form=form)


@app.route("/editarticle/<string:id>",methods=["GET","POST"])
@login_required
def edit_article(id):
    form=AddArticleForm(request.form)
    if request.method=="POST" and form.validate():
        cursor=mysql.connection.cursor()

        query="SELECT * FROM articles where author =%s and id = %s"

        result=cursor.execute(query,(session["username"],id))

        if result>0:
            edit_article=cursor.fetchone()
            
            content=form.content.data


@app.route("/delete/<string:id>",methods=["GET","POST"])
@login_required
def delete(id):
    cursor=mysql.connection.cursor()

    query="SELECT * FROM articles where author =%s and id = %s"
    result=cursor.execute(query,(session["username"],id))

    if result>0:
        query_delete="DELETE FROM articles where id=%s"
        cursor.execute(query_delete,(id,))
        mysql.connection.commit()
        flash("Makalen başarıyla silindi","success")
        return redirect(url_for("dashboard"))
    else:
        flash("Böyle bir makale yok veya bu makaleyi silme yetkiniz yok.","danger")
        return redirect(url_for("index"))



@app.route("/article/<string:id>")
def detail(id):
    cursor=mysql.connection.cursor()
    query="SELECT * FROM articles WHERE ID =%s"

    result=cursor.execute(query,(id,))

    if result>0:
       article= cursor.fetchone()
       return render_template("article.html",article=article)
    
    else:
        flash("Böyle bir makale bulunamadı.", "danger")
        return render_template("article.html")
    
@app.route("/myarticles/<string:id>")
def myarticles(id):
    cursor=mysql.connection.cursor()
    query="SELECT * FROM articles WHERE ID =%s"

    result=cursor.execute(query,(id,))

    if result>0:
       article= cursor.fetchone()
       return render_template("myarticles.html",article=article)
    
    else:
        flash("Böyle bir makale bulunamadı.", "danger")
        return render_template("myarticles.html")

if __name__=="__main__":
    app.run(debug=True)