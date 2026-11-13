import random

class Team():
    def __init__(self, name , players=0 , points=0 , games=0 , wins=0 , losses=0 , draw=0,  goals=0 , goals_up=0 ):
        self.name = name
        self.players = players
        self.points = points
        self.games = games
        self.wins = wins
        self.losses = losses
        self.draw = draw
        self.goals = goals
        self.goals_up = goals_up


    def goal_difference(self):
        return self.goals - self.goals_up

class players():
    def __init__(self, gk , defe, mid , att , cap):
        self.gk = gk
        self.defe = defe
        self.mid = mid
        self.att = att
        self.cap = cap


#players to their teams
Arsenal_players = players('David Raya' , 'William Saliba' , 'Declan Rice' ,'Bukayo Saka' , 'Martin Odegaard')
PSG_players = players('Matvey Safonov' , 'Achraf Hakimi' , 'Vitinha' , 'Ousmane Dembélé' , 'Marquinhos')
RealMadrid_players = players('Thibaut Courtois' , 'Éder Militão' , 'Jude Bellingham' , 'Kylian Mbappé' , 'Federico Valverde')
Como_players = players( 'Jean Butez' , 'Jacobo Ramón' , 'Nico Paz' , 'Tasos Douvikas' ,  'Lucas Da Cunha')
Barcelona_players = players( 'Joan García' , 'Pau Cubarsí' , 'Pedri' , 'Lamine Yamal' , 'Raphinha')
AstonVila_players = players('Zion Suzuki' , 'Victor Lindelöf' , 'Boubacar Kamara' , 'Nicolas Jackson' , 'John McGinn')
ManCity_players = players('Gianluigi Donnarumma' , 'Joško Gvardiol' , 'Phil Foden' , 'Erling Haaland' , 'Rúben Dias')
Liverpool_players = players( 'Alisson Becker' , 'Ibrahima Konaté' , 'Florian Wirtz' , 'Alexander Isak' , 'Virgil van Dijk' )
ClubBrugge_players = players('Yann Sommer' , 'Joel Ordóñez' , 'Hugo Vetlesen' , 'Nicolò Tresoldi' , '' , 'Hans Vanaken')
SportingCP_players = players('Rui Silva' , 'Eduardo Quaresma' , 'Issa Doumbia' , 'Luis Suárez' , 'Gonçalo Inácio')
RealBetis_players = players('Álvaro Vallés' , 'Natan' , 'Pablo Fornals' , 'Antony' , 'Isco')
BorussiaDortmund_players = players('Gregor Kobel' , 'Nico Schlotterbeck' , 'Felix Nmecha' , 'Serhou Guirassy' , 'Emre Can')
BayernMunich-players = players('Manuel Neuer' , 'Dayot Upamecano' , )



Arsenal = Team("Arsenal" ,Arsenal_players)
PSG = Team("Paris Saint Germain" ,PSG_players)
RealMadrid = Team("Real Madrid " ,RealMadrid_players)
Como = Team("Como" ,Como_players)
Barcelona = Team("Barcelona" ,Barcelona_players)
AstonVila = Team("Aston Vila" ,AstonVila_players)
ManCity = Team("Manchester City" ,ManCity_players)
Liverpool = Team("Liverpool" ,Liverpool_players)
ClubBrugge = Team("Club Brugge" ,ClubBrugge_players)
SportingCP = Team("Sporting CP" ,SportingCP_players)
RealBetis = Team("Real Betis" ,RealBetis_players)
BorussiaDortmund = Team("Borussia Dortmund" ,BorussiaDortmund_players)
