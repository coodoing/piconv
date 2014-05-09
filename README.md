piconv
======

Use `chardet` to auto detect file encoding format and iconv it to specified encoding format

The `piconv` includes following functions and advantages:

> * 1、正则匹配，获取所有匹配的文件列表；
> * 2、快速遍历多层级目录，获取文件列表；多线程（DFS, BFS）
> * 3、文件ENCODE自动识别；iconv需要手动去指定from to的encoding模式；
> * 4、强大的异常处理；编码问题的解决
> * 5、简化iconv对目录的处理，方便的调用接口；（指定src目录，缺省的dest目录，指定from-to coding，默认的匹配方式）
> * 6、长目录进行压缩


