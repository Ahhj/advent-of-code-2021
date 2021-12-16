from dotenv import load_dotenv
from aocd import submit

load_dotenv()


def submit_answers(year, day, answers):
    for part, answer in answers.items():
        submit(answer, part=part, year=year, day=day)
