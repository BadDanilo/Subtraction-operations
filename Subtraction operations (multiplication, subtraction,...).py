class kasr:
    def __init__(self, soorat, makhraj):
        self.soorat = soorat
        self.makhraj = makhraj

class kasrCalculator:
    
    def get_kasr_input(self):
        soorat1 = int(input("Please enter your first soorate kasr: "))
        makhraj1 = int(input("Please enter your second makhraj kasr: "))
        kasr1 = kasr(soorat1, makhraj1)

        soorat2 = int(input("Please enter your first soorat kasr: "))
        makhraj2 = int(input("Please enter your second makhraj kasr: "))
        kasr2 = kasr(soorat2, makhraj2)

        return kasr1, kasr2
    
    def __add__(self, kasr1, kasr2):
        result_soorat = (kasr1.soorat * kasr2.makhraj) + (kasr2.soorat * kasr1.makhraj)
        result_makhraj = kasr1.makhraj * kasr2.makhraj
        # if kasr1.makhraj==kasr2.makhraj:
        #     print(kasr1.makhraj)
        # else:
        return kasr(result_soorat, result_makhraj)

    def __sub__(self, kasr1, kasr2):
        result_soorat = (kasr1.soorat * kasr2.makhraj) - (kasr2.soorat * kasr1.makhraj)
        result_makhraj = kasr1.makhraj * kasr2.makhraj
        # if kasr1.makhraj==kasr2.makhraj:
        #     print(kasr1.makhraj)
        # else:
        return kasr(result_soorat, result_makhraj)
    
    def __zarb__(self, kasr1, kasr2):
        result_soorat = (kasr1.soorat * kasr2.soorat)
        result_makhraj = kasr1.makhraj * kasr2.makhraj
        return kasr(result_soorat, result_makhraj)
    
    def __taghsim__(self, kasr1, kasr2):
        result_soorat = (kasr1.soorat * kasr2.makhraj)
        result_makhraj = kasr1.makhraj * kasr2.soorat
        return kasr(result_soorat, result_makhraj)

calculator = kasrCalculator()
kasr1, kasr2 = calculator.get_kasr_input()

result_addition = calculator.__add__(kasr1, kasr2)
result_subtraction = calculator.__sub__(kasr1, kasr2)
result_zarb = calculator.__zarb__(kasr1, kasr2)
result_taghsim = calculator.__taghsim__(kasr1, kasr2)

print("jame 2 kasr be in soorat mibashad:", result_addition.soorat, "/", result_addition.makhraj)
print("tafrigh 2 kasr be in soorat mibashad:", result_subtraction.soorat, "/", result_subtraction.makhraj)
print("zarbe 2 kasr be in soorat mibashad:", result_zarb.soorat, "/", result_zarb.makhraj)
print("taghsim 2 kasr be in soorat mibashad:", result_taghsim.soorat, "/", result_taghsim.makhraj)