import tkinter as tk

dict = {
    "USD" : 5.0171,
    "AUD" : 3.1456,
    "HKD" : 0.6392,
    "CAD" : 3.6253,
    "NZD" : 2.7947,
    "SGD" : 3.4856,
    "EUR" : 4.8711,
    "HUF" : 0.0113585,
    "CHF" : 5.0179
}

def translate(value):
    curr = dict[value]
    ent = entry.get()
    try:
        ent = float(ent)
        res = ent / curr
        lbl_result["text"] = f"{res}"
    except:
        print("Nie można przekształcić na float")

window = tk.Tk()
window.title("Słownik")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
entry = tk.Entry(master=frm_entry, validate="all", width=10)

entry.grid(row=0, column=0, sticky="e")

btn1 = tk.Button(
    master=window,
    text="USD",
    command=lambda : translate("USD")
)
btn2 = tk.Button(
    master=window,
    text="AUD",
    command=lambda : translate("AUD")
)
btn3 = tk.Button(
    master=window,
    text="HKD",
    command=lambda : translate("HKD")
)
btn4 = tk.Button(
    master=window,
    text="CAD",
    command=lambda : translate("CAD")
)
btn5 = tk.Button(
    master=window,
    text="NZD",
    command=lambda : translate("NZD")
)
btn6 = tk.Button(
    master=window,
    text="SGD",
    command=lambda : translate("SGD")
)
btn7 = tk.Button(
    master=window,
    text="EUR",
    command=lambda : translate("EUR")
)
btn8 = tk.Button(
    master=window,
    text="HUF",
    command=lambda : translate("HUF")
)
btn9 = tk.Button(
    master=window,
    text="CHF",
    command=lambda : translate("CHF")
)
lbl_result = tk.Label(master=window, text="")

frm_entry.grid(row=0, column=1, padx=5)

btn1.grid(row=1, column=0, pady=2, padx=2)
btn2.grid(row=1, column=1, pady=2, padx=2)
btn3.grid(row=1, column=2, pady=2, padx=2)

btn4.grid(row=2, column=0, pady=2, padx=2)
btn5.grid(row=2, column=1, pady=2, padx=2)
btn6.grid(row=2, column=2, pady=2, padx=2)

btn7.grid(row=3, column=0, pady=2, padx=2)
btn8.grid(row=3, column=1, pady=2, padx=2)
btn9.grid(row=3, column=2, pady=2, padx=2)

lbl_result.grid(row=4, column=1, padx=10)

window.mainloop()