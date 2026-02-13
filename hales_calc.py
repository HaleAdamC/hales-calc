import math

def calculate_gpp(t, r):
    c = (t - 32) * 5/9
    svp = 6.112 * math.exp((17.67 * c) / (c + 243.5))
    vp = svp * (r / 100)
    return (4354 * vp) / (1013.25 - vp)

print("---------------------------------------")
print("  Hale's Pro Drying Calculator 2.0     ")
print("---------------------------------------")

active = True

while active:
    room = input("\nWhich room/area is this? (e.g. Basement): ")
    temp = float(input("Enter Temp (F): "))
    rh = float(input("Enter RH (%): "))

    gpp = calculate_gpp(temp, rh)
    
    print(f"\n--- {room} Results ---")
    print("GPP: " + str(round(gpp, 1)))
    
    # Simple advice based on GPP
    if gpp < 55:
        print("Status: Drying well!")
    else:
        print("Status: Still wet. Check equipment.")

    again = input("\nAdd another room? (yes/no): ")
    if again.lower() != "yes":
        active = False
        print("\nGood luck on the job site, Adam! Closing app...")
