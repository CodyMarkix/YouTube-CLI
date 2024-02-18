# I know the script itself doesn't interact with the api
# but I didn't know where to put this and did not want to
# create a whole folder just for one script so shush
import os

def downloadvideo(vId):
    try:
        pastfolder = os.path.abspath('.')
        os.chdir(os.environ['HOME'] + '/Downloads')
        testvar = os.system(f'youtube-dl https://youtube.com/watch?v={vId}')
        os.chdir(pastfolder)
        os._exit(0)
    except Exception as err:
        return