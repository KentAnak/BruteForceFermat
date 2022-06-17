import tkinter as Tk
from tkinter import messagebox
from tkinter import ttk

def fixed_map(option):
    # Fix for setting text colour for Tkinter 8.6.9
    # From: https://core.tcl.tk/tk/info/509cafafae
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.

    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if
        elm[:2] != ('!disabled', '!selected')]

style = ttk.Style()
style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))


def is_pythagorean(a,b,c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

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
        labeltext = "Displays a list of Pythagorean numbers.\n\nEnter a numerical value that is the largest diagonal.\n\nLet's find nearly isosceles triangles that Fermat proved."
        self.label = Tk.Label(self, text=labeltext)
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
            rtuple = self.print_pythagorean_triple(int(input_value))
            messagebox.showinfo("Result",str(rtuple[0])+" Pythagorean triples found.\n"+
            str(rtuple[1])+" Pythagorean triples of nearly isosceles triangle found.")
        else:
            messagebox.showinfo("Result","Error. Please enter numeric value.")
    
    def print_pythagorean_triple(self, max):
        xarray = []
        pt = 0
        ptnit = 0
        for a in range(1,max):
            for b in range(a,max):
                for c in range(b,max):
                    if(is_pythagorean(a, b, c) and is_primitive_triple(a,b,c,xarray)):
                        xarray.append((a, b, c)) 
                        pt +=1
                        self.tree.insert("", "end", values=(a, b, c), tags=(str(pt),))   
                        if(b-a ==1 and b < c):
                            ptnit+=1
                            self.tree.tag_configure(pt, background='lightgreen')
                        break          
        return (pt,ptnit)

##----------------
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()

