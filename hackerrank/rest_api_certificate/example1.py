



import requests

def getTotalGoals(team, year):
    count = 0
    r = requests.get('http:jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(team) + 'page=1').json()
    total1 = r['total_pages']
    per2 = r['per_page']

    for j in range(1, total1+1):
        r = requests.get('http:jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(team) + 'page=' + str(j)).json()
        try:
            for i in range(0, per2):
                team1 = r['data'][i]['teamgoals']
                count += int(team1)
        except:
            pass

    r2 = requests.get('http:jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(team) + 'page=1').json()
    total2 = r2['total_pages']
    pers2 = r2['per_page']

    for j in range(1, total2+1):
        r2 = requests.get('http:jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(team) + 'page=' + str(j)).json()
        try:
            for i in range(0, pers2):
                team2 = r2['data'][i]['teamgoals']
                count += int(team2)
        except:
            pass