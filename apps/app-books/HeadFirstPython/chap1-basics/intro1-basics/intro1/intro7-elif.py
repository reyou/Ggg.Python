import time
today = time.strftime("%A")

print("today: ", today)

if today == "Saturday":
    print("Take some rest..")
elif today == "Sunday":
    print("Get Ready!")
else:
    print("Working working..")


