"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
jbdurham
sayanc
sdave
ariedelm
"""
from awap2019 import Tile, Direction, State

class Team(object):
    def __init__(self, initial_board, team_size, company_info):
        """
        The initializer is for you to precompute anything from the
        initial board and the company information! Feel free to create any
        new instance variables to help you out.

        Specific information about initial_board and company_info are
        on the wiki. team_size, although passed to you as a parameter, will
        always be 4.
        """
        companyNames = []
        mapWidth = len(initial_board[0])
        mapHeight = len(initial_board)
        companyPoints = {}
        boothSquares = {}
        lineSquares = {}
        for company in company_info:
            companyNames.append(company)
        self.company_names = companyNames
        for company in companyNames:
            companyPoints[company] = company_info[company]
            boothSquares[company] = []
            lineSquares[company] = []
        self.company_points = company_info

        for yIdx in range(len(initial_board)):
            for xIdx in range(len(initial_board[0])):
                tile = initial_board[yIdx][xIdx]
                if(tile.get_booth() is not None):
                    boothSquares[tile.get_booth()].append((xIdx,yIdx))
                if(tile.get_line() is not None):
                    lineSquares[tile.get_line()].append((xIdx,yIdx))
        self.board = initial_board
        self.booth_squares = boothSquares
        self.line_squares = lineSquares

        costMap = []
        for yIdx in range(mapHeight):
            nextRow = []
            for xIdx in range(mapWidth):
                # (Total sum of costs, number of readings)
                nextRow.append((1,1))
            costMap.append(nextRow)

        self.cost_map = costMap

        valueMap = []
        for yIdx in range(mapHeight):
            nextRow = []
            for xIdx in range(mapWidth):
                nextRow.append(0)
            valueMap.append(nextRow)

        for company in companyNames:
            for (boothX, boothY) in self.booth_squares[company]:
                self.cost_map[boothY][boothX] = None
            for (lineX, lineY) in self.line_squares[company]:
                valueMap[lineY][lineX] = companyPoints[company]
        
        self.value_map = valueMap

        print(self.cost_map)
        print(self.value_map)


        self.team_size = team_size
        self.team_name = 'Al-bro-rithms'

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """
        



        return [Direction.UP, Direction.UP, Direction.UP, Direction.UP]
