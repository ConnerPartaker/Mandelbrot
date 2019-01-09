import tkinter as tk

WIDTH, HEIGHT, MAG, MAX, RAD, INITS, INITX, INITY, JULIA = 300, 300, 2, 15, 2.5, 3, 2, 1.5, None#complex(1,1)

class Mandelbrot():
    def __init__(self, img, a = None):
        
        self.img, self.scale, self.imgloc, self.a = img, (INITS*WIDTH/HEIGHT, INITS), complex(-INITX*WIDTH/HEIGHT,INITY), a
        self.pixelSet = [(x, y) for x in range(WIDTH) for y in range(HEIGHT)]
        self.colors = {0:  '#1E0C15', 1:  '#19071A', 2:  '#09012F', 3:  '#04044F',
                       4:  '#000764', 5:  '#0C2C9A', 6:  '#1852B1', 7:  '#397DD1',
                       8:  '#86B5E7', 9:  '#D3ECF8', 10: '#F1E9CF', 11: '#F8C95F',
                       12: '#FFAA00', 13: '#CC8000', 14: '#995700', 15: '#6A3403'}
    
    def repaint(self, event = None):
        if event: self.recalc(event)
        for i in self.pixelSet:
            self.img.put(self.calc(i), i)
        
    def calc(self, i):
        indice = self._indice_of(self._complex_of(i), z0 = self.a)
        return '#000000' if indice == MAX else self.colors.get(indice%16)
    
    def recalc(self, e):
        self.imgloc += complex(self.scale[0]*(e.x/WIDTH  - .5/MAG),
                              -self.scale[1]*(e.y/HEIGHT - .5/MAG))
        self.scale   = tuple(x/MAG for x in self.scale)
    
    def _complex_of(self, i):
        return complex((self.scale[0])*i[0]/WIDTH,-(self.scale[1])*i[1]/HEIGHT) + self.imgloc
        
    def _indice_of(self, z, z0 = None, level = 0):
        if not z0: z0 = z
        z = (z**2) + z0
        return level if not abs(z)<RAD or level==MAX else self._indice_of(z, z0, level+1)
        
def createCanvas(mandel, root):
    canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
    canvas.create_image((WIDTH//2, HEIGHT//2), image = mandel.img)
    canvas.bind("<Button-1>", mandel.repaint)
    canvas.pack()
    canvas.mainloop()
    
def main():
    root = tk.Tk()
    mandel = Mandelbrot(tk.PhotoImage(width = WIDTH, height = HEIGHT), JULIA)
    mandel.repaint()
    createCanvas(mandel, root)
    
if __name__ == '__main__': main()