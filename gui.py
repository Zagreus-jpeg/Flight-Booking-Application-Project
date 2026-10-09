
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
from flight import Flight
from bookingsystem import BookingSystem
from datetime import datetime, timedelta
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from passenger import Passenger
from tkcalendar import Calendar
from booking import Booking
from price import Price
import os

root=tk.Tk()
root.geometry("700x700")
root.config(bg="#C3C9E5")
root.state('zoomed')
# root.title("")
curr_tab="admin"
curr_page="sign_up_page"
selected_flight_1=""
u1="royalFlight01"
p1="royalFlight01@"


# bSystem.createBooking(1, "John", "GH123", "firstclass", 700, current_time)
# bSystem.createBooking(2, "Sarah", "LX1174", "secondclass", 600, current_time)
# bSystem.createBooking(3, "Ahmed", "GH123", "thirdclass", 99, current_time)
# bSystem.createBooking(4, "John", "JL42", "firstclass", 5200, current_time)
# bSystem.createBooking(5, "Sarah", "LX1174", "firstclass", 2200, current_time)
def user_flight_buttons():
    #Code adapted from Gemini(Google,2026).
    #Prompt: How to destroy children that are only buttons in the page
    for c in flight_selection_pg.winfo_children():
        if isinstance(c,tk.Button):
            c.destroy()
    #End of adapted code        
    ind=0
    for i in bSystem.flights:
        curr_flight =i.flg_number
        #Code adapted from Claude(Anthropic,2026).
        #Prompt:initially flight buttons should be in the middle. if new flights are created the old ones should move to the left and new ones should be created to its right column
        total=len(bSystem.flights)
        if total<=5:
            x_column=0.5
            row=ind
        else :
            half=(total+1)//2
            if ind<half:
                x_column=0.3
                row=ind
            else:
                x_column=0.7
                row=ind-half     
        #end of adapted code       
        flight_buttons=tk.Button(flight_selection_pg,text=f"{curr_flight} ({i.flg_type})",font=("Inter",18),bg="#E5DFC3",command=lambda amogus=curr_flight:choose_flight(amogus))
        flight_buttons.place(relx=x_column,rely=0.35 +(row* 0.12),anchor="center",width=250,height=45)
        ind+=1
# def booking_confirmed():
#     show_pg(price_pg,confirmed_pg)
#     confirmed_pg.after(2000, lambda: show_pg(confirmed_pg, flight_selection_pg))
def change_password():
    global curr_page
    global u1
    global p1
    
    uname=res_username_box.get()
    prev_pword=prev_password_box.get()
    new_pword=new_password_box.get()
    if uname=="" or prev_pword=="" or new_pword=="":
        messagebox.showerror("Error","Fields can not be left empty")
        return
    if(u1==uname and prev_pword==p1):
        p1=new_pword
        #Code adapted from Gemini(Google,2026).
        #Prompt: How to delete the input field in the entry box
        res_username_box.delete(0,tk.END)
        prev_password_box.delete(0,tk.END)
        new_password_box.delete(0,tk.END)
        #End of adapted code
        show_pg(pass_reset_pg,sign_up_page)
    else:
        messagebox.showerror("Error","The username or password is incorrect")
   

def signin():
    global curr_page
    global u1
    global p1
    uname=username_box.get()
    pword=password_box.get()
    if(pword==p1 and uname==u1):
        sign_up_page.place_forget()
        admin_accessed_p1.place(relx=0,rely=0,relwidth=1,relheight=1)
        curr_page="admin_accessed_p1"
    else:
        messagebox.showerror("Wrong Input","Username or Password doesn't match")
def flight_list_creation():
    ind=0
    print(len(bSystem.flights))
    for i in bSystem.flights:
        
        curr_flight =i.flg_number
        flight_buttons=tk.Button(flight_removal_list,text=curr_flight,font=("Inter",18),bg="#6F8C9F",command=lambda button=curr_flight: confirmationScreen(button))
        flight_buttons.place(relx=0.1,rely=0.1+(0.15*ind))
        ind+=1
