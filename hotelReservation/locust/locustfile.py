#!/usr/bin/python

import random

from locust import HttpUser, TaskSet, between


def get_user():
    user_id = random.randint(0, 500)
    user_name = f"Cornel_{user_id}"
    pass_word = ""
    for _ in range(10):
        pass_word += str(user_id)
    return user_name, pass_word


def index(l):
    l.client.get("/")


def search_hotel(l):
    in_date = random.randint(9, 23)
    out_date = random.randint(in_date + 1, 24)

    in_date_str = str(in_date)
    if in_date <= 9:
        in_date_str = f"2015-04-0{in_date_str}"
    else:
        in_date_str = f"2015-04-{in_date_str}"

    out_date_str = str(out_date)
    if out_date <= 9:
        out_date_str = f"2015-04-0{out_date_str}"
    else:
        out_date_str = f"2015-04-{out_date_str}"

    lat = 38.0235 + (random.randint(0, 481) - 240.5) / 1000.0
    lon = -122.095 + (random.randint(0, 325) - 157.0) / 1000.0

    path = f"/hotels?inDate={in_date_str}&outDate={out_date_str}&lat={lat}&lon={lon}"
    l.client.get(path)


def recommend(l):
    coin = random.random()
    req_param = ""
    if coin < 0.33:
        req_param = "dis"
    elif coin < 0.66:
        req_param = "rate"
    else:
        req_param = "price"

    lat = 38.0235 + (random.randint(0, 481) - 240.5) / 1000.0
    lon = -122.095 + (random.randint(0, 325) - 157.0) / 1000.0

    path = f"/recommendations?require={req_param}&lat={lat}&lon={lon}"
    l.client.get(path)


def reserve(l):
    in_date = random.randint(9, 23)
    out_date = in_date + random.randint(1, 5)

    in_date_str = str(in_date)
    if in_date <= 9:
        in_date_str = f"2015-04-0{in_date_str}"
    else:
        in_date_str = f"2015-04-{in_date_str}"

    out_date_str = str(out_date)
    if out_date <= 9:
        out_date_str = f"2015-04-0{out_date_str}"
    else:
        out_date_str = f"2015-04-{out_date_str}"

    hotel_id = str(random.randint(1, 80))
    user_id, password = get_user()
    cust_name = user_id
    num_room = "1"

    lat = 38.0235 + (random.randint(0, 481) - 240.5) / 1000.0
    lon = -122.095 + (random.randint(0, 325) - 157.0) / 1000.0

    path = f"/reservation?inDate={in_date_str}&outDate={out_date_str}&lat={lat}&lon={lon}&hotelId={hotel_id}&customerName={cust_name}&username={user_id}&password={password}&number={num_room}"
    l.client.post(path)


def user_login(l):
    user_name, password = get_user()
    path = f"/user?username={user_name}&password={password}"
    l.client.post(path)


class UserBehavior(TaskSet):

    def on_start(self):
        index(self)

    tasks = {
        index: 1,
        search_hotel: 58,
        recommend: 39,
        reserve: 1,
        user_login: 1,
    }


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 10)
