import sys

import pygame

class AlienInvasion:
    def __init__(self):
        """初始化游戏并创建游戏资源"""

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #监听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
         
                    sys.exit()
            #让最近绘制的屏幕可见
            pygame.display.flip() 
if __name__=='__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()                   