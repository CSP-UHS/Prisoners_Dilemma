'''
NOTES:

Prisoners_Dilemma.py allows hard-coding of different strategies
for the Iterative Prisoners Dilemma, the classic game of game-theory.
Each strategy plays 100 to 200 rounds against each other's strategy.
The results of all previous rounds within a 100-200 round stretch are known
to both players.

Pressing the green arrow button will allow you to run the tournament and
store the output in tournament.txt

Teams should each code their strategies in their assigned section of code.
Have students e-mail me their code and then just paste into my owned
cloned copy of PD on my computer. Gave up using the Merge method.
'''

import random
def play_round(player1, player2, history1, history2, score1, score2):
    '''
    Calls the get_action() function which will get the characters
    'c' or 'b' for collude or betray for each player.
    The history is provided in a string, e.g. 'ccb' indicates the player
    colluded in the first two rounds and betrayed in the most recent round.
    Returns a 4-tuple with updated histories and scores
    (history1, history2, score1, score2)
    '''

    RELEASE = 0 # (R) when both players collude
    TREAT = 100 # (T) when you betray your partner
    SEVERE_PUNISHMENT = -500 # (S) when your partner betrays you
    PUNISHMENT = -250 # (P) when both players betray each other
    # Keep T > R > P > S to be a Prisoner's Dilemma
    # Keep 2R > T + S to be an Iterative Prisoner's Dilemma

    #Get the two players' actions and remember them.
    action1 = get_action(player1, history1, history2, score1, score2)
    action2 = get_action(player2, history2, history1, score2, score1)
    if type(action1) != str:
        action1=' '
    if type(action2) != str:
        action2=' '
    #Append the actions to the previous histories, to return
    new_history1 = history1 + action1
    new_history2 = history2 + action2

    #Change scores based upon player actions
    if action1 not in ('c','b') or action2 not in ('c','b'):
    # Do nothing if someone's code returns an improper action
        new_score1 = score1
        new_score2 = score2

    else:
    #Both players' code provided proper actions
        if action1 == 'c':
            if action2 == 'c':
                # both players collude; get reward
                new_score1 = score1 + RELEASE
                new_score2 = score2 + RELEASE
            else:
                # players 1,2 collude, betray; get sucker, tempation
                new_score1 = score1 + SEVERE_PUNISHMENT
                new_score2 = score2 + TREAT
        else:
            if action2 == 'c':
                # players 1,2 betray, collude; get tempation, sucker
                new_score1 = score1 + TREAT
                new_score2 = score2 + SEVERE_PUNISHMENT
            else:
                # both players betray; get punishment
                new_score1 = score1 + PUNISHMENT
                new_score2 = score2 + PUNISHMENT

    #send back the updated histories and scores
    return (new_history1, new_history2, new_score1, new_score2)

def play_iterative_rounds(player1, player2):
    '''
    Plays a random number of rounds (between 100 and 200 rounds)
    of the iterative prisoners' dilemma between two strategies.
    identified in the parameters as integers.
    Returns 4-tuple, for example ('cc', 'bb', -200, 600)
    but with much longer strings
    '''
    number_of_rounds = random.randint(100,200)
    moves1 = ''
    moves2 = ''
    score1 = 0
    score2 = 0
    for round in range(number_of_rounds):
        moves1, moves2, score1, score2 = \
            play_round(player1, player2, moves1, moves2, score1, score2)
    return (moves1, moves2, score1, score2)

def get_action(player, history, opponent_history, score, opponent_score, getting_team_name=False):
    '''Gets the strategy for the player, given their own history and that of
    their opponent, as well as the current scores within this pairing.
    The parameters history and opponent history are strings with one letter
    per round that has been played so far: either an 'c' for collude or a 'b' for
    betray. The function should return one character, 'c' or 'b'.
    The history strings have the first round between these two players
    as the first character and the most recent round as the last character.'''

    #TEAMS 0-2 ARE EXAMPLE TEAMS


    #Team0: Loyal
    # This example player always colludes
    #######################################


    if player == 0:
        if getting_team_name:
            return 'Loyal'
        else:
            return 'c'



    #Team1: Backstabber
    # This example player always betrays
    #######################################


    elif player == 1:
        if getting_team_name:
            return 'Backstabber'
        else:
            return 'b'



    #Team2: Loyal Vengeful
    #This example player is silent at first and then only betrays if they were a sucker last round.
    #######################################


    elif player == 2:
        if getting_team_name:
            return 'Loyal Vengeful'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude


    # EACH STUDENT TEAM CAN CHANGE ONE OF THESE elif SEGMENTS OF CODE BELOW
    #######################################################################





    #Team3: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 3:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team4: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 4:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team5: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 5:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team6: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 6:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team7: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 7:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team8: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 8:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team9: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 9:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team10: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 10:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team11: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 11:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team12: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 12:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team13: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 13:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team14: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 14:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team15: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 15:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team16: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 16:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team17: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 17:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team18: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 18:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team19: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 19:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team20: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 20:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















#Team21: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 21:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















