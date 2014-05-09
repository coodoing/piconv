#-*-coding=utf-8-*-

import sys
import icov_handler.py

class PIconvHandlerTool(object):
    """ 
    	Application behaviour for 'piconv' program 
    """
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
        	self.file_names = args[0]
        	self.encoding = args[1]
        	print('The 2 params are [file_name] = `%s`, [encoding] = `%s`' % (args[0],args[1]))
        elif len(args)==1 or len(args)>2:
        	print('You must input 2 params')
        	sys.exit()

    def run(self):
    	print('Start to iconv files......')
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