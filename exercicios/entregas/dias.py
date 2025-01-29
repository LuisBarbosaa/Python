entrada = int(input("Por favor, entre com o numero de segundos que deseja converter: \n"))

dia = entrada // 86400
segundosRestantes = entrada % 86400
horas = segundosRestantes // 3600
segundosRestantes %= 3600
minutos = segundosRestantes // 60
segundosRestantes %= 60

print(f"{dia} dias, {horas} horas, {minutos} minutos e {segundosRestantes} segundos.")