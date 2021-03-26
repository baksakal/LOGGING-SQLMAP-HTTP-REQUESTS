#Before starting create an empty file named "a.txt"

#read from "g_data.txt"
with open("g_data.txt") as f:
    for line in f:
        if not line.isspace():
            with open('final.txt', 'a') as the_file:
                the_file.write(line)
#write to "a.txt"
with open("final.txt") as myfile:
    head = [next(myfile) for x in range(9)]
    line = myfile.readline()
head = head[:-1]

        
