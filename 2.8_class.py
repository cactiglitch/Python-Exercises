"""
Happy Birthday
to you
Happy Birthday to you!
Wake me up
when September ends!

"""

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
happy_bday = Song(["Happy Birthday",
                   "to you",
                   "Happy Birthday to you!"])

sept_ends = Song(["Wake me up", 
                  "when September ends!"])

happy_bday.sing_me_a_song()

sept_ends.sing_me_a_song()
