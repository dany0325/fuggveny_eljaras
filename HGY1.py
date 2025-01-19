import random

def random_gyumik():
    lstoffruits = ["alma", "körte", "szilva", "barack", "málna", "füge", "eper"]
    return random.choices(lstoffruits, k=30)


print(random_gyumik())