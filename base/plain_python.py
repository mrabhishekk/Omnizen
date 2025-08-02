from loguru import logger
from pprint import pprint
from rich import print as printr

mydict = {
    "Today": ["Do Jogging", "Go to Market.", "Abhi will take a shower.", "Watch a movie."],
    "Tomorrow": ["Find a shop.", "Do some study.", "Take a bus ride."],
    "Next 7 days": ["Find a beach.", "Go to School", "A bookfare visit."]
}

# print(mydict)
# pprint(mydict)
# logger.info(mydict)
# printr(mydict)


for value in mydict.values():
    # printr(value)
    value.sort()
    printr(value)













