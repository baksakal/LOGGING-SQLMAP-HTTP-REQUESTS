from itertools import islice

whole_file=[]

# Function to convert GeeksForGeeks.com   
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  


with open('final.txt') as file:
    while True:
        next_n_lines = list(islice(file, 10))
        next_n_lines = listToString(next_n_lines)       
        next_n_lines = next_n_lines.replace(" ", "")
        next_n_lines = next_n_lines.rstrip()
        whole_file.append(next_n_lines[:-2])
        if not next_n_lines:
            break
        # process next_n_lines

#remove the empty element
whole_file.pop()

