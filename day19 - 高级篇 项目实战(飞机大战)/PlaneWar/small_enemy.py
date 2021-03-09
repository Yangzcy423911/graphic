"""小型敌机"""
import random
import pygame
from pygame.sprite import Sprite
import constants


class SmallEnemy(Sprite):
    """小型敌机类"""

    def __init__(self, window):
        """初始化小型敌机"""

        # 调用父类Sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象

        self.window = window

        # 加载小型敌机图片
        self.image = self.small_image = pygame.image.load("images/small_enemy.png")

        # 加载小型敌机爆炸的第1张图片
        self.explode_image1 = pygame.image.load("images/small_enemy_explode1.png")
        # 加载小型敌机爆炸的第2张图片
        self.explode_image2 = pygame.image.load("images/small_enemy_explode2.png")
        # 加载小型敌机爆炸的第3张图片
        self.explode_image3 = pygame.image.load("images/small_enemy_explode3.png")
        # 加载小型敌机爆炸的第4张图片
        self.explode_image4 = pygame.image.load("images/small_enemy_explode4.png")
        # 获得小型敌机的矩形
        self.rect = self.image.get_rect()
        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()
        # 设置小型敌机的矩形的初始位置为: 窗口的矩形的顶部一个随机的水平位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width - self.rect.width)

        # 小型敌机每次移动时的偏移量
        self.offset = 6

        # 标记小型敌机没有在切换爆炸图片
        self.is_switching_explode_image = False
        # 切换小型敌机爆炸图片的计数器
        self.switch__explode_counter = 0

    def update(self):
        """更新小型敌机的位置"""

        # 增大小型敌机的属性top以向下移动
        self.rect.top += self.offset

    def play_explode_sound(self):
        """播放小型敌机爆炸的声音"""

        # 加载小型敌机爆炸的声音文件
        explode_sound = pygame.mixer.Sound("sounds/small_enemy_explode.wav")

        # 设置爆炸声音的音量
        explode_sound.set_volume(constants.EXPLODE_SOUND_VOLUME)

        # 播放爆炸的声音

        explode_sound.play()

    def switch_explode_image(self):
        """切换小型敌机爆炸的图片"""
        # 切换小型敌机爆炸图片的计数器加1
        self.switch__explode_counter += 1
        # 如果计数器加到指定的值，才切换一次小型敌机爆炸的图片
        if self.switch__explode_counter == \
                constants.SMALL_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY:

            # 切换到爆炸的第1张图片
            # 如果是第1张图片
            # 如果是小型敌机的图片
            if self.image == self.small_image:
                # 切换到爆炸的第1张图片
                self.image = self.explode_image1
            # 如果爆炸的第1张图片
            elif self.image == self.explode_image1:
                # 切换到爆炸的第2张图片
                self.image = self.explode_image2
            # 如果爆炸的第2张图片
            elif self.image == self.explode_image2:
                # 切换到爆炸的第3张图片
                self.image = self.explode_image3
            # 如果爆炸的第3张图片
            elif self.image == self.explode_image3:
                # 切换到爆炸的第3张图片
                self.image = self.explode_image4
            # 如果爆炸的第4张图片
            elif self.image == self.explode_image4:
                # 将小型敌机从所有分组中删除
                self.kill()
            # 计数器重置为0
            self.switch__explode_counter = 0
