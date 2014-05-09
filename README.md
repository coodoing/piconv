piconv
======

## Intro
Use `chardet`[^code] to auto detect file encoding format and iconv it to input encoding format even you don't know what the encoding format of the input file. You can also get `uchardet`[^code] for more details.


## Why piconv?
As you know, Linux provide iconv command to convert between different character encodings, but the from-encoding and to-encoding must be provided.?


## How to use
The `piconv` tool provides an easy way to use, you just need to input `'file_name'` and `'to_encoding'` params to implementing translation.

* `just run the python`
```python
piconv.py filename/dirname to_encoding
```

* `iconv input file`
```
FIconv('french-mscs.txt','utf-8')
```

* `iconv input dir`
```
diconv = DIconv('/var/www/piconv/test','utf-8')
diconv.codecs_iconv_iterator()
```

## Comparision with linux iconv command

* `simple iconv command`

* `complicated iconv command to implement dirs convert`


## Suports


## Functions & Advantages
The `piconv` includes following functions and advantages:

> * 1、正则匹配，获取所有匹配的文件列表；
> * 2、快速遍历多层级目录，获取文件列表；（DFS, BFS）
> * 3、文件ENCODE自动识别；iconv需要手动去指定from to的encoding模式；
> * 4、强大的异常处理；编码问题的解决
> * 5、简化iconv对目录的处理，方便的调用接口；（指定src目录，缺省的dest目录，指定from-to coding，默认的匹配方式）
> * 6、长目录进行压缩

[^code]: chardet
[^code]: http://lxr.mozilla.org/seamonkey/source/extensions/universalchardet/