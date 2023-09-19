pennies = input("How many pennies do you have? ")

if pennies.isdigit() == True:
    pass
else:
    quit()

pennies = int(pennies)

dollars = pennies // 100

change1 = pennies % 100

qaurters = change1 // 25

change2 = change1 % 25

dimes = change2 // 10

change3 = change2 % 10

nickels = change3 // 5

change4 = change3 % 5

pennies_left = change4

print(f"{int(pennies)} pennies will output:")
print(f"dollars = {int(dollars)}")
print(f"quarters = {int(qaurters)}")
print(f"dimes = {int(dimes)}")
print(f"nickels = {int(nickels)}")
print(f"pennies = {int(pennies_left)}")