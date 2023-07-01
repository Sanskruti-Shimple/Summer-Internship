#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess

# Run the command and capture its output
command_output = subprocess.check_output(['command', 'arg1', 'arg2'])

# Decode the output if it's in bytes
output_string = command_output.decode('utf-8')

# Print or use the output as needed
print(output_string)

