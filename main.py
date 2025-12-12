import random
import time

class Person:
    def __init__(self, count, name, age=0, energy=10, hobby=None):
        self.count = count
        self.name = name
        self.age = age
        self.energy = energy
        self.hobby = hobby or random.choice(["Python", "gaming", "reading", "ham radio"])
    
    def live_10_year(self):
        self.age += 10
        self.energy -= random.randint(0, 3)  # living costs energy
        # print(f"{self.name} is now {self.age} years old and has {self.energy} energy.")
    
    def is_alive(self):
        return int(self.energy) > 0
    
    def have_child(self, child_name):
        # Child inherits hobby from parent
        return Person(len(people) + 1, child_name, 0, 10, self.hobby)

year = 0

# Start with some people
people = [
    Person("1", "Alice"),
    Person("2", "Bob"),
    Person("3", "Charlie")
]

while people is not None:  # run the sim if people still exist
    print(f"\n--- Year {year+1} ---")
    
    new_people = []
    for person in people:
        if person.is_alive():
            person.live_10_year()
            
            # 20% chance to have a child each year
            if random.random() < 0.2 and len(people) <= 10:
                child_name = f"{person.name.split('_')[0]}_child{random.randint(1,100)}"
                new_people.append(person.have_child(child_name))
    
    # Add new children to the population
    people.extend(new_people)
    
    # Remove people who ran out of energy
    people = [p for p in people if p.is_alive()]

    for p in people:
        print(f"Number: {person.count} {p.name} (age {p.age}, energy {p.energy})")
        time.sleep(0.5)

    input("Press Enter to play out the next year...")
    year =+ 1