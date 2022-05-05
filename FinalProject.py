"""

FINAL PROJECT

Authors: Suryansh Agarwal. Utsav Sapkota, Ichhit Joshi

Purpose: Simulating tic-tac-toe in a gambling scenario and competing with other players to find out who can bet and win the prize money first

Date: December 14, 2021

CS 111-01 Fall 2021

"""

# importing all necessary libraries
import numpy as np
import random
from PIL import Image
import urllib.request
import matplotlib.pyplot as pyplot

class player:

    """
    A player in the gambling simulation game
    
    """

    
    balance = 5000      #default balance that every player starts with
    wins = 0
    bet = 0
    prediction = ""
    balanceList = []    #list that stores change in balances after every round
    gamesPlayed = 0     #counts the number of rounds played by a player

    def __init__(self, name, bet, prediction, balanceList):
        """
        Create a player with name, bet amount, prediction, list that stores change in balances throughout the game

        Parameter:
            self: the Player object
            name: Name of the player
            bet: amount in $ that the player wants to bet in the game
            prediction: predict whether Alpha or Beta has the most number of wins in the simulation
            balanceList: a list that stores change in a player"s balance after every round

        Return value: None
        
        """
        self.name = name
        self.bet = bet
        self.prediction = prediction
        self.balance = self.balance - bet
        self.balanceList = balanceList

    def getName(self):

        """
        Return the name of the player

        Parameter:
            self: the Player object

        Return value: string representing player"s name
        """
        
        return self.name

    def getBalance(self):

       """
        Return the balance of the player in current round

        Parameter:
            self: the Player object

        Return value: integer representing player"s current balance

        """
       return self.balance

    def setBalance(self, balance):
        
        """
        Set the balance of the player in current round

        Parameter:
            self: the Player object
            balance: integer representing player"s current balance

        Return value: None

        """
        
        self.balance = balance

    def setBet(self, bet):
        
        """
        Set the bet amount of the player in current round

        Parameter:
            self: the Player object
            balance: integer representing player"s bet amount

        Return value: None

        """
        
        self.bet = bet
        self.balance = self.balance - bet #Deduct the bet amount from player"s balance

    def getBet(self):

         """
        Return the bet amount placed by the player in a round

        Parameter:
            self: the Player object

        Return value: integer representing player"s current bet amount
        """
         return self.bet

    def setPrediction(self, prediction):
         """
        Set the prediction of the player in a round

        Parameter:
            self: the Player object
            prediction: predict whether Alpha or Beta has the most number of wins in the simulation

        Return value: None

        """
         self.prediction = prediction

    def getPrediction(self):

          """
        Return the prediction set by the player in a round

        Parameter:
            self: the Player object

        Return value: string representing the prediction set by the player in a round
        """
          return self.prediction

    def won(self):

        """

        Increase player"s balance if the prediction is true in a round

        Parameter:
            self: the Player object

        Return value: None

        """
        self.balance = self.balance + self.bet * 2  #Doubles the bet amount and adds it to player"s balance

    def lost(self):

        """

        Decrease player"s balance if the prediction is false in a round

        Parameter:
            self: the Player object

        Return value: None

        """
        
        self.balance = self.balance

    def draw(self):

         """

        Add player"s bet back to balance if the result is draw in a round

        Parameter:
            self: the Player object

        Return value: None

        """
         self.balance = self.balance + self.bet

    def appendBalance(self, balance):
        """

        Add current balance to balance list.

        Parameter:
            self: the Player object
            balance: integer representing player"s current balance
        
        Return value: None
        """
        
        self.balanceList.append(balance)

    def getBalanceList(self):

        """

        Returns the balance list.

        Parameter:
            self: the Player object

        Return value: list of change in balances throughout the entire game

        """
        
        return self.balanceList

    def setGamesPlayed(self):

        """
        Increase number of rounds by 1

        Parameter:
            self: the Player object

        Return value: None

        """
        
        self.gamesPlayed = self.gamesPlayed + 1

    def getGamesPlayed(self):

        """

        Return number of rounds played
        
        Parameter:
            self: the Player object

        Return value: integer representing number of rounds played by a player
    
        """
        return self.gamesPlayed



def create_board():

    """
        Creates an empty board

        Parameter: None

        Return value: Array representing the board for tic tac toe

    """
    return (np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]))



