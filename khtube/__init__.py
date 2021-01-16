# A way to import 
# import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '/home/furqan/.pyenv/versions/3.8.5/lib/python3.8/site-packages')
import youtube_dl, subprocess

#pip install --user youtube-dl

sv_path = "$HOME/Video/%(title)s.%(ext)s"

def single_video(link, quality=136, best=True, output=sv_path, verbose = 2, subprocess=subprocess):
    
    if best == True:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part -f "bestvideo+bestaudio/best"  -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
            
    else:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part -f {quality}+140 -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")

        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")

# Downloading only audio of the single video
sa_path = "$HOME/Audio/%(title)s.%(ext)s"

def only_music(link, quality=251, best=True, output=sa_path, verbose=2, subprocess = subprocess):
    if best == True:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part -f "bestaudio/best" -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
            
    else:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part -f {quality} -o "{output}" {link}', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")


def available_quality(link, subprocess = subprocess):
    subprocess = subprocess.Popen(f'youtube-dl -F "{link}"', shell = True, stdout = subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    result = str(subprocess_return)
    results = result.split("\\n")
    for i in results:
        print(i)


# Downloading the videos playlist
vp_path = "$HOME/Video/%(title)s.%(ext)s"

def video_playlist(link, min_views = 1, quality=248, start_index = 1, verbose=2, best=True, output=vp_path, subprocess = subprocess):
    if best == True:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part --min-views {min_views} -i -f "bestvideo+bestaudio/best" -ci --playlist-start {start_index} -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
            
    else:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part --min-views {min_views} -i -f {quality}+140 -ci --playlist-start {start_index} -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")

        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")

# downloading only audio playlist.
ap_path = "$HOME/Audio/%(title)s.%(ext)s"

def audio_playlist(link, min_views = 1, quality=140, verbose=2, start_index = 1, best=True, output=ap_path, subprocess = subprocess):
    if best == True:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part --min-views {min_views} -i -f "bestaudio/best" -ci --yes-playlist {start_index} -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
            
    else:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part --min-views {min_views} -i -f {quality} -ci {start_index} -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")

        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")

# Downloading only those videos in the channel which are having min 100 Views.
vc_path = f"$HOME/Video/%(title)s.%(ext)s"

def channel_video(link, min_views = 1, quality=248, verbose=2, best=True, output=vc_path, subprocess = subprocess):
    if best == True:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part --min-views {min_views} -f "bestvideo+bestaudio/best" -ciw -o "{output}" -v "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
            
    else:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part --min-views {min_views} -f {quality}+140 -ciw -o "{output}" -v "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")

        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")    

# For downloading entire channel audios
ac_path = "$HOME/Audio/%(title)s.%(ext)s"

def channel_audio(link, min_views = 1, quality=140, verbose=2, best=True, output=ac_path, subprocess = subprocess):
    if best == True:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part --min-views {min_views} -f "bestaudio/best" -ciw -o "{output}" -v "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
            
    else:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'youtube-dl --no-part --min-views {min_views} -f {quality} -ciw -o "{output}" -v "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("Please wait...")

        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")



def available_sub(link, subprocess = subprocess):
    subprocess = subprocess.Popen(f'youtube-dl --list-subs "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    result = str(subprocess_return)
    results = result.split("\\n")
    for i in results:
        print(i)

def download_sub(link, language="en-US", subprocess = subprocess):
    subprocess = subprocess.Popen(f'youtube-dl --write-sub --sub-lang {language} --skip-download "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    result = str(subprocess_return)
    print(result)

# Cropping youtube video

def crop_video(link, fromm, to, quality = "best", subprocess = subprocess):
#     A way to import 
#     FROM = "00:02:06"
#     TO = "00:03:45"
    """
    - Remeber only 3 quality types are available i.e.
    - best -> best of 720p
    - worst -> almost around 240-430p
    """

    TARGET = "demo.mp4"

    with youtube_dl.YoutubeDL({'format': quality}) as ydl:
        result = ydl.extract_info(link, download=False)
        video = result['entries'][0] if 'entries' in result else result

    url = video['url']
    print("Please wait......")
    subprocess.run('ffmpeg -i "%s" -ss %s -to %s -c:v copy -c:a copy "%s"' % (url, fromm, to, TARGET), shell=True)
    print("Downloading successfull")

# Cropping youtube audio only 

def crop_audio(link, fromm, to, quality = "best", subprocess = subprocess):
#     A way to import 
#     FROM = "00:02:06"
#     TO = "00:03:45"
    """
    - Remeber only 3 quality types are available i.e.
    - best -> best of 720p
    - worst -> almost around 240-430p
    - bestaudio -> It only downloads the audio file, no video.
    """
    if quality == "best":
        TARGET = "demo.webm"
    else:
        TARGET = "demo.m4a"

    with youtube_dl.YoutubeDL({'format': quality}) as ydl:
        result = ydl.extract_info(link, download=False)
        video = result['entries'][0] if 'entries' in result else result

    url = video['url']
    print("Please wait......")
    subprocess.run('ffmpeg -i "%s" -ss %s -to %s -c:v copy -c:a copy "%s"' % (url, fromm, to, TARGET), shell=True)
    print("Downloading successfull")

    





