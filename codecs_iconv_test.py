#-*-utf-8-*-
import sys,os
import codecs,locale
try:
    import chardet
except ImportError:
    _have_chardet = True
else:
    _have_chardet = False

def codecs_iconv_binary(filename):
	"""
		iconv the specified file use the binary way
	"""
	print('filename='+filename)	
	b = os.path.isfile(filename)
	line_list = []
	if b:
		with open(filename,'rb') as file:
			for line in file:
				line_list.append(line)

		with open('data-set\\assoc_tr.c','wb') as file:
			for i in range(len(line_list)):
				str_line = line_list[i]
				file.write(str_line)
	pass

def codecs_iconv(filename):
	"""
		iconv the codecs of the specified file and generate the new file
	"""
	print('filename='+filename)	
	b = os.path.isfile(filename)
	print(b)
	line_list = []
	if b:
		with open(filename,'r',encoding='utf-8') as file:
			for line in file:
				line_list.append(line)

		with open('data-set\\assoc_tr.c','w') as file:
			for i in range(len(line_list)):
				str_line = line_list[i]
				file.write(str_line)#.encode('utf-8'))
	pass

def get_file_encoding():
    """
        get the default file encoding of the given file
    """
    filename = 'data-set\\french-mscs.txt'
    data = codecs.open(filename,'r')
    print(data.read())
    print(data.encoding)
    filename = 'data-set\\french-utf8.txt'
    data = codecs.open(filename,'r')
    print(data.encoding)
    filename = 'data-set\\french-unicode.txt'
    data = codecs.open(filename,'r')
    print(data.encoding)  

def chardet_func():
	'''
		there are sth wrong with the ansi(mbcs) ENCODE format.
		to be specified, mbcs is an old way to represent multi byte character sets
		so in different country, it represent different encoding, and it can't be used in linux os

	'''
	data = open('data-set\\french-mscs.txt','rb+').readline()
	print(chardet.detect(data))
	data = open('data-set\\french-utf8.txt','rb+').readline()
	print(chardet.detect(data))
	data = open('data-set\\french-unicode.txt','rb+').readline()
	print(chardet.detect(data))
	data = open('data-set\\chinese-ansi.txt','rb+').read()
	print(chardet.detect(data))
	data = open('data-set\\english-ansi.txt','rb+').read()
	print(chardet.detect(data))
	data = open('data-set\\japanese-ansi.txt','rb+').read()
	print(chardet.detect(data))
	data = open('data-set\\assoc.c','rb+').read()
	print(chardet.detect(data))
	data = open('data-set\\assoc_tr.c','rb+').read()
	print(chardet.detect(data))

if __name__ == '__main__':
	print('file encoding: '+sys.getfilesystemencoding())
	print(locale.getpreferredencoding())
	fname = 'data-set\\assoc.c'
	codecs_iconv(fname)
	print('########################')
	print('chardet')
	chardet_func()
	print('########################')
	print('file encoding:')
	get_file_encoding()

	print(len('中国 re'))
	print('中国'.encode('gbk'))
	print('中国'.encode('utf-8').decode('utf-8'))
	print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8'))
	print(b'\xe4\xb8\xad'.decode('utf-8'))
