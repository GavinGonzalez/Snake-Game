from time import sleep
import numpy as np
from random import randint
import pygame
import sys
import random
import time
import copy
import sys


class Snake:
	def __init__(self, color, seg_w, segments, surface):
		self.segments = segments
		self.seg_w = seg_w
		self.surface = surface
		self.color = color

	
	def draw_snake(self, dirr):
		self.dir = dirr
	
		for i in range(len(self.segments)):
			pygame.draw.rect(self.surface, self.color, (self.segments[i].x*self.seg_w, self.segments[i].y*self.seg_w, self.seg_w, self.seg_w))

		
		if(self.dir == "up"):
			copy = self.segments[:-1]
			copy.insert(0, seg(copy[0].x, copy[0].y-1))
			copy[0].set_dir("up")
			self.segments = copy[:]

		if(self.dir == "down"):
			copy = self.segments[:-1]
			copy.insert(0, seg(copy[0].x, copy[0].y+1))
			copy[0].set_dir("down")
			self.segments = copy[:]

		if(self.dir == "right"):
			copy = self.segments[:-1]
			copy.insert(0, seg(copy[0].x+1, copy[0].y))
			copy[0].set_dir("right")
			self.segments = copy[:]

		if(self.dir == "left"):
			copy = self.segments[:-1]
			copy.insert(0, seg(copy[0].x-1, copy[0].y))
			copy[0].set_dir("left")
			self.segments = copy[:]

	def get_head_pos(self):
		return (self.segments[0].x, self.segments[0].y)

	def add_seg(self):

		
		
		if(self.segments[len(self.segments)-1].dir == "up"):
			self.segments.insert(len(self.segments), seg(self.segments[len(self.segments)-1].x, self.segments[len(self.segments)-1].y+1))
			self.segments[len(self.segments)-1].set_dir(self.segments[len(self.segments)-2].dir)

		if(self.segments[len(self.segments)-1].dir == "down"):
			self.segments.insert(len(self.segments), seg(self.segments[len(self.segments)-1].x, self.segments[len(self.segments)-1].y-1))
			self.segments[len(self.segments)-1].set_dir(self.segments[len(self.segments)-2].dir)

		if(self.segments[len(self.segments)-1].dir == "left"):
			self.segments.insert(len(self.segments), seg(self.segments[len(self.segments)-1].x+1, self.segments[len(self.segments)-1].y))
			self.segments[len(self.segments)-1].set_dir(self.segments[len(self.segments)-2].dir)

		if(self.segments[len(self.segments)-1].dir == "right"):
			self.segments.insert(len(self.segments), seg(self.segments[len(self.segments)-1].x-1, self.segments[len(self.segments)-1].y))
			self.segments[len(self.segments)-1].set_dir(self.segments[len(self.segments)-2].dir)
		
		

	def hit_edge(self, wind_w, wind_h):
		head = self.get_head_pos()
		
		if(self.segments[0].y*40 == -40 or self.segments[0].y*40 == wind_h):
			return True
		
		if(self.segments[0].x*40 == -40 or self.segments[0].x*40 == wind_w):
			return True

		else: 
			return False

	def overlap(self):
		pos = []

		for i in range(len(self.segments)):
			pos.insert(0, (self.segments[i].x, self.segments[i].y))
	
		for i in range(len(pos)):
			if(pos.count(pos[i]) > 1):
				return True

		return False


	def reset(self, segments):
		self.segments = segments
		self.dir = ""

		

class Apple:
	def __init__(self, color, surface, seg_w, seg_h, wind_w, wind_h, pos):
		self.color = color
		self.surface = surface
		self.wind_w = wind_w
		self.wind_h = wind_h
		self.seg_w = seg_w
		self.seg_h = seg_h
		self.pos = pos
		

	def draw_apple(self):
		pygame.draw.rect(self.surface, self.color, (self.pos[0]*self.seg_w, self.pos[1]*self.seg_h, self.seg_w, self.seg_w))


	def get_pos(self):
		return self.pos

	def random_pos(self):
		# calculates a random position for the apple based off the width and height of the window
		# each block is 40 pixels thats why we multiply tje radius by two
		#19 is to center the circle in the block, so the snake is able to collide with it
		self.pos = (randint(1, self.wind_w/self.seg_w)-1, randint(1, self.wind_h/self.seg_h)-1)
		


class seg:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def set_dir(self, dirr):
		self.dir = dirr

	def get_pos(self):
		return (self.x, self.y)

def redraw_window():
	screen = pygame.display.set_mode((800, 800))
	screen.fill((240, 250, 252))

def game_title(screen):
	title_font = pygame.font.SysFont('freesans', 160)
	title_surface = title_font.render("Snake", False,  (104, 209, 197))
	pygame.draw.rect(screen, (240, 250, 252), (310, 210, 100, 80))
	screen.blit(title_surface, (165, 155))

