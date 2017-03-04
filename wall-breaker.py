from Tkinter import *
import pygame
import random
import tkMessageBox

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

son1 = pygame.mixer.Sound("pawn1.wav")
son1.set_volume(0.75)

son2 = pygame.mixer.Sound("wrong.wav")
son2.set_volume(0.15)

def Drag(event):
	""" Platform moving with mouse """
	global PosX,PosY,PosX1,PosY1,X
	X = event.x
	if test == 0:
		if X >= PosX and X <= PosX1:
			if PosX1<1000 and PosX>0:
				PosX = X - 50
				PosX1 = X +50

			if PosX1 >= 1000:
				PosX = 899
				PosX1 = 999

			elif PosX <= 0:
				PosX1 = 101
				PosX = 1

			Canvas.coords(Pion,PosX,PosY,PosX1,PosY1)

def Keyboard(event):
	""" Key detection """
	global PosX,PosY,PosX1,PosY1,X,test
	Key = event.keysym
	if test == 0:
		if Key == 'Right' and PosX1<1000:
			PosX += 10
			PosX1 += 10

		elif Key == 'Left'and PosX>0:
			PosX -= 10
			PosX1 -= 10

	if Key == 'p':
		if test == 0:
			test = 1
		else:
			test = 0
			ball()
			ball1()

	X = PosX+50
	Canvas.coords(Pion,PosX,PosY,PosX1,PosY1)

def ball():
	""" First ball movement/collision """
	global Posx,Posy,x,y,X,x1,x2,y1,y2,score,erreur,son1,son2,test,test1
	if test == 0:
		Canvas.coords(Ball,Posx-5,Posy-5,Posx+5,Posy+5)
		Posy += y
		Posx += x
		if Posy+5 >= PosY and Posx > PosX and Posx < PosX1:
			son1.play()
			y = -y
			x = x+(Posx - (PosX+50))/50.0

			if x > 2:
				x = 2

			elif x < -2:
				x = -2

		elif Posy-5 <= 5:
			son1.play()
			y = -y
			x = x

		elif Posx+5 >= 1000:
			son1.play()
			x = -x

		elif Posx-5 <= 0:
			son1.play()
			x = -x

		elif Posy >= 500:
			son2.play()
			erreur += 1
			test = 0
			Heart()

		if Posx >= x1-5 and Posx <= x2+5 and Posy >= y1-5 and Posy <= y2+5:
			son1.play()
			if Posy >= y1+4.99 and Posy <= y2+4.99:
				x = -x
			else:
				y = -y
				x = x
			points()

		root.after(5,ball)

def ball1():
	""" Second ball movement/collision """
	global Posx1,Posy1,xx,yx,Xx,x1,x2,y1,y2,score,erreur,son1,son2,test,test1
	if test == 0:
		Canvas.coords(Ball1,Posx1-5,Posy1-5,Posx1+5,Posy1+5)
		Posy1 += yx
		Posx1 += xx
		if Posy1+5 >= PosY and Posx1 > PosX and Posx1 < PosX1:
			son1.play()
			yx = -yx
			xx = xx+(Posx1 - (PosX+50))/50.0

			if xx > 2:
				xx = 2

			elif xx < -2:
				xx = -2

		elif Posy1-5 <= 5:
			son1.play()
			yx = -yx
			xx = xx

		elif Posx1+5 >= 1000:
			son1.play()
			xx = -xx

		elif Posx1-5 <= 0:
			son1.play()
			xx = -xx

		elif Posy1 >= 500:
			son2.play()
			erreur += 1
			test1 = 1
			Heart()

		if Posx1 >= x1-5 and Posx1 <= x2+5 and Posy1 >= y1-5 and Posy1 <= y2+5:
			son1.play()
			if Posy1 >= y1+4.99 and Posy1 <= y2+4.99:
				xx = -xx
			else:
				yx = -yx
				xx = xx
			points()

		root.after(5,ball1)

def points():
	""" Add a point """
	global score,x1,y1,x2,y2,wall,score1,Label1
	score += 1
	score1 += 1
	Canvas.delete(wall)
	Label1.destroy()
	x1 = random.randint(1,999)
	y1 = random.randint(1,400)
	x2 = x1 + 50
	y2 = y1 + 20
	wall = Canvas.create_rectangle(x1,y1,x2,y2,fill='black')
	Label1 = Label(root, text = 'Score : %s'%score)
	Label1.pack(side = TOP, padx = 5, pady = 0)
	print 'Score :',score

