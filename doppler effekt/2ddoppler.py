import pygame
import math
from pysinewave import *

sinewave = SineWave(pitch = -10, pitch_per_second = 99)

#sinewave.set_frequency(0)

pygame.init()

wScreen = 1800
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

delta_t = 0.01
t = 0
i = 0


class sound_source():
	def __init__(self, x, y, frequency, v_phase):
		self.x = x
		self.y = y
		self.frequency = frequency
		self.v_phase = v_phase

		self.Vx = 0
		self.Vy = 0
		
		self.waves = []

	def draw_self(self):
		pygame.draw.circle(win, (0, 0, 0), [round(self.x), round(self.y)], 5, 5)

	def add_new_wave(self, t_zero):                                #radius pass IO OI
		self.waves.append([t_zero, self.x, self.y, self.Vx, self.Vy, 0, 0, 1])
		#print(t)

	def draw_waves(self, t):
		for x, wave in enumerate(self.waves):
			radius = self.v_phase * (t - wave[0])
			self.waves[x][5] = radius
			#print(len(self.waves))
			pygame.draw.circle(win, (255, 0, 0), [round(wave[1]), round(wave[2])], radius, 1)
			if radius > 10000:
				self.waves.remove(x)


class sound_reciever():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
		self.width = 5
		self.color = (0, 0, 0)

	def draw_self(self):
		pygame.draw.circle(win, self.color, [round(self.x), round(self.y)], self.width, self.width)

	def is_circle_passing(self, cc_x, cc_y, r):
		#print(cc_x, cc_y, r)
		delta_x = self.x - cc_x
		delta_y = self.y - cc_y
		dist = math.sqrt((delta_x**2) + (delta_y**2))
		if ((dist - self.width) < r) and (r < (dist + self.width)):
			self.color = (0, 255, 0)

	
	def set_color(self, waves):
		self.color = (0, 0, 0)
		for wave in waves:
			self.is_circle_passing(wave[1], wave[2], wave[5])


def check_wave_has_passed(sender, reciver):

	waves = sender.waves
	rec_xy = reciver.x, reciver.y

	for i, wave in enumerate(waves):
		radius = wave[5]

		changed_last_time = wave[6]
		quotient_below_one = wave[7]

		delta_x, delta_y = rec_xy[0] - wave[1], rec_xy[1] - wave[2]
		dist = math.sqrt((delta_x ** 2) + (delta_y ** 2))
		if i == -10:
			try:
				print(delta_x, delta_y, dist)
				print(radius/dist)
			except ZeroDivisionError:
				pass

		qotient = (radius+1)/dist
		if qotient < 1:
			sender.waves[i][7] = 1
		else:
			sender.waves[i][7] = 0
		if quotient_below_one != sender.waves[i][7]:
			return True


source = sound_source(0, 200, 1, 20)
reciever = sound_reciever(1000, 300)

def redrawWindow(t):
	win.fill((255, 255, 255))
	source.draw_waves(t)
	source.draw_self()
	reciever.draw_self()
	pygame.display.update()


run = True

passed = []

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			print(passed)
	
	t += delta_t
	reciever.set_color(source.waves)
	if t > len(source.waves)*(1/source.frequency):
		source.add_new_wave(t)

	#source.y += math.cos(t/20)/30
	source.x += 0.1# * (t/10)
	reciever.x -= 0.04
	i += 1
	if check_wave_has_passed(source, reciever):
		sinewave.play()
		passed.append(t)
	if len(passed) > 1:
		#print(passed[-1] - passed[-2])
		pch = 1/(passed[-1] - passed[-2])
		freq = pch*source.frequency*200
		print(freq)
		sinewave.set_frequency(frequency=freq)
		sinewave.play()
	redrawWindow(t)






