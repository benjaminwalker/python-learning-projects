from logging import getLogger

logger = getLogger(__name__)
def run_problem(**kwargs):
    logger.info(f"Logs work")
    return 1


if __name__ == "__main__":
    run_problem()