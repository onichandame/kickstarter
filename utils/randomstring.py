from rstr import rstr
from string import digits, ascii_lowercase, ascii_uppercase

def randomstring():
    return rstr(digits+ascii_lowercase+ascii_uppercase, 10)
