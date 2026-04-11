from pynput import mouse

# Função chamada quando um botão do mouse é pressionado
def on_click(x, y, button, pressed):
    if pressed:
        if button.name == "left":
            print(f"Botão ESQUERDO pressionado em ({x}, {y})")
        elif button.name == "right":
            print(f"Botão DIREITO pressionado em ({x}, {y})")
        elif button.name == "middle":
            print(f"Botão DO MEIO pressionado em ({x}, {y})")
    else:
        print(f"Botão {button.name.upper()} liberado em ({x}, {y})")

# Inicia o listener do mouse
with mouse.Listener(on_click=on_click) as listener:
    print("Monitorando cliques do mouse... Pressione CTRL+C para sair.")
    listener.join()