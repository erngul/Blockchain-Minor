import random
import string
from pyblake2 import blake2b

def gen_random_string(n):
    return blake2b(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n)).encode('utf-8'), 1).hexdigest()


# Ask the user to enter a name
inputName = input('Insert name: ')
# Compute the hash of the input using blake2b (hash size = 1 byte)
gfg = blake2b(inputName.encode('utf-8'), 1)
# use gen_random_string() to see if you can find a collision
print(gfg.hexdigest())
counter = 0
for x in range(1000000):
    randomString = gen_random_string(x)
    if gfg.hexdigest() == randomString:
        counter+=1
        print(counter)
    pass
print(gfg.hexdigest())
