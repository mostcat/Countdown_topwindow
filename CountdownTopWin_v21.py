# Rickwan

import sys
import tkinter as tk
from tkinter import font
# import win32api # SSS WIN10 REMOVE
# import win32con # SSS WIN10 REMOVE
# import win32gui # SSS WIN10 REMOVE

class CountdownTopWin:
    def __init__(self,time_set=5,time_total=0):
        print(f"Start time_set={time_set}m time_totle={time_total}m")         
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.5)
        self.drag_start = None
        self.drag_last = None        

        self.default_font = font.nametofont("TkDefaultFont")
        self.time_set = time_set*60
        self.time_total = time_total*60
        self.time_total_left = self.time_total
        self.time_left = self.time_set
        self.paused = False
        self.lable_flash = True
        self.ui_show = False                

        self.label = tk.Label(self.root, text="05:00", font=("Arial", 40))
        self.label.pack()

        self.add_btn = tk.Button(self.root, text=" + ", command=self.add_time) 
        self.reduce_btn = tk.Button(self.root, text=" - ", command=self.reduce_time)
        self.reset_btn = tk.Button(self.root, text=" R ", command=self.reset_time)
        self.pause_btn = tk.Button(self.root, text=" || ", command=self.toggle_pause)
        self.exit_btn = tk.Button(self.root, text=" X ")        
        self.add_btn.pack(side="left")
        self.reduce_btn.pack(side="left") 
        self.reset_btn.pack(side="left")
        self.pause_btn.pack(side="left")
        self.exit_btn.pack(side="left")  
        self.exit_btn.config(command=self.root.destroy) 
        self.root.bind("<B1-Motion>", self.drag_window)
        self.root.bind("<Enter>", self.show_buttons)
        self.add_btn.bind("<Leave>", self.hide_buttons)        
        self.reset_btn.bind("<Leave>", self.hide_buttons)        
        self.reduce_btn.bind("<Leave>", self.hide_buttons) 
        self.pause_btn.bind("<Leave>", self.hide_buttons) 
        self.exit_btn.bind("<Leave>", self.hide_buttons) 

        # self.set_default_position() # SSS WIN10 REMOVE
        self.update_time()
        self.root.after(1000, self.tick)

    def set_default_position(self):
        x = win32api.GetCursorPos()[0] - self.root.winfo_width()//2 - 100
        y = win32api.GetCursorPos()[1] - self.root.winfo_height()//2 
        self.root.geometry(f"+{x}+{y}")
        
    def show_buttons(self, event):
        self.ui_show = True
        self.root.attributes("-alpha", 0.5)        
        self.add_btn.pack(side="left")  
        self.reduce_btn.pack(side="left")
        self.reset_btn.pack(side="left")  
        self.pause_btn.pack(side="left") 
        self.exit_btn.pack(side="left")       
        
    def hide_buttons(self, event):
        self.ui_show = False
        self.add_btn.pack_forget()
        self.reduce_btn.pack_forget()
        self.reset_btn.pack_forget()
        self.pause_btn.pack_forget() 
        self.exit_btn.pack_forget()        

    def drag_window(self, event):
        if self.drag_start is None:
            self.drag_start = (event.x_root, event.y_root)
            self.drag_last = self.drag_start        
        dx = event.x_root - self.drag_last[0]  
        dy = event.y_root - self.drag_last[1]        
        x = self.root.winfo_x() + dx
        y = self.root.winfo_y() + dy        
        # x = max(0, min(x, self.root.winfo_screenwidth()-self.root.winfo_width()))  
        # y = max(0, min(y, self.root.winfo_screenheight()-self.root.winfo_height()))        
        self.root.geometry(f"+{x}+{y}")         
        self.drag_last = (event.x_root, event.y_root)

    def reset_time(self):
        self.time_left = self.time_set         
        # self.time_total_left = self.time_total 
        self.update_time() 

    def add_time(self):
        if (self.time_left < 0):
            self.time_left = 0
        self.time_left += 60
        self.time_left = (self.time_left // 60) * 60         
        self.update_time()       
        
    def reduce_time(self):
        if (self.time_left < 0):
            self.time_left = 0        
        if self.time_left <= 60:
            self.time_left = 60
        else:
            self.time_left -= 60
        self.time_left = (self.time_left // 60) * 60             
        self.update_time()
        
    def toggle_pause(self):
        self.paused = not self.paused
        
    def update_position(self):
        x = win32api.GetCursorPos()[0] - self.root.winfo_width()//2
        y = win32api.GetCursorPos()[1] - self.root.winfo_height()//2
        self.root.geometry(f"+{x}+{y}")
        
    def update_time(self): 
        print(f"\rleft={self.time_left}s total_left={self.time_total_left}s ui={self.ui_show}", end='')
        minutes, seconds = divmod(abs(self.time_left), 60)        
    
        total_str = f""
        if  self.time_total > 0 :
            total_minutes, total_seconds = divmod(abs(self.time_total_left), 60) 
            if self.time_total_left < 0:
                total_str = f"\n-{total_minutes:02d}:{total_seconds:02d}"
            else:
                total_str = f"\n{total_minutes:02d}:{total_seconds:02d}"

        if self.time_left < 0:
            self.label.configure(text=f"-{minutes:02d}:{seconds:02d}{total_str}")
        else:
            self.label.configure(text=f"{minutes:02d}:{seconds:02d}{total_str}")

        if self.time_left < 60 and self.time_left > 0:
            self.label.config(bg="red")
        else:
            self.label.config(bg="white")

        if self.time_left < 0 or self.paused:
            if self.lable_flash :
                if self.paused :
                    self.label.config(bg="yellow")
                else:
                    self.label.config(bg="red")
            else:
                self.label.config(bg="white")
            self.lable_flash = not self.lable_flash

        alpha = 0.6
        if self.time_set - self.time_left > 5 and (not self.ui_show) :
            alpha = (self.time_set - self.time_left) / self.time_set +0.1
        self.root.attributes("-alpha", alpha)
        
    def tick(self):
        if (not self.paused) :
            self.time_left -= 1
        self.time_total_left -= 1    
        self.update_time()            
        self.root.after(1000, self.tick)
        
if __name__ == "__main__":
    if len(sys.argv) == 1 :
        window = CountdownTopWin()    
        window.root.mainloop()   
    if len(sys.argv) == 2 :
        arg1 = sys.argv[1]
        arg1 = int(arg1) 
        if arg1>99 :
            print("set max 99")
            sys.exit(1)
        window = CountdownTopWin(arg1)    
        window.root.mainloop()
    if len(sys.argv) == 3 :
        arg1, arg2 = sys.argv[1:]
        arg1 = int(arg1) 
        arg2 = int(arg2)
        if arg1>99 or arg2>99:
            print("set max 99")
            sys.exit(1)        
        window = CountdownTopWin(arg1,arg2)      
        window.root.mainloop()
