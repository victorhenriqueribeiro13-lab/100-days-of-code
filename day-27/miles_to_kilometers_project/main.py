from tkinter import *
def miles_to_km():
    miles = float(miles_entry.get())
    km = miles * 1.609
    mile_to_km_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(0, 0)
window.config(padx=60, pady=30)

#label is equal
is_equal_label = Label(text="is equal to", font=("Arial", 8))
is_equal_label.grid(column=0, row=1)

#entry
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

#label

my_label_miles = Label(text="Miles", font=("Arial", 8))
my_label_miles.grid(column=2, row=0)




#Button
mile_to_km_label = Label(text="0", font=("Arial", 8))
mile_to_km_label.grid(column=1, row=1)


#label km
km_label = Label(text="km", font=("Arial", 8))
km_label.grid(column=2, row=1)



#calculate button
button_calculate = Button(text="Calculate", command=miles_to_km)
button_calculate.grid(column=1, row=2)


window.mainloop()