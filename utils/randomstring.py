from rstr import rstr
from string import digits, ascii_lowercase, ascii_uppercase

def randomstring(length=10):
    return rstr(digits+ascii_lowercase+ascii_uppercase, length)
