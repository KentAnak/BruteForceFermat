import tkinter as Tk
from tkinter import Y, messagebox
from tkinter import ttk

def hypotenuse(a,b):
    assert a > 0
    assert b > 0  
    c_squared = a ** 2 + b ** 2
    c = c_squared ** (1/2)
    assert round(c ** 2) == round(a ** 2 + b ** 2)
    return c

def is_primitive_triple(a,b,c,array):
    xarray = array
    is_primitive = True
    for row in xarray:
        x = row[0]
        y = row[1]
        z = row[2]
        if (a/x == b/y == c/z):
            is_primitive = False
            break        
    return is_primitive

class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)

        self.master.title("Brute Force de Fermat")
        self.label = Tk.Label(self, text="Displays a list of Pythagorean numbers.\n\nEnter a numerical value\nthat is the largest diagonal.")
        self.label.grid(row=0, column=0, padx=10, pady=5)

        self.input = Tk.Entry(self, width=20)
        self.input.grid(row=1, column=0,  padx=5, pady=5)
        
        self.button = Tk.Button(self, text="exec", command=self.click_botton)
        self.button.grid(row=2, column=0,  padx=5, pady=5)

        self.tree = ttk.Treeview(self)
        self.tree["column"] = (1,2,3)
        self.tree["show"] = "headings"
        self.tree.heading(1,text="a")
        self.tree.heading(2,text="b")
        self.tree.heading(3,text="c")
        self.tree.column(1, width=80)
        self.tree.column(2, width=80)
        self.tree.column(3, width=80)
        self.scrollbar = ttk.Scrollbar(self,orient=Tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.tree.grid(row=0, column=1, rowspan=3, pady=10)
        self.scrollbar.grid(row=0, column=2, rowspan=3, sticky="NS")


    def click_botton(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
            
        input_value = self.input.get()
        if(input_value.isnumeric()):
            result_list = self.print_pythagorean_triple(int(input_value))
            #messagebox.showinfo("Result",result_list)
        else:
            messagebox.showinfo("Result","Error. Please enter numeric value.")
    
    def print_pythagorean_triple(self, max_hypotenuse):
        xarray = []
        for a in range(1,max_hypotenuse):
            for b in range(a,max_hypotenuse):
                for c in range(b,max_hypotenuse):
                    if(c == hypotenuse(a, b) and is_primitive_triple(a,b,c,xarray)):
                        xarray.append((a, b, c)) 
                        self.tree.insert("", "end", values=(a, b, c))   
                        break          
        return xarray

##----------------
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()

