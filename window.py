import pygame
import logging

from assets import Assets

class Window():
    def __init__(self, game):
        settings = self.getSettings()
        self.width = settings["window_width"]
        self.height = settings["window_height"]
        self.fps = settings["fps"]
        self.window = pygame.display.set_mode((self.width, self.height))
        self.game = game
        pygame.display.set_caption("Ultimate rally")

    def getSettings(self):
        usrSettings = {
            "window_width": 1000,
            "window_height": 1000,
            "fps": 60,
        }
        try:
            import settings
        except ImportError:
            print("Error: couldn't find settings.py file")
            logging.warning("Error: couldn't find settings.py file")
            return usrSettings
        try:
            from settings import window_width
            usrSettings["window_width"] = int(window_width)
        except ValueError:
            print("Error: Variable 'window_width' must be an integer value")
            print("       Using default value")
            logging.warning("Error: Variable 'window_width' must be an integer value")
            logging.warning("       Using default value")
        except ImportError:
            print("Error: Could not find 'window_width' variable in settings.py")
            print("       Using default value")
            logging.warning("Error: Could not find 'window_width' variable in settings.py")
            logging.warning("       Using default value")
        try:
            from settings import window_height
            usrSettings["window_height"] = int(window_height)
        except ValueError:
            print("Error: Variable 'window_height' must be an integer value")
            print("       Using default value")
            logging.warning("Error: Variable 'window_height' must be an integer value")
            logging.warning("       Using default value")
        except ImportError:
            print("Error: Could not find 'window_height' variable in settings.py")
            print("       Using default value")
            logging.warning("Error: Could not find 'window_height' variable in settings.py")
            logging.warning("       Using default value")
        try:
            from settings import fps
            usrSettings["fps"] = int(fps)
        except ValueError:
            print("Error: Variable 'fps' must be an integer value")
            print("       Using default value")
            loggging.warning("Error: Variable 'fps' must be an integer value")
            loggging.warning("       Using default value")
        except ImportError:
            print("Error: Could not find variable 'fps' in settings.py")
            print("       Using default value")
            loggging.warning("Error: Could not find variable 'fps' in settings.py")
            loggging.warning("       Using default value")
        return usrSettings

    def drawFrame(self):
        for item in self.game.toDraw:
            self.window.blit(item.image, (item.x, item.y))
        pygame.display.update()

    def menuScreen(self):
        self.window.blit(self.game.assets.titleImage, (0,0))
        startText = self.game.assets.titleFont.render(
            "Press space to play", 1, (7, 44, 166)
        )
        xposition = self.width/2 - startText.get_width()/2
        yposition = self.height/2 - startText.get_height()/2 + 35
        self.window.blit(startText, (xposition, yposition))
        pygame.display.update()
