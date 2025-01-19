import random

def random_gyumik(numberoffruits):
    lstoffruits = ["alma", "körte", "szilva", "barack", "málna", "füge", "eper"]
    return random.choices(lstoffruits, k=numberoffruits)


print(random_gyumik(5))