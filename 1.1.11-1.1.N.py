#!/usr/bin/env python3
import os
import re
import subprocess
import sys

#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv)

for thisArg in sys.argv:
    if thisArg != sys.argv[0]:
        print(thisArg)
        if re.match("^/", thisArg):
            target_dir = thisArg
        else:
            print("No leading \"/\" ... assuming relative path to Current Working Directory")
            cwd = os.getcwd()
            target_dir = cwd + "/" + thisArg

        print(target_dir)

        if os.path.isdir(target_dir):
            print("Directory \"" + target_dir + "\" exists")
        else:
            print("Directory \"" + target_dir + "\" does not exist")

            


#target_dir = "/home"
#
## Rule 1.1.9
#rule = "1.1.9"
#attribute = "partition"
#print("    " + rule + " - Create Separate " + attribute + " for " + target_dir + " [Scored]")
#command = "df " + target_dir + " 2> /dev/null | awk '{print $NF}' | egrep -c \"^" + target_dir + "$\""
#commandOutput = subprocess.getoutput(command)
#if commandOutput == "0":
#    status = "FAILED"
#    disposition = "is not"
#else:
#    status = "PASSED"
#    disposition = "is"
#print("        " + status + ": \"" + target_dir + "\" " + disposition + " a separate " + attribute + "\n")
#
## Rule 1.1.10
#rule = "1.1.10"
#attribute = "nodev"
#print("    " + rule + " - Set " + attribute + " option for " + target_dir + " Partition [Scored]")
#command = "egrep \"" + target_dir + "\" /proc/mounts 2> /dev/null | egrep -c \"" + attribute + "\""
#commandOutput = subprocess.getoutput(command)
#if commandOutput == "0":
#    status = "FAILED"
#    disposition = "is not set"
#else:
#    status = "PASSED"
#    disposition = "is set"
#print("        " + status + ": \"" + attribute + "\" " + disposition + " for \"" + target_dir + "\"" + "\n")
