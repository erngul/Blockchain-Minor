
from SongList import *


linkedlist = SongList()
print(linkedlist)

# assign values to nodes
linkedlist.head = SongNode("A Hard Day's Night")
second = SongNode('A Day in the Life')
third = SongNode("Strawberry Fields Forever")

# link nodes
linkedlist.head.next = second
second.next = third
third.next = None

linkedlist.printSongs()

linkedlist.AddNewSong("She Loves You")
linkedlist.AddNewSong("Something")
linkedlist.printSongs()