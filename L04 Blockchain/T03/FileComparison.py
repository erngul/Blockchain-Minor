from cryptography.hazmat.primitives import hashes
import imageio as iio
import pathlib

# import required module
import os
from pathlib import Path
# compute the hash of original.png using SHA256
img = iio.imread("original.png")
digest = hashes.Hash(hashes.SHA256())
digest.update(img)
final = digest.finalize()
# compute hash of file copy(1).png, copy(2).png, copy(3).png, and copy(4).png
# and test which of these files is/are equal to the original file
files = Path(pathlib.Path().resolve()).glob('copy*')
for file in files:
    imgCopy = iio.imread(file)
    digestCopy= hashes.Hash(hashes.SHA256())
    digestCopy.update(imgCopy)
    finalCopy = digestCopy.finalize()
    if(finalCopy == final):
        print(file)
        print(finalCopy)