import string
from .models import bitly

def code_gen():
    import random
    shrtcd = ''
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    for i in range(6):
        shrtcd+= random.choice(chars)
    return shrtcd

def create_shortcode():
    shrtcd = code_gen()
    qs = bitly.objects.filter(shortcode__iexact=shrtcd)
    if qs.exists():
        return create_shortcode()
    return shrtcd

from datetime import date

def current_date():
    crt_date = date.today()
    print(crt_date)
    return crt_date.strftime("%d-%m-%y")
