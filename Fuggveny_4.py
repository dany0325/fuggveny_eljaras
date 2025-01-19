def kerulet(side_a, *args):
    if len(args) == 0:
        print("Ez egy négyzet!")
        return side_a * 4
    elif len(args) == 1:
        print("Ez egy téglalap!")
        return side_a * 2 + args[0] * 2
    elif len(args) == 2:
        print("Ez egy háromszög!")
        return side_a + args[0] + args[1]
    else:
        print("Ez egy sokszög!")
        return side_a + sum(args)
    

print("A síkidom kerülete:", kerulet(7))
print("A síkidom kerülete:", kerulet(5,10))
print("A síkidom kerülete:", kerulet(5,10,20))
print("A síkidom kerülete:", kerulet(5,10,20,10,30,2))