
from tkinter import *
from tkinter import ttk
from model import *


class View(object):
    def __init__(self):
        self.m = Model()

        self.font = ('System', '11', 'bold')
        self.bfont = ('System', '14', 'bold')

        self.window = Tk()
        #self.window.resizable(0, 0)


        self.game_board(self.window);


    def make_3_col(self,frame,pos,alg):
        buttons = dict()
        if pos == 0:
            for c in range(3):
                for r in range(8):
                    if ((alg==0 and (r==4 and (c==0 or c==2))) or alg==1 and (r==3 and (c==0 or c==2))):
                        b = ttk.Button(frame, background="blue", width=5, height=2).grid(row=r, column=c)
                        buttons[(r,c)] = b
                    elif (c==1):
                        if (alg==0 and r==0) or (alg==1 and r==7):
                            b = ttk.Button(frame, background="blue", width=5, height=2).grid(row=r, column=c)
                            buttons[(r,c)] = b
                        else:
                            b = ttk.Button(frame, background="red", width=5, height=2).grid(row=r, column=c)
                            buttons[(r,c)] = b
                    else:
                        b = ttk.Button(frame, width=5, height=2).grid(row=r, column=c)
                        buttons[(r,c)] = b

        else:
            for c in range(8):
                for r in range(3):
                    if ((alg==0 and (c==4 and (r==0 or r==2))) or alg==1 and (c==3 and (r==0 or r==2))):
                        b = ttk.Button(frame, background="blue", width=2, height=5).grid(row=r, column=c)
                        buttons[(r,c)] = b
                    elif (r==1):
                        if (alg==0 and c==0) or (alg==1 and c==7):
                            b = ttk.Button(frame, background="blue", width=2, height=5).grid(row=r, column=c)
                            buttons[(r,c)] = b
                        else:
                            b = ttk.Button(frame, background="red", width=2, height=5).grid(row=r, column=c)
                            buttons[(r,c)] = b
                    else:
                        b = ttk.Button(frame, width=2, height=5).grid(row=r, column=c)
                        buttons[(r,c)] = b
        return buttons


    def game_board(self, w):
        home_green = ttk.Button(w, background="green")
        home_yellow = ttk.Button(w, background="yellow")
        home_blue = ttk.Button(w, background="blue")
        home_red = ttk.Button(w, background="red")
        heaven = ttk.Button(w, background="red")
        row_green = ttk.Frame(w)
        row_yellow = ttk.Frame(w)
        row_blue = ttk.Frame(w)
        row_red = ttk.Frame(w)

        home_green.grid(row=0, column=0)
        row_green.grid(row=0, column=1)
        home_yellow.grid(row=0, column=2)

        row_red.grid(row=1, column=0)
        heaven.grid(row=1, column=1)
        row_yellow.grid(row=1, column=2)

        home_red.grid(row=2, column=0)
        row_blue.grid(row=2, column=1)
        home_blue.grid(row=2, column=2)


        bb = self.make_3_col(row_blue,0,1)
        enter_blue = Slot(bb[0,0], None)
        end = enter_blue
        for r in range(1,8):
            end.make_next(Slot(bb[r,0], None))
            end = end.next
        split = Slot(bb[7,1], None, _access_alt=Player.BLUE, _qual=Qual.SAFE)
        end.make_next(split)
        end = split
        for r in range(7,-1,-1):
            end.make_next(Slot(bb[r,2], None))
            end = end.next

        split.alt = Slot(bb[6,1], None)
        home = split
        for r in range(5,-1,-1): #alt home row
            home.make_next(Slot(bb[r,1], None, _qual=Qual.HOME))
            home = home.next
        home.make_next(Slot(heaven, None))

        background = self.make_3_col(row_green,0,0)




        br = self.make_3_col(row_red,1,0)
        by = self.make_3_col(row_yellow,1,1)


    def launch_window(self): #needs to be at end
        self.window.mainloop()
