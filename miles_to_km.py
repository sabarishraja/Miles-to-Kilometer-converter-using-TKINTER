import tkinter


def miles_to_km():
    mileskm_1 = float(mile.get())
    km_1 = mileskm_1 * 1.609
    km.config(text=f"{km_1}")


window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=100)

mile = tkinter.Entry(width=7)
mile.grid(column=2, row=1)

label_1 = tkinter.Label(text="Miles")
label_1.grid(column=3, row=1)

label_2 = tkinter.Label(text="is equal to ")
label_2.grid(column=1, row=2)

km = tkinter.Label(text="0")
km.grid(column=2, row=2)

label_3 = tkinter.Label(text="Km")
label_3.grid(column=3, row=2)

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)
window.mainloop()
