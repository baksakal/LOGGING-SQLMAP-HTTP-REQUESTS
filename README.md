# LOGGING-SQLMAP-HTTP-REQUESTS

# 1) Sample SQL command to write the requests into a "txt" file, creates a "txt" file named "data.txt". Notice this command only sends GET requests.
# sqlmap -u http://127.0.0.1 -v 4 --risk=3 --level=5 --threads=10 > data.txt

# 2) Navigate to the location of "the data.txt" and run the following command, creates a "txt" file named "g_data.txt". Can be modified to grep other methods.
# grep -i -A 8 'GET /' data.txt > g_data.txt

# 3) Put "g_data.txt" into the same folder as "prep_script.py"

# 4) Create an empty "txt" file called "final.txt" inside the folder containing "g_data.txt" and "prep_script.py"

# 5) Run "prep_script.py"

# 6) To read the file into a Python environment, put "read_script.py" in the folder containing "final.txt" and run "read_script.py"
