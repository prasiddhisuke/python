d={'akanksha':1,'tanuja':5,'amruta':3}
print("the given Dictionary:",d)
check_key=input("enter key to check:")
check_value=input("enter value to check:")
if check_key in d:
    print(check_key,"is present" in d.pop(check_key))
    d[check-key]=check_value
else:
    print(check_key," is not present.")
    d[check_key]=check_value
    print("updateddictionary:",d)    