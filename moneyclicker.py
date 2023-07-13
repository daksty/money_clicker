import tkinter as tk

def upgh():
    global money_ad, money_val, upgc
    if money_val == upgc or money_val >= upgc:
        money_val -= upgc
        money_ad *= 1.6
        upgc *= 1.8
        upgr_lel.config(text="Upgrade money adder" + "    " + format_money(upgc))
        money.config(text=format_money(money_val))
        statmoney.config(text = "Current money adder: " + format_money(money_ad))

def statschanger():
    global choosed
    if not choosed == "stats":
        choosed = "stats"
        changer()


def shopchanger():
    global choosed
    if not choosed == "shop":
        choosed = "shop"
        changer()


def homechanger():
    global choosed
    if not choosed == "home":
        choosed = "home"
        changer()

def forgetall():
    money.pack()
    money.pack_forget()
    money_add.pack()
    money_add.pack_forget()
    whit.pack()
    whit.pack_forget()
    upgr_lel.pack()
    upgr_lel.pack_forget()
    upgr.pack()
    upgr.pack_forget()
    shopt.pack()
    shopt.pack_forget()
    statmoney.pack()
    statmoney.pack_forget()


def changer():

    if choosed == "home":
        forgetall()
        mainbut.config(bg="blue")
        shopbut.config(bg="white")
        statsbutton.config(bg="white")
        money.place(y=50, x=50)
        money_add.place(y=570, x=30)
    elif choosed == "shop":
        forgetall()
        shopbut.config(bg="blue")
        mainbut.config(bg="white")
        statsbutton.config(bg="white")
        upgr_lel.place(y=270, x=50)
        upgr.place(y=260, x=500)
        whit.place(y=150, x=18)
        shopt.place(y = 160, x = 260)
    elif choosed == "stats":
        forgetall()
        statsbutton.config(bg="blue")
        shopbut.config(bg="white")
        mainbut.config(bg="white")
        whit.place(y = 150,x = 18)
        statmoney.place(y = 170, x = 70)


def func():
    global money_val, money_ad
    money_val += money_ad
    money.config(text=format_money(money_val))

def format_money(money_val):
    if money_val >= 1e9:
        return f"{money_val / 1e9:.2f}B"
    elif money_val >= 1e6:
        return f"{money_val / 1e6:.2f}M"
    elif money_val >= 1e3:
        return f"{money_val / 1e3:.2f}K"
    else:
        return f"{money_val:.2f}"

w = tk.Tk()
w.config(bg="blue")

choosed = "home"
money_val = 0.0
money_ad = 1.0
upgc = 1000.0

down_label = tk.Label(w, width=50, height=3, bg="white")
down_label.place(y=1352)

money = tk.Label(w, text=format_money(money_val), bg="white", font=("ariel", 20, "bold"), width=14, height=5)
money.place(y=50, x=50)

money_add = tk.Button(w, text="Add money", font=("ariel", 10, "bold"), width=27, height=15, bg="white", command=func)
money_add.place(y=570, x=30)

mainbut = tk.Button(w, text="Home", width=4, height=2, bg="white", relief="sunken", command=homechanger)
mainbut.place(y=1360, x=300)
shopbut = tk.Button(w, text="Shop", width=4, height=2, bg="white", relief="sunken", command=shopchanger)
shopbut.place(y=1360, x=450)

statsbutton = tk.Button(w, text="Business", width=4, height=2, relief="sunken", bg="white", command=statschanger)
statsbutton.place(y=1360, x=150)

whit = tk.Label(w, width=40, height=30, bg="white")

upgr = tk.Button(w, text="Buy", relief="ridge", width=2, height=1, bg="white", command=upgh)
upgr_lel = tk.Label(w, text="Upgrade money adder" + "    " + format_money(upgc), bg="white", font=("airlel", 7, "bold"))

shopt = tk.Label(w, text = "SHOP", bg = "white", font = ("ariel",20,"bold"))

statmoney = tk.Label(w, text = "Current money adder:  " + format_money(money_ad), bg = "white", font = ("",10,"bold"))

changer()
w.mainloop()
