import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import time
from threading import Timer

class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self._draw()
        self.current_user = None
    

    def _draw(self):
        """Draws the tkinter application"""     

        self.body = Body(self.root)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.footer = Footer(self.root)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)



class RepeatedTimer(object):
    """A timer class used to execute functions every x seconds"""
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class Body(tk.Frame):
    """Body of tkinter application"""
    def __init__(self, root, select_callback = None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._select_callback = select_callback

        self._draw()
    
    

    def _draw(self):
        """Draws body of tkinter application"""
        user_frame = tk.Frame(master=self, width=250)
        user_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        self.users_tree = ttk.Treeview(user_frame)
        self.users_tree.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        
        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
        
        self.entry_editor = tk.Text(editor_frame, width=0)
        self.entry_editor.config(state=DISABLED)
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame, command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT, expand=False, padx=0, pady=0)




        #print(self.users_tree.get_children())
        



class Footer(tk.Frame):
    """Footer of tkinter application"""
    def __init__(self, root, select_callback = None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._select_callback = select_callback

        self._draw()
    

            


    def _draw(self):
        """Draws footer in tkinter application"""
        send_button = tk.Button(master=self, text="Send", width=10)
        send_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        #self.footer_label = tk.Label(master=self, text="Enter a username to the right to message a new person.")
        #self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)

        self.add_user = tk.Text(master=self, width=25, height=1)
        self.add_user.pack(fill=tk.BOTH, side=tk.LEFT, padx=0, pady=0)

        self.message_box = tk.Text(master=self, width=0, height=1)
        self.message_box.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=0, pady=0)

        
if __name__ == '__main__':
    """Initialized mainloop for tkinter application"""
    main = tk.Tk()

    main.title("Diary")


    main.geometry("720x480")
    main.option_add('*tearOff', False)

    MainApp(main)


    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())

    main.mainloop()