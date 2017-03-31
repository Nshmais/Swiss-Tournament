#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
# created by: noah Shmais
# Date: 03/31/2017

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deletePlayers():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM scoreboard")     #delete players from scoreboard table
    d = DB.cursor()
    d.execute("DELETE FROM players")        # delete players from players table
    DB.commit()
    DB.close()


def deleteMatches():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    # c.execute("DELETE FROM players")
    c.execute('UPDATE scoreboard SET matches = 0, winner=0, loser=0, score=0')              # set the players matches to zero
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT COUNT(name) FROM players")
    data = c.fetchone()
    DB.commit()
    DB.close()
    return data[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB=connect()
    c=DB.cursor()
    c.execute('INSERT INTO players (name) VALUES (%s)', (name,))
    x=DB.cursor()
    x.execute('INSERT INTO scoreboard (player, winner, loser, score, matches) VALUES (%s, 0,0,0,0)', (name,))
    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB=connect()
    c=DB.cursor()
    c.execute("SELECT * FROM scoreboard order by score DESC")    #sort the scoreboard table by score

    scoreboard = c.fetchall()
    scoreboard= [list(row) for row in scoreboard]     # change tuple to list to make del work
    # print 'scoreboard before delete', scoreboard
    num=countPlayers()
    for x in xrange(num):
        del scoreboard[x][3]        #remove column 3 loser form table scoreboard
        del scoreboard[x][3]        #remove column 4 (3 after first del)  score form table scoreboard
    # print 'scoreboard after delete', scoreboard
    DB.commit()
    DB.close()
    return scoreboard


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    win_points = 3
    lost_points = 0

    DB=connect()
    c=DB.cursor()
    c.execute('UPDATE scoreboard SET score = score+%s, matches = matches+1, winner = winner+1  WHERE match_id= (%s)',(win_points, winner))
                # add three points to the winner and update matches and winner_count
    c=DB.cursor()
    c.execute('UPDATE scoreboard SET score = score+%s, matches = matches+1, loser = loser+1 WHERE match_id= (%s)',(lost_points, loser,))
                # add no points to the loser and update matches and loser_count
    DB.commit()
    DB.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    num = int(countPlayers())
    pairs = []
    if (num > 0):
        for i in range (num):
            if (i % 2 == 0):
                id1 = standings[i][0]
                name1 = standings[i][1]
                id2 = standings[i + 1][0]
                name2 = standings[i + 1][1]
                pair = (id1, name1, id2, name2)
                pairs.append(pair)
    return pairs

    """this function will divide the list into odd and even (pased on the score that we get win 3_points lost 0_point)
    and then pair ever odd with the ext even score"""