def revenue_frame():
    global curr_page
    rev.place(relx=0, rely=0, relwidth=1, relheight=1)
    curr_page="revenue"
    # admin_accessed_p1.place_forget()
    #Code adapted from Claude(Anthropic,2026).
    #Prompt:help me create the revenue bar chart
    grid.clear()
    dt=bSystem.total_revenue_per_flight()
    grid.bar(dt.keys(),dt.values())
    grid.set_title("Revenue per Flight")
    grid.set_xlabel("Flight")
    grid.set_ylabel("Revenue in Pounds")
    canvas.draw()
    #End of adapted code

def redirect_to_original_admin_frame():
    global curr_page
    added.place_forget()
    flight_deleted.place_forget()
    flight_info.place_forget()
    admin_accessed_p3.place_forget()
    admin_accessed_p1.place(relx=0,rely=0,relwidth=1,relheight=1)
    curr_page="admin_accessed_p1"
def add_flight_frame():
    global curr_page
    admin_accessed_p1.place_forget()
    admin_accessed_p3.place(relx=0, rely=0, relwidth=1, relheight=1)
    flight_info.place(relx=0.20,rely=0.1,relwidth=0.6,relheight=0.8)
    curr_page="flight_info"
def flight_added():
    global curr_page
    #Code adapted from Gemini(Google,2026).
    #Prompt 1: how to lower variable we get from the entry boxes?
    #Prompt 2:how to check if name is mix of alphabets and numbers
    name=flight_name_box.get().strip()
    flight_type=flight_type_box.get().strip().lower()
    if not name.isalnum():
        messagebox.showerror("Error", "Flight name can be a mix of alphabet and numeric value")
        return
    #End of adapted code    
    if flight_type!="short" and flight_type!="medium" and flight_type!="long":
        messagebox.showerror("Error", "Type can only be between short, medium and long")
        return
    try:        
        capacity=int(flight_capacity_box.get())
    except:
        messagebox.showerror("Error","Capacity can only be whole numbers")
        return    
    try:
        price=float(flight_bp_box.get())
    except:
        messagebox.showerror("Error","Please Enter a valid number")
        return   
    o_date=open_date.get_date()
    o_d=datetime(o_date.year,o_date.month,o_date.day) 
    c_date=close_date.get_date()
    c_d=datetime(c_date.year,c_date.month,c_date.day)
    f_date=flight_date.get_date()
    f_d=datetime(f_date.year,f_date.month,f_date.day)
    if(o_d>c_d):
        messagebox.showerror("Error","Closing date cannot be before Opening date")
        return
    if(f_d<c_d):
        messagebox.showerror("Error","Flight date cannot be before Closing date")
        return         
    if(f_d<o_d):
        messagebox.showerror("Error","Flight date cannot be before Opening date")
        return
    new_flight=Flight(name,flight_type,capacity,o_d,c_d,f_d)
    bSystem.addflight(new_flight)
    user_flight_buttons()
    flight_name_box.delete(0,tk.END)
    flight_capacity_box.delete(0,tk.END)
    flight_bp_box.delete(0,tk.END)
    flight_type_box.delete(0,tk.END)
    flight_info.place_forget()
    added.place(relx=0.20,rely=0.1,relwidth=0.6,relheight=0.8)
    curr_page="added"
    added.after(2000,redirect_to_original_admin_frame)   

def remove_flight_frame():
    global curr_page
    admin_accessed_p1.place_forget()
    admin_accessed_p3.place(relx=0,rely=0,relwidth=1,relheight=1)
    flight_removal_list.place(relx=0.20,rely=0.1,relwidth=0.6,relheight=0.8)
    flight_list_creation()
    curr_page="flight_removal_list"
def confirmationScreen(flight):
    global selected_flight_1
    global curr_page
    selected_flight_1=flight
    flight_removal_list.place_forget()
    confirmation_screen.place(relx=0.20,rely=0.1,relwidth=0.6,relheight=0.8)
    curr_page="confirmation_screen"
    confirm_message.place(relx=0.5,rely=0.4,anchor="center")
    confirm_button.place(relx=0.6,rely=0.7,anchor="center",width=100,height=35)
    flight_cancel_button.place(relx=0.4,rely=0.7,anchor="center",width=100,height=35)
