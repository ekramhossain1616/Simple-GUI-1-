import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Ekram')

nb = ttk.Notebook(win)

page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1, text='ONE')
nb.add(page2, text='TWO')
# nb.grid(row=0, column=0)
nb.grid(row=0, column=0)

label_frame1 = ttk.Labelframe(page1, text='Enter your info')
label_frame1.grid(row=0, column=0)

# ****************Creating Labels for label_frame1 *************

name_label = ttk.Label(label_frame1, text='Enter your name :')
name_label.grid(row=0, column=0, sticky=tk.W)

email_label = ttk.Label(label_frame1, text='Enter your e-mail :')
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(label_frame1, text='Enter your age :')
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(label_frame1, text='Enter your gender :')
gender_label.grid(row=3, column=0, sticky=tk.W)

# *************** Creating Entryboxes for label_frame1 ***************

name_var = tk.StringVar()
name_entrybox = ttk.Entry(label_frame1, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(label_frame1, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(label_frame1, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(label_frame1, width=13, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.grid(row=3, column=1)
gender_combobox.current(0)

label_frame2 = ttk.Labelframe(page2, text='Enter your info')
label_frame2.grid(row=0, column=0)

# ****************** Creating label for label_frame2 *************

Type_label = ttk.Label(label_frame2, text='Type ? :')
Type_label.grid(row=4, column=0, sticky=tk.W)

# *************** creating radiobtn for label_frame2 *************

usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(label_frame2, text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=4, column=1)

radiobtn2 = ttk.Radiobutton(label_frame2, text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column=2)

# *****************creating checkbutton for label_frame2 ********************

checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(label_frame2, text='Check if you want to subscribe our newsletter.', variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)


# ************* creating Submit button *******************

def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    check_btn = checkbtn_var.get()
    if user_gender == 'Male':
        he = 'He'
    elif user_gender == 'Other':
        he = 'He'
    else:
        he = 'She'

    if check_btn == 1:
        Subscribed = 'subscribed'
    else:
        Subscribed = 'not subscribed'
    print(
        f'{username}\'s age is {userage}, gender is {user_gender}, email is {user_email}. {he} is a {user_type} and {Subscribed} to our newsletter.')

    with open('ekram.txt', 'a') as f:
        f.write(
            f'{username}\'s age is {userage}, gender is {user_gender}, email is {user_email}. {he} is a {user_type} and {Subscribed} to our newsletter.\n')

    name_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)


submit_button = ttk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, columnspan= 2)

win.mainloop()
