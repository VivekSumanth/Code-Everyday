
def distinct_string(string):
    
    string =''.join(sorted(string)) 
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    
    return True

print(distinct_string('helowrd'))
    

