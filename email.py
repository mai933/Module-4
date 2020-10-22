"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""


addresses = []

more = input("Do you have an email address to enter (y/n)? ") 
asks for email address

while more == "y": if you have one then 
    email = input("Enter the address: ") asks for email 
    addresses.append(email)
    more = input("Do you have another address(y/n)? ") asks for another email
    while more != "y": if you hit yes then it will ask you for more 
        if more == "n":if u select not
            break then it will break and ask please enter  yes or no
        else:
            more = input("Please enter a y or n: ") will ask please enter yes or no
    
print(addresses)  
prints addresses 
