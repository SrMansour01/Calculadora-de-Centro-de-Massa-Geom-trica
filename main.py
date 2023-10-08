import math

QF = int(input("Quantas formas tem na imagem: "))

altura = []
largura = []
cordenadaX = []
cordenadaY = []
area = []
AX = []
AY = []

for c in range(QF):

    print("=========================================================")
    Formato = int(input(f"Qual a {c+1} imagem? \n1 - Retângulo\n2 - Triângulo retângulo\n3 - Círculo\nQual: "))

    altura.append(float(input(f"Qual a medida da altura da imagem {c+1}: ")))
    largura.append(float(input(f"Qual a medida da largura da imagem {c+1}: ")))
    cordenadaX.append(float(input(f"Valor da cordenada X da imagem {c+1}: ")))
    cordenadaY.append(float(input(f"Valor da cordenada Y da imagem {c+1}: ")))\

    if Formato == 1:
        area.append(altura[c] * largura[c]) 
        print("retângulo")

    if Formato == 3:
        area.append(math.pi * largura[c]**2 )
        print("Círculo")

    if Formato == 2 :
        area.append(largura[c] * altura[c] / 2)
        print("Triângulo retângulo")

    AX.append(area[c] * cordenadaX[c])
    AY.append(area[c] * cordenadaY[c])
print("=========================================================")
Centro_de_gravidade_X = (sum(AX)/sum(area))
Centro_de_gravidade_Y = (sum(AY)/sum(area))

print(f"O centro de massa da forma esta nas coordenadas x: {round(Centro_de_gravidade_X, 3)}cm | y: {round(Centro_de_gravidade_Y, 3)}cm")