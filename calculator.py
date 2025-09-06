from tkinter import *
import tkinter as tk

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = tk.Tk()
root.title("Calculator")
width = root.winfo_screenwidth()
heigth = root.winfo_screenheight()
root.geometry(f"{width}x{heigth}")
root.maxsize(600,700)


scvalue = StringVar()
scvalue.set("")

screen = tk.Entry(root, bg="Grey",textvar=scvalue, font="lucida 40 bold", relief=SUNKEN)
screen.pack( ipadx=8, padx=10, pady=10)

frame_1 = tk.Frame(root, bg="Grey")
frame_1.pack()

btn_9 = tk.Button(frame_1, text="9", padx=20, pady=20, font="lucida 20 bold")
btn_9.grid(row=0, column=0, padx=20, pady=20)
btn_9.bind("<Button-1>", click)

btn_8 = tk.Button(frame_1, text="8", padx=20, pady=20, font="lucida 20 bold")
btn_8.grid(row=0, column=1, padx=20, pady=20)
btn_8.bind("<Button-1>", click)

btn_7 = tk.Button(frame_1, text="7", padx=20, pady=20, font="lucida 20 bold")
btn_7.grid(row=0, column=2, padx=20, pady=20)
btn_7.bind("<Button-1>", click)

btn_6 = tk.Button(frame_1, text="6", padx=20, pady=20, font="lucida 20 bold")
btn_6.grid(row=1, column=0, padx=20, pady=20)
btn_6.bind("<Button-1>", click)

btn_5 = tk.Button(frame_1, text="5", padx=20, pady=20, font="lucida 20 bold")
btn_5.grid(row=1, column=1, padx=20, pady=20)
btn_5.bind("<Button-1>", click)

btn_4 = tk.Button(frame_1, text="4", padx=20, pady=20, font="lucida 20 bold")
btn_4.grid(row=1, column=2, padx=20, pady=20)
btn_4.bind("<Button-1>", click)

btn_3 = tk.Button(frame_1, text="3", padx=20, pady=20, font="lucida 20 bold")
btn_3.grid(row=2, column=0, padx=20, pady=20)
btn_3.bind("<Button-1>", click)

btn_2 = tk.Button(frame_1, text="2", padx=20, pady=20, font="lucida 20 bold")
btn_2.grid(row=2, column=1, padx=20, pady=20)
btn_2.bind("<Button-1>", click)

btn_1 = tk.Button(frame_1, text="1", padx=20, pady=20, font="lucida 20 bold")
btn_1.grid(row=2, column=2, padx=20, pady=20)
btn_1.bind("<Button-1>", click)

btn_0 = tk.Button(frame_1, text="0", padx=20, pady=20, font="lucida 20 bold")
btn_0.grid(row=3, column=1, padx=20, pady=20)
btn_0.bind("<Button-1>", click)

add = tk.Button(frame_1, text="+", padx=20, pady=20, font="lucida 20 bold")
add.grid(row=0, column=3, padx=20, pady=20)
add.bind("<Button-1>", click)

sub = tk.Button(frame_1, text="-", padx=20, pady=20, font="lucida 20 bold")
sub.grid(row=1, column=3, padx=20, pady=20)
sub.bind("<Button-1>", click)

mul = tk.Button(frame_1, text="*", padx=20, pady=20, font="lucida 20 bold")
mul.grid(row=2, column=3, padx=20, pady=20)
mul.bind("<Button-1>", click)

div = tk.Button(frame_1, text="/", padx=20, pady=20, font="lucida 20 bold")
div.grid(row=3, column=3, padx=20, pady=20)
div.bind("<Button-1>", click)

equal = tk.Button(frame_1, text="=", padx=20, pady=20, font="lucida 20 bold")
equal.grid(row=3, column=2, padx=20, pady=20)
equal.bind("<Button-1>", click)

clear = tk.Button(frame_1, text="C", padx=20, pady=20, font="lucida 20 bold")
clear.grid(row=3, column=0, padx=20, pady=20)
clear.bind("<Button-1>", click)

# percentage = tk.Button(frame_1, text="%", padx=20, pady=20, font="lucida 20 bold")
# percentage.grid(row=1, column=0, padx=20, pady=20)
# percentage.bind("<Button-1>", click)

quit_button = tk.Button(root, text="Quit", font="lucida 14 bold",command=root.destroy, bg="Red")
quit_button.pack(side=BOTTOM,anchor="e", fill=X, padx=20, pady=20)

root.mainloop()

