import sys
import api
import os, subprocess
import html

youtube = api.ytapi
youtubedl = api.ytdl
videosearch = """Search for a video: """
mainmenuUI = """Youtube-CLI - What would you like to do?

[0] Search
[1] Download
[2] Exit

"""

def enterMenu():
    menuchoice = input(mainmenuUI)
    if menuchoice == "0":
        searchtype = input("What are you searching for?\n(Possible values: video, playlist, back) ")
        searcher(searchtype, "play")
    elif menuchoice == "1":
        searchtype = input("What are you searching for?\n(Possible values: video, playlist) ")
        searcher(searchtype, "download")
    elif menuchoice == "2":
        sys.exit(0)
    else:
        pass
            
def searcher(type, action):
    try:
        if type == "video":
            searchchoice = input(videosearch)
            videoid = youtube.search(searchchoice, "ids", "video")
            videoname = youtube.search(searchchoice, "names", "video")
            searcherUI = f"""Select one of the videos:

[1] {html.unescape(videoname[0])} (id: {videoid[0]})
[2] {html.unescape(videoname[1])} (id: {videoid[1]})
[3] {html.unescape(videoname[2])} (id: {videoid[2]})
[4] {html.unescape(videoname[3])} (id: {videoid[3]})
[5] {html.unescape(videoname[4])} (id: {videoid[4]})

"""
            if action == "play":
                videochoice = input(f"{searcherUI}\nSelect: ")
                print(f"Video selected! MPV will soon open and play \"{html.unescape(videoname[(int(videochoice) - 1)])}\"")
                playVideo(videoid[(int(videochoice)-1)])
                videoInfoSection(videoid[(int(videochoice)-1)])
            elif action == "download":
                videochoice = input(f"{searcherUI}\nSelect: ")
                print(f"Video selected! Downloading \"{html.unescape(videoname[(int(videochoice) - 1)])}\"")
                youtubedl.downloadvideo(videoid[(int(videochoice)-1)])
                enterMenu()
            else:
                videochoice = input(f"{searcherUI}\nSelect: ")
                print(f"Video selected! MPV will soon open and play \"{html.unescape(videoname[(int(videochoice) - 1)])}\"")
                playVideo(videoid[(int(videochoice)-1)])

        elif type == "playlist":
            pass

        elif type == "back":
            enterMenu()

    except KeyboardInterrupt:
        pass

def playVideo(url):
    try:
        if url == "":
            raise ValueError
        else:
            os.system(f'mpv https://youtube.com/watch?v={url}')
    except ValueError as valerr:
        print(f"Something went wrong!\n{valerr}")

def getPlaylistVideos():
    pass


def videoInfoSection(videoId):
    comments = youtube.fetchVideoInfo(videoId)
    commentText = ""
    tempFolder = f"{os.environ['USERPROFILE']}\\AppData\\Local\\Temp" if os.name == 'nt' else "/tmp"

    for x in comments["items"]:
        commentThread = x['snippet']
        comment = x['snippet']['topLevelComment']['snippet']
        likeText = 'likes' if comment['likeCount'] != 1 else 'like'
        replyText = 'replies' if commentThread['totalReplyCount'] != 1 else 'reply'

        commentText += f"{comment['authorDisplayName']}\n-------------\n{comment['textOriginal']}\n-------------\n{comment['likeCount']} {likeText}, {commentThread['totalReplyCount']} {replyText}\n\n"

    with open(os.path.join(tempFolder, "comments"), 'w', encoding='utf-8') as f:
        f.write(commentText)

    os.system(f"less {os.path.join(tempFolder, 'comments')}")
    enterMenu()