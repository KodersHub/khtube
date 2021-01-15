# khtube

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

Download your first YouTube video
=======

```python
import khtube

khtube.single_video(link, quality, verbose, output = "./Videos/", verbose)
```
* Where `link` is string containing YouTube's video url.
* `quality` is by default best. But  you can change it by passing the available quality in integer value. Tou find the all available formats of any YouTube video along with their quality extensions. Use `khtube.available_quality(link)`, where `link` is again the string containing YouTube's url. It will print the available qualities of any video.
* `verbose` is being used to express details in more words. It can be `1`, `2` or `3` depending upon your needs.
* `output` is the saving directory of your downloaded YouTube video. If you don't pass it it will save in your default location.

Using khtube on windows
=======

In windows, make sure that if you don't have ffmpeg pre-installed in your computer then do install it first by 
visiting the link : https://ffmpeg.org/download.html

Download .exe file by clicking "Windows builds from gyan.dev". After downloading go to bin folder, copy ffmpeg.exe and
paste it in the folder in which you are actually runing the main python code and you are good to go.


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

kodershub.net

License
=======
[MIT](https://choosealicense.com/licenses/mit/)
