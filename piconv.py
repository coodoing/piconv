#-*-coding=utf-8-*-

import sys,os
import iconv_handler

class PIconvHandlerTool(object):
    """ 
        Application behaviour for 'piconv' program 
    """
    running = False
    def __init__(self, argv):
        """ Set up a new instance """
        self.parse_commandline(argv)        

    def parse_commandline(self, argv):
        """ 
            Parse command-line arguments 
        """
        from optparse import OptionParser
        usage = "usage: %prog [options] arg"        
        parser = OptionParser(usage)
        #parser.add_option("-f", "--file", dest="filename",help="read data from FILENAME")
        #parser.add_option("-v", "--verbose",action="store_true", dest="verbose")
        #parser.add_option("-q", "--quiet",action="store_false", dest="verbose")
        (options, args) = parser.parse_args(argv[1:])        
        if len(args)==2:            
            self.name = args[0]
            self.encoding = args[1]
            self.is_file = os.path.isfile(args[0])
            self.is_dir = os.path.isdir(args[0])
            if self.is_file or self.is_dir:
                self.running = True
            
            self.check_commandline(args)            

        elif len(args) ==1 or len(args)>2:
            print('You must input 2 params')
            sys.exit()

    def check_commandline(self,args):        
        from support_encodings import SupportEncodings
        supports = SupportEncodings().get_support_encodings()        
        encoding_illegal = str.upper(args[1]) in supports
        if encoding_illegal is False:
            print('The encoding format is illegal, please choose the encoding to convert below:')
            print("[ %s ]" % ','.join(supports))
            sys.exit()
        
        if not self.is_file and not self.is_dir:            
            print('path is illegal, input again')
            sys.exit()             

    def run(self):
        if self.running:
            print('Start to iconv files......')

            if self.is_file:
                from iconv_handler import FIconv
                print('[file_name] = `%s`, [encoding] = `%s`' % (self.name,self.encoding))                
                ficonv = FIconv(self.name,self.encoding)
                sys.exit()
            if self.is_dir:
                from iconv_handler import DIconv                
                print('[dir_path] = `%s`, [encoding] = `%s`' % (self.name,self.encoding))
                diconv = DIconv(self.name,self.encoding)
                diconv.codecs_iconv_iterator()
                sys.exit
        pass
    def help(self):
        print('Usage')
        pass

def main(argv=None):
    from sys import argv as sys_argv
    #print(argv)
    if argv is None:
        argv = sys_argv

    piconv = PIconvHandlerTool(argv)
    exitcode = None
    try:
        piconv.run()
    except SystemExit as e:
        exitcode = e.code
    return exitcode

if __name__ == '__main__':
    exitcode = main(argv=sys.argv)
    sys.exit(exitcode)
