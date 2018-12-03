class GenderInfo:
    pronouns = []
    label = ""
    honorific = ""
    name = ""
    def __init__(self, label, honorific, name, pronouns):
        self.name = name
        self.pronouns = pronouns
        self.label = label
        self.honorific = honorific

def detect_gender():
    print("Hi there! What's your name?")
    name = input()
    print("\nNice to meet you, " + name + ". Please enter your gender. (Any string of characters allowed, even empty string.)")
    label = input()
    print("\nPlease enter a title (Mr, Ms, Mx, etc.)")
    honorific = input()
    print("\nFinally, please enter your pronouns. (Format: 'she/her, he/him' in order of preference.)")
    print("Please leave an empty string if you would prefer not to have pronouns used to refer to you.")
    pronouns = input().split(",")
    return GenderInfo(label, honorific, name, pronouns)

gender = detect_gender()

print("\nYour gender profile:\n")
print("(" + gender.honorific + ") " + gender.name + "\n")
print("Gender: " + gender.label)
print("Pronouns:")
for pronoun in gender.pronouns:
    print(pronoun)