def confirmed(flight_name):
    global curr_page
    bSystem.removeFlight(flight_name)
    user_flight_buttons()
    #Code adapted from Claude(Anthropic,2026)
    #Prompt: How to ensure the back button does not get deleted here
    for c in flight_removal_list.winfo_children():
        if(c.cget("text")!="Back"):
            c.destroy()
    #End of adapted code        
    flight_list_creation()
    confirmation_screen.place_forget()
    flight_deleted.place(relx=0.20,rely=0.1,relwidth=0.6,relheight=0.8)
    curr_page="admin_accessed_p3"
    flight_deleted.after(2000,redirect_to_original_admin_frame)    
def prev_screen():
    global curr_page
    if(curr_page=="flight_info"):
        flight_info.place_forget()
        admin_accessed_p3.place_forget()
        admin_accessed_p1.place(relx=0,rely=0,relwidth=1,relheight=1)
        curr_page="admin_accessed_p1"
    elif(curr_page=="confirmation_screen"):
        confirmation_screen.place_forget()
        flight_removal_list.place(relx=0.20,rely=0.1,relwidth=0.6,relheight=0.8)
        curr_page="flight_removal_list"
    elif(curr_page=="revenue"):
        rev.place_forget()
        admin_accessed_p1.place(relx=0,rely=0,relwidth=1,relheight=1)
        curr_page="admin_accessed_p1"
    elif(curr_page=="flight_removal_list"):
        flight_removal_list.place_forget()
        admin_accessed_p3.place_forget()
        admin_accessed_p1.place(relx=0,rely=0,relwidth=1,relheight=1)
        curr_page="admin_accessed_p1"
def create_flight(name,type,closing_date,flight_d):
    open_date=current_time
    close_date=open_date+timedelta(days=closing_date)
    flight_date=open_date+timedelta(days=flight_d)
    return Flight(name, type, 150, open_date, close_date,flight_date)
            
bSystem=BookingSystem()
current_time = datetime.now()

flight1 = create_flight("GH123", "short", 29 ,30)
flight2 = create_flight("LX1174", "medium", 44,45)
flight3 = create_flight("JL42", "long",59,60)

bSystem.addflight(flight1)
bSystem.addflight(flight2)
bSystem.addflight(flight3)
ps1 = Passenger(1, "John", "07911111111")
ps2 = Passenger(2, "Sarah", "07922222222")
ps3 = Passenger(3, "Ahmed", "07933333333")

bSystem.add_passenger(ps1)
bSystem.add_passenger(ps2)
bSystem.add_passenger(ps3)       

frame=tk.Frame(root,bg="#E5DFC3",width=1440,height=100,bd=3)
frame.pack(fill="x")
frame.pack_propagate(False)
label=tk.Label(frame,text="Royal Flights",bg="#E5DFC3")
label.config(font=("Inter",24))
label.pack(expand="True",anchor="center")

notebook_style=ttk.Style()
notebook_style.theme_use("clam")
notebook_style.configure("TNotebook.Tab",background="#E5DFC3",padding=[10,8],bordercolor="black")
notebook_style.map("TNotebook.Tab",background=[("!selected","#E5DFC3"),("selected", "#6F8C9F")],padding=[("selected",20),("!selected",20)])
notebook_style.configure("TNotebook", background="#E5DFC3", tabmargins=[10,0,0,0], borderwidth=20,relief="solid",bordercolor="black")
notebook_style.configure("TFrame",background="#C3C9E5")
notebook=ttk.Notebook(root)

user_tab=ttk.Frame(notebook)
admin_tab=ttk.Frame(notebook)

notebook.add(user_tab,text="User")
notebook.add(admin_tab,text="Admin")


# =================================== USER SECTION ==============================================

selected_flight = None
selected_flight_obj = None
selected_seat=None
selected_date=None
customer_name = ""
customer_phone = ""
available_seats= 150
placeholder_ticket_price=400

base_price = {
    "short": {
        "First Class": 700,
        "Second Class": 250,
        "Third Class": 99
    },
    "medium": {
        "First Class": 2200,
        "Second Class": 600,
        "Third Class": 200
    },
    "long": {
        "First Class": 5200,
        "Second Class": 2400,
        "Third Class": 900
    }
}


def flight_frame():
    global curr_page
    

def seat_frame():
    flight_selection_pg.place_forget()
    seat_selection_pg.place(relx=0,rely=0,relwidth=1,relheight=1)

#chatgpt helped w/ this v
def show_pg(hide_page,show_page):
    hide_page.place_forget()
    show_page.place(relx=0,rely=0,relwidth=1,relheight=1)


