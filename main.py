ciga = float(input("Informe a quantidade de cigarros fumado por dia: "))
anos = float(input("Digite a quantos anos usa cigarro: "))
minutos = anos * 365 * ciga * 10
dias: float = minutos / (24 * 60)

print("Esse fumante perdera %.2f dias de vida" % dias)