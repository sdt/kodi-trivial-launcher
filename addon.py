# This python script just executes its command-line.
# Used as a trampoline for kodi to execute an external command.
import os
import sys

os.execv(sys.argv[1], sys.argv[1:])
