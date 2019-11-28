from faker import Faker
fake = Faker()

def populate():

    people=[]

    for _ in range(10,30):
        p={'firstname': fake.first_name(), 'lastname': fake.last_name()}
        people.append(p)
    return iter(people)

if __name__ == '__main__':
    
    new_people = populate()

    new_data = [f"{p['firstname']} {p['lastname']}" for p in new_people]
    new_data = ", ".join(new_data) + ", "

    with open('people.txt','a') as f:
        f.write(new_data)
