import json

class Game_stats():

    def __init__(self, settings):
        self.settings = settings
        self.game_active = False
        self.scores_active = False
        self.settings_active = False
        self.high_score = 0
        self.import_high_score()

    def dynamic_stats(self):
        self.alien_point = 1
        self.score = 0
        self.lvl = 1
        self.ships_left = 3
        self.ship_speed_factor = self.settings.ship_speed_factor
        self.alien_speed_factor = self.settings.alien_speed_factor
        self.alien_drop_speed = self.settings.alien_drop_speed
        self.bullet_speed_factor = self.settings.bullet_speed_factor

    def import_high_score(self):
        try:
            with open('data/scores.json', 'r') as file:
                datas = json.load(file)
                print('loaded data: ', datas)
                self.high_score = datas['scores'][0]
        except IndexError:
            pass