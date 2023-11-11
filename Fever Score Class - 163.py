from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Fever Reoprt")
root.geometry("400x400")

Question1_radiobutton = StringVar(value = "0")

Question1 = Label(root, text = "Do you have headache and sore throat ?")
Question1.pack()
Question1_Rb1 = Radiobutton(root, text = "yes", variable = Question1_radiobutton, value = "yes")
Question1_Rb1.pack()
Question1_Rb2 = Radiobutton(root, text = "no", variable = Question1_radiobutton, value = "no")
Question1_Rb2.pack()

Question2_radiobutton = StringVar(value = "0")

Question2 = Label(root, text = "Is your body temprature higher than 98.6 F or 37 C ?")
Question2.pack()
Question2_Rb1 = Radiobutton(root, text = "yes", variable = Question2_radiobutton, value = "yes")
Question2_Rb1.pack()
Question2_Rb2 = Radiobutton(root, text = "no", variable = Question2_radiobutton, value = "no")
Question2_Rb2.pack()

Question3_radiobutton = StringVar(value = "0")

Question3 = Label(root, text = "Are there any symptoms of eye redness ?")
Question3.pack()
Question3_Rb1 = Radiobutton(root, text = "yes", variable = Question3_radiobutton, value = "yes")
Question3_Rb1.pack()
Question3_Rb2 = Radiobutton(root, text = "no", variable = Question3_radiobutton, value = "no")
Question3_Rb2.pack()

def fever_score():
    score = 0
    if Question1_radiobutton.get() == "yes":
        score += 20
        print(score)
    if Question2_radiobutton.get() == "yes":
        score += 20
        print(score)
    if Question3_radiobutton.get() == "yes":
        score += 20
        print(score) 
        
    if score <= 20:
        messagebox.showinfo("Report", "You don't need to visit to a doctor")
    elif score > 20 and score <= 40:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor")
    else :
        messagebox.showinfo("Report", "I strongly advised you to vist a doctor")

button = Button(root, text = "Show report", command = fever_score)
button.pack()

root.mainloop()        
        