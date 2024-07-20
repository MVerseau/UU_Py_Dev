import runner_and_tournament
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            rn = runner_and_tournament.Runner(name='A', speed=-9)
            if rn.speed <= 0:
                raise ValueError(f'Скорость не может быть отрицательной, сейчас: {rn.speed}')
            for _ in range(10):
                rn.walk()
            self.assertEqual(rn.distance, 50)
            logging.info('"test_run" выполнен успешно')
        except ValueError:

            logging.warning(msg='Скорость не может быть отрицательной,', exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            rn = runner_and_tournament.Runner(10)
            if not isinstance(rn.name, str):
                raise TypeError(f'Имя не может быть {type(rn.name).__name__}')
            for _ in range(10):
                rn.run()
            self.assertEqual(rn.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning(msg="Неверный тип данных для имени экземпляра Runner", exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rn1 = runner_and_tournament.Runner('1')
        rn2 = runner_and_tournament.Runner('2')
        for _ in range(10):
            rn1.walk()
            rn2.run()
        self.assertNotEqual(rn1.distance, rn2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        for item in cls.all_results:
            print({k: v.name for k, v in item.items()})

    def setUp(self):
        self.rn1 = runner_and_tournament.Runner('Усэйн', speed=10)
        self.rn2 = runner_and_tournament.Runner('Андрей', speed=9)
        self.rn3 = runner_and_tournament.Runner('Ник', speed=3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        part_tuple = (self.rn3, self.rn1)
        results = runner_and_tournament.Tournament(90, *part_tuple).start()
        TournamentTest.all_results.append(results)
        self.assertTrue(sorted(results.items(), key=lambda i: i[0])[-1][1] ==
                        sorted(part_tuple, key=lambda i: i.speed, reverse=True)[-1].name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        part_tuple = (self.rn3, self.rn2)
        results = runner_and_tournament.Tournament(90, *part_tuple).start()
        TournamentTest.all_results.append(results)
        self.assertTrue(sorted(results.items(), key=lambda i: i[0])[-1][1] ==
                        sorted(part_tuple, key=lambda i: i.speed, reverse=True)[-1].name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        part_tuple = (self.rn3, self.rn2, self.rn1)
        results = runner_and_tournament.Tournament(90, *part_tuple).start()
        TournamentTest.all_results.append(results)
        self.assertTrue(sorted(results.items(), key=lambda i: i[0])[-1][1] ==
                        sorted(part_tuple, key=lambda i: i.speed, reverse=True)[-1].name)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
