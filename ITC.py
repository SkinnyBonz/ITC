from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
import pywhatkit

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
ICON_PATH = OUTPUT_PATH / Path("./assets/Icon.ico")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("352x269")
window.configure(bg = "#0A1022")
window.title('ITC') 
window.iconbitmap(ICON_PATH)


canvas = Canvas(
    window,
    bg = "#0A1022",
    height = 269,
    width = 352,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    9.0,
    13.0,
    342.0,
    259.0,
    fill="#0F162F",
    outline="")

# convert button=======================================================================================================================================
def combo():
    pywhatkit.image_to_ascii_art(text_top.get().replace("/", "\\\\"),text_buttom.get().replace("/", "\\\\"))

button_1 = Button(
    text = "Convert",
    fg="white",
    font=("Inter", 10),
    borderwidth=0,
    highlightthickness=0,
    command=combo,
    relief="flat",
    bg="#122436",
)
button_1.place(
    x=86.0,
    y=187.0,
    width=179.0,
    height=28.0
)
# file choosing button===================================================================================================================================
def OpenFile():
    file_path = filedialog.askopenfilename(initialdir="Slecting Image", title="Select File", filetypes=(
        ("PNG", "*.png"),
        ("JPG", "*.jpg")
        ))
    text_top.insert('0', file_path)

text_top = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
text_top.place(
    x=15.0,
    y=65.0,
    width=319.0,
    height=23.0
)


button_2 = Button(
    text = "Choose File",
    fg="white",
    font=("Inter", 12),
    borderwidth=0,
    highlightthickness=0,
    command=OpenFile,
    activebackground = "#122436",
    relief="flat",
    bg="#122436",
)
button_2.place(
    x=15.0,
    y=30.0,
    width=320.0,
    height=23.0
)
# save as/folder button===================================================================================================================================
def openDirectory():
    final_Text = "/Converted Text.txt"
    dir_path = filedialog.askdirectory(initialdir="Directory Path", title="Path Location")
    ending_text = dir_path + final_Text
    text_buttom.insert('0', ending_text)

text_buttom = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
text_buttom.place(
    x=15.0,
    y=130.0,
    width=290.0,
    height=23.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=openDirectory,
    relief="flat"
)
button_3.place(
    x=305.0,
    y=130.,
    width=30.0,
    height=23.0
)

# misc stuff==============================================================================================================================================

canvas.create_text(
    15.0,
    110.0,
    anchor="nw",
    text="Save In",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    36.0,
    222.0,
    image=image_image_1
)

window.resizable(False, False)
window.mainloop()
