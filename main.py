import random
import time

class Person:
    def __init__(self, name, age=0, energy=10, hobby=None):
        self.name = name
        self.age = age
        self.energy = energy
        self.hobby = hobby or random.choice(["Python", "gaming", "reading", "ham radio"])
    
    def live_10_year(self):
        self.age += 10
        self.energy -= random.randint(0, 5)  # living costs energy
        # print(f"{self.name} is now {self.age} years old and has {self.energy} energy.")
    
    def is_alive(self):
        return int(self.energy) > 0
    
    def have_child(self, child_name):
        # Child inherits hobby from parent
        return Person(child_name, 0, 10, self.hobby)

year = 0
count = 0

# Start with some people
people = [
    Person("Alice"),
    Person("Bob"),
    Person("Charlie"),
    Person("Madison Zamora"),
    Person("Quentin Lowery"),
    Person("Estelle Bullock"),
    Person("Ben Roberts"),
    Person("Paisley Cardenas"),
    Person("Johnathan Meyers"),
    Person("Leyla Henry"),
    Person("Carlos Evans"),
    Person("Eliana Floyd"),
    Person("Pierce Hughes"),
    Person("Samantha Cisneros"),
    Person("Alden Sims"),
    Person("Lena Vincent"),
    Person("Aarav Lamb"),
    Person("Amaia Ferguson"),
    Person("Moon Isleifson")
]

while people:  # run the sim if people still exist
    print(f"\n--- Year {year} ---")
    
    new_people = []
    for person in people:
        if person.is_alive():
            person.live_10_year()
            
            # 20% chance to have a child each year
            if random.random() < 0.2 and len(people) <= 100 and person.age >= 20:
                child_name = f"{person.name.split('_')[0]}_child{random.randint(1,10)}"
                new_people.append(person.have_child(child_name))
    
    # Add new children to the population
    people.extend(new_people)
    
    # Remove people who ran out of energy
    # Save the current population before filtering
    alive_last_year = people.copy()

    # Remove people who ran out of energy
    people = [p for p in people if p.is_alive()]

    # Figure out who died this year
    died_this_year = [p for p in alive_last_year if p not in people]

    # Print who died
    if died_this_year:
        print("\033[31mWho died this year:\033[0m")  # Red text
        for p in died_this_year:
            print(f"\033[31m{p.name} (age {p.age}, hobby {p.hobby})\033[0m")
    else:
        print("\nNo one died this year.")


    print("Those who are still alive: ")
    for p in people:
        count += 1
        print(f"Number: {count} {p.name} (age {p.age}, energy {p.energy})")
        time.sleep(0.5)

    input("Press Enter to play out the next year...")
    year += 1