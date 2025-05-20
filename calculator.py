from tkinter import *
import tkinter.font as tkFont
from sympy import *


class Calculator():
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.bind("<Key>",self.keyboard_entry)
        self.content_string = ""
        self.is_negative = False
        self.result=""
        self.is_result_calculated=False
        self.title = Label(self.main_window, bg="#1e1e1e", fg="white", text="Calculator", font=("Times New Roman", 18, "bold"), pady=10)
        self.title.pack(side="top")
        self.display_frame = Frame(self.main_window, bg="white", width=330, height=100)
        self.display_frame.place(x=10, y=50)
        self.display_frame.pack_propagate(False)
        self.content = Label(self.display_frame, font=("Times New Roman", 16,), wraplength=330, justify="right", anchor='e')
        self.content.pack(fill="both", expand=True)
        self.buttons_frame = Frame(self.main_window, bg="#1e1e1e", width=330, height=300)
        self.buttons_frame.grid_propagate(False)
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)
        self.buttons_frame.place(x=10, y=175)
        self.button_font = tkFont.Font(family="Times New Roman", size=16, weight="bold")
        self.button_7 = Button(self.buttons_frame, text="7", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('7'))
        self.button_7.grid(row=0, column=0, sticky="nsew")
        self.button_8 = Button(self.buttons_frame, text="8", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('8'))
        self.button_8.grid(row=0, column=1, sticky="nsew")
        self.button_9 = Button(self.buttons_frame, text="9", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('9'))
        self.button_9.grid(row=0, column=2, sticky="nsew")
        self.button_plus = Button(self.buttons_frame, text="+", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('+'))
        self.button_plus.grid(row=0, column=3, sticky="nsew")
        self.button_4 = Button(self.buttons_frame, text="4", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('4'))
        self.button_4.grid(row=1, column=0, sticky="nsew")
        self.button_5 = Button(self.buttons_frame, text="5", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('5'))
        self.button_5.grid(row=1, column=1, sticky="nsew")
        self.button_6 = Button(self.buttons_frame, text="6", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('6'))
        self.button_6.grid(row=1, column=2, sticky="nsew")
        self.button_minus = Button(self.buttons_frame, text="-", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('-'))
        self.button_minus.grid(row=1, column=3, sticky="nsew")
        self.button_1 = Button(self.buttons_frame, text="1", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('1'))
        self.button_1.grid(row=2, column=0, sticky="nsew")
        self.button_2 = Button(self.buttons_frame, text="2", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('2'))
        self.button_2.grid(row=2, column=1, sticky="nsew")
        self.button_3 = Button(self.buttons_frame, text="3", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('3'))
        self.button_3.grid(row=2, column=2, sticky="nsew")
        self.button_multiply = Button(self.buttons_frame, text="x", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('*'))
        self.button_multiply.grid(row=2, column=3, sticky="nsew")
        self.button_plus_minus = Button(self.buttons_frame, text="+/-", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content("negative"))
        self.button_plus_minus.grid(row=3, column=0, sticky="nsew")
        self.button_0 = Button(self.buttons_frame, text="0", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('0'))
        self.button_0.grid(row=3, column=1, sticky="nsew")
        self.button_dot = Button(self.buttons_frame, text=".", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('.'))
        self.button_dot.grid(row=3, column=2, sticky="nsew")
        self.button_divide = Button(self.buttons_frame, text="/", bg="white", fg="#1e1e1e", font=self.button_font, command=lambda: self.add_content('/'))
        self.button_divide.grid(row=3, column=3, sticky="nsew")
        self.button_ac = Button(self.buttons_frame, text="AC", bg="red", fg="white", font=self.button_font, command=self.all_clear)
        self.button_ac.grid(row=4, column=0, sticky="nsew")
        self.button_del = Button(self.buttons_frame, text="del", bg="yellow", fg="#1e1e1e", font=self.button_font, command=self.delete)
        self.button_del.grid(row=4, column=1, sticky="nsew")
        self.button_equal = Button(self.buttons_frame, text="=", bg="green", fg="white", font=self.button_font,command=self.solve)
        self.button_equal.grid(row=4, column=2, columnspan=2, sticky="nsew")

    def content_refresher(self):
        self.content.config(text=self.content_string)

    def last_part_extractor(self, check=None,digit_required=False):
        parts = self.content_string.split(' ')
        digit_part = ""
        last_part = parts[-1]
        if digit_required:
            for i in last_part:
                if i in check:
                    digit_part = digit_part + i
            return digit_part
        else:
            return last_part

    def add_content(self, ch):
        if self.is_result_calculated:
            if ch in ['+', '-', '*', '/']:
                self.content_string=str(self.result)
            else:
                self.content_string=""
            self.is_result_calculated=False
        if self.content_string:
            last_character = self.content_string.rstrip()[-1]
            if ch in ['+', '-', '*', '/']:
                if last_character not in ['+', '-', '*', '/', '.']:
                    if self.is_negative:
                        temp_1=self.last_part_extractor(check=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],digit_required=True)
                        if temp_1 == '0':
                            self.content_string = self.content_string[:-3] + '0' + ' ' + ch + ' '
                        else:
                            self.content_string = self.content_string + ')' + ' ' + ch + ' '
                        self.is_negative = False
                    else:
                        self.content_string = self.content_string + ' ' + ch + ' '
                elif last_character == '.':
                    self.content_string = self.content_string[:-1]
                    if self.is_negative:
                        self.content_string = self.content_string + ')' + ' ' + ch + ' '
                        self.is_negative = False
                    else:
                        self.content_string = self.content_string + ' ' + ch + ' '
                else:
                    if not self.is_negative:
                        self.content_string = self.content_string[:-2] + ch + ' '
            elif ch == "negative":
                if last_character not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                    if not self.is_negative:
                        self.is_negative = True
                        self.content_string = self.content_string + '(' + '-'
                    else:
                        self.is_negative=False
                        self.content_string=self.content_string[:-2]

            elif ch == '.':
                last_part=self.last_part_extractor()
                if '.' not in last_part and len(last_part) > 0:
                    if last_part[-1] != '-':
                        self.content_string = self.content_string + '.'
            else:
                last_part=self.last_part_extractor()
                if ch != '0':
                    if len(last_part) == 0:
                        self.content_string = self.content_string + ch
                    else:
                        temp_1=self.last_part_extractor(check=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'],digit_required=True)
                        if temp_1 == '0':
                            self.content_string = self.content_string[:-1] + ch
                        else:
                            self.content_string = self.content_string + ch
                else:
                    temp_1=self.last_part_extractor(check=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'],digit_required=True)
                    if temp_1 != '0':
                        self.content_string = self.content_string + ch
        else:
            if ch in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.content_string = self.content_string + ch
            elif ch == "negative":
                self.is_negative = True
                self.content_string = self.content_string + '(' + '-'
        self.content_refresher()

    def delete(self):
        if self.is_result_calculated:
            self.content_string=""
        else:
            self.content_string = self.content_string[:-1]
        self.content_refresher()

    def all_clear(self):
        self.content_string=""
        self.content_refresher()

    def check_before_solve(self):
        if self.is_negative:
            temp_1 = self.last_part_extractor(check=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0','.'],digit_required=True)
            if temp_1:
                if temp_1 == '0':
                    self.content_string = self.content_string[:-3] + '0'
                elif temp_1[-1]=='.':
                    self.content_string=self.content_string[:-1]+')'
                else:
                    self.content_string = self.content_string + ')'
            else:
                self.content_string=self.content_string[:-2]
                temp_2=self.content_string.rstrip()
                if temp_2:
                    self.content_string=self.content_string[:-3]
            self.is_negative=False
        else:
            temp_1=self.content_string.rstrip()
            if temp_1:
                last_part = temp_1[-1]
                if last_part in ['-', '+', '*', '/']:
                    self.content_string = self.content_string[:-3]
                if last_part == '.':
                    self.content_string = self.content_string[:-1]
        self.content_refresher()


    def solve(self):
        if self.is_result_calculated:
            pass
        else:
            self.check_before_solve()
            self.result = simplify(self.content_string)
            self.result=self.result.evalf()
            self.result="{:g}".format(float(self.result))
            self.content_string = self.content_string + " = " + str(self.result)
            self.is_result_calculated = True
            self.content_refresher()

    def keyboard_entry(self,event):
        key=event.char
        keysym=event.keysym
        if key in ['0','1','2','3','4','5','6','7','8','9','.','+','-','/','*']:
            self.add_content(key)
        elif key =='=':
            self.solve()
        elif keysym=="Return":
            self.solve()
        elif keysym=="BackSpace":
            self.delete()
        elif keysym=="Escape":
            self.all_clear()
        else:
            pass

window = Tk()
window.geometry("350x500")
window.configure(bg="#1e1e1e")
window.resizable(False, False)
calculator = Calculator(window)
window.mainloop()
