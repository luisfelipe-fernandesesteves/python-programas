'''
3. Cálculo de Área e Perímetro
Enunciado: Escreva um programa que leia a base e a altura de um retângulo e exiba sua área e seu perímetro.
Fórmulas: Area = base * altura | Perimetro = 2 * (base + altura).
'''

print("Cálculo de Área e Perímetro de um Retângulo")
print("VAMOS CALCULAR A AREA E O PERIMETRO")
print("é necessario que escreva o numero no formato seguinte --> 00.00")
base = float(input("INFORME O TAMANHO DA BASE: "))
altura = float(input("INFORME A ALTURA: "))

area = base * altura
perimetro = 2 * (base + altura)

print("A AREA DO RETANGULO É:", area, "\nO PERIMETRO DO RETANGULO É: ",perimetro)