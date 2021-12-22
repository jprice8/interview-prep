

def tournamentWinner(teams, results):
    hashtable = {}

    for i in range(len(teams)):
        currTeams = teams[i]
        currResult = results[i]

        handleWinner(currResult, currTeams, hashtable)

    standings = sorted(hashtable.items(), key=lambda x: x[1], reverse=True)

    return standings[0][0]

def handleWinner(currResult, currTeams, hashtable):
    if currResult == 1:
        winner = currTeams[0]
    else:
        winner = currTeams[1]

    if winner in hashtable:
        hashtable[winner] += 3
    else:
        hashtable[winner] = 3


print(tournamentWinner([['team1', 'team2'], ['team2', 'team3'], ['team3', 'team1']], [0, 0, 1]))

HOMETEAM_WON = 1

# def tourneyWinner(competitions, results):
    # bestTeam = ""
    # currentBestTeam = {bestTeam, 0}

    # for i in range(len(competitions)):
    #     homeTeam, awayTeam = competitions[i]
    #     result = results[i]
    #     if result == HOMETEAM_WON:
            
