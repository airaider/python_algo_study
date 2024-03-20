import random

TRIAL = 100000
same_birthday = 0

# 10aksqjs tlfgja wlsgod

for _ in range(TRIAL):
    birthdays = []
    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthday+=1
            break
        birthdays.append(birthday)
print(same_birthday/TRIAL*100)