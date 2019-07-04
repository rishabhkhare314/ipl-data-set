import csv

teams = [] #teams
total_team_played = [] #total teams
winner_team = []       #winning teams
data = {}              #data of total teams played match,won matches ,lost matches
reader = csv.DictReader(open("matches.csv"))
for raw in reader:
   # print(raw)
    teams.append(raw['team1'])
    total_team_played.append(raw['team1'])
    total_team_played.append(raw['team2'])
    winner_team.append(raw['winner'])

teams=set(teams)
for team in teams:
    data[team] = {"Total_played": total_team_played.count(team), "won": winner_team.count(team), "lost": total_team_played.count(team)-winner_team.count(team)}
print(data)