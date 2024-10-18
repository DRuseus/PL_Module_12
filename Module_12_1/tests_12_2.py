import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    is_frozen = False
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        super().setUpClass()

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for _dict in cls.all_results:
            print(_dict)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_long_distance_1(self):
        self.tournament_1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        all_results = {k: v.name for k, v in self.tournament_1.start().items()}
        self.all_results.append(all_results)
        self.assertTrue(all_results[2] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_long_distance_2(self):
        self.tournament_1 = runner_and_tournament.Tournament(90,self.runner_2, self.runner_3)
        all_results = {k: v.name for k, v in self.tournament_1.start().items()}
        self.all_results.append(all_results)
        self.assertTrue(all_results[2] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_long_distance_3(self):
        self.tournament_1 = runner_and_tournament.Tournament(90,
                                                             self.runner_1, self.runner_2, self.runner_3)
        all_results = {k: v.name for k, v in self.tournament_1.start().items()}
        self.all_results.append(all_results)
        self.assertTrue(all_results[3] == self.runner_3)

    # Дополнительная проверка на выявление логической ошибки
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_short_distance(self):
        self.tournament_1 = runner_and_tournament.Tournament(1,
                                                             self.runner_1, self.runner_2, self.runner_3)
        all_results = {k: v.name for k, v in self.tournament_1.start().items()}
        self.all_results.append(all_results)
        self.assertTrue(all_results[3] == self.runner_3)


if __name__ == '__main__':
    unittest.main()