def choose_flight(flight):
    global selected_flight, selected_flight_obj

    selected_flight = flight
    selected_flight_obj = bSystem.find_flight(flight)
    cal.config(
        mindate=datetime.now().date(),
        maxdate=selected_flight_obj.close_time.date()
    )
    show_pg(flight_selection_pg, seat_selection_pg)
    print("Selected flight:", flight)

def choose_seat(seat):
    global selected_seat
    selected_seat = seat
    show_pg(seat_selection_pg,date_selection_pg)

    print(seat)
#Code adapted from ChatGPT(OpenAI,2026).
#Prompt : how do fix the current update price info function
def update_price_info():
    global final_price

    if not selected_flight_obj or not selected_seat or not selected_date:
        print("Missing selection")
        return

    flight_obj = selected_flight_obj
    
    if flight_obj is None:
        print("Flight not found:", selected_flight)
        return
    

    big_T = flight_obj.get_proportional_time(selected_date)
    big_B = base_price[flight_obj.flg_type][selected_seat]

    price_obj = Price(big_B, big_T)
    final_price = price_obj.price_equation()

    flight_display.config(text=f"Flight: {selected_flight_obj.flg_number}")
    seat_display.config(text=f"Seat: {selected_seat}")
    date_display.config(text=f"Date: {selected_date.strftime('%d/%m/%Y %H:%M')}")
    availability_display.config(text=f"Available Seats: {flight_obj.availability()}")
    price_text_display.config(text=f"Price: £{round(final_price, 2)}")

    if not selected_flight or not selected_seat:
        print("Select flight and seat first")
        return

    if flight_obj.availability()<=0:
        messagebox.showerror("Error", "No seats available")
        return
    show_pg(date_selection_pg, price_pg)

    print("update_price_info ran")
#End of adapted code

#Code adapted from ChatGPT(OpenAI,2026).
#Prompt : given the current backend code how do i change the current booking confirmed function to fit this?
def booking_confirmed():
    flight_obj = selected_flight_obj

    if flight_obj is None:
        messagebox.showerror("Error", "Flight not found")
        return

    if flight_obj.availability() <= 0:
        messagebox.showerror("Error", "Flight is full")
        return

    booking_id = len(flight_obj.bookings) + 1

    booking = Booking(
        booking_id,
        Passenger(0, customer_name, customer_phone),
        flight_obj,
        selected_seat,
        final_price
    )

    flight_obj.add_booking(booking, datetime.now())
    bSystem.bookings.append(booking)
    show_pg(customer_info_pg, confirmed_pg)

    confirmed_pg.after(2000, return_home)
#End of adapted code
def confirm_date():
    global selected_date

    selected_date = datetime.combine(cal.selection_get(), datetime.now().time())


    print("DEBUG selected_date =", selected_date)
    update_price_info()

def refresh_date():
    cal.selection_set(cal.get_date())
    show_pg(price_pg,date_selection_pg)


def process_customer_info():
    global customer_name
    global customer_phone
    global customer_passport

    customer_name = name_entry.get().strip()
    customer_phone = phone_entry.get().strip()
    customer_passport = passport_entry.get().strip()
    if customer_name == "":
        messagebox.showerror("Error","Please enter a name")
        return
        #gpt
    elif not customer_name.replace(" ","").isalpha():
        messagebox.showerror("Error","Please enter a valid Name")
        return 

    if customer_phone == "":
        messagebox.showerror("Error","Please enter a phone number")
        return
    elif not customer_phone.isdigit() or not (len(customer_phone)>9 and len(customer_phone)<12):
        messagebox.showerror("Error","Please enter a valid Phone Number")
        return
    if customer_passport == "":
        messagebox.showerror("Error","Please enter your passport number")
        return
    elif not customer_passport.isalnum() or  len(customer_passport)!=9:
        messagebox.showerror("Error","Passport number needs to be both Alphanumeric and 9 characters long.")
        return


    booking_confirmed()

def reset_booking_flow():
    global selected_flight_obj, selected_seat, selected_date, customer_name, customer_phone, final_price

    selected_flight_obj = None
    selected_seat = None
    selected_date = None
    customer_name = ""
    customer_phone = ""
    final_price = 0

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    passport_entry.delete(0,tk.END)
    cal.selection_set(datetime.now().date())
    cal.see(datetime.now().date())
    flight_display.config(text="")
    seat_display.config(text="")
    date_display.config(text="")
    price_text_display.config(text="")
    availability_display.config(text="")

