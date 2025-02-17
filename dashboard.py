from flask import Flask, render_template, request, redirect, session
import os  # Import os for secret key generation

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key

users = {"admin": "password123", "user": "test123"}

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect("/dashboard")

        error = "Invalid username or password"

    return render_template("login.html", error=error)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    grafana_url = "http://localhost:3000/goto/m6QjcG5HR?orgId=1"  # Or your actual Grafana URL
    print("Grafana URL:", grafana_url)  # Print for debugging
    return render_template("dashboard.html", grafana_url=grafana_url)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)