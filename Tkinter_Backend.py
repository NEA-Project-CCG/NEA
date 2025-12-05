from Database_Querying import Database
from tkinter import Button, Tk
class Tkinter_Backend():
    @staticmethod
    def Character_selection_screen_setup(names, root):

        button_dict = {}
        for i in range(len(names)):
            name = names[i]
            # https://stackoverflow.com/questions/21990685/tkinter-creating-an-arbitrary-number-of-buttons-widgets command=
            temp_button = Button(root, text=name)
            temp_button.grid(row=i // 2, column=i % 2, padx=5)
            button_dict[temp_button] = name

        return button_dict, root

    @staticmethod
    def add_char(name, root):
        global char_name
        character_id: int = Database.Char_id_from_name(name)
        char_name = name
        global c_id
        c_id = character_id

        root.destroy()









    @staticmethod
    def Button_functionality(button_dict, root):
        for key in button_dict:
            name = button_dict[key]
            key["command"] = lambda dat=name: Tkinter_Backend.add_char(dat, root)




    @staticmethod
    def loop(root):
        root.mainloop()

    @staticmethod
    def Player_chars(names):
        root = Tk()
        button_dict, root = Tkinter_Backend.Character_selection_screen_setup(names, root)
        print("DEBUG: 1")
        Tkinter_Backend.Button_functionality(button_dict, root)
        print("DEBUG: 2")
        Tkinter_Backend.loop(root)
        print("DEBUG: 3")
        
        print(f"DEBUG: {c_id}, {char_name}")
        return c_id, char_name

        




if __name__ == '__main__':
    names = ['Cragger']
    Tkinter_Backend.Player_chars(names)
