#!/usr/bin/env python3

import subprocess

# Remove old files
subprocess.call("./remove_old_data_files.py", shell=True)

# Load single files
subprocess.call("./single_level_data_manager.py", shell=True)

# Load multilevel files
subprocess.call("./multi_level_data_manager.py", shell=True)
diff --git a/multi_level_data_manager.py b/multi_level_data_manager.py
