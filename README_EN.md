# Sync Player Video Synchronization User Guide 🎞️🔄

![demo](https://github.com/Oliver0804/sync_player/blob/main/%E6%88%AA%E5%9C%96%202023-08-03%20%E4%B8%8A%E5%8D%8812.10.35.png)
This program is used to synchronize the playback of multiple videos within a local area network, allowing video synchronization on different hosts. 🎬

## Video Playback Control Keys 🎛️

Here are some common keyboard shortcuts available in MPlayer to give you more control over video playback:
- F: Fullscreen toggle
- Spacebar: Pause/Play
- Left/Right Arrow: Fast forward/Rewind (10 seconds)
- P or SPACE: Pause (the same as the spacebar function)
- M: Mute toggle
- / and *: Decrease/Increase volume (on the numeric keypad)
- Z and X: Delay subtitle forward/backward (0.1 seconds per press)
- J: Switch between available subtitles
- Up/Down Arrow: Increase/Decrease volume
- Q or ESC: Stop playback and exit

Tip: The available shortcuts may vary depending on the version of MPlayer you are using or the specific operating system. Please consult your MPlayer documentation for a complete list of shortcuts.

Please note: This program requires the installation of MPlayer to function properly. 📌

## Program Advantages 🌟
1. Developed with Python, easy to maintain and develop further. 🐍
2. It can be run as long as Python and MPlayer are supported, strong cross-platform compatibility. 🌐
3. A complete installation script makes the installation process simple and fast. 📜
4. It has a graphical interface, no programming knowledge is required, just move the mouse, and record the Server IP. 🖱️

Come and experience the fun of synchronized playback! 🎉

## Installation 🛠️

1. Install mplayer
```
sudo apt install mplayer
```

2. Install the required Python packages
```
pip install - r requirements.txt
```

## How to Use 📖

Check the loop playback before selecting the video ✔️

1. After running the `python3 main.py` program, you will see two tabs: Master and Slave.

```
python3 main.py
```

2. Master Tab: 🔗

![demo](https://github.com/Oliver0804/sync_player/blob/main/%E6%88%AA%E5%9C%96%202023-08-03%20%E4%B8%8A%E5%8D%8812.10.47.png)

   - Displays the current host's IP address.
   - Click the 'Select Video' button to choose the video file you want to play.
   - 'Loop Playback' checkbox: Once you choose a video and click play, the loop playback setting cannot be changed.

3. Slave Tab: 🔗

![demo](https://github.com/Oliver0804/sync_player/blob/main/%E6%88%AA%E5%9C%96%202023-08-03%20%E4%B8%8A%E5%8D%8812.11.22.png)

   - Click the 'Server IP' button and enter the Master host's IP address.
   - Click the 'Select Video' button to choose the video file you want to play.
   - 'Play Video' button: Synchronize with the Master host and start playing the video.
   - 'Loop Playback' checkbox: Once you choose a video and click play, the loop playback setting cannot be changed.