#Team22: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 22:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















#Team23: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 23:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















#Team24: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 24:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















#Team25: Enter Team Name Here
    #Team Members:
    #######################################


    elif player == 25:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude



def play_tournament(num_players):
    #create a list of zeros, one per player
    scores = []
    for i in range(num_players):
        scores += [0]


    ''' Get the team name from each team algorithm'''
    #create a list of the right length
    team_names = list(range(num_players))
    for player in range(num_players):
        team_names[player] = get_action(player,'','',0,0,getting_team_name=True)

    # each element will become a column for each player
    # range is just to get list of correct size
    result_table=list(range(num_players))
    moves_table=list(range(num_players))


    for player1 in range(num_players):
        # create the column for each player
        # range just to get list of correct size
        result_table[player1]=list(range(num_players))
        result_table[player1][player1]=0 # initialize unused diagonal to 0
        moves_table[player1]=list(range(num_players))
        # play a game between with every other player of lower number
        for player2 in range(player1):
            moves1, moves2, score1, score2 = \
                play_iterative_rounds(player1, player2)

            rounds = len(moves1)
            score1_per_round = score1/rounds
            score2_per_round = score2/rounds

            result_table[player1][player2]=score1_per_round
            result_table[player2][player1]=score2_per_round

            moves_table[player1][player2] = moves1
            moves_table[player2][player1] = moves2

            #accumulate the results for the two players
            scores[player1] += score1*1.0/len(moves1)#ends up same as column sum
            scores[player2] += score2*1.0/len(moves2)#ends up same as column sum

    '''report round-level results in a data file'''
    use_datafile=True
    if use_datafile:
        # use the same directory as the python script
        import os.path
        directory = os.path.dirname(os.path.abspath(__file__))

        #name the file tournament.txt
        filename = os.path.join(directory, 'tournament.txt')
        #create the file for the round-by-round results
        results = open(filename,'w')
        for player1 in range(num_players):
            for player2 in range(player1):
                # store the results in the file
                #title by team numbers
                results.write('team ' + str(player1) +
                              ' vs. ' + 'team ' + str(player2) +'\n')
                #title by player-on-player average score
                results.write(str(result_table[player1][player2]) +
                              ' vs. ' + str(result_table[player2][player1])+'\n')
                #title by team names
                results.write(team_names[player1] +
                             ' vs. ' + team_names[player2] + '\n')
                #show the moves, aligned vertically
                results.write(moves_table[player1][player2] +'\n')
                results.write(moves_table[player2][player1] +'\n')
                #blank line between each pair's results
                results.write('\n')

        #at the bottom repeat the output that was sent to the screen
        #print a title for the table
        results.write('\n\n\n\tEach column shows score earned per round against each other player.\n\n\n')
        #print header line
        results.write('\t') #skip 1st column
        for player1 in range(num_players):
            results.write('P'+str(player1)+'\t') # label each additional column
        results.write('\n')

        #print each player's scores
        for player2 in range(num_players):
            results.write('P'+str(player2)+'\t') #label the player's row
            for player1 in range(num_players):
                #print score against each other player
                results.write(str(result_table[player1][player2])+'\t')
            results.write('\n')
        results.write('Total:\t')
        for player1 in range(num_players):
            results.write(str(int(scores[player1]))+'\t')
        results.write('\n\n\n Average per round, with team strategy names:\n\n')

        #print team ids, total scores, and names
        for player in range(num_players):
            results.write('player ' + str(player) + ': ' + \
                    str(int(scores[player])/num_players) + ' points: '+\
                    team_names[player]+'\n')


        #append the file showing algorithms
        results.write('\n\n' + '-'*79 + '\n' + \
                    'Here is the code that produced this data:\n\n')
        this_code_file = open(__file__, 'r')
        for line in this_code_file:
            results.write(line)

    '''report the results on screen'''
    #print a title for the table
    print('\n\n\tEach column shows score earned per round against each other player.\n\n')

    #print header line
    print('\t', end='') #skip 1st column
    for player1 in range(num_players):
        print('P',player1, end='\t') # label each additional column
    print()

    #print each player's scores
    for player2 in range(num_players):
        print('P',player2, end='\t') #label the player's row
        for player1 in range(num_players):
            #print score against each other player
            print("{:.2f}".format(result_table[player1][player2]), end='\t')
        print()
    #print row of total scores
    print('Total:\t',end='')
    for player1 in range(num_players):
        print(str("{:.2f}".format(scores[player1])),end='\t')

    print('\n\n\n Average per round, with team strategy names:\n\n')
    #print team ids, total scores, and names
    for player in range(num_players):
        print('player ' + str(player) , ': ' ,
               str("{:.2f}".format((scores[player])/num_players)) , ' points: ',
               team_names[player])
def main():
    howmanyteams=int(input("How many teams do you want to run in this tournament? Max:25  "))
    howmanyteams+=1
    if howmanyteams>26:
        play_tournament(26)
    else:
        play_tournament(howmanyteams)

if __name__=="__main__":
    main()
