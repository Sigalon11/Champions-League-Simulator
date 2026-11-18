import random

class Team():
    def __init__(self, name , pot , country, players=0, opponents=None , pots_count=None , points=0 , games=0 , wins=0 , losses=0 , draw=0,  goals=0 , goals_up=0):
        self.name = name
        self.pot = pot
        self.country = country
        self.players = players
        self.opponents = []
        self.pots_count = {1:0 , 2:0 , 3:0 , 4:0}
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
Arsenal_players = players('David Raya' , 'William Saliba' , 'Declan Rice' ,'Bukayo Saka' , 'Martin Ødegaard')
PSG_players = players('Matvey Safonov' , 'Achraf Hakimi' , 'Vitinha' , 'Ousmane Dembélé' , 'Marquinhos')
RealMadrid_players = players('Thibaut Courtois' , 'Éder Militão' , 'Jude Bellingham' , 'Kylian Mbappé' , 'Federico Valverde')
Como_players = players( 'Jean Butez' , 'Jacobo Ramón' , 'Nico Paz' , 'Tasos Douvikas' ,  'Lucas Da Cunha')
Barcelona_players = players( 'Joan García' , 'Pau Cubarsí' , 'Pedri' , 'Lamine Yamal' , 'Raphinha')
AstonVila_players = players('Zion Suzuki' , 'Victor Lindelöf' , 'Boubacar Kamara' , 'Nicolas Jackson' , 'John McGinn')
ManCity_players = players('Gianluigi Donnarumma' , 'Joško Gvardiol' , 'Phil Foden' , 'Erling Haaland' , 'Rúben Dias')
Liverpool_players = players( 'Alisson Becker' , 'Ibrahima Konaté' , 'Florian Wirtz' , 'Alexander Isak' , 'Virgil van Dijk')
ClubBrugge_players = players('Yann Sommer' , 'Joel Ordóñez' , 'Hugo Vetlesen' , 'Nicolò Tresoldi' , 'Hans Vanaken')
SportingCP_players = players('Rui Silva' , 'Eduardo Quaresma' , 'Issa Doumbia' , 'Luis Suárez' , 'Gonçalo Inácio')
RealBetis_players = players('Álvaro Vallés' , 'Natan' , 'Pablo Fornals' , 'Antony' , 'Isco')
BorussiaDortmund_players = players('Gregor Kobel' , 'Nico Schlotterbeck' , 'Felix Nmecha' , 'Serhou Guirassy' , 'Emre Can')
BayernMunich_players = players('Manuel Neuer' , 'Dayot Upamecano' , 'Jamal Musiala' , 'Harry Kane' , 'Joshua Kimmich')
VfBStuttgart_players = players('Dennis Seimen' , 'Finn Jeltsch' , 'Angelo Stiller' , 'Ermedin Demirovic' , 'Deniz Undav' )
InterMilan_players = players('Josep Martínez' , 'Alessandro Bastoni' , 'Nicolò Barella' , 'Marcus Thuram' ,'Lautaro Martínez')
LASK_players = players('Lukas Jungwirth' , 'Andrés Andrade' , 'Robert Ljubičić' , 'Samuel Adeniran' , 'Sascha Horvath')
ManUnited_players = players('Senne Lammens' , 'Lisandro Martínez' , 'Kobbie Mainoo' , 'Bryan Mbeumo' , 'Bruno Fernandes')
Galatasaray_players = players('Uğurcan Çakır' , 'Davinson Sánchez' , 'Gabriel Sara' , 'Victor Osimhen' , 'Abdülkerim Bardakcı')
Fenerbahce_players = players('Ederson' , 'Nathan Aké' , "N'Golo Kanté" , 'Mason Greenwood' , 'Mert Hakan Yandaş')
ASRoma_players = players('Mile Svilar' , 'Evan Ndicka' , 'Manu Koné' , 'Donyell Malen' , 'Bryan Cristante')
Shakhtar_players = players('Dmytro Riznyk' , 'Valeriy Bondar' , 'Marlon Gomes' , 'Kauã Elias' ,'Mykola Matviyenko')
VikingFK_players = players('Arild Østbø' , 'Henrik Falchener' , 'Joe Bell' , 'Erik Botheim' , 'Zlatko Tripić')
AtleticoMadrid_players = players('Jan Oblak' , 'Marc Pubil' , 'Pablo Barrios' , 'Julián Álvarez' , 'koke')
PSV_players = players('Matěj Kovář' , 'Lutsharel Geertruida' , 'Paul Wanner' , 'Ricardo Pepi' , 'Ivan Perišić')
Bodo_players = players('Nikita Haikin' , 'Fredrik Bjørkan' , 'Sondre Brunstad Fet' , 'Jens Petter Hauge' , 'Patrick Berg')
Porto_players = players('Diogo Costa' , 'Jakub Kiwior' , 'Alan Varela' , 'Samu Aghehowa' , 'Jan Bednarek') #Diogo Costa is porto's captain but because he's the goalkeeper Jan bedanrek replaced him as he's a sub captain.
Napoli_players = players('Vanja Milinković-Savić' , 'Alessandro Buongiorno' , 'Scott McTominay' , 'Rasmus Højlund' , 'Giovanni Di Lorenzo')
Villarreal_players = players('Luiz Júnior' , 'Renato Veiga' , 'Pape Gueye' , 'Georges Mikautadze' , 'Gerard Moreno')
AEKAthens_players = players('Thomas Strakosha' , 'Harold Moukoudi' , 'Lovro Majer' , 'Luka Jović' , 'Petros Mantalos')
RBLeipzig_players = players('Maarten Vandevoordt' , 'Castello Lukeba' , 'Christoph Baumgartner' , 'Antonio Nusa' , 'David Raum')
SabahFK_Players = players('Stas Pokatilov' , 'Tymoteusz Puchacz' , 'Umarali Rakhmonaliev' ,'Veljko Simic' , 'Rahman Dashdamirov') #Same as Porto, goalkeeper is the main captain so the role moved to Rahman Dashdamirov, the sub captain.
Feyenoord_players = players('Tjark Ernst' , 'Givairo Read' , 'Oussama Targhalline' , 'Anis Hadj Moussa' , 'Luciano Valente')
RCLens_players = players('Robin Risser' , 'Samson Baidoo' , 'Yacine Titraoui' , 'Odsonne Édouard' , 'Florian Thauvin')
SlaviaPrague_players = players('Jakub Markovic' , 'Stepan Chaloupek' , 'David Moses' , 'Danijel Sturm' , 'Lukas Provod')
Lille_players = players('Berke Özer' , 'Alexsandro' , 'Nabil Bentaleb' , 'Olivier Giroud' , 'Benjamin André')
SlovanBratislava_players = players('Dominik Takáč' , 'Kenan Bajric' , 'Rahim Ibrahim' , 'Suleiman Camara' , 'Andraž Šporar')