def return_home():
    print("Returning to flight selection")
    reset_booking_flow()
    show_pg(confirmed_pg, flight_selection_pg)


# def compute_T(open_date, close_date, selected_date):
#     total = (close_date - open_date).days
#     if total <= 0:
#         return 1

#     raw = (selected_date - open_date).days / total
#     return max(0.0001, min(1, raw))



# Code adapted from Claude(Anthropic,2026).
#Prompt: the image file is in the project folder of gitlab. how to ensure any laptop that clones it can access the image file dynamically 

Base_Dir=os.path.dirname(os.path.abspath(__file__))
Image_Path=os.path.join(Base_Dir,"Pictures","check-solid-full (1).png")
right_tick_pil=Image.open(Image_Path)
right_tick_pil_re=right_tick_pil.resize((40,40))
#End of adapted code
right_tick_tk=ImageTk.PhotoImage(right_tick_pil_re)

#flight page
flight_selection_pg=tk.Frame(user_tab,bg="#C3C9E5")
flight_title = tk.Label(flight_selection_pg, text="Select Flight", font=("Inter", 20), bg="#C3C9E5")
flight_selection_pg.place(relx=0,rely=0,relwidth=1,relheight=1)
flight_title.place(relx=0.5, rely=0.1, anchor="center")


#seat page
seat_options = ["First Class", "Second Class", "Third Class"]
seat_selection_pg = tk.Frame(user_tab,bg="#C3C9E5")
seat_title = tk.Label(seat_selection_pg, text="Select a Seat",font=("Inter", 20), bg="#C3C9E5")

seat_title.place(relx=0.5, rely=0.1, anchor="center")

for i in range (len(seat_options)):
    curr_seat = seat_options[i]
    seat_button = tk.Button(seat_selection_pg,text=curr_seat, font=('Inter',14), bg="#E5DFC3",command=lambda bozo=curr_seat: choose_seat(bozo))
    seat_button.place(relx=0.5,rely=0.35 +(i* 0.12),anchor="center",width=250,height=45)

seat_back_button=tk.Button(seat_selection_pg,text="Back",bg="#8C6BD8",font=("Inter",20),command=lambda:show_pg(seat_selection_pg,flight_selection_pg))
seat_back_button.place(relx=0.5,rely=0.8,anchor="center")


#calander

date_selection_pg = tk.Frame(user_tab,bg="#C3C9E5")
date_title = tk.Label(date_selection_pg,text="Select a date",font=("Inter", 20), bg= "#C3C9E5")
date_title.place(relx=0.5,rely=0.1,anchor="center")
cal = Calendar(date_selection_pg,selectmode='day',mindate=datetime.now().date(), font=("Inter", 20), width=30,height=15)
cal.place(relx=0.5,rely=0.45,anchor="center")
# selected_date_str = cal.get_date()

date_back_button=tk.Button(date_selection_pg,text="Back",bg="#8C6BD8",font=("Inter",20),command=lambda:show_pg(date_selection_pg,seat_selection_pg))
date_back_button.place(relx=0.4,rely=0.8,anchor="center")
# date_label = tk.Label(date_selection_pg,text="No date selected",font=("Inter", 12),bg="#C3C9E5")

# date_label.place(relx=0.5,rely=0.62,anchor="center")

confirm_date_button = tk.Button(date_selection_pg,text="Confirm Date",font=("Inter",20),command=confirm_date)
confirm_date_button.place(relx=0.6,rely=0.8,anchor="center")

#customer info
customer_info_pg = tk.Frame(user_tab, bg="#C3C9E5")

customer_info_card = tk.Frame(customer_info_pg, bg="#E5DFC3")
customer_info_card.place(relx=0.5, rely=0.5, anchor="center",width=900, height=600)

customer_title = tk.Label(customer_info_card,text="Customer Information",font=("Inter", 20),bg="#E5DFC3")
customer_title.place(relx=0.5, rely=0.1, anchor="center")

name_label = tk.Label(customer_info_card,text="Full Name",font=("Inter", 14),bg="#E5DFC3")
name_label.place(relx=0.2, rely=0.25)

