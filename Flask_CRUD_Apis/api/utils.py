from datetime import datetime

def gen_id():
    now = datetime.now()
    generated_id = now.strftime("9%S%f")
    return generated_id[-10:]
gen_id()