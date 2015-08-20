# This python script just executes its command-line.
# Used as a trampoline for kodi to execute an external command.
import subprocess
import sys

subprocess.call(sys.argv[1:])
