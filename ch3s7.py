string = input()

length=len(string)
if length ==1:
    
    
    if string.isalpha()==False :
        
        if string.isdigit()==1:
            print("it's a number",int(string))
    if string.isspace()==True : 
        print("It's whitespace.")       
    if string.isalpha()==True :  
        print("It's a letter.") 




else: 
    print("It is more than 1 char so here is your string xd: ",string)