#log parser for search term
search = "Authorization" #input("Please specify a search term:")
counter= 0

with open("keystone.common.wsgi","r") as log:
    for line in log:
        if search in line:
            counter += 1
            print(line)
            with open("failure.log", "a") as errorfile:
                errorfile.write(line + "\n")
            
print(counter)