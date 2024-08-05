import logging
from logging import getLogger,INFO

logger = getLogger(__name__)


def run_problem(**kwargs) -> bool:
    ###
    # evaluates a string, returns true or false depending on whether characters are unique
    ###
    string_value = kwargs['string_value']
    return len(set(string_value)) == len(string_value)


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    run_problem(string_value='test')