import unittest

import rt_with_exceptions
import runner
import runner_and_tournament


# from runner_and_tournament import Runner


class RunnerTest1(unittest.TestCase):
    def setUp(self):
        self.test_cls_1 = rt_with_exceptions.Runner('runner_1')
        self.test_cls_2 = rt_with_exceptions.Runner('runner_2')

    def test_walk(self):
        for _ in range(10):
            self.test_cls_1.walk()
        self.assertEqual(self.test_cls_1.distance, 50)

    def test_run(self):
        for _ in range(10):
            self.test_cls_1.run()
        self.assertEqual(self.test_cls_1.distance, 100)

    def test_challenge(self):
        for _ in range(10):
            self.test_cls_1.run()
            self.test_cls_2.walk()
        self.assertNotEqual(self.test_cls_1.distance, self.test_cls_2.distance)


class RunnerTest2(unittest.TestCase):
    def setUp(self):
        self.test_cls_1 = runner.Runner('runner_1')
        self.test_cls_2 = runner.Runner('runner_2')

    def test_walk(self):
        for _ in range(10):
            self.test_cls_1.walk()
        self.assertEqual(self.test_cls_1.distance, 50)

    def test_run(self):
        for _ in range(10):
            self.test_cls_1.run()
        self.assertEqual(self.test_cls_1.distance, 100)

    def test_challenge(self):
        for _ in range(10):
            self.test_cls_1.run()
            self.test_cls_2.walk()
        self.assertNotEqual(self.test_cls_1.distance, self.test_cls_2.distance)


class RunnerTest3(unittest.TestCase):
    def setUp(self):
        self.test_cls_1 = runner_and_tournament.Runner('runner_1')
        self.test_cls_2 = runner_and_tournament.Runner('runner_2')

    def test_walk(self):
        for _ in range(10):
            self.test_cls_1.walk()
        self.assertEqual(self.test_cls_1.distance, 50)

    def test_run(self):
        for _ in range(10):
            self.test_cls_1.run()
        self.assertEqual(self.test_cls_1.distance, 100)

    def test_challenge(self):
        for _ in range(10):
            self.test_cls_1.run()
            self.test_cls_2.walk()
        self.assertNotEqual(self.test_cls_1.distance, self.test_cls_2.distance)


# if __name__ == '__main__':
#     unittest.main()


test_cases = (RunnerTest1, RunnerTest2, RunnerTest3)


def load_tests(loader, tests, pattern):
    t_suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        t_suite.addTests(tests)
    return t_suite


if __name__ == '__main__':
    suite = load_tests()

    runner = unittest.TextTestRunner()
    runner.run(suite)
