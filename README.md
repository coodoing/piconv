piconv
======

## Intro
Use `chardet` to auto detect file encoding format and iconv it to input encoding format even you don't know what the encoding format of the input file. You can also get `uchardet` for more details.


## Why piconv?
As you know, Linux provide iconv command to convert between different character encodings, but the from-encoding and to-encoding must be provided......


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



[^code]: chardet
[^code]: http://lxr.mozilla.org/seamonkey/source/extensions/universalchardet/