def possibilities(board):

    """
        Check for empty places on board

        Parameter:
         board: Array representing the current board for tic tac toe

        Return value: List representing all the indices of empty spaces in the board

    """
    l = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0:
                l.append((i, j))
    return l



def random_place(board, bot):

    """
        Select a random place for the player

        Parameter:
            board: array representing the current board for tic tac toe
            bot: integer representing 1 or 2 as a player

        Return value: current board in the form of list after random placing a player 

    """
    
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = bot 
    return board


def row_win(board, bot):

    """

        Checks whether the player has three of their marks in a horizontal row

        Parameter:
            board: array representing the current board for tic tac toe
            bot: integer representing 1 or 2 as a player

        Return value: boolean representing player has won with a horizontal row having 3 marks

    """
    
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x, y] != bot:
                win = False
                continue

        if win:
            return win


    return win


def col_win(board, bot):
    """
    Checks whether the player has three of their marks in a vertical row

        Parameter:
            board: array representing the current board for tic tac toe
            bot: integer representing 1 or 2 as a player

        Return value: boolean representing player has won with a vertical row having 3 marks

    """
    for x in range(len(board)):
        
        win = True

        for y in range(len(board)):
            if board[y][x] != bot:
                win = False
                continue

        if win:
            return win

    return win

def diag_win(board, bot):

    """
    Checks whether the player has three of their marks in a diagonal row

        Parameter:
            board: array representing the current board for tic tac toe
            bot: integer representing 1 or 2 as a player

        Return value: boolean representing player has won with a diagonal row having 3 marks
    """
    
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != bot:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != bot:
                win = False
    return win


def evaluate(board):


    """
        Evaluates whether there is a winner or a tie

        Parameter:
            board: array representing the current board for tic tac toe

        Return value: integer representing if won or tie (1 means player 1 won, 2 means player 2 won, -1 is tie)

    """
    
    winner = 0

    for bot in [1, 2]:
        if (row_win(board, bot) or
                col_win(board, bot) or
                diag_win(board, bot)):
            winner = bot

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def play_game(alternate):

    """
        Main function to start one game of tic tac toe

        Parameter:
            alternate: boolean representing whether Alpha or Beta starts the game first

        Return value: integer representing who won a game (1 means Alpha won, 2 means Beta won, -1 means draw)


    """
    
    board, winner = create_board(), 0

    while winner == 0:
        if alternate: #play a game with alpha starting
            
            for bot in [1, 2]:
                board = random_place(board, bot)
                winner = evaluate(board)
                if winner != 0:
                   break
        else:
            
            for bot in [2, 1]: #play a game with beta starting
                board = random_place(board, bot)
                winner = evaluate(board)
                if winner != 0:
                    break
    return winner


def play_games_monte_carlo(games):

    """
        Simulate tic tac toe for a given number of games

        Parameter:
            games: number of trials to run the simulation

        Return value: string representing who won most number of games in the simulation among alpha and beta

    """

    
    alpha_wins = 0
    draw = 0
    beta_wins = 0
    winner = ""

    for game in range(int(games/2)): #Play half of the games with Alpha being the one who starts the game
        result = play_game(True)
        
        if result == 1:
            alpha_wins = alpha_wins + 1
        elif result == 2:
            beta_wins = beta_wins + 1
        elif result == -1:
            draw = draw+1

    for game in range(int(games/2)): #Play half of the games with Beta being the one who starts the game
        result = play_game(False)
        
        if result == 1:
            alpha_wins = alpha_wins + 1
        elif result == 2:
            beta_wins = beta_wins + 1
        elif result == -1:
            draw = draw+1
            
    print()
    print("Draws: ", draw)
    print("Alpha Wins: ", alpha_wins)
    print("Beta Wins: ", beta_wins)
    print()
    
    if alpha_wins > beta_wins:
        winner = "a"
    elif alpha_wins < beta_wins:
        winner = "b"
    elif alpha_wins == beta_wins:
        winner = "draw"

    return winner



def graph(playerList):

    """
    Plot a line chart with number of rounds in the x-axis and change in balances in the y-axis for all players

    Parameter:
        playerList: list containing all the player objects

    Return value: None

    """
    
    for _player in range(len(playerList)):
    
        pyplot.plot(range(playerList[0].getGamesPlayed()+1), playerList[_player].getBalanceList(), label = playerList[_player].getName())
        pyplot.title("Gambling Tic-Tac-Toe Simulation")
        pyplot.xlabel("Number of Rounds")
        pyplot.ylabel("Balance")
        
    pyplot.legend()
    pyplot.show()
    
