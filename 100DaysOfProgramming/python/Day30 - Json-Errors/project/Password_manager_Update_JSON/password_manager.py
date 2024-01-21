from tkinter import *
from tkinter import messagebox
from random import randint
import json


def generate_password():
    password_entry.delete(0, END)
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
                  'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
                  'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', 
                  '$', '%', '&', '(', ')', '*', '+']    
    #Generate the password of 25 characters, symbols, etc.
    password =  [ characters[randint(0, len(characters) - 1)] for character in range(0,25)]
    #Join will combine the values on '' for anything 
    password_final = ''.join(password)

    #Copy to the users clipboard
    password_entry.clipboard_append(password_final)
    password_entry.insert(END, password_final)


def search_for_entry():
    password_entry.delete(0, END)
    try:
        with open("data/user_password_data.json", "r") as password_file:
            website = website_entry.get()
            passwords = json.load(password_file)
            email = passwords[website]['email']
            password = passwords[website]['password']

            try:
                messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
            except Exception as e:
                print(e)
    except FileNotFoundError as e:
        messagebox.showinfo(title=f"Error", message=f"File does not exist.")
    except KeyError as e:
        messagebox.showinfo(title=f"Error", message=f"{website} does not exsit.")


def add_to_db():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    #Check for len of elements
    if len(website) == 0:
        messagebox.showinfo(title=f"Empty value", message="Website can not be empty.")
    elif len(password) == 0:
        messagebox.showinfo(title=f"Empty value", message="Password can not be empty.")
    elif len(username) == 0:
        messagebox.showinfo(title=f"Empty value", message="Username can not be empty.")
    else:
        #Dialog boxes
        save_entry = messagebox.askokcancel(title=website, message=f"These are the details: \n{username}\n{password}\nSave?")
        if save_entry == True:

            try:
                with open('data/user_password_data.json', 'r') as password_file:
                    new_password = {
                        website: {
                            "email": username,
                            "password": password
                        }
                    }
                    #read the old data
                    passwords = json.load(password_file)
            except FileNotFoundError as e:
                with open('data/user_password_data.json', 'w') as password_file:
                    #Saving the udpated data
                    json.dump(passwords, password_file, indent=4) # This will writes dict to file
            else:
                with open('data/user_password_data.json', 'w') as password_file:
                    #Load the old data with new data
                    passwords.update(new_password)
                    #Saving the udpated data
                    json.dump(passwords, password_file, indent=4) # This will writes dict to file                

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)                    


if __name__ == "__main__":
    #Main Window
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)
    window.minsize(width=300, height=300)
    
    #Canvas + Image
    image = PhotoImage(file='images/logo.png')
    canvas = Canvas(window, width=200, height=200)
    canvas.create_image(100, 100, image=image)
    canvas.grid(column=1, row=0)

    #labels
    website_title_label = Label(text="Website:")
    website_title_label.grid(column=0 ,row=1)
    
    email_label = Label(text="Email/Username:",padx=0)
    email_label.grid(column=0 ,row=2)
    
    password_label = Label(text="Password:", padx=0)
    password_label.grid(column=0 ,row=3)

    #buttons
    generate_password_button = Button(text="Generate Password", command=generate_password, padx=2,pady=2)
    generate_password_button.grid(column=2 ,row=3)
    
    search_for_entry_button = Button(text="Search", command=search_for_entry, padx=2,pady=2, width=16)
    search_for_entry_button.grid(column=2 ,row=1)

    add_button = Button(text="Add", command=add_to_db)
    add_button.config(width=39)
    add_button.grid(column=1 ,row=5, columnspan=2)

    #entry
    website_entry = Entry(width=25)
    website_entry.grid(column=1 ,row=1)
    website_entry.focus()

    username_entry = Entry(width=42)
    username_entry.grid(column=1 ,row=2, columnspan=2)
    username_entry.insert(0, "brandon@brandonwest.tech")

    password_entry = Entry(width=25)
    password_entry.grid(column=1 ,row=3)
   
    
    
    
    window.mainloop()