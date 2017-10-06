#created by Malcolm McCarthy
#created on september 2017
#created for ICS3U
#this program will display a splash screen for 2 seconds, then disappear

from scene import *
import ui

from splash_scene import *

class SplashScene(Scene):
    def setup(self):
    	 #this is used when user moves to this scene
		
       self.start_time = time.time()
       #after 2 seconds it changes scenes

       self.background = SpriteNode(position = self.size / 2,
                             color = (0.61, 0.78, 0.87) ,
                             parent = self,
                             size = self.size)

       self.school_crest = SpriteNode('./assets/sprites/school_crest.jpg')
