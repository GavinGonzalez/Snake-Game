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
		self.segments = segments
		self.seg_w = seg_w
		self.surface = surface
		self.color = color

	
	def draw_snake(self, dirr):
		self.dir = dirr
	
		for i in range(len(self.segments)):
			pygame.draw.rect(self.surface, self.color, (self.segments[i][0]*self.seg_w, self.segments[i][1]*self.seg_w, self.seg_w, self.seg_w))

		if(self.dir == "up"):
			copy = self.segments[:-1]
			copy.insert(0, (copy[0][0], copy[0][1]-1))
			self.segments = copy[:]

		if(self.dir == "down"):
			copy = self.segments[:-1]
			copy.insert(0, (copy[0][0], copy[0][1]+1))
			self.segments = copy[:]

		if(self.dir == "right"):
			copy = self.segments[:-1]
			copy.insert(0, (copy[0][0]+1, copy[0][1]))
			self.segments = copy[:]

		if(self.dir == "left"):
			copy = self.segments[:-1]
			copy.insert(0, (copy[0][0]-1, copy[0][1]))
			self.segments = copy[:]

	def get_head_pos(self):
		return self.segments[2]

	def add_seg(self):

		print(self.segments)
		
		if(self.dir == "up"):
			self.segments.insert(len(self.segments), (self.segments[len(self.segments)-1][0], self.segments[len(self.segments)-1][0]-1))

		if(self.dir == "left"):
			self.segments.insert(len(self.segments), (self.segments[len(self.segments)-1][0]+1, self.segments[len(self.segments)-1][0]))

		if(self.dir == "right"):
			self.segments.insert(len(self.segments), (self.segments[len(self.segments)-1][0]-1, self.segments[len(self.segments)-1][0]))

		print(self.segments[len(self.segments)-1])
		

	def hit_edge(self, wind_w, wind_h):
		head = self.get_head_pos()
		
		if(self.segments[0][1]*40 == -40 or self.segments[0][1]*40 == wind_h):
			return True
		
		if(self.segments[0][0]*40 == -40 or self.segments[0][0]*40 == wind_w):
			return True

		else: 
			return False

		

class Apple:
	def __init__(self, color, center, radius, surface, wind_w, wind_h):
		self.color = color
		self.center = center
		self.radius = radius
		self.surface = surface
		self.wind_w = wind_w
		self.wind_h = wind_h
		

	def draw_apple(self):
		pygame.draw.circle(self.surface, self.color, self.center, self.radius)


	def get_center(self):
		return self.center

	def random_pos(self):
		# calculates a random position for the apple based off the width and height of the window
		# each block is 40 pixels thats why we multiply tje radius by two
		#19 is to center the circle in the block, so the snake is able to collide with it
		self.center = (randint(0, self.wind_w/(self.radius*2))*(self.radius*2)+19, randint(0, self.wind_h/(self.radius*2))*(self.radius*2)+19)
		pygame.draw.circle(self.surface, self.color, self.center, self.radius)






def redraw_window():
	screen = pygame.display.set_mode((800, 800))
	screen.fill((240, 250, 252))

def direction_false(direct_1, direct_2, direct_3):
	direct_1 = False
	direct_2 = False
	direct_3 = False



def main():
	i = False
	hit = False
	left = False
	right = False
	up = False
	down = False
	started = False
	start_box_pos = (326, 320)
	last_dir = ""
	pygame.init()
	snake = []
	screen = pygame.display.set_mode((800, 800))
	pygame.display.set_caption("Snake Game")
	clock = pygame.time.Clock()


	start_font = pygame.font.SysFont('microsofttaile', 30)
	title_font = pygame.font.SysFont('freesans', 160)

	title_surface = title_font.render("Snake", False,  (104, 209, 197))
	start_surface = start_font.render("Start Game", False,  (104, 209, 197))
			
	
	segments = [(8, 11), (7, 11), (6, 11)]
	snake = Snake((104, 209, 197), 40, segments, screen)
	apple = Apple((242, 183, 184), (40*3+19, 40*3+19), 20, screen, 800, 800)
	
	
	while(True):
		redraw_window()
		
		#snake.p()


		apple_c = apple.get_center()
		snake_h = snake.get_head_pos()
		


		if(started == False):


			#game title
			pygame.draw.rect(screen, (240, 250, 252), (310, 210, 100, 80))
			screen.blit(title_surface, (220, 160))

			#start buttom 
			pygame.draw.rect(screen, (244, 179, 206), (start_box_pos[0], start_box_pos[1], 148, 40))
			screen.blit(start_surface, (326, 320))


		


			
		else:
			
			if(snake.hit_edge(800, 800)):
				started = True

		
			
			apple.draw_apple()	


			if((apple_c[0]-20 <= snake_h[0]*40 and apple_c[0]+20 >= snake_h[0]*40) and (apple_c[1]-20 <= snake_h[1]*40+20 and apple_c[1]+20 >= snake_h[1]*40+20)):
				snake.add_seg()
				apple.random_pos()
				
				


			if(last_dir == ""):
				snake.draw_snake("")


			if(up):
				if(last_dir != "down"):
					snake.draw_snake("up")
					last_dir = "up"

				else:
					snake.draw_snake("down")

			if(down):
				if(last_dir != "up"):
					snake.draw_snake("down")
					last_dir = "down"

				else:
					snake.draw_snake("up")

			if(left):

				if(last_dir != ""):
					

					if(last_dir != "right"):
						snake.draw_snake("left")
						last_dir = "left"

					else:	
						snake.draw_snake("right")

			if(right):
				if(last_dir != "left"):
					snake.draw_snake("right")
					last_dir = "right"

				else:	
					snake.draw_snake("left")



			

		
		
		



		
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				
				movement = pygame.mouse.get_pos()
				mouse_c = movement[0]
				mouse_r = movement[1]
				print(movement)
				
				if mouse_c >= start_box_pos[0] and mouse_c <= start_box_pos[0]+148 and mouse_r >= start_box_pos[1] and mouse_r <= start_box_pos[1]+40:
					started = True
					print("hit")
			
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





