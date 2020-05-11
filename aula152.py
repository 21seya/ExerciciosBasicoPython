def print_header(str):     
    print ("+++%s+++" % str)   
print_header.category = 1 
print_header.text = "some info"   
print_header("%d %s" %  (print_header.category, print_header.text))