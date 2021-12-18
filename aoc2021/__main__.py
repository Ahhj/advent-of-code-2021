import argparse
from .solution_pipeline import SolutionPipeline

parser = argparse.ArgumentParser(
    prog="aoc2021",
    description="Solve Advent of Code 2021 problems and submit the solutions!",
)
parser.add_argument("--day", metavar="DAY", type=int, help="The day to solve")


args = parser.parse_args()
YEAR = 2021
DAY = args.day

pipeline = SolutionPipeline(YEAR, DAY)
pipeline.create()
pipeline.run()
pipeline.submit()
