import random


#generate integer
def random_integer():
    rand_int = random.randint(0,10)
    return [str(rand_int).encode(), str(rand_int).encode()]


#serve an html file 
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #rand_int is an integer and I need to return bytes
    return random_integer()
