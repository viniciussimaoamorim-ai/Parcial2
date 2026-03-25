# Função para converter segundos para horas, minutos e segundos
def converter_para_horas_minutos_segundos(segundos):
    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    segundos_restantes = resto % 60
    return horas, minutos, segundos_restantes

# Função para converter horas, minutos e segundos para segundos
def converter_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

# Parte 1: Converter segundos para horas, minutos e segundos
segundos_input = int(input("Digite a quantidade de segundos: "))
horas, minutos, segundos_restantes = converter_para_horas_minutos_segundos(segundos_input)

print(f"{segundos_input} segundos é igual a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")

# Parte 2: Converter horas, minutos e segundos para segundos
horas_input = int(input("Digite as horas: "))
minutos_input = int(input("Digite os minutos: "))
segundos_input = int(input("Digite os segundos: "))

total_segundos = converter_para_segundos(horas_input, minutos_input, segundos_input)
print(f"{horas_input} horas, {minutos_input} minutos e {segundos_input} segundos são {total_segundos} segundos.")
