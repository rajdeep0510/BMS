from tkinter import *
from tkinter import messagebox
import pymysql
import mail


#import new_account
font_size = 15

#---------GUI for three buttons----------------
def new_account():

    global value_uname
    global value_email
    global value_pass
    global value_cpass

    f_new_acc = Frame(root, bg='#CBF1F5', bd=5)
    f_new_acc.place(x=100,y=135, width=800, height=500)

    username = Label(f_new_acc, text="Username", font=('Arial',font_size))
    username.place(x=150,y=50,)
    value_uname = Entry(f_new_acc, bd=2 , width=15, font=('Arial',font_size))
    value_uname.place(x=400, y=50,)

    email = Label(f_new_acc, text="Email", font=('Arial',font_size))
    email.place(x=150,y=100,)
    value_email = Entry(f_new_acc, bd=2 , width=15, font=('Arial',font_size))
    value_email.place(x=400, y=100,)


    password = Label(f_new_acc, text="password", font=('Arial',font_size))
    password.place(x=150, y=150,)
    value_pass = Entry(f_new_acc, bd=2 , width=15, font=('Arial',font_size))
    value_pass.place(x=400, y=150,)

    confirm_pass = Label(f_new_acc, text="Confirm password", font=('Arial',font_size))
    confirm_pass.place(x=150, y=200,)
    value_cpass = Entry(f_new_acc, bd=2 , width=15, font=('Arial',font_size))
    value_cpass.place(x=400, y=200,)

    submit_btw = Button(f_new_acc,text="submit", width=20, height=3, command=insert)
    submit_btw.place(x=150, y=350)

    close = Button(f_new_acc,text="close", width=20, height=3, command=f_new_acc.destroy)
    close.place(x=550, y=350)


def deposit():
    #Todo : change layout of the frame
    global value_uname_depo
    global value_amount_depo
    global value_pass_depo

    f_deposit = Frame(root, bg='#CBF1F5', bd=5)
    f_deposit.place(x=100,y=135, width=800, height=500)

    username_deposit = Label(f_deposit, text="Username", font=('Arial',font_size))
    username_deposit.place(x=150,y=50,)
    value_uname_depo = Entry(f_deposit, bd=2 , width=15, font=('Arial',font_size))
    value_uname_depo.place(x=400, y=50,)
    
    amount = Label(f_deposit,text="Amount", font=('Arial',font_size))
    amount.place(x=150,y=100)
    value_amount_depo = Entry(f_deposit, bd=2 , width=15, font=('Arial',font_size))
    value_amount_depo.place(x=400, y=100)

    password_deposit = Label(f_deposit, text="password", font=('Arial',font_size))
    password_deposit.place(x=150, y=150,)
    value_pass_depo = Entry(f_deposit, bd=2 , width=15, font=('Arial',font_size))
    value_pass_depo.place(x=400, y=150,)

    send_btw = Button(f_deposit,text="Send", width=20, height=3, command=deposit_fun)
    send_btw.place(x=150, y=350)

    close = Button(f_deposit,text="close", width=20, height=3, command=f_deposit.destroy)
    close.place(x=550, y=350)


def withdraw():

    global value_uname_wd
    global value_amount_wd
    global value_pass_wd

    f_withdraw = Frame(root, bg='#CBF1F5', bd=5)
    f_withdraw.place(x=100,y=135, width=800, height=500)

    username = Label(f_withdraw, text="Username", font=('Arial',font_size))
    username.place(x=150,y=50,)
    value_uname_wd = Entry(f_withdraw, bd=2 , width=15, font=('Arial',font_size))
    value_uname_wd.place(x=400, y=50,)
    
    amount = Label(f_withdraw,text="Amount", font=('Arial',font_size))
    amount.place(x=150,y=100)
    value_amount_wd = Entry(f_withdraw, bd=2 , width=15, font=('Arial',font_size))
    value_amount_wd.place(x=400, y=100)

    password = Label(f_withdraw, text="password", font=('Arial',font_size))
    password.place(x=150, y=150,)
    value_pass_wd = Entry(f_withdraw, bd=2 , width=15, font=('Arial',font_size))
    value_pass_wd.place(x=400, y=150)

    withdraw_btw = Button(f_withdraw,text="Withdraw", width=20, height=3, command=withdraw_fun)
    withdraw_btw.place(x=150, y=350)

    close = Button(f_withdraw,text="close", width=20, height=3, command=f_withdraw.destroy)
    close.place(x=550, y=350)


