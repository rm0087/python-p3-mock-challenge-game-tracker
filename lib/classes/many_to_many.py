class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title,str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title
        else:
            raise Exception("Title must be a string longer than 0 characters, cannot change title after instantiation")

    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
           raise Exception("Player username must be a string between 2 and 16 characters inclusive")

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    def __init__(self, player, game, score):
        self.player = Player(player)
        self.game = Game(game)
        self.score = score

    @property
    def score(self):
        return self._result

    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self ,"score"):
            self._score = score
        else:
            raise Exception("Score must be an integer between 1 and 5000")

    

    