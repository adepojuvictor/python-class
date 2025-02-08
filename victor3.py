#if condition
#compare minimum marks to mark of the studentdef get_userpassword():

def get_userpassword():
    try:
        userpassword = int(input("Enter your password: "))  
        if userpassword == 12345:
            print("Access granted")  
        else:
            print("Access denied")  
    except ValueError:
        print("Invalid input. Please enter a numeric password.")  
        
get_userpassword()




