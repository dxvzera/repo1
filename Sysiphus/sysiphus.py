import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sys
import pyautogui as pag
import pyperclip as pyp

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def Sysiphus():

    # pag.alert("this one works too my nigga")

    pyp.copy("exit")
    pag.hotkey('ctrl', 'v')
    pag.press('enter')

    while True:
        root = tk.Tk()
        root.title("One must imagine sysiphus happy")

        # Carrega a imagem
        diretorio = resource_path("D:/Users/Davi/Desktop/programas/codes/python/pyautogui/Sysiphus/sysiphus.jpg")
        imagem = Image.open(os.path.join(diretorio, "D:/Users/Davi/Desktop/programas/codes/python/pyautogui/Sysiphus/sysiphus.jpg"))
        ImgResize = imagem.resize((450,300))

        imagem = ImageTk.PhotoImage(ImgResize)

        # Adiciona a imagem a um widget Label
        label_imagem = tk.Label(root, image=imagem)
        label_imagem.pack()

        root.mainloop()


# pag.alert("it works my pookie bear")

# pag.hotkey('win','r')
# pyp.copy("cmd")
# pag.hotkey('ctrl', 'v')
# pag.press('enter')

# pag.sleep(0.5)

# pyp.copy("taskkill /F /IM explorer.exe /T")
# pag.hotkey('ctrl', 'v')
# pag.press('enter')

# pyp.copy("exit")
# pag.hotkey('ctrl', 'v')
# pag.press('enter')


if __name__ == "__main__":
    Sysiphus()



