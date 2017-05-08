import cmd
import datetime
import random


def play(zapas):
    """vyberie vitaza zapasu nahodne s pravdepodobnostou priamo umernou jeho skillu
    a oznaci ze tieto dva timy uz proti sebe hrali"""
    ratio = zapas[0].skill / (zapas[1].skill + 0.0000001)
    vitaz = random.choices([0, 1], [ratio, 1], k=1)[0]
    zapas[vitaz].points += 1
    for i in range(2):
        zapas[i].played.add(zapas[(i + 1) % 2])
        zapas[i].matches += 1
    print('\nzapas medzi', zapas[0].name, 'a', zapas[1].name, 'vyhral', zapas[vitaz].name)


class State:
    """trieda reprezentujuca stav turnaja"""

    def __init__(self, teams):
        self.teams = teams
        self.date = datetime.date(2015, 1, 1)
        self.games = 0


class Team:
    """trieda reprezentujuca tim"""

    def __init__(self, name, skill):
        self.name = name
        self.points = 0
        self.matches = 0
        self.played = set()
        self.skill = float(skill)


class ParseCommands(cmd.Cmd):
    """komunikacia s uzivatelom: caka na prikazy a vykonava ich"""
    intro = 'napis help'
    prompt = ''

    def do_stav(self, args):
        """vypise stav turnaja v tvare nazov timu, pocet zapasov a body"""
        print(state.date)
        length = max(len('nazov timu '), max(len(team.name) for team in state.teams))
        length2 = len('pocet zapasov ')
        print('nazov timu '.ljust(length), 'pocet zapasov ', 'body', sep='|')
        for team in sorted(state.teams, key=lambda team: (team.points, team.matches), reverse=True):
            print(team.name.ljust(length), str(team.matches).ljust(length2), team.points)

    def do_next(self, args):
        """odsimuluje jeden den turnaja: vyberie na zapas nahodne dva timy
        ktore proti sebe nehrali"""
        while True:
            zapas = random.sample(state.teams, 2)
            if zapas[0] not in zapas[1].played: break
        play(zapas)
        self.do_stav(args)
        state.date += datetime.timedelta(days=1)
        state.games += 1
        if state.games == len(state.teams) * (len(state.teams) - 1) / 2:
            print('\nodohrali sa vseky zapasy')
            return True

    def do_cely_turnaj(self, args):
        """odsimuluje cely turnaj"""
        if not self.do_next(args): self.do_cely_turnaj(args)
        return True


n = int(input('Napis pocet timov: '))
teams = set()
for i in range(n):
    nazov, skill = input('nazov timu medzera jeho skill: ').split()
    teams.add(Team(nazov, skill))

state = State(teams)
ParseCommands().cmdloop()
