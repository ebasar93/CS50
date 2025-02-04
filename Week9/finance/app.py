import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    #get current user_id
    try:
        id = session["user_id"][0]['id']
    except:
        id = session["user_id"]
    cash = db.execute("SELECT cash FROM users WHERE id = ?", id)
    cash = round(cash[0]["cash"],3)
    accounts = db.execute("SELECT * FROM accounts WHERE account_id = ? AND number_of_shares >= 1 ", id)
    for row in accounts:
        db.execute("UPDATE accounts SET price = ? WHERE name = ? ", lookup(row['name'])['price'], row['name'])
    total_stock = 0
    for account in accounts:
        total_stock += account['number_of_shares'] * account['price']

    total = cash + total_stock



    #show index page
    return render_template("index.html", accounts=accounts, cash = cash, total = total )



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)
        else:
            symbol = request.form.get("symbol").capitalize()

        # Ensure shares was submitted
        if not request.form.get("shares"):
            return apology("missing shares", 400)
        else:
            shares = request.form.get("shares")

        # Ensure symbol is correct
        quotes = lookup(symbol)

        # Total value of shares bought
        try:
            total = round(quotes["price"],3) * float(shares)
        except:
            return apology("invalid symbol", 400)
        # Ensure total less than cash of user
        try:
            id = session["user_id"][0]['id']
        except:
            id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?",id)
        cash = cash[0]["cash"]
        if cash < total:
            return apology('insufficient funds', 400)
        else:
            accounts = db.execute("SELECT * FROM accounts WHERE account_id = ? AND number_of_shares >= 1 ", id)
            # buying same share
            for account in accounts:
                if symbol == account['name']:
                    db.execute("UPDATE accounts SET number_of_shares = number_of_shares + ? WHERE name = ? AND account_id = ? ", shares, symbol,id )

                    db.execute("UPDATE users SET cash = cash - ?  WHERE id = ? ", total, id )
                    db.execute("INSERT INTO trans (account_id,number_of_shares,name,price,transacted) Values  (?,?,?,?,?)" , id,shares ,symbol ,total, str(datetime.datetime.utcnow()))
                    return redirect("/")

                    #return render_template("index.html", accounts=accounts, cash=cash)

            db.execute("INSERT INTO accounts (account_id,number_of_shares,name,price) Values  (?,?,?,?)" , id,shares,symbol,round(quotes["price"],3))
            #accounts = db.execute("SELECT * FROM accounts WHERE account_id = ? AND number_of_shares >= 1 ", id)
            total_stock = 0
            for account in accounts:
                total_stock += account['number_of_shares'] * account['price']
            cash = cash - total
            all_total = cash + total_stock
            db.execute("UPDATE users SET cash = ? WHERE id = ? ", cash, id )
            db.execute("INSERT INTO trans (account_id,number_of_shares,name,price,transacted) Values  (?,?,?,?,?)" , id,shares ,symbol ,total, str(datetime.datetime.utcnow()))
            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    try:
        id = session["user_id"][0]['id']
    except:
        id = session["user_id"]
    trans = db.execute("SELECT * FROM trans WHERE account_id = ? ", id)
    return render_template("history.html", trans = trans)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)
        else:
            symbol = request.form.get("symbol")



        quotes = lookup(symbol)

        # Retrieve quote info

        if quotes is None:
            return apology("invalid symbol", 400)

        #render quote if symbol is valid
        else:

            return render_template("quoted.html", quotes=quotes)
    else :
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    #if user sends a GET request show form
    if request.method == "GET":
        return render_template("register.html")

    # if user sends a POST request
    else :

        # Validate submission
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")


        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure passwords match
        elif not password == confirmation:
            return apology("passwords do not match", 400)

         # if not user error generate password hash, insert user and set session id
        else:
            hash = generate_password_hash(password)
            try:
                #try an insert user except the user is already in the db
                db.execute("INSERT INTO users (username, hash ) VALUES (?,?)",username , hash)
                session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", username)

                a = db.execute("SELECT id FROM users WHERE username = ?", username )
                b = a[0]['id']

                db.execute("INSERT INTO accounts (account_id,number_of_shares,name,price) Values  (?,?,?,?)" , b,0,'placeholder',0)

                # redirect to the quotes page
                return redirect("/quote")
            except ValueError:
                return apology("username already exists", 400)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    #if user sends a GET request show form
    id = session["user_id"][0]['id']
    accounts = db.execute("SELECT * FROM accounts WHERE account_id = ? AND number_of_shares >= 1 ", id)

    if request.method == "GET":


        return render_template("sell.html", accounts = accounts)

    # if user sends a POST request
    else :

        symbol = request.form.get("symbol")

        shares = int(request.form.get("shares"))
        am = db.execute("SELECT * FROM accounts WHERE account_id = ? AND number_of_shares >= 1 AND name = ? ", id,symbol)
        if am[0]['number_of_shares'] < shares:
            return apology("too many shares", 400)
        else:
            quotes = lookup(symbol)
            total = round(quotes["price"],3) * float(shares)
            db.execute("UPDATE accounts SET number_of_shares = number_of_shares - ? WHERE name = ? AND account_id = ? ", shares, symbol,id )
            db.execute("UPDATE users SET cash = cash + ?  WHERE id = ? ", total, id )
            db.execute("INSERT INTO trans (account_id,number_of_shares,name,price,transacted) Values  (?,?,?,?,?)" , id,shares ,symbol ,total, str(datetime.datetime.utcnow()))
            return redirect("/")


