from time import sleep
import numpy as np
from random import randint
import pygame
import sys
import random
import time
import copy
from segment import Segment

def draw_grid(w, r, surface):
	rows = 40
	size = w // r
	x = 0
	y = 0
	for i in range(r):
		x = x + size
		y = y + size

		pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
		pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redraw_window():
	screen.fill((40, 0, 0))
	draw_grid(800, 20, screen)


def main():
	segments = []
	screen = pygame.display.set_mode((800, 800))
	head = Segment((34, 67, 7), 40, 40, screen)
	
	'''
	for x in range(5):

			arr.append()
	'''
	while(True):

		head.print_segment(40, (10, 10))

		redraw_window();

		

		pygame.display.update()


		clock.tick(6)		
if __name__ == '__main__':
	main()