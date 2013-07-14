#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Без имени.py
#  
#  Copyright 2013 Strannik-j <mail@strannik-j.org>
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the Strannik Foundation nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#  * All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#  
#     This product includes software developed by a Strannik-j
#     and his contributors.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#import getpass
#import itertools
#import logging
#import os
#import sys
#import urllib
#from yafotki.utils import OptionParser, Option
#from optparse import OptionGroup, IndentedHelpFormatter, SUPPRESS_USAGE
#from functools import wraps
from yaploader import *

#import yafotki

pwd = os.getcwd()
#CONFIG_PATH = os.path.join(pwd, '.fotki/fotki.conf')
#TOKEN_CACHE = os.path.join(pwd, '.fotki/fotki.token')
#print TOKEN_CACHE
#_username = 'strannik-jb'
#CONFIG_PATH = os.path.expanduser('~/.fotki.conf')
#TOKEN_CACHE = os.path.expanduser('~/.fotki.token')


def main():
    
    config = Config()
    
    usage = 'usage: %prog command [options] [args]'
    option_list = [
        Option('-h', '--help', dest='help', action='store_true',
                help='Print help and exit.', default=False),
        Option('-v', '--verbose', dest='verbose', action='store_true',
                help='Output more information.', default=False),
        Option('-q', '--quiet', dest='quiet', action='store_true',
                help='Output less information.', default=False),
        Option('-V', '--version', dest='version', action='store_true',
                help='Show version number and quit.', default=False),
    ]

    uploader = Uploader()

    commands = dict(
        (command.name, command()) \
        for key, command in globals().iteritems() \
            if key.startswith('Command'))
    #for i in commands:
        #print i, " : ", commands[i]

    #sys.exit()
    #args = sys.argv

    #if len(args) > 1:
        #command_name = args.pop(1)
    #else:
        #command_name = None
    #command_name = None
    #command = commands.get(command_name, None)
    #if command:
        #option_list.extend(command.option_list)
        #usage = getattr(command, 'usage', usage)

    #parser = OptionParser(
        #option_list=option_list,
        #usage=usage,
        #add_help_option=False,
    #)

    #def print_help():
        #parser.print_help()
        #if command is None:
            #print '\nCommands:'
            #for cmd in commands.values():
                #print '%16s %s' % (cmd.name, getattr(cmd, 'description', ''))

    #opts, args = parser.parse_args(args)

    #if opts.version:
        #print 'Python uploader for http://fotki.yandex.ru, version %s.' % yafotki.__version__
        #print 'For more information and new versions, visit http://svetlyak.ru.'
        #sys.exit(0)

    #if opts.help or command is None:
        #print_help()
        #sys.exit(1)

    #if opts.verbose:
        #logging.basicConfig(level = logging.DEBUG, format = '%(message)s')
    #elif opts.quiet:
        #logging.basicConfig(level = logging.ERROR, format = '%(message)s')
    #else:
        #logging.basicConfig(level = logging.WARNING, format = '%(message)s')

    config = Config()
    #config.update(opts)
    #logging.debug('Config values %r' % config)

    #command.run(uploader, opts, args)
    
    if not os.path.exists(TOKEN_CACHE):
        command = commands.get('auth', "str")
        #command.run(uploader, 'auth', None)
    #command.run(uploader, 'albums', None)
    command = commands.get('albums', None)
    
    command.run(uploader, 'albums', None)
    _albums = command.user.albums
    print _albums
    
    return 0

if __name__ == "__main__":
    main()
    sys.exit(0)

