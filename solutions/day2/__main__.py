from src.solution_pipeline import SolutionPipeline

from .preprocess import preprocess
from .run_calculations import run_calculations

YEAR = 2021
DAY = 2

pipeline = SolutionPipeline(YEAR, DAY, preprocess, run_calculations)
pipeline.create()
pipeline.run()
