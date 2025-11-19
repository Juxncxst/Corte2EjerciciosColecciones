agenda = {}
while True:
    nombre = input()
    if nombre.lower()=="fin":
        break
    tel = input()
    agenda[nombre]=tel
print(agenda)
