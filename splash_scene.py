# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.

from scene import *
import ui
import time


class SplashScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        #creates timer, after 2 seconds, moves to next scene
        self.start_time = time.time()
        
        #adds MT background
        self.background = SpriteNode(position = self.size / 2,
                                     color = (0.61, 0.78, 0.87),
                                     parent = self,
                                     size = self.size)
        
        self.school_crest = SpriteNode('./assets/sprites/school_crest.jpg',
                                       parent = self, 
                                       position = self.size / 2)
                                       
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        self.school_crest = touch.location
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
