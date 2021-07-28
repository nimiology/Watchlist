from pathlib import Path
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Window(Json):




    window = Tk()

    window.geometry("1152x700")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 700,
        width = 1152,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        596.0,
        326.0,
        anchor="nw",
        text="Creators :  David Benioff | D.B. Weiss",
        fill="#000",
        font=("RobotoSlab Regular", 17 * -1),
        width=503.0
    )

    canvas.create_text(
        596.0,
        358.0,
        anchor="nw",
        text="Release Date : April 17, 2011 (United States) ",
        fill="#000",
        font=("RobotoSlab Regular", 17 * -1),
        width=503.0
    )

    canvas.create_text(
        597.0,
        390.0,
        anchor="nw",
        text="Language : English",
        fill="#000",
        font=("RobotoSlab Regular", 17 * -1),
        width=503.0
    )

    canvas.create_text(
        596.0,
        297.0,
        anchor="nw",
        text="Stars : Emilia Clarke | Peter Dinklage | Kit Harington\n\n",
        fill="#000",
        font=("RobotoSlab Regular", 17 * -1),
        width=436.0
    )

    canvas.create_text(
        597.0,
        265.0,
        anchor="nw",
        text="Genre : Action | Adventure | Drama | Fantasy",
        fill="#000",
        font=("RobotoSlab Regular", 17 * -1),
        width=436.0
    )

    canvas.create_text(
        597.0,
        141.0,
        anchor="nw",
        text="NINE NOBLE FAMILIES FIGHT FOR CONTROL OVER THE LANDS OF WESTEROS, WHILE AN ANCIENT ENEMY RETURNS AFTER BEING DORMANT FOR MILLENNIA.",
        fill="#000",
        font=("RobotoSlab Medium", 20 * -1),
        width=528.0
    )

    canvas.create_text(
        576.0,
        77.0,
        anchor="nw",
        text="Game of Thrones",
        fill="#484848",
        font=("RobotoSlab Bold", 48 * -1),
        width=503.0
    )

    canvas.create_text(
        576.0,
        66.0,
        anchor="nw",
        text="TV Series | 2011-2019 | TV-MA",
        fill="#000",
        font=("RobotoMono Light", 14 * -1),
        width=244.0
    )

    canvas.create_text(
        1055.0,
        38.0,
        anchor="nw",
        text="/10",
        fill="#000",
        font=("Roboto Light", 16 * -1),
        width=25.0
    )

    canvas.create_text(
        1019.0,
        33.0,
        anchor="nw",
        text="9.2",
        fill="#000",
        font=("Roboto Black", 24 * -1),
        width=36.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        964.0,
        47.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        283.0,
        331.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        835.0,
        252.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=960.0,
        y=556.0,
        width=139.0,
        height=60.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=806.0,
        y=556.0,
        width=139.0,
        height=60.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=652.0,
        y=556.0,
        width=139.0,
        height=60.0
    )
    window.resizable(False, False)
    window.mainloop()