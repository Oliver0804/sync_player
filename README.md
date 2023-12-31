# Sync Player 影片同步播放器使用說明 🎞️🔄

![demo](https://github.com/Oliver0804/sync_player/blob/main/%E6%88%AA%E5%9C%96%202023-08-03%20%E4%B8%8A%E5%8D%8812.10.35.png)
此程式用於在區域網路中同步播放多部影片，可以在不同主機上同步播放影片。🎬

## 影片播放控制鍵 🎛️


以下是MPlayer中可用的一些常見快捷鍵，讓你對影片播放有更多的控制：
常用
- ***F：全螢幕切換***
- 方向鍵左/右：快進/倒帶 (10秒)
- P 或 SPACE：暫停 (與空白鍵功能相同)
- M：靜音切換
- / 和 *：降低/提高音量 (在數字小鍵盤上)
- Z 和 X：延遲字幕前進/後退 (每次按下 0.1 秒)
- J：在可用的字幕之間切換
- 方向鍵上/下：增加/減少音量
- Q 或 ESC：停止播放並退出

提示：如果你正在使用的是不同版本的MPlayer或在特定操作系統上，可用的快捷鍵可能會有所不同。請查閱你的MPlayer文檔來獲取完整的快捷鍵列表。

請注意：此程式需要安裝 MPlayer 才能正常使用。📌

## 程序優勢 🌟
1. 使用python開發，易於維護和二次開發。🐍
2. 只要有支持python與mplayer即可運行，跨平台兼容性強。🌐
3. 完善的安裝腳本，讓安裝過程簡單快速。📜
4. 具有圖形介面，無需編程知識，只要動動滑鼠即可操作，並且記錄下Server IP即可。🖱️

快來體驗同步播放的樂趣吧！🎉

## 安裝方式 🛠️

1. 安裝mplayer
```
sudo apt install mplayer
```

2. Clone本項目
```
git clone https://github.com/Oliver0804/sync_player
```

3. 安裝python所需的套件
```
cd sync_player
pip install - r requirements.txt
```

## 使用方法 📖

循環播放在選擇影片前勾選 ✔️

1. `python3 main.py` 運行程式後，將會看到兩個分頁：Master 和 Slave。

```
python3 main.py
```

2. Master 分頁：🔗

![demo](https://github.com/Oliver0804/sync_player/blob/main/%E6%88%AA%E5%9C%96%202023-08-03%20%E4%B8%8A%E5%8D%8812.10.47.png)

   - 會顯示當前主機的 IP 地址。
   - 點擊 '選擇影片' 按鈕，選擇你要播放的影片檔案。
   - '循環播放' 的核取方塊：選擇影片並點擊播放後，將無法更改循環播放的設定。

3. Slave 分頁：🔗

![demo](https://github.com/Oliver0804/sync_player/blob/main/%E6%88%AA%E5%9C%96%202023-08-03%20%E4%B8%8A%E5%8D%8812.11.22.png)

   - 點擊 '服務器 IP' 按鈕，輸入 Master 主機的 IP 地址。
   - 點擊 '選擇影片' 按鈕，選擇你要播放的影片檔案。
   - '播放影片' 按鈕：與 Master 主機同步並開始播放影片。
   - '循環播放' 的核取方塊：選擇影片並點擊播放後，將無法更改循環播放的設定。

