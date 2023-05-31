from tkinter import *
root=Tk()
root.title("Multidimensional Arrays")

root.geometry("500x500")
label= Label(root)


array_1d = ["John", "James" ," Thomsan"]
print( array_1d[2] )

array_2d = [["john","A"], ["james", "B"],["Thomson","C"]]
print(array_2d[1][1])

array_3d = [[["John","A+","Excellent"],["James","A","Very Good"],["Thomson","B","Good"]]]
print(array_3d[0][0][2])

def report():
    label["text"] = array_1d[2] + " got grade " + array_2d[1][1] +" and he is doing "
    + array_3d[0][0][2]

btn = Button(root, text= "show report", command = report)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)

label.place(relx = 0.5, rely =0.6, anchor = CENTER)

root.mainloop()