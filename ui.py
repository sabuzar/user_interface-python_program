import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title('DETAIL.OUTPUT')




name_label1 = ttk.Label(window, text="Enter your name : " ).grid(row=0, column=0, sticky=tk.W)

email_label1 = ttk.Label(window, text="Enter your email : ").grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(window, text = "Enter your age :").grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(window, text = "Select your gender :").grid(row=3, column=0, sticky=tk.W)

name_var = tk.StringVar()
name_entrybox = ttk.Entry(window, width=20, textvariable = name_var)
name_entrybox.grid(row=0, column=1,)
name_entrybox.focus()



email_var = tk.StringVar()
email_entrybox = ttk.Entry(window, width=20, textvariable = email_var).grid(row=1, column=1,)


age_var = tk.StringVar()
age_entrybox = ttk.Entry(window, width=20, textvariable = age_var).grid(row=2, column=1,)



gender_var=tk.StringVar()
gender_combobox = ttk.Combobox(window, width=17, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)


usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(window,text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=4, column=0, sticky=tk.W)

radiobtn2 = ttk.Radiobutton(window,text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column=1)


radiobtn3 = ttk.Radiobutton(window,text='Worker', value='Worker', variable=usertype)
radiobtn3.grid(row=4, column=2)

radiobtn4 = ttk.Radiobutton(window,text='Businessman', value='Businessman', variable=usertype)
radiobtn4.grid(row=4, column=3)


user_sub = tk.IntVar(0)
checkbtn = ttk.Checkbutton(window, text='check if you want to subcribed', variable=user_sub)
checkbtn.grid(row=5, columnspan=3, sticky=tk.W)



def action():
    Username=name_var.get()
    Userage=age_var.get()
    Useremail=email_var.get()
    print(f"{Username} is {Userage} years old and his/her email, is {Useremail} his gender is  ")
    user_gender = gender_var.get()
    user_type = usertype.get()
    if user_sub.get() == 0:
        subcribed = 'NO'
    else:
        subcribed = 'YES'
    print(user_gender, user_type, user_sub )

    with open('file.txt', 'a') as f:
         f.write(f'{name_var},{age_var}, {email_var} ,{gender_var} ,{user_type} ,{checkbtn }\n')


submit_button = ttk.Button(window, text='Submit', command=action).grid(row=6, column=0, sticky=tk.W)


window.mainloop()