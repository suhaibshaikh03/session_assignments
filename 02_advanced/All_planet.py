Mercury : float = 0.376
Venus : float = 0.889
Mars : float = 0.378
Jupiter : float = 2.36
Saturn : float = 1.081
Uranus : float = 0.815
Neptune : float = 1.14

def planet_weight_calculator():
    while True:
        try:
            user_weight : float = float(input("Enter a weight on Earth?\n"))
            break;
        except ValueError:
            print("invalid input ! Weight must be in float or string")
            
    planet_name : str = input("What is your planet name?\n")
    gravity_constant : float = 0
    if planet_name.lower() == "mars":
        gravity_constant = Mars
    elif planet_name.lower() == "mercury":
        gravity_constant = Mercury
    elif planet_name.lower() == "venus":
        gravity_constant = Venus
    elif planet_name.lower() == "jupiter":
        gravity_constant = Jupiter
    elif planet_name.lower() == "saturn":
        gravity_constant = Saturn
    elif planet_name.lower() == "uranus":
        gravity_constant = Uranus
    elif planet_name.lower() == "neptune":
        gravity_constant = Neptune
    else:
        print("Enter a valid planet name")
        exit()
    weight_on_planet = round(user_weight * gravity_constant , 2)
    print(f"Your weight on planet {planet_name} is {weight_on_planet}")    

planet_weight_calculator()