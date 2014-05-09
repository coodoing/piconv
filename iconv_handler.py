#-*-coding=utf-8-*-
import sys,os
import codecs,locale
import types,re
try:
    import chardet
except ImportError:
    _have_chardet = True
else:
    _have_chardet = False

"""
    ignore_encode_error uses for encoding ignore
"""
ignore_encode_error = False

class CodecsDetect(object):    
	pass

class Iconv(object):
	'''
		The class just act as the linux iconv command.
		Because of that linux doesn't support ansi(mscs) encoding, so we consider the ascii encdoing as 
		the default from_encode param, so as the utf-8 to to_encode param.

		There is a familiar tool as node-iconv and uchardet.
	'''	
	def  __init__(self,from_encode='',to_encode=''):
		self.from_encode = from_encode
		self.to_encode = to_encode
		self.from_file = ''
		self.to_file = ''		

class FIconv(Iconv):
	detect_dict = {}
	def __init__(self,from_file='',to_encoding='utf-8',to_file=''):
		"""	
			To iconv the file, you just need to pass the to_encoding and from_files params
		"""
		#super()		
		self.from_file = from_file
		if to_file == '':
			dirpath = os.path.dirname(from_file)
			filename = os.path.basename(from_file)
			self.to_file = dirpath+'\\iconv_'+filename
		else:
			self.to_file = to_file
		self.to_encoding = to_encoding
		if _have_chardet:
			self.from_encoding = locale.getpreferredencoding()
		else:
			self.from_encoding = self.detect_file_encoding(self.from_file)
                
		print("Before iconv encoding:"+self.from_encoding+"")
		self.codecs_iconv_binary()
		print("After iconv encoding:"+self.detect_file_encoding(self.to_file))
	
	def detect_file_encoding(self,filename):
		"""
			pre-processing the file encoding 
		"""
		print('The processing file is:'+filename)
		from os import path
		b = path.isfile(filename)
		if b:
			with open(filename,'rb+') as file:
				data = file.read()
				try:
					if self.file_empty(filename):
						return locale.getpreferredencoding()
					else:
						self.detect_dict = chardet.detect(data)
						#print(self.detect_dict)
						return self.detect_dict['encoding']
				except:
					print("TypeError: cannot concatenate 'str' and 'NoneType' objects")
	
	def file_empty(self,filename):
		file_size = os.stat(filename).st_size
		if file_size == 0:
			return True
		else:
			return False

	def codecs_iconv(self):
		b = os.path.isfile(self.from_file)
		line_list = []
		if b:
			with open(self.from_file,'r',encoding = 'gbk') as file:
				for line in file:
					line_list.append(line)

			with open(self.to_file,'w',encoding = self.to_encoding) as file:
				for i in range(len(line_list)):
					str_line = line_list[i]
					file.write(str_line)#.encode('utf-8'))	
		pass

	def codecs_iconv_binary(self):
		b = os.path.isfile(self.from_file)
		line_list = []
		if b:
			with open(self.from_file,'rb') as file:
				#print(file.read()) #read() will flush all data of the file
				for line in file:
					line_list.append(line)

			with open(self.to_file,'wb') as file:
				for i in range(len(line_list)):
					try:
						str_line = line_list[i].decode(self.from_encoding).encode(self.to_encoding)
					except:
						str_line = line_list[i]#.decode(self.from_encoding).encode(self.from_encoding)
					file.write(str_line)			

class DIconv(Iconv):
	def __init__(self,root_path,to_encoding='utf-8'):
		self.root = root_path
		self.new_root = root_path+'_iconv'
		self.to_encoding = to_encoding

	def dir_cas(self,dirpath):
		if os.path.exists(dirpath) is not True:
			os.mkdir(dirpath)

	def get_new_root_path(self,filepath):
		#filepath = os.path.dirname(filepath)
		#filename = os.path.basename(filepath)	

		#list insert and remove
		#filepath = filepath.split('\\')[0:]		
		#print(filepath)#type(filepath)
		#filepath.insert(0,self.new_root)#print(filepath)
		#new_path = '\\'.join(filepath)	

		new_path = filepath.replace(self.root,self.new_root)
		#print(new_path)
		return new_path

			
	def codecs_iconv(self,filepath):		
		print('source filepath:' + filepath)
		new_filepath = self.get_new_root_path(filepath)
		print('dest filepath:' + new_filepath)
		dirpath = os.path.dirname(new_filepath)
		filename = os.path.basename(new_filepath)
		self.dir_cas(dirpath)		
		ficonv = FIconv(filepath,self.to_encoding,new_filepath)
		pass

	def codecs_iconv_iterator(self):
		self.dir_cas(self.root+'_iconv')
		list_dirs = os.walk(self.root)
		for root,dirs,files in list_dirs:
			for f in files:
				if root == self.root:			
					pass
				filepath = os.path.join(root,f)				
				self.codecs_iconv(filepath)
			#for d in dirs:
			#	print(os.path.join(d))
		pass
	pass

def main():	
	print(ignore_encode_error)	
	regex = re.search(r'new\\test','new\\test\\123\\456\\new\\test')
	print(regex.group())
	src = 'new\\test\\123\\456\\new\\test'
	sub = 'new\\test'
	idx = src.index(sub)
	print(src.replace(sub,sub+'_conv'))

	print('########################')
	print('File chardet ')
	#ficonv = FIconv('french-mscs.txt','utf-8')
	#ficonv = FIconv('ansi-to-utf8.txt','utf-8')
	#ficonv = FIconv('utf8-to-ansi.txt','utf-8')
	##ficonv = FIconv('utf8-to-ansi.txt','ascii',)
	print('########################')
	print('Dir chardet')	
	diconv = DIconv('D:\\book\\decode-memcached-master\\memcached-1.4.15','utf-8')#DIconv('D:\\book\\decode-memcached-master\\memcached-1.4.15')#
	diconv.codecs_iconv_iterator()
	pass

if __name__ == '__main__':
	main()