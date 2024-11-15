# Milestone 1 : Get User Weight
mars_constant : float = 0.378
def get_mars_weight():
    user_weight : float = float(input("Enter a weight on Earth?\n"))
# Find user weight on mars
    mars_weight : float = round(user_weight * mars_constant, 2) 
    return mars_weight

answer : float = get_mars_weight()
print(f"Your weight on mars is {answer}")


# Milestone 2 : Adding in all planets
