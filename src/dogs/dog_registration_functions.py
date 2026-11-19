dogs = []
def register_dog(dog_name, dog_age, dog_breed):
    dog = {
        "name": dog_name,
        "age": dog_age,
        "breed": dog_breed
    }
    return dog

dogs.append(register_dog("Max", 2, "Golden Retriever"))
dogs.append(register_dog("Luna", 1, "Husky"))

for dog in dogs:
    print(f"{dog['name']} is {dog['age']} years old and its breed is {dog['breed']}.")
