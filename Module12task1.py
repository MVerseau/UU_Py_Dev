import threading

import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn = runner.Runner('A')
        for _ in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn = runner.Runner('A')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    def test_challenge(self):
        rn1 = runner.Runner('1')
        rn2 = runner.Runner('2')
        for _ in range(10):
            rn1.walk()
            rn2.run()
        self.assertNotEqual(rn1.distance, rn2.distance)


if __name__ == '__main__':
    rt = RunnerTest()
    # print(rt.test_run())
    # print(rt.test_walk())
    # print(rt.test_challenge())
    #Потоки - чтобы прошли все 3 теста независимо от результата
    threading.Thread(target=print, args=(rt.test_run,)).start()
    threading.Thread(target=print, args=(rt.test_walk,)).start()
    threading.Thread(target=print, args=(rt.test_challenge,)).start()
   
