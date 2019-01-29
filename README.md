# download_ios_system_symbols
下载指定版本iOS系统的symbol，并且自动解压到 `~/Library/Developer/Xcode/iOS DeviceSupport` 目录。(由于资源在Google Drive，所以懂的...)

资源来自：[https://github.com/Zuikyo/iOS-System-Symbols](https://github.com/Zuikyo/iOS-System-Symbols)

使用前必须先安装 [gdrive](https://github.com/prasmussen/gdrive)

解压工具 p7zip

```
brew install p7zip
```

使用方法

```
例如
python download_symbols.py -v 16D39
注：16D39 是系统版本号
```


推荐一个Crash符号化工具

[https://github.com/zqqf16/SYM](https://github.com/zqqf16/SYM)


