import arcade
from random import *
class Window(arcade.Window):
    def __init__(self):
        super().__init__(1000,800,"Star Wars")
        self.BG = arcade.load_texture("space_background.png")
        self.player_1 = Player()
        self.set_mouse_visible(False)
        self.laser_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.score = 0
        self.health = 5
        self.stop = False
        self.laser_sound = arcade.load_sound("laser.wav")
        self.star_sound = arcade.load_sound("star_wars.wav")
        arcade.play_sound(self.star_sound)
        for i in range(50):
            enemy_1_1 = Enemy()
            enemy_1_1.center_x = randint(50,950)
            enemy_1_1.center_y = i * 200 + 800
            enemy_1_1.change_y = -3
            self.enemy_list.append(enemy_1_1)
            
    def update(self,delta_time):
        if self.health == 0:
            self.stop = True
        if self.stop == True:
            quit()
        if self.stop == False:
            self.laser_list.update()
            self.enemy_list.update()
            self.enemy_list.update_animation()
##            for laser in self.laser_list:
##                collision_list = arcade.check_for_collision_with_list(laser, self.enemy_list)
##                for enemy in collision_list:
##                    enemy.kill()
##                    laser.kill()
##                    self.score += 1
                
            
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(500,400,1000,800,self.BG)
        self.player_1.draw()
        self.laser_list.draw()
        self.enemy_list.draw()
        arcade.draw_text(f"Счет: {self.score}",50,750,arcade.color.WHITE,20)
        arcade.draw_text(f"Жизни: {self.health}",850,750,arcade.color.WHITE,20)
        if self.health == 0:
            arcade.draw_text("Проигрыш",500,400,arcade.color.WHITE,20)
    def on_mouse_motion(self, x,y, dx,dy):
        self.player_1.center_x = x
        
    def on_mouse_press(self,x,y,button,modifiers):
        laser_1 = Laser()
        laser_1.center_x = x
        laser_1.center_y = self.player_1.top
        self.laser_list.append(laser_1)
        arcade.play_sound(self.laser_sound)
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("x-wing.png", 1)
        self.center_x = 500
        self.center_y = 100
        


class Laser(arcade.Sprite):
    def __init__(self):
        super().__init__("laser.png", 1)
        
        self.change_y = 6
        
    def update(self):
        self.center_y += self.change_y
        if self.center_y >= 800:
            self.kill()
        collision_list = arcade.check_for_collision_with_list(self, window.enemy_list)
        for enemy in collision_list:
            enemy.kill()
            self.kill()
            window.score += 1
        

class Enemy(arcade.AnimatedTimeBasedSprite):
    def __init__(self):
        super().__init__()
        cadr = arcade.AnimationKeyframe(0,200, arcade.load_texture("tie fighter.png"))
        self.frames.append(cadr)
        cadr_2 = arcade.AnimationKeyframe(1,200, arcade.load_texture("tie fighter2.png"))
        self.frames.append(cadr_2)
        self.scale = 1.3
    def update(self):
        self.center_y += self.change_y
        if self.center_y <= 0:
            self.kill()
            window.health -= 1
        









window = Window()
arcade.run()



















