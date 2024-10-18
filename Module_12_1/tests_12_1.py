import unittest

import rt_with_exceptions
import runner
import runner_and_tournament


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


@unittest.skip('Пропущен весь класс с проверками одним декоратором')
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
    is_frozen = True

    def setUp(self):
        self.test_cls_1 = runner_and_tournament.Runner('runner_1')
        self.test_cls_2 = runner_and_tournament.Runner('runner_2')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        for _ in range(10):
            self.test_cls_1.walk()
        self.assertEqual(self.test_cls_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        for _ in range(10):
            self.test_cls_1.run()
        self.assertEqual(self.test_cls_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        for _ in range(10):
            self.test_cls_1.run()
            self.test_cls_2.walk()
        self.assertNotEqual(self.test_cls_1.distance, self.test_cls_2.distance)


if __name__ == '__main__':
    unittest.main()
