from datetime import date

data_atual = date.today()
data_format = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
ultimo_dia = date(date.today().year, 12, 31)

print('Data atual:',data_format)
print('Dias até o final do ano:',abs(ultimo_dia - data_atual).days)
