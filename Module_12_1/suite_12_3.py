import unittest
import tests_12_2
import tests_12_1


suite_my_tests = unittest.TestSuite()
suite_my_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest1))
suite_my_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest2))
suite_my_tests.addTests(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest3))
suite_my_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

if __name__ == '__main__':
    runner = unittest.runner.TextTestRunner(verbosity=2)
    runner.run(suite_my_tests)
