#!/usr/bin/env python

import os, sys, utils, shutil
import optparse

#  Create dictionary that describes:
#
#  - layout of directories
#  - index files to be created
#  - subdirectories (tests/tutorials) to be copied
#

#
# Verificaiton Tests
#
verification={}
verification['index']={'index_title':'Verification Testing',
                       'index_file':'ats-testsuite-doc/doc/verification/index.rst',
                       'index_list':['1D'],
}

verification['1D']={'index_entry': '1D/index.rst',
                                 'index' : 
                                 {'index_title' : '1D Column',
                                  'index_file' : 'ats-testsuite-doc/doc/verification/index.rst',
                                  'index_list' : ['1D'], 
                                  },
                                 '1D':
                                     {'from_dir' : 'ats-testsuite-doc/testing/test0',
                                      'dest_dir' : 'ats-testsuite-doc/doc/verification/test0',
                                      'index_entry' : 'test0/test0.rst'
                                      },
                                 }

# =========================================================================================================================
#
#  Create parser and options
#
#p = optparse.OptionParser()
#p.add_option('--full-guide', help='Build the full User Guide', default=False, dest='full_guide', action='store_true')
#p.add_option('--mycase', help='Build the "mycase" test', default=False, dest='mycase', action='store_true')
#p.add_option('--verification', default=False, dest='verification', action='store_true')

#(opts,args) = p.parse_args()

#
#  Create dictionary for sections
#
sections={}
sections['verification'] = verification

#
#  Table of Contents (Top Level)
#
toc_user_guide = {'index_list' : [ 'verification' ],
                  'verification'   : { 'index_entry' : 'verification/index.rst' },
            }

#if ( opts.verification or opts.full_guide ):
#    toc_user_guide['index_list'].append('verification')
#    toc_user_guide['1D'] = { 'index_entry' : 'verification/index.rst' }
#    sections['verification'] = verification

# =========================================================================================================================

# Set the logfile
logfile=sys.stdout

# Set Amanzi source directory
amanzi_home=utils.AmanziHome(logfile)

# Set level counter
level=1

# Copy top-level base index file
shutil.copyfile('index.in','index.rst')

# Create index files
utils.RecurseIndex(amanzi_home,sections,level,logfile)

# Copy content 
utils.RecurseCopy(amanzi_home,sections,level,logfile)

# Fix top-level index 

index_entries = [ ]
for e in toc_user_guide['index_list']:
    index_entries.append(toc_user_guide[e]['index_entry'])
utils.IndexInsert('index.rst',index_entries)

# Fix paths on plot directives
utils.WalkRstFiles(amanzi_home,sections,logfile)

