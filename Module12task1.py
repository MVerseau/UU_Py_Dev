import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen=False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        rn = runner.Runner('A')
        for _ in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rn = runner.Runner('A')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rn1 = runner.Runner('1')
        rn2 = runner.Runner('2')
        for _ in range(10):
            rn1.walk()
            rn2.run()
        self.assertNotEqual(rn1.distance, rn2.distance)


if __name__ == '__main__':
    unittest.main()
    # rt = RunnerTest()
    # try:
    #     print(rt.test_run())
    # except:
    #     raise AssertionError
    # try:
    #     print(rt.test_walk())
    # except:
    #     raise AssertionError
    # try:
    #     print(rt.test_challenge())
    # except:
    #     raise AssertionError

    # # try:
    # threading.Thread(target=print, args=(rt.test_run,))
    # # except:
    # #     raise AssertionError
    # # try:
    # threading.Thread(target=print, args=(rt.test_walk,)).start()
    # # except:
    # #     raise AssertionError
    # # try:
    # threading.Thread(target=print, args=(rt.test_challenge,)).start()
    # # except:
    # #     raise AssertionError

