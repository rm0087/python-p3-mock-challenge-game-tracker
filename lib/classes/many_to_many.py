class Game:
    all = []
    
    def __init__(self, title):
        self.title = title
        Game.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if  isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title
            
        else:
            print("Game title must be a string greater than 1 character!")

    def results(self):
        return [result for result in Result.all if self == result.game]
    
    def players(self):
        # unique_players = set()
        return list({result.player for result in self.results()})
    
    def average_score(self, player):
        total_score = 0
        games_played = 0
        for result in self.results():
            if result.player == player:
                total_score += result.score
                games_played +=1
        return total_score / games_played
            
class Player:
    all = []
    

    def __init__(self, username):
        self.username = username
        self.all_results = []
        Player.all.append(self)


    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16 :
            self._username = username
        else:
            print("Player username must be a string between 2 and 16 characters!")

    def results(self):
        return [result for result in Result.all if result.player == self]
    
    def games_played(self):
        return list({result.game for result in self.results()})
    
    def played_game(self, game):
        for gamed in self.games_played(): 
            if gamed == game:
                return True
            else:
                return False
            



class Result:
    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score:int):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, 'score'):
            self._score = score
        else:
            print("Score must be an integer between 1 and 5000!")

player1 = Player("Joe")
player2 = Player("Mike")
game1 = Game("Galaga")
game2 = Game("Tetris")
result1 = Result(player1, game1, 105)
result2 = Result(player1, game2, 200)
result3 = Result(player2, game1, 300)
result2 = Result(player1, game1, 200)
result4 = Result(player1, game1, 205)