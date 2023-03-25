import tkinter as tk

window = tk.Tk()
window.title("Kalkulator")
window.configure(bg='purple')
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window, width=42)
entry = tk.Entry(master=frm_entry, validate="all", width=25, font='Bold')


def input_into_entry(symbol):
    entry.insert(tk.END, symbol)


def input_into_entry_sqrt(symbol):
    entry.insert(0, symbol)

def clear():
    entry.delete(0, tk.END)

def calculation():
    text=entry.get()
    result=0
    if '+' in text:
        split_text=text.split('+')
        num1=float(split_text[0])
        num2=float(split_text[1])
        result=num1+num2
        clear()
    if '-' in text:
        split_text=text.split('-')
        num1=float(split_text[0])
        num2=float(split_text[1])
        result=num1-num2
        clear()
    if '*' in text:
        split_text=text.split('*')
        num1=float(split_text[0])
        num2=float(split_text[1])
        result=num1*num2
        clear()
    if '/' in text:
        split_text=text.split('/')
        num1=float(split_text[0])
        num2=float(split_text[1])
        try:
            result=num1/num2
            clear()
        except:
            clear()
            result=None
            entry.insert(0,'nie dziel przez 0')
    if '√' in text:
        split_text=text.split('√')
        num1=float(split_text[1])
        result=num1**(0.5)
        clear()
    if result%1:
        result = round(result, 10)
    else:
        result = int(result)
    entry.insert(0, result)


entry.grid(row=0, column=0, columnspan=4)

btn1 = tk.Button(
    master=window,
    text="1",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('1')
)
btn2 = tk.Button(
    master=window,
    text="2",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('2')
)
btn3 = tk.Button(
    master=window,
    text="3",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('3')
)
btn4 = tk.Button(
    master=window,
    text="+",
    width=7,
    height=3,
    bg='#7323fc',
    fg='pink',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('+')
)
btn5 = tk.Button(
    master=window,
    text="4",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('4')
)
btn6 = tk.Button(
    master=window,
    text="5",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('5')
)
btn7 = tk.Button(
    master=window,
    text="6",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('6')
)
btn8 = tk.Button(
    master=window,
    text="-",
    width=7,
    height=3,
    bg='#7323fc',
    fg='pink',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('-')
)
btn9 = tk.Button(
    master=window,
    text="7",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('7')
)
btn10 = tk.Button(
    master=window,
    text="8",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('8')
)
btn11 = tk.Button(
    master=window,
    text="9",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('9')
)
btn12 = tk.Button(
    master=window,
    text="/",
    width=7,
    height=3,
    bg='#7323fc',
    fg='pink',
    font=('Arial 9 bold'),
    command=lambda: input_into_entry('/')
)
btn13 = tk.Button(
    master=window,
    text="0",
    width=7,
    height=3,
    bg='pink',
    fg='#7323fc',
    font=('Arial 9 bold'),
    command=lambda:input_into_entry('0')
)
btn14 = tk.Button(
    master=window,
    text=",",
    width=7,
    height=3,
    bg='#7323fc',
    fg='pink',
    font=('Arial 9 bold'),
    command=lambda:input_into_entry('.')
)
btn15 = tk.Button(
    master=window,
    text="√",
    width=7,
    height=3,
    bg='#7323fc',
    fg='pink',
    font=('Arial 9 bold'),
    command=lambda:input_into_entry_sqrt('√')
)
btn16 = tk.Button(
    master=window,
    text="*",
    width=7,
    height=3,
    bg='#7323fc',
    fg='pink',
    font=('Arial 9 bold'),
    command=lambda:input_into_entry('*')
)
btn17 = tk.Button(
    master=window,
    text="C",
    width=16,
    height=3,
    bg='#fa5f5c',
    fg='red',
    font=('Arial 9 bold'),
    command=lambda:clear()
)
btn18 = tk.Button(
    master=window,
    text="=",
    width=16,
    height=3,
    bg='#5cfaae',
    fg='green',
    font=('Arial 9 bold'),
    command=lambda:calculation()
)
frm_entry.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

btn1.grid(row=1, column=0, padx=1, pady=1)
btn2.grid(row=1, column=1, padx=1, pady=1)
btn3.grid(row=1, column=2, padx=1, pady=1)
btn4.grid(row=1, column=3, padx=1, pady=1)

btn5.grid(row=2, column=0, padx=1, pady=1)
btn6.grid(row=2, column=1, padx=1, pady=1)
btn7.grid(row=2, column=2, padx=1, pady=1)
btn8.grid(row=2, column=3, padx=1, pady=1)

btn9.grid(row=3, column=0, padx=1, pady=1)
btn10.grid(row=3, column=1, padx=1, pady=1)
btn11.grid(row=3, column=2, padx=1, pady=1)
btn12.grid(row=3, column=3, padx=1, pady=1)

btn13.grid(row=4, column=0, padx=1, pady=1)
btn14.grid(row=4, column=1, padx=1, pady=1)
btn15.grid(row=4, column=2, padx=1, pady=1)
btn16.grid(row=4, column=3, padx=1, pady=1)

btn17.grid(row=5, column=0, columnspan=2, padx=1, pady=1)
btn18.grid(row=5, column=2, columnspan=2, padx=1, pady=1)

window.mainloop()