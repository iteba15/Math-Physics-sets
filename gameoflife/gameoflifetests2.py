import unittest
from gameoflife import ConwaysGame

class ConwaysGameTests(unittest.TestCase):
    def test_set_world_size(self):
        '''set_world_size should set the width and height of the world'''
        game = ConwaysGame()
        game.set_world_size(10, 5)
        self.assertEqual(game.width, 10)
        self.assertEqual(game.height, 5)
    
    def test_populate_and_cell_is_alive(self):
        game = ConwaysGame()
        game.set_world_size(10,10)
        game.populate(1, 2)
        game.populate(7, 4)
        self.assertEqual(game.cell_is_alive(2, 2), False)
        self.assertEqual(game.cell_is_alive(1, 2), True)
        self.assertEqual(game.cell_is_alive(7, 4), True)

    def test_populate_outside_of_range(self):
        game = ConwaysGame()
        game.set_world_size(3, 1)
        self.assertRaises(IndexError, game.populate, 3, 0)
        self.assertRaises(IndexError, game.populate, 0, 1)

# OOOOO
# OOOOO
# XXOOO
# XOOOO
# OOOOO

    def test_number_of_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(5, 5)
        game.populate(0, 2)
        game.populate(0, 3)
        game.populate(1, 2)
        self.assertEqual(game.number_of_live_neighbours(1, 3), 3)
        self.assertEqual(game.number_of_live_neighbours(1, 1), 2)
        self.assertEqual(game.number_of_live_neighbours(2, 2), 1)
        self.assertEqual(game.number_of_live_neighbours(0, 0), 0)

    def test_step_two_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(2, 2)
        game.populate(0, 0)
        game.populate(1, 0)
        self.assertEqual(game.cell_is_alive(0, 0), True)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(1, 0), True)
        self.assertEqual(game.cell_is_alive(1, 1), False)
        game.step()
        self.assertEqual(game.cell_is_alive(0, 0), False)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(1, 0), False)
        self.assertEqual(game.cell_is_alive(1, 1), False)

    def test_step_live_cell_with_two_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(3, 1)
        game.populate(0, 0)
        game.populate(1, 0)
        game.populate(2, 0)
        self.assertEqual(game.cell_is_alive(0, 0), True)
        self.assertEqual(game.cell_is_alive(1, 0), True)
        self.assertEqual(game.cell_is_alive(2, 0), True)
        game.step()
        self.assertEqual(game.cell_is_alive(0, 0), False)
        self.assertEqual(game.cell_is_alive(1, 0), True)
        self.assertEqual(game.cell_is_alive(2, 0), False)

    def test_step_live_cell_with_three_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(3, 3)
        game.populate(0, 0)
        game.populate(0, 2)
        game.populate(1, 1)
        game.populate(2, 1)
        self.assertEqual(game.cell_is_alive(0, 0), True)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(0, 2), True)
        self.assertEqual(game.cell_is_alive(1, 0), False)
        self.assertEqual(game.cell_is_alive(1, 1), True)
        self.assertEqual(game.cell_is_alive(1, 2), False)
        self.assertEqual(game.cell_is_alive(2, 0), False)
        self.assertEqual(game.cell_is_alive(2, 1), True)
        self.assertEqual(game.cell_is_alive(2, 2), False)
        game.step()
        self.assertEqual(game.cell_is_alive(0, 0), False)
        self.assertEqual(game.cell_is_alive(0, 1), True)
        self.assertEqual(game.cell_is_alive(0, 2), False)
        self.assertEqual(game.cell_is_alive(1, 0), True)
        self.assertEqual(game.cell_is_alive(1, 1), True)
        self.assertEqual(game.cell_is_alive(1, 2), True)
        self.assertEqual(game.cell_is_alive(2, 0), False)
        self.assertEqual(game.cell_is_alive(2, 1), False)
        self.assertEqual(game.cell_is_alive(2, 2), False)

    def test_step_live_cell_with_four_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(3, 3)
        game.populate(0, 0)
        game.populate(1, 0)
        game.populate(0, 2)
        game.populate(1, 1)
        game.populate(2, 1)
        self.assertEqual(game.cell_is_alive(0, 0), True)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(0, 2), True)
        self.assertEqual(game.cell_is_alive(1, 0), True)
        self.assertEqual(game.cell_is_alive(1, 1), True)
        self.assertEqual(game.cell_is_alive(1, 2), False)
        self.assertEqual(game.cell_is_alive(2, 0), False)
        self.assertEqual(game.cell_is_alive(2, 1), True)
        self.assertEqual(game.cell_is_alive(2, 2), False)
        game.step()
        self.assertEqual(game.cell_is_alive(0, 0), True)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(0, 2), False)
        self.assertEqual(game.cell_is_alive(1, 0), True)
        self.assertEqual(game.cell_is_alive(1, 1), False)
        self.assertEqual(game.cell_is_alive(1, 2), True)
        self.assertEqual(game.cell_is_alive(2, 0), True)
        self.assertEqual(game.cell_is_alive(2, 1), True)
        self.assertEqual(game.cell_is_alive(2, 2), False)

    def test_step_dead_cell_with_three_live_neighbours(self):
        game = ConwaysGame()
        game.set_world_size(3, 3)
        game.populate(0, 0)
        game.populate(0, 2)
        game.populate(2, 1)
        self.assertEqual(game.cell_is_alive(0, 0), True)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(0, 2), True)
        self.assertEqual(game.cell_is_alive(1, 0), False)
        self.assertEqual(game.cell_is_alive(1, 1), False)
        self.assertEqual(game.cell_is_alive(1, 2), False)
        self.assertEqual(game.cell_is_alive(2, 0), False)
        self.assertEqual(game.cell_is_alive(2, 1), True)
        self.assertEqual(game.cell_is_alive(2, 2), False)
        game.step()
        self.assertEqual(game.cell_is_alive(0, 0), False)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(0, 2), False)
        self.assertEqual(game.cell_is_alive(1, 0), False)
        self.assertEqual(game.cell_is_alive(1, 1), True)
        self.assertEqual(game.cell_is_alive(1, 2), False)
        self.assertEqual(game.cell_is_alive(2, 0), False)
        self.assertEqual(game.cell_is_alive(2, 1), False)
        self.assertEqual(game.cell_is_alive(2, 2), False)

    def test_glider(self):
        game = ConwaysGame()
        game.set_world_size(6, 6)
        game.populate(2, 1)
        game.populate(3, 2)
        game.populate(1, 3)
        game.populate(2, 3)
        game.populate(3, 3)
        game.step()
        self.assertEqual(game.cell_is_alive(0, 0), False)
        self.assertEqual(game.cell_is_alive(0, 1), False)
        self.assertEqual(game.cell_is_alive(0, 2), False)
        self.assertEqual(game.cell_is_alive(0, 3), False)
        self.assertEqual(game.cell_is_alive(0, 4), False)
        self.assertEqual(game.cell_is_alive(0, 5), False)
        self.assertEqual(game.cell_is_alive(1, 0), False)
        self.assertEqual(game.cell_is_alive(1, 1), False)
        self.assertEqual(game.cell_is_alive(1, 2), True)
        self.assertEqual(game.cell_is_alive(1, 3), False)
        self.assertEqual(game.cell_is_alive(1, 4), False)
        self.assertEqual(game.cell_is_alive(1, 5), False)
        self.assertEqual(game.cell_is_alive(2, 0), False)
        self.assertEqual(game.cell_is_alive(2, 1), False)
        self.assertEqual(game.cell_is_alive(2, 2), False)
        self.assertEqual(game.cell_is_alive(2, 3), True)
        self.assertEqual(game.cell_is_alive(2, 4), True)
        self.assertEqual(game.cell_is_alive(2, 5), False)
        self.assertEqual(game.cell_is_alive(3, 0), False)
        self.assertEqual(game.cell_is_alive(3, 1), False)
        self.assertEqual(game.cell_is_alive(3, 2), True)
        self.assertEqual(game.cell_is_alive(3, 3), True)
        self.assertEqual(game.cell_is_alive(3, 4), False)
        self.assertEqual(game.cell_is_alive(3, 5), False)
        self.assertEqual(game.cell_is_alive(4, 0), False)
        self.assertEqual(game.cell_is_alive(4, 1), False)
        self.assertEqual(game.cell_is_alive(4, 2), False)
        self.assertEqual(game.cell_is_alive(4, 3), False)
        self.assertEqual(game.cell_is_alive(4, 4), False)
        self.assertEqual(game.cell_is_alive(4, 5), False)
        self.assertEqual(game.cell_is_alive(5, 0), False)
        self.assertEqual(game.cell_is_alive(5, 1), False)
        self.assertEqual(game.cell_is_alive(5, 2), False)
        self.assertEqual(game.cell_is_alive(5, 3), False)
        self.assertEqual(game.cell_is_alive(5, 4), False)
        self.assertEqual(game.cell_is_alive(5, 5), False)

    def test_to_string(self):
        game = ConwaysGame()
        game.set_world_size(2, 2)
        game.populate(0, 0)
        game.populate(1, 1)
        self.assertEqual(str(game), "◼◻\n◻◼")

if __name__ == '__main__':
    unittest.main()

