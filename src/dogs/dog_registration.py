dogs = []
answer = "yes"

while answer == "yes":
    print("Register a dog")
    dog_name = input("dog name ")
    dog_age = int(input("dog age "))
    dog_breed = input("dog breed ")

    dog = {
        "name": dog_name,
        "age": dog_age,
        "breed": dog_breed,
    }

    dogs.append(dog)
    answer = input("Do you have more dogs? yes/no: ").lower()

for dog in dogs:
    print(f"{dog['name']} is {dog['age']} years old and its breed is {dog['breed']}.")
