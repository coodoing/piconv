#-*-coding=utf-8-*-
import sys,os
import codecs
try:
    import chardet
except ImportError:
    _have_chardet = True
else:
    _have_chardet = False

class CodecsDetect(object):
	pass

class Iconv(object):
	'''
		The class just act as the linux iconv command.
		Because of that linux doesn't support ansi(mscs) encoding, so we consider the ascii encdoing as 
		the default from_encode param, so as the utf-8 to to_encode param.

		There is a familiar tool as node-iconv and uchardet.
	'''	
	def  __init__(self,from_encode='ascii',to_encode='utf-8'):
		self.from_encode = from_encode
		self.to_encode = to_encode
		self.from_file = ''
		self.to_file = ''
		self._to_string()
	
	def _to_string(self):
		print('***iconv output***')

	pass

class FIconv(Iconv):
	detect_dict = {}
	def __init__(self,to_encoding='utf-8',from_file='',to_file=''):
		"""	
			To iconv the file, you just need to pass the to_encoding and from_files params
		"""
		super()		
		self.from_file = from_file
		if to_file == '':
			self.to_file = 'iconv_'+from_file
		else:
			self.to_file = to_file
		self.to_encoding = to_encoding
		if _have_chardet:
			self.from_encoding = 'utf-8'
		else:
			self.from_encoding = self._detect_file_encoding(self.from_file)
                
		print("Before iconv encoding:"+self.from_encoding+"")
		self._codecs_iconv_binary()
		print("After iconv encoding:"+self._detect_file_encoding(self.to_file))
	
	def _detect_file_encoding(self,filename):
		"""
			pre-processing the file encoding 
		"""
		print('The processing file is:'+filename)
		from os import path
		b = path.isfile(filename)
		if b:
			with open(filename,'rb+') as file:
				data = file.read()
				self.detect_dict = chardet.detect(data)
				#print(self.detect_dict)
				return self.detect_dict['encoding']
		pass

	def _codecs_iconv(self):
		b = os.path.isfile(self.from_file)
		line_list = []
		if b:
			with open(self.from_file,'r',encoding = 'gbk') as file:
				for line in file:
					print(line)
					line_list.append(line)

			with open(self.to_file,'w',encoding = self.to_encoding) as file:
				for i in range(len(line_list)):
					str_line = line_list[i]
					file.write(str_line)#.encode('utf-8'))	
		pass

	def _codecs_iconv_binary(self):
		b = os.path.isfile(self.from_file)
		line_list = []
		if b:
			with open(self.from_file,'rb') as file:
				#print(file.read()) #this will flush all data of the file
				for line in file:
					#print(line.decode(self.from_encoding))
					line_list.append(line)

			with open(self.to_file,'wb') as file:
				for i in range(len(line_list)):
					str_line = line_list[i].decode('gbk').encode(self.to_encoding)#.decode(self.from_encoding).encode(self.from_encoding)
					file.write(str_line)#.encode('utf-8'))	
		pass

class DIconv(Iconv):

	pass

def main():	
	print('########################')
	print('chardet')
	#chardet_func()
	#iconv = Iconv()
	ficonv = FIconv('utf-8','french-mscs.txt')
	#ficonv = FIconv('utf-8','ansi-to-utf8.txt')
	#ficonv = FIconv('utf-8','utf8-to-ansi.txt')
	#ficonv = FIconv('ascii','utf8-to-ansi-test.txt')
	pass

if __name__ == '__main__':
	main()
