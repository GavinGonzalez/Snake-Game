from time import sleep
import numpy as np
from random import randint
import pygame
import sys
import random
import time
import copy


class Snake:
	def __init__(self, color, seg_w, segments, surface):
		self.color = color
		self.segments = segments
		self.seg_w = seg_w
		self.surface = surface

		
	def draw_snake(self, dir):

		self.dir = dir

		#x, y does not get updated(there whole numbers instead of being multiply by 40)
		for i in range(len(self.segments)):
			pygame.draw.rect(self.surface, self.color, (self.segments[i][0]*self.seg_w, self.segments[i][1]*self.seg_w, self.seg_w, self.seg_w))

		if(dir == "up"):
			copy = self.segments[:-1]
			copy.insert(0, (copy[0][0], copy[0][1]-1))
			self.segments = copy[:]

		if(dir == "down"):
			copy = self.segments[:-1]
			copy.insert(0, (copy[0][0], copy[0][1]+1))
			self.segments = copy[:]

		if(dir == "right"):
			copy = self.segments[:-1]
			copy.insert(0, (copy[0][0]+1, copy[0][1]))
			self.segments = copy[:]

		if(dir == "left"):
			copy = self.segments[:-1]
			copy.insert(0, (copy[0][0]-1, copy[0][1]))
			self.segments = copy[:]

	def get_head_pos(self):
		return self.segments[2]

	def add_seg(self):
		
		if(dir == "up"):
			self.segments.insert(0, (segments[0][0], segments[0][1]+1))

		if(dir == "down"):
			self.segments.insert(0, (segments[0][0], segments[0][0]-1))

		if(dir == "left"):
			self.segments.insert(0, (segments[0][0]+1, segments[0][0]))

		if(dir == "right"):
			self.segments.insert(0, (segments[0][0]-1, segments[0][0]))




class Apple:
	def __init__(self, color, center, radius, surface):
		self.color = color
		self.center = center
		self.radius = radius
		self.surface = surface
		

	def draw_apple(self):
		pygame.draw.circle(self.surface, self.color, self.center, self.radius)


	def get_center(self):
		return self.center


#pygame.draw.line(surface, (255, 255, 255), (x, 40), (x, w))



def redraw_window():
	screen = pygame.display.set_mode((800, 800))
	screen.fill((40, 0, 0))

def direction_false(direct_1, direct_2, direct_3):
	direct_1 = False
	direct_2 = False
	direct_3 = False



def main():
	
	hit = False
	left = False
	right = False
	up = False
	down = False
	snake = []
	screen = pygame.display.set_mode((800, 800))
	clock = pygame.time.Clock()
	segments = [(5, 10), (6, 10), (7, 10)]
	snake = Snake((255,100,10), 40, segments, screen)
	apple = Apple((180,255,100), (40*3+20, 40*3+20), 20, screen)
	
	
	while(True):
		redraw_window()
		apple_c = apple.get_center()
		snake_h = snake.get_head_pos()

		
		if((apple_c[0]-20 <= snake_h[0]*40 and apple_c[0]+20 >= snake_h[0]*40) and (apple_c[1]-20 <= snake_h[1]*40+20 and apple_c[1]+20 >= snake_h[1]*40+20)):
		
			snake.add_seg()
		


		if(hit == False):
			apple.draw_apple()	

		if(up):
			snake.draw_snake("up")

		if(down):
			snake.draw_snake("down")

		if(left):
			snake.draw_snake("left")

		if(right):
			snake.draw_snake("right")




		
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_DOWN:
					left = False
					right = False
					up = False
					down = True	

				if event.key == pygame.K_UP:
					up = True
					left = False
					right = False
					down = False
					
				if event.key == pygame.K_LEFT:
					left = True
					right = False
					up = False
					down = False

				if event.key == pygame.K_RIGHT:
					left = False
					right = True
					up = False
					down = False
			

		
		clock.tick(5)		
if __name__ == '__main__':
	main()
