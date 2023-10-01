from Puzzle_resolve import result_with_matrix
import unittest

class TestPuzzle(unittest.TestCase):
    
    def testing_combination(self):
        dados = result_with_matrix([[6,2,8],[4,7,1],[0,3,5]])
        tamanho = len(dados) - 1
        self.assertEqual(tamanho, 24, "Should be 24")

    def testing_puzzel_impossible(self):
        with self.assertRaises(Exception) as context:
            result_with_matrix([[1,2,3],[4,5,6],[0,8,7]])
        self.assertEqual(str(context.exception),"Looping não foi possivel fazer esse puzzle, pois ele não é existe")

if __name__ == '__main__':
    # esting_combination()
    unittest.main()