name_entry = tk.Entry(customer_info_card,font=("Inter", 14))
name_entry.place(relx=0.45, rely=0.25,width=250)

phone_label = tk.Label(customer_info_card,text="Phone Number",font=("Inter", 14),bg="#E5DFC3")
phone_label.place(relx=0.2, rely=0.4)

phone_entry = tk.Entry(customer_info_card,font=("Inter", 14))
phone_entry.place(relx=0.45, rely=0.4,width=250)

passport_label = tk.Label(customer_info_card,text="Passport Number",font=("Inter", 14),bg="#E5DFC3")
passport_label.place(relx=0.2, rely=0.55)
passport_entry = tk.Entry(customer_info_card,font=("Inter", 14))
passport_entry.place(relx=0.45, rely=0.55,width=250)

customer_back_button = tk.Button(customer_info_card,text="Back",font=("Inter", 20),bg="#8C6BD8",command=lambda: show_pg(customer_info_pg,price_pg))
customer_back_button.place(relx=0.35, rely=0.8)

customer_next_button = tk.Button(customer_info_card,text="Next",font=("Inter", 20),command=lambda: process_customer_info())
customer_next_button.place(relx=0.55, rely=0.8)

#price$$$

price_pg = tk.Frame(user_tab,bg="#C3C9E5")
price_card= tk.Frame(price_pg,bg="#E5DFC3")

price_card.place(relx=0.5,rely=0.5,anchor="center",width=700,height=420)

flight_display=tk.Label(price_card,text="",font=("Inter",16),bg="#E5DFC3")
seat_display=tk.Label(price_card,text="",font=("Inter",16),bg="#E5DFC3")
availability_display = tk.Label(price_card, text="", font=("Inter",16), bg="#E5DFC3")
availability_display.place(x=50, y=300)
date_display=tk.Label(price_card,text="",font=("Inter",16),bg="#E5DFC3")
price_text_display=tk.Label(price_card,text="",font=("Inter",16),bg="#E5DFC3")

flight_display.place(x=50,y=60)
seat_display.place(x=50,y=120)
date_display.place(x=50,y=180)
price_text_display.place(x=50,y=240)

back_button=tk.Button(price_card,text="Back",bg="#8C6BD8",font=("Inter",12),command=lambda: show_pg(price_pg,date_selection_pg))
back_button.place(x=220,y=340,width=100,height=40)

next_button=tk.Button(price_card,text="Next",font=("Inter",12),command=lambda: show_pg(price_pg,customer_info_pg))
next_button.place(x=380,y=340,width=100,height=40)



#booking confirmed page

confirmed_pg=tk.Frame(user_tab,bg="#C3C9E5")
confirmed_card=tk.Frame(confirmed_pg,bg="#E5DFC3")
confirmed_card.place(relx=0.5,rely=0.5,anchor="center",width=700,height=420)

booking_confirmed_tick=tk.Label(confirmed_card,image=right_tick_tk,bg="#E5DFC3")
booking_confirmed_tick.place(relx=0.3,rely=0.5,anchor="center")

confirmed_text=tk.Label(confirmed_card,text="Booking Confirmed",font=("Inter",18),bg="#E5DFC3")
confirmed_text.place(relx=0.5,rely=0.5,anchor="center")



#=================================================== END OF USER SECTION =============================================================

sign_up_page=tk.Frame(admin_tab)
sign_up_page.config(bg="#C3C9E5")
sign_up_page.place(relx=0,rely=0,relwidth=1,relheight=1)
pass_reset_pg=tk.Frame(admin_tab)
pass_reset_pg.config(bg="#C3C9E5")


username=tk.Label(sign_up_page,text="Username")
username.config(font=("Inter",18),bg="#C3C9E5")
username.place(relx=0.5,rely=0.3,anchor="center")
username_box=tk.Entry(sign_up_page)
username_box.config(bg="white",fg="black",font=("Inter",14))
username_box.place(relx=0.5,rely=0.37,anchor="center",width=250,height=30)
password=tk.Label(sign_up_page,text="Password")
password.config(font=("Inter",18),bg="#C3C9E5")
password.place(relx=0.5,rely=0.45,anchor="center")
password_box=tk.Entry(sign_up_page)
password_box.config(bg="white",fg="black",show="*",font=("Inter",14))
password_box.place(relx=0.5,rely=0.52,anchor="center",width=250,height=30)
sign_in=tk.Button(sign_up_page,text="Sign-in",command=signin)
sign_in.place(relx=0.5,rely=0.59,anchor="center")
reset_password=tk.Button(sign_up_page,text="Reset Password",command=lambda: show_pg(sign_up_page,pass_reset_pg))
reset_password.place(relx=0.5,rely=0.66,anchor="center")

