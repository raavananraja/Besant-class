import datetime
print("This is my home")

print("Now Puzzle time")
date = datetime.date.today()
year = date.strftime("%Y")
age=int(input("What year were you born?"))
year = int(year)
old = year-age
print(old)
print(year)
print(f"In the year {year} you'll be {old} years old!")
