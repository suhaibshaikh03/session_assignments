Prompt : str = "What do you want\n"

def joke():
    user_input : str = input(Prompt)
    joke : str =" Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
    if user_input.lower() == "joke":
        print(joke)
    else:
        print("Sorry I only tell jokes")

joke()