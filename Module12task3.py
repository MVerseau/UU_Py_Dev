import unittest
import test_12_1

my_TS = unittest.TestSuite()
my_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
my_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_TS)
