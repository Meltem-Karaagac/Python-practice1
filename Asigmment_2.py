cigaretteAdd = input("Do you addict to Cigarette?").lower()
Old = input("Are you older than 75?").lower()
Chronic = input("Do you have cronical illness:?").lower()
weakImmune = input("Do you have week immunity?").lower()
if ((cigaretteAdd == "yes" and Old == "yes") or weakImmune == "yes" or Chronic == "yes" or Chronic == "y"):
    print("You are in risky group")
else:
    print("You are not in risky group")
