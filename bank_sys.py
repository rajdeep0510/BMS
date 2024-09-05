from tkinter import *
#import new_account
font_size = 15


def new_account():

    f_new_acc = Frame(root, bg='#CBF1F5', bd=5)
    f_new_acc.place(x=100,y=135, width=800, height=500)

    username = Label(f_new_acc, text="Username", font=('Arial',font_size))
    username.place(x=150,y=50,)
    value_uname = Entry(f_new_acc, bd=2 , width=15, font=('Arial',font_size))
    value_uname.place(x=400, y=50,)

    password = Label(f_new_acc, text="password", font=('Arial',font_size))
    password.place(x=150, y=150,)
    value_pass = Entry(f_new_acc, bd=2 , width=15, font=('Arial',font_size))
    value_pass.place(x=400, y=150,)

    confirm_pass = Label(f_new_acc, text="Confirm password", font=('Arial',font_size))
    confirm_pass.place(x=150, y=250,)
    value_cpass = Entry(f_new_acc, bd=2 , width=15, font=('Arial',font_size))
    value_cpass.place(x=400, y=250,)

    submit_btw = Button(f_new_acc,text="submit", width=20, height=3)
    submit_btw.place(x=150, y=350)

    close = Button(f_new_acc,text="close", width=20, height=3, command=f_new_acc.destroy)
    close.place(x=550, y=350)
    


def deposit():
    #Todo : change layout of the frame

    f_deposit = Frame(root, bg='#CBF1F5', bd=5)
    f_deposit.place(x=100,y=135, width=800, height=500)

    username = Label(f_deposit, text="Username", font=('Arial',font_size))
    username.place(x=150,y=50,)
    value_uname = Entry(f_deposit, bd=2 , width=15, font=('Arial',font_size))
    value_uname.place(x=400, y=50,)
    
    amount = Label(f_deposit,text="Amount", font=('Arial',font_size))
    amount.place(x=150,y=100)
    value_amount = Entry(f_deposit, bd=2 , width=15, font=('Arial',font_size))
    value_amount.place(x=400, y=100)

    password = Label(f_deposit, text="password", font=('Arial',font_size))
    password.place(x=150, y=150,)
    value_pass = Entry(f_deposit, bd=2 , width=15, font=('Arial',font_size))
    value_pass.place(x=400, y=150,)

    send_btw = Button(f_deposit,text="Send", width=20, height=3)
    send_btw.place(x=150, y=350)

    close = Button(f_deposit,text="close", width=20, height=3, command=f_deposit.destroy)
    close.place(x=550, y=350)


def withdraw():

    f_withdraw = Frame(root, bg='#CBF1F5', bd=5)
    f_withdraw.place(x=100,y=135, width=800, height=500)

    username = Label(f_withdraw, text="Username", font=('Arial',font_size))
    username.place(x=150,y=50,)
    value_uname = Entry(f_withdraw, bd=2 , width=15, font=('Arial',font_size))
    value_uname.place(x=400, y=50,)
    
    amount = Label(f_withdraw,text="Amount", font=('Arial',font_size))
    amount.place(x=150,y=100)
    value_amount = Entry(f_withdraw, bd=2 , width=15, font=('Arial',font_size))
    value_amount.place(x=400, y=100)

    password = Label(f_withdraw, text="password", font=('Arial',font_size))
    password.place(x=150, y=150,)
    value_pass = Entry(f_withdraw, bd=2 , width=15, font=('Arial',font_size))
    value_pass.place(x=400, y=150)

    withdraw_btw = Button(f_withdraw,text="Withdraw", width=20, height=3)
    withdraw_btw.place(x=150, y=350)

    close = Button(f_withdraw,text="close", width=20, height=3, command=f_withdraw.destroy)
    close.place(x=550, y=350)




root = Tk()

root.geometry("1000x700")
root.config(bg='')                                       #! add approate background color

main_title = Label(root,
                   text="Bank Management System",
                   font=("Arial", 40),
                   #bg='------',                         #! add approate background color
                   relief='groove',borderwidth=2,         #BORDER
                   )
main_title.pack(side="top", fill="x")

#TODO : THIS IS THE MASTER 
master = Frame(root, bg='#CBF1F5', bd=5)
master.place(x=100,y=135, width=800, height=500)

#BUTTONS
new_account = Button(master,
                     text="Open New Account",
                     width=100, height=5,
                     command=new_account)
new_account.pack(padx=30,pady=40)

deposit = Button(master,
                     text="Deposit",
                     width=100, height=5,
                     command = deposit)
deposit.pack(padx=30,pady=40)

Withdraw = Button(master,
                     text="Withdraw",
                     width=100, height=5,
                     command=withdraw)
Withdraw.pack(padx=30,pady=40)



root.mainloop()