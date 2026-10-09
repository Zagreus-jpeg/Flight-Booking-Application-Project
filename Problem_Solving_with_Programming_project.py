from tkinter import *
import tkinter as tk


root = tk.Tk()
root.title("welcome")
root.geometry('600x400')

flight_list = ["Flight_1","Flight_2","Flight_3"]

lbl_flight_selected = tk.Label(root, text = f"Selected: {flight_list[0]}")

lbl_flight_selected.pack(anchor="w", padx=10, pady=10)

def selection():
    lbl_flight_selected.config(text=f"Selected: {variable.get()}")

#Flight selection below

variable = tk.StringVar(root, f"{flight_list[0]}")

for flight in flight_list:
    tk.Radiobutton(
        root,
        text=flight,
        variable=variable,
        value=flight,
        command=selection,
    ).pack(anchor="w", padx=10, pady=5)

#Seat code below

seats_options = ["First_Class","Second_Class","Econ_Class"]

v_2 = tk.IntVar()

tk.Label(root,
         text="Select a seat",
         justify=tk.LEFT,
         padx=20).pack()

for seat in seats_options:
    tk.Radiobutton(root,
                   text=seat,
                   variable=v_2,
                   value=seat,
                   command=selection,).pack(anchor="w",padx=10,pady=5)


#date


date_title = tk.Label(root, text="Select a date",
                      justify=LEFT,
                      padx=20).pack()


cal = Calendar(root, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)

cal.pack(pady = 20)

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())

Button(root, text= "Select Date",
       command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)



root.mainloop()


#finding the difference in time from the user input
def delta_t():


# finding the final price of the flight
def final_price(delta_t,base_price):
    price = base_price*(1+(((-0.557)*sin(((-48.264)*delta_t)))+((delta_t-0.231)*pow(delta_t,2))))