import sqlite3 as sql
import time
import random
import bcrypt


def insertUser(username, password, salt):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO users (username,password, salt) VALUES (?,?,?)",
        (username, password, salt),
    )
    con.commit()
    con.close()


def retrieveUsers(username, password):

    # connect to the database
    con = sql.connect("database_files/database.db")
    cur = con.cursor()

    # search the database for the hashed password
    cur.execute(
        "SELECT password FROM users WHERE username == ?",
        (username,),
    )
    # get and store result
    result = cur.fetchone()

    # check that there is that user
    if result == None:
        con.close()
        return False
    # otherwise complete the matchup up
    else:
        hashedpw = result[0]
        compare = bcrypt.checkpw(password.encode("utf-8"), hashedpw)
        # return the correct status
        if compare == True:
            con.close()
            return True
        else:
            con.close()
            return False

    # Original
    # Original was f string that was implementing the User's input in the username field directly into the SQL query making it runnable.
    # cur.execute(
    #     "SELECT * FROM users WHERE username = ?",  # putting ? means using the placeholder fro the next parameter.
    #     (username,),
    # )  # The parameter on which ? works.

    # if cur.fetchone() == None:
    #     con.close()
    #     return False
    # else:
    #     # This statement is really bad as it just looks for if there is a password that is entered, not necessarily matching the users input.
    #     cur.execute("SELECT * FROM users WHERE password = ?", (password))
    #     # Plain text log of visitor count as requested by Unsecure PWA management
    #     with open("visitor_log.txt", "r") as file:
    #         number = int(file.read().strip())
    #         number += 1
    #     with open("visitor_log.txt", "w") as file:
    #         file.write(str(number))
    #     # Simulate response time of heavy app for testing purposes
    #     time.sleep(random.randint(80, 90) / 1000)
    #     con.close()
    #     return True


def insertFeedback(feedback):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    # Fix
    cur.execute("INSERT INTO feedback (feedback) VALUES (?)", (feedback,))
    con.commit()
    con.close()


def listFeedback():
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM feedback").fetchall()
    con.close()
    f = open("templates/partials/success_feedback.html", "w")
    for row in data:
        f.write("<p>\n")
        f.write(f"{row[1]}\n")
        f.write("</p>\n")
    f.close()
