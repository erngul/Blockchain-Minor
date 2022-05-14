from pyblake2 import blake2b


# Read the text file "names.txt" 
with open('names.txt') as f:
    lines = f.readlines()
# Ask the user to enter a name
inputName = input('type a name')
# Compute the hash of the input using blake2b (hash size = 1 byte)
gfg = blake2b(inputName.encode('utf-8'), 1)
hashList = [gfg.hexdigest()]
print(gfg.hexdigest())
# Check the names in the file to see if you can find a collision
count =0
for l in lines:
    gfg1 = blake2b(l.encode('utf-8'), 1)
    if gfg1.hexdigest() == gfg.hexdigest():
        count+=1
        print(f'collisions: {count}')
    hashList.append(gfg1.hexdigest())

