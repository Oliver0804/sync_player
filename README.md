# 影片同步播放器使用說明


![demo](https://github.com/Oliver0804/sync_player/blob/main/%E6%88%AA%E5%9C%96%202023-08-03%20%E4%B8%8A%E5%8D%8812.10.35.png)
此程式用於在區域網路中同步播放多部影片，可以在不同主機上同步播放影片。
## 安裝方式
1. 安裝mplayer
```
sudo apt install mplayer
```


2. 安裝pyqt5
```
pip install - r requirements.txt
```

## 使用方法

循環播放在選擇影片前勾選

1. python3 main.py 運行程式後，將會看到兩個分頁：Master 和 Slave。
```
python3 main.py
```

2. Master 分頁：

![demo](https://github.com/Oliver0804/sync_player/blob/main/%E6%88%AA%E5%9C%96%202023-08-03%20%E4%B8%8A%E5%8D%8812.10.47.png)

   - 會顯示當前主機的 IP 地址。
   - 點擊 '選擇影片' 按鈕，選擇你要播放的影片檔案。
   - '循環播放' 的核取方塊：選擇影片並點擊播放後，將無法更改循環播放的設定。

3. Slave 分頁：

![demo](https://github.com/Oliver0804/sync_player/blob/main/%E6%88%AA%E5%9C%96%202023-08-03%20%E4%B8%8A%E5%8D%8812.11.22.png)

   - 點擊 '服務器 IP' 按鈕，輸入 Master 主機的 IP 地址。
   - 點擊 '選擇影片' 按鈕，選擇你要播放的影片檔案。
   - '播放影片' 按鈕：與 Master 主機同步並開始播放影片。
   - '循環播放' 的核取方塊：選擇影片並點擊播放後，將無法更改循環播放的設定。

## 影片播放控制鍵

- 空白鍵：暫停/播放
- 方向鍵左/右：快進/倒帶
- F：全螢幕切換

請注意：此程式需要安裝 MPlayer 才能正常使用。
