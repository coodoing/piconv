piconv
======

## Desciption
Use `chardet` to auto detect file encoding format and iconv it to the input encoding format even you don't know what the encoding format of the input files. You can also get more details from `uchardet`. 



## Why piconv?
As you know, Linux provide iconv command to convert between different character encodings, but the from-encoding and to-encoding must be provided......


When encounting some garbled characters encoding problem, you want to convert it to the correct format, linux provides `iconv` to do it. ***If you know the file's encoding, just ignore what I descibe  below***. But when you don't get the right file encoding or you don't even know the file's encoding, you can't convert the file correctly. The encoding format of **data-set/chinese-ansi.txt** is *GBK*, but you will get *ISO-8859* when use the `file` command, then the format will be wrong. 
```
file data-set/chinese-ansi.txt #ISO-8859
iconv -f iso-8859-1 -t utf-8 data-set/chinese-ansi.txt > chinese-ansi.txt # garbled character-ÂÒÂë

Or

iconv -f GBK -t utf-8 data-set/chinese-ansi.txt > chinese-ansi.txt # correctly

```

Comparision with `iconv / piconv(perl)` command through the given file **data-set/assoc.c** which contains chinese characters 'Í·²å·¨' and is *utf-8* encoding format.Use `file FILENAME` command to get the file's format. The source content:
```
    // Í·²å·¨
    return 1;
}
```

* **convert utf-8 to gbk**
  command:
```
iconv -f utf-8 -t gbk data-set/assoc.c > utf8-gbk.c
 
piconv -f utf-8 -t gbk data-set/assoc.c > utf8-gbk-p.c
```
  result:
```   
  // ¨ª¡¤2?¡¤¡§
     return 1;
  }
```

* **convert gbk to utf-8** 
Now we take a look at the result when convert gbk to utf-8 through `iconv`.
```
 iconv -f gbk -t utf-8 data-set/assoc.c > gbk-utf8.c
 #iconv: illegal input sequence at position 16
```
Result:(terminated by the unicode error)
```
    // å¤´æ’æ³
```
Then we use **`iconv -c`** option to omit invalid characters from output.
```
iconv -c -s -f gbk -t utf-8 data-set/assoc.c > gbk-utf8-c.c
```
result:
```
    // å¤´æ’æ³
    return 1;
}
```
* **utf8-utf8 & gbk-gbk**
```
iconv -c -s -f utf-8 -t utf-8 data-set/assoc.c > utf8-utf8.c

iconv -c -s -f gbk -t gbk data-set/assoc.c > gbk-gbk.c
```
result
```
     // Í·²å·¨
    return 1;
}
  
    // ?¡è¡ä?<8f><92>?3
    return 1;
}

```
You can also test other convertion cases. 


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