Arsenal = Team("Arsenal", 1, "England", Arsenal_players)
PSG = Team("Paris Saint Germain", 1, "France", PSG_players)
RealMadrid = Team("Real Madrid ", 1, "Spain", RealMadrid_players)
Como = Team("Como", 4, "Italy", Como_players)
Barcelona = Team("Barcelona", 1, "Spain", Barcelona_players)
AstonVila = Team("Aston Vila", 2, "England", AstonVila_players)
ManCity = Team("Manchester City", 1, "England", ManCity_players)
Liverpool = Team("Liverpool", 1, "England", Liverpool_players)
ClubBrugge = Team("Club Brugge", 2, "Belgium", ClubBrugge_players)
SportingCP = Team("Sporting CP", 2, "Portugal", SportingCP_players)
RealBetis = Team("Real Betis", 2, "Spain", RealBetis_players)
BorussiaDortmund = Team("Borussia Dortmund", 2, "Germany", BorussiaDortmund_players)
BayernMunich = Team("Bayern Munich", 1, "Germany", BayernMunich_players)
VfBStuttgart = Team("VfB Stuttgart", 4, "Germany", VfBStuttgart_players)
InterMilan = Team("Inter Milan", 1, "Italy", InterMilan_players)
LASK = Team("LASK", 4, "Austria", LASK_players)
MAnUnited = Team("Manchester United", 2, "England", ManUnited_players)
Galatasaray = Team("Galatasaray", 3, "Turkey", Galatasaray_players)
Fenerbahce = Team("Fenerbahçe", 3, "Turkey", Fenerbahce_players)
ASRoma = Team("AS Roma", 2, "Italy", ASRoma_players)
Shakhtar = Team("Shakhtar Donetsk", 3, "Ukraine", Shakhtar_players)
VikingFK = Team("Viking FK", 4, "Norway", VikingFK_players)
AtleticoMadrid = Team("Atlético de Madrid", 1, "Spain", AtleticoMadrid_players)
PSV = Team("PSV Eindhoven", 2, "Netherlands", PSV_players)
Bodo = Team("Bodø/Glimt", 3, "Norway", Bodo_players)
Porto = Team("Porto", 2, "Portugal", Porto_players)
napoli = Team("SSC Napoli", 3, "Italy", Napoli_players)
Villarreal = Team("Villarreal", 3, "Spain", Villarreal_players)
AEKAthens = Team("AEK Athens", 4, "Greece", AEKAthens_players)
RBLeipzig = Team("RB Leipzig", 3, "Germany", RBLeipzig_players)
SabahFK = Team("Sabah FK" , 4 , "Azerbaijan" , SabahFK_Players)
Feyenoord = Team("Feyenoord Rotterdam" , 3 , "Netherlands", Feyenoord_players)
RCLens = Team("RC Lens" , 4 , "France", RCLens_players)
SlaviaPrague = Team("SK Slavia Prague" , 4 , "Czechia" , SlaviaPrague_players)
Lille = Team("LOSC Lille" , 3, "France", Lille_players)
SlovanBratislava = Team("Slovan Bratislava" , 4 , "Slovakia" , SlovanBratislava_players)

all_teams = [
    Arsenal, PSG, RealMadrid, Como, Barcelona, AstonVila, ManCity, Liverpool,
    ClubBrugge, SportingCP, RealBetis, BorussiaDortmund, BayernMunich, VfBStuttgart,
    InterMilan, LASK, MAnUnited, Galatasaray, Fenerbahce, ASRoma, Shakhtar,
    VikingFK, AtleticoMadrid, PSV, Bodo, Porto, napoli, Villarreal, AEKAthens,
    RBLeipzig, SabahFK, Feyenoord, RCLens, SlaviaPrague, Lille, SlovanBratislava
]

def draw_teams():
    NOG = 0
    chosen = random.choice(all_teams)
    alr_rival = []
    while True:
        rival = random.choice(all_teams)
        if rival in alr_rival:
            continue
        elif rival == chosen:
            continue
        elif chosen.country == rival.country:
            continue
        else:
            if chosen.pots_count[rival.pot] == 2:
                continue
            chosen.pots_count[rival.pot] += 1
            print(f'{chosen.name} is playing {rival.name}')
            alr_rival.append(rival)
            NOG +=1
            if NOG == 8:
                chosen.opponents = alr_rival
                break
draw_teams()