res_username=tk.Label(pass_reset_pg,text="Username")
res_username.config(font=("Inter",18),bg="#C3C9E5")
res_username.place(relx=0.5,rely=0.3,anchor="center")
res_username_box=tk.Entry(pass_reset_pg)
res_username_box.config(bg="white",fg="black",font=("Inter",14))
res_username_box.place(relx=0.5,rely=0.37,anchor="center",width=250,height=30)
prev_password=tk.Label(pass_reset_pg,text="Previous Password")
prev_password.config(font=("Inter",18),bg="#C3C9E5")
prev_password.place(relx=0.5,rely=0.45,anchor="center")
prev_password_box=tk.Entry(pass_reset_pg)
prev_password_box.config(bg="white",fg="black",show="*",font=("Inter",14))
prev_password_box.place(relx=0.5,rely=0.52,anchor="center",width=250,height=30)
new_password=tk.Label(pass_reset_pg,text="New Password")
new_password.config(font=("Inter",18),bg="#C3C9E5")
new_password.place(relx=0.5,rely=0.59,anchor="center")
new_password_box=tk.Entry(pass_reset_pg)
new_password_box.config(bg="white",fg="black",show="*",font=("Inter",14))
new_password_box.place(relx=0.5,rely=0.65,anchor="center",width=250,height=30)
confirm_pass=tk.Button(pass_reset_pg,text="Confirm",command=change_password)
confirm_pass.place(relx=0.55,rely=0.72,anchor="center")
cancel_pass=tk.Button(pass_reset_pg,text="Cancel",command=lambda: show_pg(pass_reset_pg,sign_up_page))
cancel_pass.place(relx=0.45,rely=0.72,anchor="center")
admin_accessed_p1=ttk.Frame(admin_tab)
revenue_button=tk.Button(admin_accessed_p1,text="Revenue",command=revenue_frame,font=("Inter",14),bg="#E5DFC3",bd=3,relief="solid")
add_button=tk.Button(admin_accessed_p1,text="Add Flight",command=add_flight_frame,font=("Inter",14),bg="#E5DFC3",bd=3,relief="solid")
remove_button=tk.Button(admin_accessed_p1,text="Remove Flight",command=remove_flight_frame,font=("Inter",14),bg="#E5DFC3",bd=3,relief="solid")
revenue_button.place(relx=0.5,rely=0.37,anchor="center",width=300,height=60)
add_button.place(relx=0.5,rely=0.5,anchor="center",width=300,height=60)
remove_button.place(relx=0.5,rely=0.63,anchor="center",width=300,height=60)

admin_accessed_p3=ttk.Frame(admin_tab)
rev=ttk.Frame(admin_tab)
#Code adapted from Claude(Anthropic,2026)
#Prompt:how to add a bar chart in tkinter. help me set it up
revFig=Figure(figsize=(5,4),dpi=100)
grid=revFig.add_subplot(111)

canvas=FigureCanvasTkAgg(revFig,master=rev)
canvas.draw()
canvas.get_tk_widget().place(relx=0.1,rely=0.1,relwidth=0.75,relheight=0.7)
#end of adapted code
revenue_back_button=tk.Button(rev,text="Back",bg="#8C6BD8",font=("Inter",20),command=prev_screen)
revenue_back_button.place(relx=0.4,rely=0.9,width=100,height=40)
flight_info=tk.Frame(admin_accessed_p3)
flight_info.config(bg="#E5DFC3")
flight_name=tk.Label(flight_info,text="Flight Name",font=("Inter",14),bg="#E5DFC3")
flight_name.place(relx=0.1,rely=0.1)
flight_name_box=tk.Entry(flight_info)
flight_name_box.config(font=("Inter",18),bg="white")
flight_name_box.place(relx=0.1,rely=0.17)
flight_type=tk.Label(flight_info,text="Type",font=("Inter",14),bg="#E5DFC3")
flight_type.place(relx=0.1,rely=0.24)
flight_type_box=tk.Entry(flight_info)
flight_type_box.config(font=("Inter",18),bg="white")
flight_type_box.place(relx=0.1,rely=0.31)

