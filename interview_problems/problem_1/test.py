from unittest import TestCase

from interview_problems.problem_1.main import run_problem
class TestProblem(TestCase):


    def test_problem_1(self):
        expected = 1
        actual = run_problem()
        self.assertEqual(expected, actual)

