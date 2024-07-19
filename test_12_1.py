import runner_and_tournament
import unittest




class RunnerTest(unittest.TestCase):
    is_frozen=False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        rn = runner_and_tournament.Runner('A')
        for _ in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rn = runner_and_tournament.Runner('A')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

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
            print({k:v.name for k,v in item.items()})
        # print(cls.all_results)

    def setUp(self):
        self.rn1 = runner_and_tournament.Runner('Усэйн', speed=10)
        self.rn2 = runner_and_tournament.Runner('Андрей', speed=9)
        self.rn3 = runner_and_tournament.Runner('Ник', speed=3)

    @unittest.skipIf(is_frozen==True,'Тесты в этом кейсе заморожены')
    def test_run1(self):
        part_tuple=(self.rn3, self.rn1)
        results = runner_and_tournament.Tournament(90,*part_tuple ).start()
        TournamentTest.all_results.append(results)
        # print({k: v.name for k, v in results.items()})
        self.assertTrue(sorted(results.items(), key=lambda i: i[0])[-1][1] == sorted(part_tuple, key=lambda i: i.speed, reverse=True)[-1].name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        part_tuple = (self.rn3, self.rn2)
        results = runner_and_tournament.Tournament(90, *part_tuple).start()
        TournamentTest.all_results.append(results)
        # print({k: v.name for k, v in results.items()})
        self.assertTrue(sorted(results.items(), key=lambda i: i[0])[-1][1] == sorted(part_tuple, key=lambda i: i.speed, reverse=True)[-1].name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        part_tuple = (self.rn3, self.rn2, self.rn1)
        results = runner_and_tournament.Tournament(90, *part_tuple).start()
        TournamentTest.all_results.append(results)
        # print({k: v.name for k, v in results.items()})
        self.assertTrue(sorted(results.items(), key=lambda i: i[0])[-1][1] == sorted(part_tuple, key=lambda i: i.speed, reverse=True)[-1].name)


if __name__ == '__main__':
    unittest.main()


