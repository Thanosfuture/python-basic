indian=["chapati","rice","samosa"]
italy =["pasta","pizza","garlic bread"]
arab=["biryani","mutton","grill chicken"]

dish= input("enter a dish name")

if dish in indian:
    print("indian")
elif dish in italy:
    print("italy")
elif dish in indian:
    print("arab")
else:
    print("sorry we dnt have")