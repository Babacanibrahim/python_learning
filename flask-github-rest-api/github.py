from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route("/", methods =["GET","POST"])
def index():
    base_url = "https://api.github.com/users/"
    if request.method == "POST":
      githubname = request.form.get("githubname")
      response = requests.get(base_url + (githubname))
      response_repos = requests.get(base_url + githubname+ "/repos")

      data  = response.json()
      repos = response_repos.json()

      if "message" in data:
          return render_template("index.html", error = "Kullanıcı bulunamadı...")
      else:
        return render_template("index.html", profile = data, repos = repos)

    else:
        return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True)