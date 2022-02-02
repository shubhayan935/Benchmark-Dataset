from __future__ import unicode_literals
from pytube import Playlist
import os
import youtube_dl
from pathlib import Path

# dictionary of the links to the playlists
playlist_links = {'ParishkarWorld_Q&A':"https://www.youtube.com/watch?v=RoPzDX_qKtQ&list=PL6TVOPSRQK7gnwpKpk7Lhv0OYeW-_squv", 
                 'ParishkarWorld_Patwar2020':"https://www.youtube.com/watch?v=8WXnwtaNZQs&list=PL6TVOPSRQK7j2-vFM-_Ea7I7giO0g-npu",
                'BeerBicepsPodcast':"https://www.youtube.com/watch?v=uc_plE-nOAc&list=PL9uK6jbdzfVfBzNfitRmYaCXCyq9TaY8q",
                 'ParishkarWorld_REETLive2020':"https://www.youtube.com/watch?v=-Z8RNf-23VY&list=PL6TVOPSRQK7h2P5qsjhvk1t88QjpAUQYL",
                 'ParishkarWorld_ImportantEvents':"https://www.youtube.com/watch?v=kN5H-SZIcVM&list=PL6TVOPSRQK7icn73OT1UBAOboeLQFLJRN"}
				 

# downloading the audios of each video in each playlist and saving it.
# each playlist has its one folder named "playlist name" and the individual audio file in them are names "playlist name_0, playlist name_1, etc."
for playist_link in playlist_links.values():
    count = 0
    play = 0
    p = Playlist(playlist_link)
    for vid_url in p.video_urls:
        my_file = Path("Audios/"+str(list(playlist_links.keys())[play])+"/"+str(count)+".mp3")
        if my_file.is_file():
            count += 1
            continue
        else:
            filename = "Audios/"+str(list(playlist_links.keys())[play])+"/"+str(count)+".mp3"
            ydl_opts = {'outtmpl': filename}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([vid_url])
            count += 1
    play+=1
