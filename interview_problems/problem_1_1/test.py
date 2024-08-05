from unittest import TestCase

from interview_problems.problem_1_1.main import run_problem

from logging import getLogger

logger = getLogger(__name__)


class TestProblem(TestCase):
    def test_problem_1_unique(self):
        actual = run_problem(string_value="naomi")
        logger.debug(actual)
        self.assertTrue(actual)

    def test_problem_1_dups(self):
        actual = run_problem(string_value="pizza")
        logger.debug(actual)
        self.assertFalse(actual)

