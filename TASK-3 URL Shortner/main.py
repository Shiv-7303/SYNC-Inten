from tkinter import *
from logic import *
from tkinter import messagebox


# ---------------------------Url shorten logic------------------------#
def url_shortner():
    root.clipboard_clear()
    url = url_entry.get()
    short = Shortner(url)
    try:
        shorted_link = short.get_shorten()
        short_url.config(text=f"{shorted_link}")
    except KeyError:
        messagebox.showerror(message="Enter the Correct URL..!")
    else:
        root.clipboard_append(shorted_link)
        url_entry.delete(0, END)
        messagebox.showinfo(message="Copied to clipboard")


# ----------------------------UI-----------------------------#
root = Tk()
root.geometry("700x500")
root.title("Url Shortner")
root.config(padx=20, pady=20,)

heading_label = Label(text="URL Shortner\nMake your url shortner", font=("Arial", 30, "bold"))
heading_label.grid(column=1, row=0, )

enter_label = Label(text="Enter the Url : ", font=("Arial", 15, "bold"))
enter_label.grid(column=0, row=1)

url_entry = Entry(width=60, )
url_entry.grid(column=1, row=1, padx=10, ipady=15)

shorten_button = Button(border=2 , width=30, text="Get Shorten", font=("Arial", 15, "italic"), background="#ffafcc", fg="white",
                        command=url_shortner)
shorten_button.grid(column=1, row=3, pady=20)

short_url = Label(text=" ", font=("Arial", 15, "italic"), )
short_url.grid(column=1, row=5, )

get_url_label = Label(text="Get the shorted url : ", font=("Arial", 15, "italic"), )
get_url_label.grid(column=0, row=5, )

root.mainloop()
