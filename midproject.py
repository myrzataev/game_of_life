from msilib.schema import Upgrade
from tkinter import*
from time import sleep
from random import randint, choice
from turtle import heading
 
class Field:
    def __init__(self, c, n, m, width, height, walls=False):
        '''
        c - canvas instance
        n - number of rows
        m - number of columns
        width - width of game field in pixels
        height - width of game field in pixels
        walls - if True matrix should have 0's surrounded by 1's (walls)
        example
        1 1 1 1
        1 0 0 1
        1 1 1 1
        '''
        self.l = []
        
        self.c = c
        self.a = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            self.l.append([])
            for j in range(self.m):
                # self.a[i].append(choice([0, 1]))
                self.a[i].append(0)
                self.l[i].append(0)
        for i in range(1,self.m):
            self.l[self.n//2][i] = 2

        self.draw()

        self.a[1][1] = 1
        self.a[1][3] = 1
        self.a[2][2] = 1
        self.a[2][3] = 1
        self.a[3][2] = 1
        self.draw()
    
    def step(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(0)
        
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                neib_sum = self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a[i - 1][j + 1] + self.a[i][j - 1] + self.a[i][j + 1] + self.a[i + 1][j - 1] + self.a[i + 1][j] + self.a[i + 1][j + 1]
                if neib_sum < 2 or neib_sum > 3:
                    b[i][j] = 0
                elif neib_sum == 3:
                    b[i][j] = 1
                else:
                    b[i][j] = self.a[i][j]
        
        self.a = b
    
 
    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()



    def draw(self):
        '''
        draw each element of matrix as a rectangle with white background and wall rectangle should have dark grey background
        '''
        color = "grey"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = "green"
                elif (self.a[i][j] == 1):
                    color = "black"
                else:
                    color = "white"
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) * sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(100, self.draw)
 

class NewClass(Field):
    def __init__(self, c, n, m, width, height, walls=False ):
        super().__init__(c, n, m, width, height, walls)


    def draw(self):
        '''
        draw each element of matrix as a rectangle with white background and wall rectangle should have dark grey background
        '''
        color = "white"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        
        
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):             
             
                if self.a[i][j] == 1 and i > (self.n//2) and j > (self.m//2):
                    color = "magenta"
                elif self.a[i][j] == 1 and i < (self.n//2) and j <  (self.m//2):
                    color = "lime"

                
                else:
                    color = "white"
                if self.l[i][j] == 2:
                    color ='gold'
                
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) * sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(100, self.draw)

    



root = Tk()
root.geometry("500x500")
c = Canvas(root, width=500, height=500)
c.pack()
 
upgrade = NewClass(c, 20, 20, 500, 500)
upgrade.print_field()

root.mainloop()
# c.create_oval(p.x + 5,p.y + 5,p.x+p.size + 5,p.y+p.size + 5)
