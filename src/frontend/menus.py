import sys
import api
import subprocess
import html

youtube = api.ytapi
videosearch = """Search for a video: """
mainmenuUI = """Youtube-CLI - What would you like to do?

[0] Search
[1] Exit

"""

def enterMenu():
    menuchoice = input(mainmenuUI)
    if menuchoice == "0":
        searcher()
    elif menuchoice == "1":
        sys.exit(0)
    else:
        pass
            
def searcher():
    try:
        searchchoice = input(videosearch)
        videoid = youtube.search(searchchoice, "ids")
        videoname = youtube.search(searchchoice, "names")
        searcherUI = f"""Select one of the videos:

[1] {html.unescape(videoname[0])} (id: {videoid[0]})
[2] {html.unescape(videoname[1])} (id: {videoid[1]})
[3] {html.unescape(videoname[2])} (id: {videoid[2]})
[4] {html.unescape(videoname[3])} (id: {videoid[3]})
[5] {html.unescape(videoname[4])} (id: {videoid[4]})

"""
        videochoice = input(searcherUI)
        print(f"Video selected! MPV will soon open and play {html.unescape(videoname[0])}")
        playVideo(videoid[(int(videochoice)-1)])
    except KeyboardInterrupt:
        pass

def playVideo(url):
    try:
        if url == "":
            raise ValueError
        else:
            subprocess.Popen(['mpv', f'https://youtube.com/watch?v={url}'])
    except ValueError as valerr:
        print(f"Something went wrong!\n{valerr}")

