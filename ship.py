import pygame

class Ship():
	"""飞船类
	
	Attributes:
		screen: 屏幕surface
		rect: 飞船rect
		screen_rect: 屏幕rect
		moving_right: 向右移动标记
		center: 飞船位置相关，小数值

	"""
	def __init__(self, ai_settings, screen):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# 将每艘新飞船放置屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# 皆标记为False
		self.moving_right = False
		self.moving_left = False
		
		self.center = float(self.rect.centerx)

	def blitme(self):
		"""在指定的位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""更新飞船位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		# 更新其rect位置（只保存后者整数部分
		self.rect.centerx = self.center 	




