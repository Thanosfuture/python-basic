chair_location = "room4"
rms= ("room1","room2","room3","room4")
for i in rms:
    if i == chair_location:
        print("Got it:",i)
        break
    else:
        print("not here", i)