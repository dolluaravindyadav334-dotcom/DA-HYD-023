'''#Task: Ask the user to enter a sentence. Display the same sentence in several different letter cases.
# 1. Get user input
user_text = input("Enter a sentence: ")

# 2. Store case-conversion labels and method references in a collection
conversion_methods = [
    ("Upper", str.upper),
    ("Lower", str.lower),
    ("Title", str.title),
    ("Capitalized", str.capitalize),
    ("Swap case", str.swapcase),
    ("Casefold", str.casefold),
]

# Display converted cases using a loop
print("\n--- Converted Cases ---")
for label, method in conversion_methods:
    print(f"{label:<11} : {method(user_text)}")

# 3. Use conditions to describe the original text
print("\n--- Text Description ---")
if user_text.isupper():
    print("The original text is completely UPPERCASE.")
elif user_text.islower():
    print("The original text is comple lowercase.")
elif user_text.istitle():
    print("The original text is in Title Case.")
else:
    print("The original text contains a mix of uppercase and lowercase letters.")

'''

#Task: Repeatedly ask the user for a username and report which validation rules it passes. Stop when the user enters quit.

while True:
    username = input("Enter username (or 'quit' to exit): ")
    if username.lower() == "quit":
        break
    if not username:
        print("Please enter a non-empty username.\n")
        continue
    if username.isidentifier():
        print("Valid Python identifier")
    else:
        print("Not a valid Python identifier")
    if username.isascii():
        print("Contains only ASCII characters")
    else:
        print("Does not contain only ASCII characters")
    if username[0].isalpha():
        print("Begins with a letter")
    else:
        print("Does not begin with a letter")
    if username.isalnum():
        print("Contains only letters and numbers")
    else:
        print("Does not contain only letters and numbers")


        
