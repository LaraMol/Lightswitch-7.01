import tkinter as tk
window = tk.Tk()

def toggle():
    if window['background'] == 'white':
        window['background'] = 'pink'
    else:
        window['background'] = 'white'

button = tk.Button(text='Knop', bg="white", fg="black", command=toggle)
button.pack(pady = 20, padx = 20)

window.mainloop() 