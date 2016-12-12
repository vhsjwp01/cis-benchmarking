#!/usr/bin/env python3
import subprocess

target_dir = "/tmp"

# Rule 1.1.1
rule = "1.1.1"
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

# Rule 1.1.2
rule = "1.1.2"
attribute = "nodev"
print("    " + rule + " - Set " + attribute + " option for " + target_dir + " Partition [Scored]")
command = "egrep \"" + target_dir + "\" /proc/mounts 2> /dev/null | egrep -c \"" + attribute + "\""
commandOutput = subprocess.getoutput(command)
if commandOutput == "0":
    status = "FAILED"
    disposition = "is not set"
else:
    status = "PASSED"
    disposition = "is set"
print("        " + status + ": \"" + attribute + "\" " + disposition + " for \"" + target_dir + "\"" + "\n")

# Rule 1.1.3
rule = "1.1.3"
attribute = "nosuid"
print("    " + rule + " - Set " + attribute + " option for " + target_dir + " Partition [Scored]")
command = "egrep \"" + target_dir + "\" /proc/mounts 2> /dev/null | egrep -c \"" + attribute + "\""
commandOutput = subprocess.getoutput(command)
if commandOutput == "0":
    status = "FAILED"
    disposition = "is not set"
else:
    status = "PASSED"
    disposition = "is set"
print("        " + status + ": \"" + attribute + "\" " + disposition + " for \"" + target_dir + "\"" + "\n")

# Rule 1.1.4
rule = "1.1.4"
attribute = "noexec"
print("    " + rule + " - Set " + attribute + " option for " + target_dir + " Partition [Scored]")
command = "egrep \"" + target_dir + "\" /proc/mounts 2> /dev/null | egrep -c \"" + attribute + "\""
commandOutput = subprocess.getoutput(command)
if commandOutput == "0":
    status = "FAILED"
    disposition = "is not set"
else:
    status = "PASSED"
    disposition = "is set"
print("        " + status + ": \"" + attribute + "\" " + disposition + " for \"" + target_dir + "\"" + "\n")
