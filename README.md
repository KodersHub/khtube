<img src = "https://raw.githubusercontent.com/KodersHub/khtube/master/khtube.png?token=AMSGSQZM5LKYESD3SHNGLILAAKQSQ" width=400>

khtube is an opensource software library enables you to download YouTube videos easily at all available qualities along with subtitles and can also download your videos in audio format.

<hr>

Install
=======

For installation::
  
  ```bash
  pip install khtube
  ```

(For macOS)::

  ```bash
  pip3 install khtube
  ```
  
Using khtube on Windows
=======

In windows, make sure that if you don't have ffmpeg pre-installed in your computer then do install it first by visiting the link : https://ffmpeg.org/download.html

Download .exe file by clicking "Windows builds from gyan.dev". After downloading go to bin folder, copy ffmpeg.exe and paste it in the folder in which you are actually runing the main python code and you are good to go.


Download your first YouTube video
=======

```python
import khtube

khtube.single_video(link, quality, verbose, output = "./Videos/", verbose)
```
* Where `link` is string containing YouTube's video URL.
* `quality` is by default best. But  you can change it by passing the available quality in integer value. Tou find the all available formats of any YouTube video along with their quality extensions. Use `khtube.available_quality(link)`, where `link` is again the string containing YouTube's url. It will print the available qualities of any video.
* `verbose` is being used to express details in more words. It can be `1`, `2` or `3` depending upon your needs.
* `output` is the saving directory of your downloaded YouTube video. If you don't pass it it will save in your default location.


Download the videos of Entire Playlist of YouTube
=======

```python
khtube.video_playlist(link, min_views = 1, quality=248, start_index = 1, verbose, best=True, output="./Videos/")
```
* Where `link` is string containing YouTube's Playlist URL.
* `min_views` is the filtration of views. By default it is 1. So if there's any video with NO VIEWS, it will not be downloaded. However you can change it accordingly. 
* `quality` is by default best. But  you can change it by passing the available quality in integer value. Tou find the all available formats of any YouTube video along with their quality extensions. Use `khtube.available_quality(link)`, where `link` is again the string containing YouTube's url. It will print the available qualities of any video.
* `start_index` is the Starting index of a video in playlist. For example, if you pass 4 and there are only 10 videos, only 7 will be downloaded. Given that, 0 is not inclusive.
* `verbose` is being used to express details in more words. It can be `1`, `2` or `3` depending upon your needs.
* `output` is the saving directory of your downloaded YouTube video. If you don't pass it it will save in your default location.

Download the videos of Entire Channel on YouTube
=======

```python
khtube.video_playlist(link, min_views = 1, quality=248, start_index = 1, verbose, best=True, output="./Videos/")
```
* Where `link` is string containing YouTube's Channel URL.
* `min_views` is the filtration of views. By default it is 1. So if there's any video with NO VIEWS, it will not be downloaded. However you can change it accordingly. 
* `quality` is by default best. But  you can change it by passing the available quality in integer value. Tou find the all available formats of any YouTube video along with their quality extensions. Use `khtube.available_quality(link)`, where `link` is again the string containing YouTube's url. It will print the available qualities of any video.
* `start_index` is the Starting index of a video in channel. For example, if you pass 4 and there are only 10 videos, only 7 will be downloaded. Given that, 0 is not inclusive.
* `verbose` is being used to express details in more words. It can be `1`, `2` or `3` depending upon your needs.
* `output` is the saving directory of your downloaded YouTube video. If you don't pass it it will save in your default location.

Download Subtitles of any Video
=======

```python
khtube.download_sub(link, language="en-US")
```
* Where `link` is string containing YouTube's Video URL.
* `language` is the parameter in string for language format. A video can have multiple subtitles. By default it will download in **English US**. But you can always change that upon your needs. To find out the available subtitles, use `khtube.available_sub(link)`, where `link` is again the string containing YouTube's url. It will print the available subtitle languages of any video with codes.


Download AudioOnly of any Video
=======

```python
khtube.only_music(link, quality=251, verbose=2)
```
* Where `link` is string containing YouTube's Video URL.
* `quality` is by default best. But  you can change it by passing the available quality in integer value. Tou find all the available formats of any YouTube video along with their quality extensions. Use `khtube.available_quality(link)`, where `link` is again the string containing YouTube's url. It will print the available qualities of any video. **Caution: Be careful, only use audio quality code** or else you can leave it by default.
* `verbose` is being used to express details in more words. It can be `1`, `2` or `3` depending upon your needs.


Download the AudioOnly of videos of Entire Playlist of YouTube
=======

```python
khtube.audio_playlist(link, min_views = 1, quality=248, start_index = 1, verbose = 2 , best=True, output="./Videos/")
```
* Where `link` is string containing YouTube's Playlist URL.
* `min_views` is the filtration of views. By default it is 1. So if there's any video with NO VIEWS, it will not be downloaded. However you can change it accordingly. 
* `quality` is by default best. But  you can change it by passing the available quality in integer value. Tou find all the available formats of any YouTube video along with their quality extensions. Use `khtube.available_quality(link)`, where `link` is again the string containing YouTube's url. It will print the available qualities of any video. **Caution: Be careful, only use audio quality code** or else you can leave it by default.
* `start_index` is the Starting index of a video in playlist. For example, if you pass 4 and there are only 10 videos, only 7 will be downloaded. Given that, 0 is not inclusive.
* `verbose` is being used to express details in more words. It can be `1`, `2` or `3` depending upon your needs.
* `output` is the saving directory of your downloaded YouTube video. If you don't pass it it will save in your default location.


Download the AudioOnly of videos of Entire Channel of YouTube
=======

```python
khtube.channel_audio(link, min_views = 1, quality=248, start_index = 1, verbose = 2 , best=True, output="./Videos/")
```
* Where `link` is string containing YouTube's Channel URL.
* `min_views` is the filtration of views. By default it is 1. So if there's any video with NO VIEWS, it will not be downloaded. However you can change it accordingly. 
* `quality` is by default best. But  you can change it by passing the available quality in integer value. Tou find all the available formats of any YouTube video along with their quality extensions. Use `khtube.available_quality(link)`, where `link` is again the string containing YouTube's url. It will print the available qualities of any video. **Caution: Be careful, only use audio quality code** or else you can leave it by default.
* `start_index` is the Starting index of a video in channel. For example, if you pass 4 and there are only 10 videos, only 7 will be downloaded. Given that, 0 is not inclusive.
* `verbose` is being used to express details in more words. It can be `1`, `2` or `3` depending upon your needs.
* `output` is the saving directory of your downloaded YouTube video. If you don't pass it it will save in your default location.


Contribute
==========
You've discovered a bug or something else you want to change - excellent!

You've worked out a way to fix it – even better!

You want to tell us about it – best of all!

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

Contact
=======
Send your message at this form <https://forms.gle/eoxmiRzLiKJLSvTF7>, We will review it shortly.

Developers
=======
Kodershub Developers ©
https://kodershub.tech

License
=======
[MIT](https://choosealicense.com/licenses/mit/)
