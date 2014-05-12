piconv
======

## Description
The `piconv` tool use `chardet` to auto detect the file's encoding format and convert it to the specified encoding format even you don't know what the file's encoding is. If you want to know more about `chardet`, you can checkout the `uchardet`.  

## How to use the `piconv` tool
The `piconv` tool provides an easy way to convert the file's encoding, you just need to input `'file_name'` and `'to_encoding'` params to realizing the convertion process.

Run the ***piconv.py*** script as following:
```
python piconv.py filename/dirname to_encoding
```

## Why piconv?

When you encounter some garbled characters problem, you must want to convert it to the correct encoding, linux provides `iconv` command to convert file between different character encodings. The from-encoding and to-encoding params must be specified and even though it may still generate some garbled characters like **'?? ¨ª¡¤2?¡¤¡§'**. 

***If you know the file's correct encoding(includes from and to encodings), just ignore what I descibe  below***. But when you don't get the file's right encoding or you don't even know the file's encoding, you can't convert the file correctly. 

I develop `piconv` tool to solve the encoding problem and simplify this convertion process of many files in the input directory. When you use the `piconv ` tool, you just need to input the 'file/dir' and 'to-encoding' param to realize the right convertion. For more usage detail, just checkout the **How to use `piconv` section**.

At first, I will show you some test cases about some garbled characters problem during using `iconv` command. Then I will compare the usage beetween  `iconv` and `piconv`.

### `iconv` garbled characters problem

The encoding format of **data-set/chinese-ansi.txt** is *GBK*, but you will get *ISO-8859* when use the `file` command, then the format will be wrong. So if you don't know the right encoding of the file and use the *ISO-8859-1* encoding, the convertion will be wrong and cause some encoding problems.  
```
file data-set/chinese-ansi.txt #ISO-8859
iconv -f iso-8859-1 -t utf-8 data-set/chinese-ansi.txt > chinese-ansi.txt # garbled character-ÂÒÂë

Or

iconv -f GBK -t utf-8 data-set/chinese-ansi.txt > chinese-ansi.txt # correctly

```

The input file **data-set/assoc.c** contains chinese characters **"Í·²å·¨"** and is *utf-8* encoding format. The source content is:
```
    // Í·²å·¨
    return 1;
}
```
* **convert utf-8 to gbk**

```
iconv -f utf-8 -t gbk data-set/assoc.c > utf8-gbk.c
#piconv -f utf-8 -t gbk data-set/assoc.c > utf8-gbk-p.c
```
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
(**terminated by the unicode error**)
```
    // å¤´æ’æ³
```
Then we use **`iconv -c`** option to omit invalid characters from output.
```
iconv -c -s -f gbk -t utf-8 data-set/assoc.c > gbk-utf8-c.c
```
```
    // å¤´æ’æ³
    return 1;
}
```

* **utf8 to utf8 & gbk to gbk**
```
iconv -c -s -f utf-8 -t utf-8 data-set/assoc.c > utf8-utf8.c

iconv -c -s -f gbk -t gbk data-set/assoc.c > gbk-gbk.c
```
```
     // Í·²å·¨
    return 1;
}
  
    // ?¡è¡ä?<8f><92>?3
    return 1;
}

```
You can also test other convertion cases. 

### Usage comparision between `piconv` and `iconv` 

* **Use `iconv` to convert input file and directory**
    use the `exec`  or `bash` to iterator directories
```
iconv -c -s -f gbk -t utf-8 data-set/assoc.c > gbk-utf8-c.c

find iconv-test/ -name gbk-gbk.c -exec iconv -c -f gbk 
-t utf-8 "{}" -o "{}" \;
find iconv-test/ -name gbk-gbk.c -type f | (while read file; do  iconv -c -f gbk -t utf-8 "$file" >"${file%.txt}-utf8.txt"; done);
```
* **How we do through `piconv` tool**
```
FIconv('Filename',to-encoding)
#FIconv('french-mscs.txt','utf-8')

DIconv('Dirname',to-encoding).codecs_iconv_iterator()
#diconv = DIconv('/var/www/piconv/test','utf-8')
#diconv.codecs_iconv_iterator()
```

## Supports Encodings
As using `chardet` to detect the file's encoding, `piconv` supports the follow encodings:
> * ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
> * Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified Chinese)
> * EUC-JP, SHIFT_JIS, ISO-2022-JP (Japanese)
> * EUC-KR, ISO-2022-KR (Korean)
> * KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
> * ISO-8859-2, windows-1250 (Hungarian)
> * ISO-8859-5, windows-1251 (Bulgarian)
> * windows-1252 (English)
> *ISO-8859-7, windows-1253 (Greek)
> * ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
> * TIS-620 (Thai)

## Functions & Advantages
The `piconv` includes following functions and advantages:
> * auto-detect files' encoding
> * encoding exception handler
> * simplify the convertion of `iconv` and easy to use

**todo**
> * regex match convertion
> * compress the dirname and improve the iteration speed

## References
* [chardet](https://github.com/chardet/chardet)
* [mozilla chardet](http://lxr.mozilla.org/seamonkey/source/extensions/universalchardet/)