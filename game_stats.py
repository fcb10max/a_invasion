class Game_stats():

    def __init__(self, settings):
        self.settings = settings
        self.game_active = False
        self.scores_active = False
        self.settings_active = False
        self.alien_point = 1
        self.high_score = 0

    def dynamic_stats(self):
        self.score = 0
        self.lvl = 1
        self.ships_left = 3
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 5
        self.alien_drop_speed = 10
        self.bullet_speed_factor = 3
