from rich import print
from rich.panel import Panel
#python -m rich.emoji
caixa = Panel("[bold yellow]este é um teste rich[/]",title='apresentação',style='green')
print(caixa)
window = Panel(":red_circle: :blue_circle: :green_circle:")
print(window)