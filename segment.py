class Segment:
	def __init__(self, color, width, height, surface):
		self.color = color
		self.width = width
		self.height = height
		self.surface = surface

	def print_segment(self, w, point):
		pygame.draw.rect(self.surface, self.color, (point[0]*w, point[1]*w, w, w));



