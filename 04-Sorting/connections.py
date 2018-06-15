#!/usr/bin/python
from __future__ import division
from collections import Counter

users = [
    { "id":0, "name": "Hero"},
    { "id":1, "name": "Dunn"},
    { "id":2, "name": "Foo"},
    { "id":3, "name": "Rhe"},
    { "id":4, "name": "Thor"},
    { "id":5, "name": "Clive"},
    { "id":6, "name": "Hicks"},
    { "id":7, "name": "Even"},
    { "id":8, "name": "Kate"},
    { "id":9, "name": "Shine"},
]

friendships = [
    (0,1), (0,2),
    (1, 2), (1, 3),
    (2,3), 
    (3, 4),
    (4, 5), 
    (5, 6), (5, 7), 
    (6, 8),
    (7, 8),
    (8, 9)]

def not_the_same(user, other_user):
    """two users are not the same if they have different IDs"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other user is not a friend if he's not in the user["friends"]"""
    return all(not_the_same(friend, other_user)
                for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                    for friend in user["friends"]
                    for foaf in friend["friends"]
                    if not_the_same(user, foaf)
                    and not_friends(user, foaf))

def number_of_friends(user):
    """How many friends does _user_ have?"""
    return len(user["friends"])

def friend_of_friend_ids_bad(user):
    return [foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]]

# make a new hash. 
for user in users:
    user["friends"] = []

# add each friend to the friendships.
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)


num_users = len(users)
avg_connections = total_connections / num_users
print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
x = sorted(num_friends_by_id,
    key=lambda (user_id, num_friends): num_friends, reverse=True)
print(x)

print(friend_of_friend_ids_bad(users[0]))