def stf():

    global value_sender_username_stf
    global value_reciver_username_stf
    global value_amount_stf
    global value_password_stf
    

    f_stf = Frame(root, bg='#CBF1F5', bd=5)
    f_stf.place(x=100,y=135, width=800, height=500)

    sender_username_stf = Label(f_stf, text="Sender Username", font=('Arial',font_size))
    sender_username_stf.place(x=150,y=50,)
    value_sender_username_stf= Entry(f_stf, bd=2 , width=15, font=('Arial',font_size))
    value_sender_username_stf.place(x=400, y=50,)

    reciver_username_stf = Label(f_stf, text="Reciver Username", font=('Arial',font_size))
    reciver_username_stf.place(x=150,y=100,)
    value_reciver_username_stf = Entry(f_stf, bd=2 , width=15, font=('Arial',font_size))
    value_reciver_username_stf.place(x=400, y=100,)

    amount_stf = Label(f_stf, text="Amount", font=('Arial',font_size))
    amount_stf.place(x=150,y=150,)
    value_amount_stf = Entry(f_stf, bd=2 , width=15, font=('Arial',font_size))
    value_amount_stf.place(x=400, y=150,)

    password_stf = Label(f_stf, text="Password", font=('Arial',font_size))
    password_stf.place(x=150,y=200,)
    value_password_stf = Entry(f_stf, bd=2 , width=15, font=('Arial',font_size))
    value_password_stf.place(x=400, y=200,)


    send_btw = Button(f_stf,text="Send", width=20, height=3, command=stf_fun)
    send_btw.place(x=150, y=350)

    close = Button(f_stf,text="close", width=20, height=3, command=f_stf.destroy)
    close.place(x=550, y=350)


def acc_info():

    global value_uname_info
    global value_pass_info

    
    f_acc_info = Frame(root, bg='#CBF1F5', bd=5)
    f_acc_info.place(x=100,y=135, width=800, height=500)

    username_info = Label(f_acc_info, text="Username", font=('Arial',font_size))
    username_info.place(x=150,y=50,)
    value_uname_info = Entry(f_acc_info, bd=2 , width=15, font=('Arial',font_size))
    value_uname_info.place(x=400, y=50,)

    password_info = Label(f_acc_info, text="password", font=('Arial',font_size))
    password_info.place(x=150, y=100,)
    value_pass_info = Entry(f_acc_info, bd=2 , width=15, font=('Arial',font_size))
    value_pass_info.place(x=400, y=100,)

    go_btw = Button(f_acc_info,text="GO", width=20, height=3, command=info_fun)
    go_btw.place(x=150, y=350)

    close = Button(f_acc_info,text="Close", width=20, height=3, command=f_acc_info.destroy)
    close.place(x=550, y=350)




#-----------Functions--------------------
def insert():
    uName = value_uname.get()
    uEmail = value_email.get()
    uPW = value_pass.get()
    confirmPW =  value_cpass.get()
    first_depo = 0

    if uPW == confirmPW:
        con = pymysql.connect(host="localhost", user="root", passwd="rajdeep0510", database="bank_db")
        cur = con.cursor()
        cur.execute("INSERT INTO account(userName, userPW, balance, email) VALUES(%s,%s,%s,%s)", (uName,uPW,first_depo,uEmail))
        con.commit()
        con.close()
        messagebox.showinfo("SUCCESS", "Your Account was created successfully")
        clear()
    else:
        messagebox.showerror("Error", "Both password should be same")
        clear()

def clear():
    value_uname.delete(0,END)
    value_email.delete(0,END)
    value_pass.delete(0,END)
    value_cpass.delete(0,END)
    

def deposit_fun():

    uname_depo = value_uname_depo.get()
    amount_depo = int(value_amount_depo.get())
    password_depo = value_pass_depo.get()

    con = pymysql.connect(host="localhost", user="root", passwd="rajdeep0510", database="bank_db")
    cur = con.cursor()
    cur.execute("SELECT userPW FROM account WHERE userName = %s", uname_depo)
    result = cur.fetchone()


    if result[0] == password_depo:
        cur.execute("UPDATE account SET balance = balance + %s WHERE userName = %s",(amount_depo, uname_depo))
        con.commit()
        con.close()
        messagebox.showinfo("SUCCESS", "Money deposited successfully")
        clear_depo()
    else:
        messagebox.showerror("Error", "Password was incorrect")
        con = pymysql.connect(host="localhost", user="root", passwd="rajdeep0510", database="bank_db")
        cur = con.cursor()
        cur.execute("SELECT email FROM account WHERE userName = %s", uname_depo)
        email = cur.fetchone()
        mail.security_mail(email[0])
        clear_depo()

def clear_depo():

    value_uname_depo.delete(0,END)
    value_amount_depo.delete(0,END)
    value_pass_depo.delete(0,END)


