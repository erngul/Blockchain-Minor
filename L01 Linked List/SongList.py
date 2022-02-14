
class SongNode:
    def __init__(self, song_title=None, next = None):
        self.song_title = song_title
        self.next = next

class SongList:
    def __init__(self):  
        self.head = None

    def printSongs(self):
        current_node = self.head
        while current_node != None:
            print(current_node.song_title)
            current_node = current_node.next

    def AddNewSong(self, new_song_title):
        if self.head is None:
            self.head = SongNode(new_song_title)
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = SongNode(new_song_title)