def congrats():

    """
    Display a congratulatory picture when a player wins the entire game

    Parameter: None

    Return value: None
        
    """
    
    urllib.request.urlretrieve("https://image.freepik.com/free-vector/congratulations-typography-wording-style-vector_53876-56738.jpg",
   "congratulations-typography-wording-style-vector_53876-56738.jpg.webp")
 
    img = Image.open("congratulations-typography-wording-style-vector_53876-56738.jpg.webp")
    img.show()

    
def main():

    """
    Run the entire game

    Parameter: None

    Return value: None

    """

    print("Welcome to the Tic-Tac-Toe gambling simulation game!\n")

    print("""

    Rules of the game:
    
    ➡ Everyone have a starting balance of $5000

    ➡ Reach $50,000 to win.

    ➡ If your prediction is correct, the money is doubled.

    ➡ If the prediction is wrong, the money you chip in will be lost.

    ➡ If there is a draw, the money that you chip in will be refunded to your account.

    ➡ Any number of players can play this game. """)

    print()
    
    num_of_players = int(input("How many players are there? "))
    print("")
    playerList = []
    won = False

    for _player in range(num_of_players):
        playerName = input("Player number " + str(_player+1) + "! Enter your Name: ")
        print("")
        playerBet = int(input("How much do you want to bet? "))
        print("")
        print("Predict the winner (Alpha or Beta):")
        playerPrediction = input("Enter a or b: ")
        
        playerList.append(player(playerName, playerBet, playerPrediction, [5000])) #create a player object and add it the playerList

        result = play_games_monte_carlo(1000).lower() #run the tic tac toe simulation 1000 times and get result

        if result == playerPrediction.lower():
            playerList[_player].won()
        elif result == "draw":
            playerList[_player].draw()
        elif result != playerPrediction.lower():
            playerList[_player].lost()

        playerList[_player].appendBalance(playerList[_player].getBalance())
        playerList[_player].setGamesPlayed()

        if result == "a":
            print("Alpha Won. " + playerList[_player].getName() + ", your balance is $" + str(playerList[_player].getBalance()), "\n")
        elif result == "b":
            print("Beta Won. " + playerList[_player].getName() + ", your balance is $" + str(playerList[_player].getBalance()), "\n")
        elif result == "draw":
            print("Draw. " + playerList[_player].getName() + ", your balance is $" + str(playerList[_player].getBalance()), "\n")

    print("***********************")    
    print("" )
            
    while not won: #Place bets and run the tic tac toe simulation until the goal of $50,000 is achieved by a player
        for _player in range(num_of_players):
            print(playerList[_player].getName() + ", predict the winner (Alpha or Beta):")
            playerPrediction = input("Enter a or b: ")
            print()
            print("Your current balance is $" + str(playerList[_player].getBalance()))
            playerBet = int(input("How much do you want to bet? "))

            playerList[_player].setPrediction(playerPrediction)
            playerList[_player].setBet(playerBet)
            
            result = play_games_monte_carlo(1000).lower()

            if result == playerPrediction.lower():
                playerList[_player].won()
            elif result == "draw":
                playerList[_player].draw()
            else:
                playerList[_player].lost()

            playerList[_player].appendBalance(playerList[_player].getBalance())
            playerList[_player].setGamesPlayed()

            if result == "a":
                print("Alpha Won. " + playerList[_player].getName() + ", your balance is $" + str(playerList[_player].getBalance()), "\n")
            elif result == "b":
                print("Beta Won. " + playerList[_player].getName() + ", your balance is $" + str(playerList[_player].getBalance()), "\n")
            elif result == "draw":
                print("Draw. " + playerList[_player].getName() + ", your balance is $" + str(playerList[_player].getBalance()), "\n")
                
            if playerList[_player].getBalance() >= 50000:
                print(playerList[_player].getName() + " won")
               
                for a in range(_player+1,num_of_players):
                    playerList[a].appendBalance(playerList[a].getBalance())

                graph(playerList)
                congrats()
                won = True
            
                break
            
        print("***********************")
        print()
        
    
main()
