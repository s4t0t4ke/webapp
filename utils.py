import data
import random
import time


def prepare():
    data.idx = random.choice(data.order)
    random.shuffle(data.role_list)


def make_chat(history):
    time.sleep(2)
    return "Over"