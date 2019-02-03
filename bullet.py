import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""子弹类

	Attributes:
		screen: 屏幕surface
		rect: 子弹rect
		y: 子弹位置相关，小数值 
	"""
	def __init__(self, ai_settings, screen, ship):
		"""在飞船所在处创建一个子弹对象"""
		super().__init__()		# 调用父类构造方法
		self.screen = screen
		# 创建子弹矩形，并设置位置
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		# 存储用小数表示的子弹位置
		self.y = float(self.rect.y)
		# 设置颜色、速度
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""更新子弹位置"""
		self.y -= self.speed_factor
		# 更新其rect位置（保留后者整数部分
		self.rect.y = self.y

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect)

