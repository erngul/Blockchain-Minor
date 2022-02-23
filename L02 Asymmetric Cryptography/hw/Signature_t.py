from Signature import *

if __name__ == '__main__':
    
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()


    pws = input("Enter a password for saving the keys: ")

    save_keys('alex.keys', (alex_prv, alex_pbc), pws)
    save_keys('mike.keys', (mike_prv, mike_pbc), pws)
    save_keys('rose.keys', (rose_prv, rose_pbc), pws)


    print('keys are successfully saved.')

    alex_message = 'pay 10 euro to mike'
    mike_message = 'pay 5 euro to josé'
    rose_message = 'Hello, this is rose!'

    alex_signature = sign(alex_message, alex_prv)
    mike_signature = sign(mike_message, mike_prv)
    rose_signature = sign(rose_message, rose_prv)


    pwl = input("Enter a password for loading the keys: ")
    (_, alex_pbc_loaded) = load_keys('alex.keys', pwl)
    (_, mike_pbc_loaded) = load_keys('mike.keys', pwl)
    (_, rose_pbc_loaded) = load_keys('rose.keys', pwl)

    for p in ['alex', 'mike', 'rose']:
        r_message = input(f"What was {p}'s message? ")
        
        (_, pbc_loaded) = load_keys(p+'.keys', pwl)
        sig = globals()[p+'_signature']
        correct = verify(r_message, sig, pbc_loaded)
        if correct:
            print('Great! You correctly entered the message.')
        else:
            print('Oops! The message you entered is not correct')
