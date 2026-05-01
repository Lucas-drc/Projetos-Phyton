nota = float (input("Qual a nota do aluno? "))
10
if nota >=8 and nota <=10:
    print("O aluno atende ao indicador. Está aprovado!")

elif nota >=0 and nota <4.5:
     print("O aluno não atende ao indicador. Está reprovado!")

elif nota >=6 and nota <8:
    print("O aluno atende parcialmente. Está aprovado, mas precisa de atenção!")

elif nota >=4.5 and nota < 6:
    print("O aluno não atende ao indicador, mas pode ser aplicado recuperação!")

else:
     print("Nota do aluno está digitada errada!")
   

