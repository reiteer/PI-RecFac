from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame

# Caminho dos assets da primeira tela
ASSETS_PATH_1 = Path(r"C:\Users\22.01388-0\Documents\build\assets\frame0")
# Caminho dos assets da segunda tela
ASSETS_PATH_2 = Path(r"C:\Users\22.01388-0\Downloads\build\assets\frame0")

# Função auxiliar para construir o caminho dos assets
def relative_to_assets(path: str, assets_path: Path) -> Path:
    return assets_path / Path(path)  # Concatena o caminho base dos assets com o caminho do arquivo fornecido

# Função para trocar para a segunda tela
def switch_to_second_frame():
    first_frame.pack_forget()  # Esconde o primeiro frame
    second_frame.pack(fill="both", expand=True)  # Mostra o segundo frame e o ajusta para ocupar a janela toda

# Janela principal do Tkinter
window = Tk()  # Cria a janela principal
window.geometry("752x686")  # Define o tamanho da janela
window.configure(bg="#FFFFFF")  # Define a cor de fundo como branca
window.title("SAD-RF")  # Define o título da janela

# Primeira Tela (Frame)
first_frame = Frame(window)  # Cria o primeiro frame, que será a primeira tela
first_frame.pack(fill="both", expand=True)  # Exibe o primeiro frame, preenchendo toda a janela

canvas1 = Canvas(
    first_frame,
    bg="#FFFFFF",
    height=686,
    width=752,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)  # Cria um canvas dentro do primeiro frame para desenhar elementos gráficos (como imagens e botões)
canvas1.place(x=0, y=0)  # Posiciona o canvas na origem (0,0) da tela

# Carrega e exibe a imagem no canvas da primeira tela
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png", ASSETS_PATH_1))  # Carrega a imagem
canvas1.create_image(376.0, 217.0, image=image_image_1)  # Exibe a imagem no canvas na posição central

# Botão "Entrar" na primeira tela
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png", ASSETS_PATH_1))  # Carrega a imagem do botão
button_1 = Button(
    first_frame,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_second_frame,  # Define que ao clicar o botão vai chamar a função que troca de tela
    relief="flat"
)  # Cria o botão com a imagem carregada
button_1.place(x=271.0, y=549.0, width=211.0, height=39.0)  # Posiciona o botão na tela

# Caixa de entrada de texto na primeira tela
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png", ASSETS_PATH_1))  # Carrega a imagem da caixa de entrada
canvas1.create_image(376.0, 498.5, image=entry_image_1)  # Exibe a imagem da caixa de entrada no canvas
entry_1 = Text(first_frame, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)  # Cria uma caixa de texto (campo de entrada)
entry_1.place(x=255.0, y=476.0, width=242.0, height=43.0)  # Posiciona a caixa de entrada

# Segunda caixa de entrada de texto na primeira tela
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png", ASSETS_PATH_1))  # Carrega a imagem da segunda caixa de entrada
canvas1.create_image(376.0, 434.5, image=entry_image_2)  # Exibe a imagem da segunda caixa de entrada no canvas
entry_2 = Text(first_frame, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)  # Cria outra caixa de texto
entry_2.place(x=260.0, y=412.0, width=232.0, height=43.0)  # Posiciona a segunda caixa de entrada

# Segunda Tela (Frame)
second_frame = Frame(window)  # Cria o segundo frame, que será exibido após clicar no botão "Entrar"

canvas2 = Canvas(
    second_frame,
    bg="#FFFFFF",
    height=644,
    width=812,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)  # Cria um canvas dentro do segundo frame
canvas2.place(x=0, y=0)  # Posiciona o canvas na origem (0,0) do frame

# Cria um retângulo na parte inferior da segunda tela
canvas2.create_rectangle(0.0, 590.0, 812.0, 644.0, fill="#272727", outline="")  # Cria uma barra na parte inferior da tela

# Adiciona um texto na parte inferior da segunda tela
canvas2.create_text(
    264.0,
    610.0,
    anchor="nw",
    text="© 2024 - Todos os direitos reservados a SAD-RF",  # Texto de rodapé
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)  # Define a posição e o estilo do texto de rodapé

# Carrega e exibe a imagem no canvas da segunda tela
image_image_2 = PhotoImage(file=relative_to_assets("image_1.png", ASSETS_PATH_2))  # Carrega a imagem para o segundo frame
canvas2.create_image(406.0, 53.0, image=image_image_2)  # Exibe a imagem no canvas

# Botão na segunda tela (primeiro botão)
button_image_2 = PhotoImage(file=relative_to_assets("button_1.png", ASSETS_PATH_2))  # Carrega a imagem do botão
button_2 = Button(
    second_frame,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),  # Ação que ocorre ao clicar no botão
    relief="flat"
)  # Cria o botão
button_2.place(x=130.0, y=210.0, width=242.0, height=45.0)  # Posiciona o botão na tela

# Botão na segunda tela (segundo botão)
button_image_3 = PhotoImage(file=relative_to_assets("button_2.png", ASSETS_PATH_2))  # Carrega a imagem do segundo botão
button_3 = Button(
    second_frame,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),  # Ação ao clicar no botão
    relief="flat"
)  # Cria o botão
button_3.place(x=447.0, y=210.0, width=242.0, height=45.0)  # Posiciona o botão

# Botão grande na segunda tela
button_image_4 = PhotoImage(file=relative_to_assets("button_3.png", ASSETS_PATH_2))  # Carrega a imagem do botão grande
button_4 = Button(
    second_frame,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),  # Ação ao clicar no botão
    relief="flat"
)  # Cria o botão
button_4.place(x=258.0, y=382.0, width=296.0, height=80.0)  # Posiciona o botão grande na tela

# Inicialmente, exibe a primeira tela
first_frame.pack(fill="both", expand=True)  # Exibe o primeiro frame (primeira tela)

window.resizable(False, False)  # Desativa a redimensionabilidade da janela
window.mainloop()  # Inicia o loop principal da aplicação, permitindo interação contínua
