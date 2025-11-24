# this module handles the secure functions for the app
import bcrypt


def getSalt():
    salt = bcrypt.gensalt()
    return salt


def getHash(password, salt):
    bytes = password.encode("utf-8")
    hashedpw = bcrypt.hashpw(bytes, salt)
    return hashedpw
