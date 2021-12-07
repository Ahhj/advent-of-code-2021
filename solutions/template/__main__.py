from src.solution_pipeline import SolutionPipeline

from .preprocess import preprocess
from .run_calculations import calc_a, calc_b

YEAR = 2021
DAY = 2

pipeline = SolutionPipeline(YEAR, DAY, preprocess, calc_a, calc_b)
pipeline.create()
pipeline.run()