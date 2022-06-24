# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:01:43 2022

@author: Anna
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []  
    size = 0
    
    if songs[0][2] <= max_size:
        playlist.append(songs[0][0])
        size+=songs[0][2]
    else:
        return playlist
    
    
    songs.sort(key=lambda a:a[2])
    
    for i in songs:
        if i[2] <= max_size-size:
            if i[0] not in playlist:
                playlist.append(i[0])
                size+=i[2]
        else:
            break
    
   
    return playlist

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 2

print(song_playlist(songs, max_size))
