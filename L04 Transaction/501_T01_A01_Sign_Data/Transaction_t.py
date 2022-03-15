from Signature import *

if __name__ == '__main__':
    
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()

    data = [
        'Alex pays 2 coin to mike', 
        'Alex pays 1.2 coins to Mara', 
        'Mike pays 0.6 coin to Alex'
        ]

# sign data using alex signature and then verify it using the same signature
    for d in data:
        print(d)
        singed = sign(d.encode(), alex_prv)
        print(verify(d.encode(), singed, alex_pbc))

# sign data using alex signature and then verify it using mike signature
    for d in data:
        print(d)
        singed = sign(d.encode(), alex_prv)
        print(verify(d, singed, mike_pbc))