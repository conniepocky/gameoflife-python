import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../gameoflife')))
from gameoflife import GameOfLife

class TestGameOfLife(unittest.TestCase):

    def test_cell_with_less_than_two_neighbours_dies(self):
        expect = [
                [False, False, False],
                [False, False, False],
                [False, False, False]]
        board = [
                [False, False, False],
                [True, True, False],
                [False, False, False]]

        gameoflife = GameOfLife(board)
        gameoflife.nextGen()

        self.assertEqual(expect, gameoflife.board)

    def test_cell_with_two_neighbours_lives(self):
        board =   [[True, False, False],
                  [False, True, False],
                  [False, False, True]]

        expect = [[False, False, False],
                  [False, True, False],
                  [False, False, False]]

        gameoflife = GameOfLife(board)
        gameoflife.nextGen()

        self.assertEqual(expect, gameoflife.board)
        
unittest.main()
