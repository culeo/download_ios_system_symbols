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


#### 关于 gdrive

[How to access Google Drive using a service account JSON file](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=2ahUKEwi3-cvpyYrpAhWmy4sBHUIJCIYQFjABegQIMBAD&url=https%3A%2F%2Fhelp.talend.com%2Freader%2FE3i03eb7IpvsigwC58fxQg%2Fol2OwTHmFbDiMjQl3ES5QA&usg=AOvVaw2G6FpeJjlqz-nVsxHWZfFn)

下载 service account JSON file 放到 ~/.gdrive 目录下，保存为 Key.json

