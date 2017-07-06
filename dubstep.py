import re
def song_decoder(song):
    return " ".join(song.replace('WUB',' ').split())

print song_decoder("AWUBWUBWUBWUBBWUBC")
