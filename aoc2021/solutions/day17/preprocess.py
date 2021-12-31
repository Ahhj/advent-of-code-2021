from .target_area import TargetArea
import re


def preprocess(raw_data):
    pattern = re.compile(
        r"target area: x=([\-]?\d+)..([\-]?\d+), y=([\-]?\d+)..([\-]?\d+)"
    )
    endpoints = map(int, pattern.search(raw_data).groups(0))
    target_area = TargetArea(*endpoints)
    return target_area
