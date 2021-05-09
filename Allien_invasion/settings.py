class Settings():
    """
    a class to store all settings for alien invasion
    """

    def __init__(self):

        "Initialize the game's setting"
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_facotr = 1
        
