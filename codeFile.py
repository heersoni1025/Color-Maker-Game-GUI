from tkinter import *  #importing necessaryv sources
import random 



#list of colors just so it is easy to use and can be used in the code
colors = {
    "#FF0000": "Red",     
    "#FFA500": "Orange",
    "#FFFF00": "Yellow",
    "#00FF00": "Green",
    "#0000FF": "Blue",
    "#800080": "Purple",
    "#FFC0CB": "Pink",
    "#FFFFFF": "White",
    "#000000": "Black"
}

#function to create a new window 
def newWin():
    window2 = Toplevel()
    window2.title("Game window")  #window title
    window2.geometry("600x600")  #window geometry
    window2.config(bg="#FFFFE0")  # Light Yellow (bright color) for background
    Label(window2, image=resized_color_image, bg="#FFFFE0").place(x=80, y=80) #label to add image

    
    #function to change bg colors randomly 
    def random_color_generator():   
        color_values = list(colors.keys())
        random_color = random.choice(color_values)
        window2.config(bg=random_color)  #using it for window2
        
    #function to check if the guess entered by the user for the color is correct
    def check_guess():    
        user_guess = guess_entry.get().capitalize()  #cstoring the entered value in variable and captalizing it
        current_color = window2.cget("bg")   #getting the window2 bg color
        if colors.get(current_color) == user_guess:  #if the guess entered by the user is equal to the bg color...
            message_label.config(text="Correct Guess!", fg="green")   #prints "Correct Guess!" and changes font color to green
        else:
            message_label.config(text="Try Again!", fg="red")#if entered value isn't the same as bg color, prints "Try again!" in red"
 
   #label on window2 on top for instructions
    Label(window2, text="Guess the Color! Click on the Next Color button below to start!", font=("Arial", 28), bg="#FFFFE0").pack(pady=20)
    
    #button for changing bg color, calls random_color_generator function for the process
    Button(window2, text="Next Color", padx=25, pady=25, bd=8, bg="#FF69B4", fg="white", font=("Arial", 22), command=random_color_generator).pack(pady=20)
    #another label to ask the user to enter their guess
    guess_label = Label(window2, text="Enter your guess:", font=("Arial", 18), bg="#FFFFE0")
    guess_label.pack(pady=20)

    #entry box for user to enter their color guessed value
    guess_entry = Entry(window2, font=("Arial", 14), bg="#FFDAB9")  # Peach Puff (bright color)
    guess_entry.pack(pady=10)

    #button to check if the input is correct, calls the check_guess function
    Button(window2, text="Check", padx=10, pady=10, bd=8, bg="#00CED1", fg="white", font=("Arial", 16, "bold"), command=check_guess).pack(pady=20)
    message_label = Label(window2, text="", font=("Arial", 20), bg="#FFFFE0")  #another label, space for the check_guess functions' results
    message_label.pack(pady=20)
    
    #button to close the game window
    Button(window2, text="Back to Start window", padx=10, pady=10, bd=8, bg="#FF6347", fg="white", font=("Arial", 14, "bold"), command=window2.destroy).pack(pady=20)

#to remove/close window, used to close the program or a window
def exitApp():
    root.destroy()


#display the name of the player input on the start window
def displayName():
    x = entry.get().capitalize()  # User input
    if x != "":
        Label(text="Welcome,", bg="#FFD700", font=("Arial", 24)).pack(pady=10)  # Gold (bright color)
        Label(text=x, bg="#FFD700", font=("Arial", 24)).pack(pady=10)  # Gold (bright color)
        #button to create the game window
        Button(root, text="Click me!", padx=25, pady=25, bd=8, bg="#FF69B4", fg="white",
               font=("Arial", 22), command=newWin).pack(pady=20)
        #button to close both windows
        Button(root, text="Close both windows", padx=10, pady=10, bd=8, bg="#FF6347", fg="white",
               font=("Arial", 18, "bold"), command=exitApp).pack(pady=20)

            
#setting up program by creating the start window
root = Tk()
root.title("Start - The Color Maker")  #start window title
root.geometry("900x600")  #start window geo/size
root.config(bg="#FFFFE0")  # Light Yellow (bright color)
gif_image_file = "color1.gif"   #image for window2
gif_image = PhotoImage(file=gif_image_file)  #sets up the image
resized_color_image = gif_image.subsample(4)  # Adjust the subsample factor to resize the image

#label for instruction on start window
Label(root, text="Hello, let's play The Color Maker, kids' favorite game!", font=("Arial", 24), bg="#FFFFE0").pack(pady=20)
image_file = "smile.gif"   #smile image on start window
image = PhotoImage(file=image_file)       #sets up the image
resized_image = image.subsample(3)  # Adjust the subsample factor to resize the image
Label(root, image=resized_image, bg="#FFFFE0").place(x=80, y=30)  # Adjust the x and y coordinates so that the image is at a good location 
Label(root, text="First, enter your name below and click 'Done' when ready", font=("Arial", 16), bg="#FFFFE0", fg="black").pack(pady=10)
#label for instruction on start window
entry = Entry(root, font=("Arial", 14), bg="#FFDAB9")  #for user to enter their name on start window
entry.pack(pady=10)
#button to print the name entered and display it by caling the func
Button(root, text="Done", padx=10, pady=10, bd=8, bg="#FF8C00", fg="white", font=("Arial", 16, "bold"), command=displayName).pack(pady=20)
Button(root, text="Exit", padx=10, pady=10, bd=8, bg="#FF6347", fg="white", font=("Arial", 16, "bold"), command=exitApp).pack(pady=20)
#button to close the window



#running the program
root.mainloop()
