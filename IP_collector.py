### IP_collector_0.1 ###
# Simple IP filtering tool for my personal programming and regex practice

# Import libraries
import re
import sys

# Open target file
source_file = open("<PROVIDE_FILE_PATH>")

# Load target file output to variable
data_loaded = source_file.read()

# Change target file type to string 
data_loaded_stringed = str(data_loaded)

# Regex for matching all IP addresses
data_loaded_stringed_parsed = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", data_loaded_stringed)

# Print output after regex was applied
print(data_loaded_stringed_parsed)

# Close file and terminate program
source_file.close
sys.exit()
