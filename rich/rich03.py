from rich import print
from rich.table import Table
tabela = Table(title='tabela de\nprodutos')
tabela.add_column('nome',style='blue')
tabela.add_column('quant',justify='center',style='green')
tabela.add_column('preço',justify='center',style='yellow')
tabela.add_row('coca cola','1','13.45')
tabela.add_row('chettos /g','1','11.23')
tabela.add_row('babalu','20','6.99')
print(tabela)