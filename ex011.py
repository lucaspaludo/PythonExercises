altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

areaParede = altura * largura
litrosTinta = areaParede / 2

print(f"A área da parede é: {areaParede} metros quadrados")
print(f"Você precisará de {litrosTinta:.2f} litros de tinta para pintar a parede")

