# this module handles the secure functions for the app
import bcrypt
import html

# Generates unique salt everytime its called


def getSalt():
    salt = bcrypt.gensalt()
    return salt


# create has for the password


def getHash(password, salt):
    bytes = password.encode("utf-8")
    hashedpw = bcrypt.hashpw(bytes, salt)
    return hashedpw


# take the input for each time we need it, manipulate
# the html parts like < and > adn make them plain text


def xssremove(input: str) -> str:
    return html.escape(input)