def start_button(screen):
	start_font = pygame.font.SysFont('microsofttaile', 30)
	start_surface = start_font.render("Start Game", False,  (104, 209, 197))
	pygame.draw.rect(screen, (244, 179, 206), (326, 320, 148, 40))
	screen.blit(start_surface, (326, 320))

def score_counter(screen, counter):
	counter_font = pygame.font.SysFont('freesans', 35)
	counter_surface = counter_font.render(("Counter: " + str(counter)), False, (240, 250, 252))
	pygame.draw.rect(screen, (244, 179, 206), (0, 0, 170, 40))
	screen.blit(counter_surface, (5, 0))

def after_game_score(screen, counter):
	score_font = pygame.font.SysFont('freesans', 60)
	score_surface = score_font.render("SCORE OF " + str(counter), False, (104, 209, 197))
	screen.blit(score_surface, (200, 230))

def reset_button(screen):
	reset_font = pygame.font.SysFont('freesans', 35)
	reset_surface = reset_font.render("Reset", False, (104, 209, 197))
	pygame.draw.rect(screen, (244, 179, 206), (390, 300, 120, 40))
	screen.blit(reset_surface, (405, 300))

def exit_button(screen):
	exit_font = pygame.font.SysFont('freesans', 35)
	exit_surface = exit_font.render("Exit", False, (104, 209, 197))
	pygame.draw.rect(screen, (244, 179, 206), (275, 300, 100, 40))
	screen.blit(exit_surface, (295, 300))


def main():
	i = False
	
	started = False
	reset = False
	game_over = True
	counter = 0
	l = False
    
	start_box_pos = (326, 320)
	reset_box_pos = (405, 300)
	exit_box_pos =  (295, 300)

	last_dir = ""
	dirr = ""

	pygame.init()
	snake = []
	screen = pygame.display.set_mode((800, 800))
	pygame.display.set_caption("Snake Game")
	clock = pygame.time.Clock()
	
	segments = []
	segments.insert(0, seg(6, 11))
	segments.insert(0, seg(7, 11))
	segments.insert(0, seg(8, 11))

	snake = Snake((104, 209, 197), 40, segments, screen)
	apple = Apple((242, 183, 184), screen, 40, 40, 800, 800, (5, 5))
	
	
	while(True):
		redraw_window()
		
		#snake.p()


		apple_pos = apple.get_pos()
		snake_h = snake.get_head_pos()
		


		if(started == False):


			if(game_over == True):
				game_title(screen)

				start_button(screen)

			if(reset == True):
				
				reset_button(screen)

				exit_button(screen)

				after_game_score(screen, counter)
			
		else:

			#counter
			score_counter(screen, counter)
			
			apple.draw_apple()
			
			if(snake.hit_edge(800, 800) or snake.overlap()):
				snake.reset(segments)
				started = False
				game_over = False
				reset = True
				last_dir = ""
				dirr = ""
			
			

			if(apple_pos == snake_h):
				snake.add_seg()
				apple.random_pos()
				counter = counter + 1

				
				
				


			if(last_dir == ""):
				snake.draw_snake("")


			if(dirr == "up"):
				if(last_dir != "down"):
					snake.draw_snake("up")
					last_dir = "up"

				else:
					snake.draw_snake("down")

			if(dirr == "down"):
				if(last_dir != "up"):
					snake.draw_snake("down")
					last_dir = "down"

				else:
					snake.draw_snake("up")

			if(dirr == "left"):

				if(last_dir != ""):
					

					if(last_dir != "right"):
						snake.draw_snake("left")
						last_dir = "left"

					else:	
						snake.draw_snake("right")

			if(dirr == "right"):
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
				
				if(reset == False):
					if mouse_c >= start_box_pos[0] and mouse_c <= start_box_pos[0]+148 and mouse_r >= start_box_pos[1] and mouse_r <= start_box_pos[1]+40:
						started = True
						counter = 0

				else:
					if mouse_c >= reset_box_pos[0] and mouse_c <= reset_box_pos[0]+120 and mouse_r >= reset_box_pos[1] and mouse_r <= reset_box_pos[1]+40:
						started = True
						counter = 0

					if mouse_c >= exit_box_pos[0] and mouse_c <= exit_box_pos[0]+100 and mouse_r >= exit_box_pos[1] and mouse_r <= exit_box_pos[1]+40:
						sys.exit()
						break


			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_DOWN:
					dirr = "down"
				if event.key == pygame.K_UP:
					dirr ="up"
				if event.key == pygame.K_LEFT:
					
					dirr = "left"

				if event.key == pygame.K_RIGHT:
					dirr = "right"
					

		
		clock.tick(5)		
if __name__ == '__main__':
	main()





