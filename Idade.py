idade = int (input("Colque a idade da pessoa: "))

if idade >=0 and idade <=1:
    print("A pessoa é recém nascida!")

elif idade >1 and idade<=8:
    print("A pessoa é uma criança!")

elif idade >8 and idade <=12:
    print("A pessoa é pré-adolescente!")

elif idade >12 and idade <=17:
    print("A pessoa é adolescente!")

elif idade >17 and idade <=25:
    print("A pessoa é jovem!")

elif idade >25 and idade <=60:
    print("A pessoa é adulta!")

elif idade <0:
    print("Idade errada")

else:
    print("A pessoa é idosa!")