def carre():
	""" Replace wall """
	global score,x1,y1,x2,y2,wall,bonu,Label1
	if bonu >0:
		Canvas.delete(wall)
		x1 = random.randint(1,947)
		y1 = random.randint(1,385)
		x2 = x1 + 50
		y2 = y1 + 20
		wall = Canvas.create_rectangle(x1,y1,x2,y2,fill='black')
		if bonu == 3:
			bonu -= 1
			Canvas.delete(item5)

		elif bonu == 2:
			bonu -= 1
			Canvas.delete(item4)

		elif bonu == 1:
			bonu -= 1
			Canvas.delete(item3)

	else:
		if score > 0:
			Label1.destroy()
			score -= 1
			print 'Score :',score
			Label1 = Label(root, text = 'Score : %s'%score)
			Label1.pack(side = TOP, padx = 5, pady = 0)

		Canvas.delete(wall)
		x1 = random.randint(1,947)
		y1 = random.randint(1,385)
		x2 = x1 + 50
		y2 = y1 + 20
		wall = Canvas.create_rectangle(x1,y1,x2,y2,fill='black')

def Heart():
	""" Remove a life """
	global erreur,item,item1,item2,Posx,Posy,x,y,X,score,test1,Posx1,Posy1,xx,yx,Xx,Label1
	if test1 == 0:
		Posx = 500
		Posy = 10

		x = 0
		y = 1
		X = 500

	else:
		Posx1 = 500
		Posy1 = 10

		xx = 0
		yx = 1
		Xx = 500

	if erreur == 1:
		Canvas.delete(item)
		item = Canvas.create_image(1000,0,anchor=NE, image=photo1)
		score -= 5

	elif erreur == 2:
		Canvas.delete(item1)
		item1 = Canvas.create_image(975,0,anchor=NE, image=photo1)
		score -= 10

	if score < 0:
		score = 0
		print 'Score :',score

	else:
		print 'Score :',score

	Label1.destroy()
	Label1 = Label(root, text = 'Score : %s'%score)
	Label1.pack(side = TOP, padx = 5, pady = 0)

	if erreur == 3:
		Canvas.delete(item2)
		item2 = Canvas.create_image(950,0,anchor=NE, image=photo1)
		Gameover()

def Gameover():
	""" Game Over message """
	global test
	test = 1
	tkMessageBox.showwarning('CASSE BRIQUE','Score : '+str(score)+'\nScore(sans malus) : '+str(score1)+'\n\n!!!!!GAME OVER !!!!!')
	root.destroy()

def new():
	""" Add a ball """
	global Ball1,plaba
	plaba.destroy()
	Ball1 = Canvas.create_oval(Posx1-5,Posy1-5,Posx1+5,Posy1+5,width=1,outline='black',fill='Wheat')
	ball1()

root = Tk()
root.title('CASSE BRIQUE')

PosX = 450
PosY = 480
PosX1 = 550
PosY1 = 490

Posx = 500
Posy = 250
Posx1 = 500
Posy1 = 250

erreur = 0
bonu = 3

x = 0
y = 1
X = 500

xx = 0
yx = 1

x1 = 100
y1 = 100
x2 = 150
y2 = 120

score = 0
score1 = 0

Largeur = 1000
Hauteur = 500

test = 0
test1 = 0

Canvas = Canvas(root, width = Largeur, height =Hauteur,bg='Firebrick')

photo = PhotoImage (file="heart.gif")
photo1 = PhotoImage (file="over1.gif")
photo2 = PhotoImage (file="over.gif")
photo3 = PhotoImage (file="bonus.gif")

item = Canvas.create_image(1000,0,anchor=NE, image=photo)
item1 = Canvas.create_image(975,0,anchor=NE, image=photo)
item2 = Canvas.create_image(950,0,anchor=NE, image=photo)

item3 = Canvas.create_image(0,0,anchor=NW, image=photo3)
item4 = Canvas.create_image(25,0,anchor=NW, image=photo3)
item5 = Canvas.create_image(50,0,anchor=NW, image=photo3)

Pion = Canvas.create_rectangle(PosX,PosY,PosX1,PosY1,width=2,outline='black',fill='Salmon')
Ball = Canvas.create_oval(Posx-5,Posy-5,Posx+5,Posy+5,width=1,outline='black',fill='Wheat')

wall = Canvas.create_rectangle(x1,y1,x2,y2,fill='black')

Canvas.focus_set()

Canvas.bind('<Key>', Keyboard)
Canvas.bind('<B1-Motion>',Drag)
Canvas.pack(padx =5, pady =5)


h1 = Hauteur//2
l1 = Largeur//2

ball()
print 'Score :',score


Button(root, text ='Quitter', command = Gameover).pack(side=RIGHT,padx=5,pady=5)
plaba = Button(root, text ='ba', command = new)
Button(root, text ='Placer un carre', command = carre).pack(side=LEFT,padx=5,pady=5)
plaba.pack(side=LEFT,padx=5,pady=5)
Label1 = Label(root, text = 'Score : %s'%score)
Label1.pack(side = TOP, padx = 0, pady = 0)

root.mainloop()

root.destroy()
