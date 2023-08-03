# https://faker.readthedocs.io/en/master/

from faker import Faker

fake = Faker()

for _ in range(10):
    print(fake.name())

print("------------------------")

n1 = fake.name()
print(n1)
n2 = fake.name()
print(n2)

print("------------------------")

fake = Faker(["en_US"])
for _ in range(10):
    print(fake.name())

print("------------------------")

from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

print(fake.ipv4_private())
