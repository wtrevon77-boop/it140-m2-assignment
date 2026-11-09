This program is designed to be able to output a sentence that includes someone's name they input with the sentence also containing
what year they were born based off the current date and their age input



"""

# === Imports ===
import datetime

# === Constants ===

current_year = datetime.datetime.now().year

# === Main Function ===
import datetime
name = input("What is your name?")
age_input = input("How old are you?")
age = int(age_input)
current_year = datetime.datetime.now().year
birth_year = current_year - age
print(f"Hello {name}! You were born in {birth_year}.")

# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
zyBooks, a Wiley brand. (2026). It 140: Introduction to Scripting: ZyLabs source code.
zyBooks, a Wiley brand. (2026). Section 2.6. In IT 140: Introduction to Scripting. zyBooks.