def withdraw_fun():

    uname_wd = value_uname_wd.get()
    amount_wd = int(value_amount_wd.get())
    password_wd = value_pass_wd.get()

    con = pymysql.connect(host="localhost", user="root", passwd="rajdeep0510", database="bank_db")
    cur = con.cursor()
    cur.execute("SELECT userPW FROM account WHERE userName = %s", uname_wd)
    result = cur.fetchone()


    if result[0] == password_wd:
        cur.execute("UPDATE account SET balance = balance - %s WHERE userName = %s",(amount_wd, uname_wd))
        con.commit()
        con.close()
        messagebox.showinfo("SUCCESS", "Money withdraw successfully")
        clear_wd()
    else:
        messagebox.showerror("Error", "Password was incorrect")
        con = pymysql.connect(host="localhost", user="root", passwd="rajdeep0510", database="bank_db")
        cur = con.cursor()
        cur.execute("SELECT email FROM account WHERE userName = %s", uname_wd)
        email = cur.fetchone()
        mail.security_mail(email[0])

        clear_wd()

def clear_wd():

    value_uname_wd.delete(0,END)
    value_amount_wd.delete(0,END)
    value_pass_wd.delete(0,END)


def stf_fun():
    sender_uName_stf = value_sender_username_stf.get()
    reciver_uName_stf = value_reciver_username_stf.get()
    amount_stf = int(value_amount_stf.get())
    password_stf = value_password_stf.get()

    con = pymysql.connect(host="localhost", user="root", passwd="rajdeep0510", database="bank_db")
    cur = con.cursor()
    cur.execute("SELECT userPW FROM account WHERE userName = %s", sender_uName_stf)
    result = cur.fetchone()

    if result[0] == password_stf:
        cur.execute("UPDATE account SET balance = balance + %s WHERE userName = %s",(amount_stf, reciver_uName_stf))
        cur.execute("UPDATE account SET balance = balance - %s WHERE userName = %s",(amount_stf, sender_uName_stf))
        con.commit()
        con.close()
        messagebox.showinfo("SUCCESS", f"Money deposited successfully to {reciver_uName_stf}")
        clear_stf()
    else:
        messagebox.showerror("Error", "Password was incorrect")
        con = pymysql.connect(host="localhost", user="root", passwd="rajdeep0510", database="bank_db")
        cur = con.cursor()
        cur.execute("SELECT email FROM account WHERE userName = %s", sender_uName_stf)
        email = cur.fetchone()
        mail.security_mail(email[0])

        clear_stf()

def clear_stf():
    value_sender_username_stf.delete(0,END)
    value_reciver_username_stf.delete(0,END)
    value_amount_stf.delete(0,END)
    value_password_stf.delete(0,END)


def info_fun():

    uname_info = value_uname_info.get()
    password_info = value_pass_info.get()

    con = pymysql.connect(host="localhost", user="root", passwd="rajdeep0510", database="bank_db")
    cur = con.cursor()
    cur.execute("SELECT userPW FROM account WHERE userName = %s", uname_info)
    amount_r = cur.fetchone()

    if amount_r[0] == password_info:
        cur.execute("SELECT balance FROM account WHERE userName = %s;",(uname_info))
        amount = cur.fetchone()
        con.commit()
        con.close()
        messagebox.showinfo(title="Information", message=f"Your current balance is {amount}", icon='info')
        clear_info()
    else:
        messagebox.showerror("Error", "Password was incorrect")
        con = pymysql.connect(host="localhost", user="root", passwd="rajdeep0510", database="bank_db")
        cur = con.cursor()
        cur.execute("SELECT email FROM account WHERE userName = %s", uname_info)
        email = cur.fetchone()
        mail.security_mail(email[0])
        clear_info()

def clear_info():
    value_uname_info.delete(0,END)
    value_pass_info.delete(0,END)



#------------------Tkinter code for GUI-----------------------

root = Tk()


root.geometry("1000x700")

main_title = Label(root,
                   text="Bank Management System",
                   font=("Arial", 40),
                   relief='groove',borderwidth=2,         
                   )
main_title.pack(side="top", fill="x")

#TODO : THIS IS THE MASTER 
master = Frame(root, bg='#CBF1F5', bd=5)
master.place(x=100,y=135, width=800, height=500)

#BUTTONS
new_account = Button(master,
                     text="Open New Account",
                     width=50, height=4,
                     command=new_account)
new_account.pack(pady="10")

deposit = Button(master,
                     text="Deposit",
                     width=50, height=4,
                     command = deposit)
deposit.pack(pady="10")

Withdraw = Button(master,
                     text="Withdraw",
                     width=50, height=4,
                     command=withdraw)
Withdraw.pack(pady="10")

send_to_frind = Button(master,
                     text="Send to Friend",
                     width=50, height=4,
                     command=stf)
send_to_frind.pack(pady="10")

acc_info= Button(master,
                     text="Account Information",
                     width=50, height=4,
                     command=acc_info)
acc_info.pack(pady="10")



root.mainloop()