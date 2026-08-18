import time

print("SPEED TYPING TEST...")

sentance = "abcdefghijklmnopqrstuvwxyz"
print("\n Type this Exactly...")
print(sentance)

input("\n Press enter to start...")

start = time.time()

typed = input("\n START TYPING !!\n")
end = time.time()

time_taken = round(end-start,2)
speed = round(len(sentance)/time_taken,2)

print("Time taken: ",time_taken,"Seconds")
print("Typing Speed",speed,"letters/sec")