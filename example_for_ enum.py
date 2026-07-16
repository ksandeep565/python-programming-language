from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5

print("Day Name:", Day.MONDAY.name)
print("Day Value:", Day.MONDAY.value)