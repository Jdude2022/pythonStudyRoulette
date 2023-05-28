
# Impliment through command line
from src.roulette.data.PickASubject import PickASubject

user_input = input("Type Y to continue anything else to Quit ")

while user_input.upper() == "Y":
    print("Hello World")
    PickASubject.main()
    user_input = input("Type Y to continue ")
else:
    print("GoodBye")