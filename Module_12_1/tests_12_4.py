import unittest
import logging

import rt_with_exceptions


def log_decorator(func):
    def wrapper(self):
        try:
            func(self)
            logging.info(f'"{func.__name__}" выполнен успешно',)
        except Exception as e:
            logging.warning(f'В "{func.__name__}" ПРОИЗОШЛА ОШИБКА!!!', exc_info=e.args[0])
    return wrapper


class RunnerTest(unittest.TestCase):

    @log_decorator
    def test_walk(self):
        runner_1 = rt_with_exceptions.Runner('Runner_1', speed=-1)
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @log_decorator
    def test_run(self):
        runner_2 = rt_with_exceptions.Runner(1, speed=5)
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @log_decorator
    def test_challenge(self):
        runner_3 = rt_with_exceptions.Runner('Runner_3', 8)
        runner_4 = rt_with_exceptions.Runner('Runner_4', 10)
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='runner_test.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()
