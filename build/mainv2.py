import cv2  # Biblioteca usada para reconhecimento facial
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame

# Caminho dos assets da primeira tela
ASSETS_PATH_1 = Path(r"C:\Users\22.01388-0\Documents\build\assets\frame0")
# Caminho dos assets da segunda tela
ASSETS_PATH_2 = Path(r"C:\Users\22.01388-0\Downloads\build\assets\frame0")

# Função auxiliar para construir o caminho dos assets
def relative_to_assets(path: str, assets_path: Path) -> Path:
    return assets_path / Path(path)

# Função para trocar para a segunda tela
def switch_to_second_frame():
    first_frame.pack_forget()
    second_frame.pack(fill="both", expand=True)

# Função para abrir a tela de reconhecimento facial
def open_face_recognition():
    second_frame.pack_forget()
    recognition_frame.pack(fill="both", expand=True)
    start_face_recognition()

# Função para iniciar o sistema de reconhecimento facial
def start_face_recognition():
    cap = cv2.VideoCapture(0)  # Abre a webcam

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()  # Captura o frame da webcam
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converte o frame para escala de cinza
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Detecta rostos

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Desenha um retângulo em torno do rosto

        cv2.imshow('Reconhecimento Facial', frame)  # Exibe o frame na tela

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
            break

    cap.release()
    cv2.destroyAllWindows()

# Janela principal do Tkinter
window = Tk()
window.geometry("752x686")
window.configure(bg="#FFFFFF")
window.title("SAD-RF")

# Primeira Tela (Frame)
first_frame = Frame(window)
first_frame.pack(fill="both", expand=True)

canvas1 = Canvas(
    first_frame,
    bg="#FFFFFF",
    height=686,
    width=752,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas1.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png", ASSETS_PATH_1))
canvas1.create_image(376.0, 217.0, image=image_image_1)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png", ASSETS_PATH_1))
button_1 = Button(
    first_frame,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_second_frame,
    relief="flat"
)
button_1.place(x=271.0, y=549.0, width=211.0, height=39.0)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png", ASSETS_PATH_1))
canvas1.create_image(376.0, 498.5, image=entry_image_1)
entry_1 = Text(first_frame, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=255.0, y=476.0, width=242.0, height=43.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png", ASSETS_PATH_1))
canvas1.create_image(376.0, 434.5, image=entry_image_2)
entry_2 = Text(first_frame, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place(x=260.0, y=412.0, width=232.0, height=43.0)

# Segunda Tela (Frame)
second_frame = Frame(window)

canvas2 = Canvas(
    second_frame,
    bg="#FFFFFF",
    height=644,
    width=812,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas2.place(x=0, y=0)

canvas2.create_rectangle(0.0, 590.0, 812.0, 644.0, fill="#272727", outline="")
canvas2.create_text(
    264.0,
    610.0,
    anchor="nw",
    text="© 2024 - Todos os direitos reservados a SAD-RF",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

image_image_2 = PhotoImage(file=relative_to_assets("image_1.png", ASSETS_PATH_2))
canvas2.create_image(406.0, 53.0, image=image_image_2)

button_image_2 = PhotoImage(file=relative_to_assets("button_1.png", ASSETS_PATH_2))
button_2 = Button(
    second_frame,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(x=130.0, y=210.0, width=242.0, height=45.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_2.png", ASSETS_PATH_2))
button_3 = Button(
    second_frame,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(x=447.0, y=210.0, width=242.0, height=45.0)

# Botão que inicia o reconhecimento facial
button_image_4 = PhotoImage(file=relative_to_assets("button_3.png", ASSETS_PATH_2))
button_4 = Button(
    second_frame,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_face_recognition,  # Abre a tela de reconhecimento facial
    relief="flat"
)
button_4.place(x=258.0, y=382.0, width=296.0, height=80.0)

# Tela de Reconhecimento Facial (Frame)
recognition_frame = Frame(window)

canvas3 = Canvas(
    recognition_frame,
    bg="#FFFFFF",
    height=644,
    width=812,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas3.place(x=0, y=0)

canvas3.create_text(
    300.0,
    300.0,
    anchor="nw",
    text="Aguarde, reconhecimento facial em andamento...",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

# Inicialmente, exibe a primeira tela
first_frame.pack(fill="both", expand=True)

window.resizable(False, False)
window.mainloop()