flight_capacity=tk.Label(flight_info,text="Capacity",font=("Inter",14),bg="#E5DFC3")
flight_capacity.place(relx=0.1,rely=0.38)
flight_capacity_box=tk.Entry(flight_info)
flight_capacity_box.config(font=("Inter",18),bg="white")
flight_capacity_box.place(relx=0.1,rely=0.45)
flight_bp=tk.Label(flight_info,text="Base Price",font=("Inter",14),bg="#E5DFC3")
flight_bp.place(relx=0.1,rely=0.52)
flight_bp_box=tk.Entry(flight_info)
flight_bp_box.config(font=("Inter",18),bg="white")
flight_bp_box.place(relx=0.1,rely=0.59)
flight_booking_open=tk.Label(flight_info,text="Booking opens",font=("Inter",14),bg="#E5DFC3")
flight_booking_open.place(relx=0.6,rely=0.1)
#code adapted from Claude(Anthropic,2026).
#Prompt:how to add dates in a tkinter frame
open_date=DateEntry(flight_info,mindate=datetime.now().date())
#end of adapted code
open_date.place(relx=0.6,rely=0.17)
flight_booking_close=tk.Label(flight_info,text="Booking closes",font=("Inter",14),bg="#E5DFC3")
flight_booking_close.place(relx=0.6,rely=0.24)
close_date=DateEntry(flight_info,mindate=datetime.now().date()+timedelta(days=1))
close_date.place(relx=0.6,rely=0.31)
flight_departure=tk.Label(flight_info,text="Flight Departs",font=("Inter",14),bg="#E5DFC3")
flight_departure.place(relx=0.6,rely=0.38)
flight_date=DateEntry(flight_info,mindate=datetime.now().date()+timedelta(days=2))
flight_date.place(relx=0.6,rely=0.45)

next_button=tk.Button(flight_info,text="next",font=("Inter",18),bg="#6F8C9F",command=flight_added)
next_button.place(relx=0.8,rely=0.8, width=100,height=30)
cancel_button=tk.Button(flight_info,text="cancel",font=("Inter",18),bg="red",command=prev_screen)
cancel_button.place(relx=0.68,rely=0.8, width=100,height=30)

added=tk.Frame(admin_accessed_p3)
added.config(bg="#E5DFC3")
right_tick=tk.Label(added,image=right_tick_tk,bg="#E5DFC3")
right_tick.place(relx=0.38,rely=0.5,anchor="center")
flight_added_label=tk.Label(added,text="Flight Added",font=("Inter",18),bg="#E5DFC3")
flight_added_label.place(relx=0.5,rely=0.5,anchor="center")

flight_removal_list=tk.Frame(admin_accessed_p3)
flight_removal_list.config(bg="#E5DFC3")
flight_removal_back_button=tk.Button(flight_removal_list,text="Back",bg="#8C6BD8",font=("Inter",20),command=prev_screen)
flight_removal_back_button.place(relx=0.5,rely=0.9,width=100,height=40)


confirmation_screen=tk.Frame(admin_accessed_p3)
confirmation_screen.config(bg="#E5DFC3")
confirm_message=tk.Label(confirmation_screen,text="Confirm Deletion?",font=("Inter",14),bg="#E5DFC3")     
confirm_button=tk.Button(confirmation_screen,text="Confirm",font=("Inter",18),bg="red",command=lambda: confirmed(selected_flight_1))
flight_cancel_button=tk.Button(confirmation_screen,text="cancel",font=("Inter",18),bg="grey",command=prev_screen)
flight_deleted=tk.Frame(admin_accessed_p3)
flight_deleted.config(bg="#E5DFC3")
right_tick2=tk.Label(flight_deleted,image=right_tick_tk,bg="#E5DFC3")
right_tick2.place(relx=0.38,rely=0.5,anchor="center")
flight_d=tk.Label(flight_deleted,text="Flight Deleted",font=("Inter",18),bg="#E5DFC3")
flight_d.place(relx=0.5,rely=0.5,anchor="center")




user_flight_buttons()
notebook.pack(expand="1",fill="both")

root.mainloop()