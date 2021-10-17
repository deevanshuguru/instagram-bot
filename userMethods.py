from instagrapi import Client

c1 = Client()

# Authenticate User
user = input('Please enter your username: ')
password = input('Please enter your password: ')
c1.login(user, password)

# Get a list of Followers by username

def getFollowersByUsername(user_name):
    user_id = c1.user_info_by_username(user_name).pk
    followers = c1.user_followers(user_id)
    followers_list = []
    for follower in followers:
        followers_list.append(followers[follower].username)
    return followers_list


#  Get a list of Followings by username

def getFollowingsByUsername(user_name):
    user_id = c1.user_info_by_username(user_name).pk
    followings = c1.user_following(user_id)
    followings_list = []
    for following in followings:
        followings_list.append(followings[following].username)
    return followings_list


# Get userIds of Followers of a user

def getUserIdsOfFollowersByUsername(user_name):
    user_id = c1.user_info_by_username(user_name).pk
    followers = c1.user_followers(user_id)
    followers_list = []
    for follower in followers:
        followers_list.append(follower)
    return followers_list


# Get userIds of Followings of a user

def getUserIdsOfFollowingsByUsername(user_name):
    user_id = c1.user_info_by_username(user_name).pk
    followings = c1.user_following(user_id)
    followings_list = []
    for following in followings:
        followings_list.append(following)
    return followings_list


followingsIdList = getUserIdsOfFollowingsByUsername('stocks.in.india')

print(followingsIdList)
