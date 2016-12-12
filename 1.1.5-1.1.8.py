#!/usr/bin/env python3
import subprocess

target_dir = "/var"

# Rule 1.1.5
rule = "1.1.5"
attribute = "partition"
print("    " + rule + " - Create Separate " + attribute + " for " + target_dir + " [Scored]")
command = "df " + target_dir + " 2> /dev/null | awk '{print $NF}' | egrep -c \"^" + target_dir + "$\""
commandOutput = subprocess.getoutput(command)
if commandOutput == "0":
    status = "FAILED"
    disposition = "is not"
else: 
    status = "PASSED"
    disposition = "is"
print("        " + status + ": \"" + target_dir + "\" " + disposition + " a separate " + attribute + "\n")

# Rule 1.1.6
rule = "1.1.6"
source_dir = "/var/tmp"
target_dir = "/tmp"
attribute = "bind mounted"
print("    " + rule + " - Bind mount the " + source_dir + " directory to " + target_dir + " [Scored]")
command = "mount | egrep \"^" + target_dir + "[[:space:]]\" | egrep -c \"[[:space:]]" + source_dir + "[[:space:]]\""
commandOutput = subprocess.getoutput(command)
if commandOutput == "0":
    status = "FAILED"
    disposition = "is not"
else:
    status = "PASSED"
    disposition = "is"
print("        " + status + ": \"" + source_dir + "\" " + disposition + " " + attribute + " to \"" + target_dir + "\"" + "\n")

# Rule 1.1.7
rule = "1.1.7"
target_dir = "/var/log"
attribute = "partition"
print("    " + rule + " - Create Separate " + attribute + " for " + target_dir + " [Scored]")
command = "df " + target_dir + " 2> /dev/null | awk '{print $NF}' | egrep -c \"^" + target_dir + "$\""
commandOutput = subprocess.getoutput(command)
if commandOutput == "0":
    status = "FAILED"
    disposition = "is not"
else:
    status = "PASSED"
    disposition = "is"
print("        " + status + ": \"" + target_dir + "\" " + disposition + " a separate " + attribute + "\n")

# Rule 1.1.8
rule = "1.1.8"
target_dir = "/var/log/audit"
attribute = "partition"
print("    " + rule + " - Create Separate " + attribute + " for " + target_dir + " [Scored]")
command = "df " + target_dir + " 2> /dev/null | awk '{print $NF}' | egrep -c \"^" + target_dir + "$\""
commandOutput = subprocess.getoutput(command)
if commandOutput == "0":
    status = "FAILED"
    disposition = "is not"
else:
    status = "PASSED"
    disposition = "is"
print("        " + status + ": \"" + target_dir + "\" " + disposition + " a separate " + attribute + "\n")
