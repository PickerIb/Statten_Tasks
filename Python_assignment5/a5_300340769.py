#Family Name:Emmanuel ngabo
#Student Number:300340769
#Course:IT1 1120
#Assignment Number 5 
#Year 2026

#####################################################
#Social Networks: friends recommendations and more
#####################################################


import random

def _find_user_index(network, user_id):
    
    '''
    (2Dlist, int)->int

    Given a 2D-list representing a friendship network and a user ID,
    returns the position (index) of that user in the network.

    The function uses binary search to find the user because the
    users in the network are sorted by their IDs.

    If the user ID exists in the network, the function returns
    the index where that user is found.

    If the user ID does not exist in the network, it returns -1.

    but  the users in the network are sorted by ID.
    
    '''
    low = 0
    high = len(network) - 1

    while low <= high:
        middle = (low + high) // 2

        if network[middle][0] == user_id:
            return middle
        elif network[middle][0] < user_id:
            low = middle + 1
        else:
            high = middle - 1

    return -1

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]

    user_ids = []
    friendships = []

    for line in friends[1:]:
        values = line.split()

        if len(values) == 2:
            user1 = int(values[0])
            user2 = int(values[1])

            friendships.append((user1, user2))
            user_ids.append(user1)
            user_ids.append(user2)

    user_ids.sort()

    unique_user_ids = []

    for user_id in user_ids:
        if len(unique_user_ids) == 0 or user_id != unique_user_ids[-1]:
            unique_user_ids.append(user_id)

    for user_id in unique_user_ids:
        network.append((user_id, []))

    for friendship in friendships:
        user1 = friendship[0]
        user2 = friendship[1]

        index1 = _find_user_index(network, user1)
        index2 = _find_user_index(network, user2)

        network[index1][1].append(user2)
        network[index2][1].append(user1)

    for user in network:
        user[1].sort()
    
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    
    index1 = _find_user_index(network, user1)
    index2 = _find_user_index(network, user2)

    friends1 = network[index1][1]
    friends2 = network[index2][1]

    i = 0
    j = 0

    while i < len(friends1) and j < len(friends2):
        if friends1[i] == friends2[j]:
            common.append(friends1[i])
            i += 1
            j += 1
        elif friends1[i] < friends2[j]:
            i += 1
        else:
            j += 1

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom the user has the maximum number of friends in common
    return the one with the smallest ID. '''

    user_index = _find_user_index(network, user)
    user_friends = network[user_index][1]

    best_candidate = None
    maximum_common = 0

    for candidate in network:
        candidate_id = candidate[0]

        if candidate_id == user:
            continue

        if candidate_id in user_friends:
            continue

        common_friends = getCommonFriends(user, candidate_id, network)
        number_common = len(common_friends)

        if number_common > maximum_common:
            maximum_common = number_common
            best_candidate = candidate_id

        elif number_common == maximum_common and number_common > 0:
            if best_candidate is None or candidate_id < best_candidate:
                best_candidate = candidate_id

    return best_candidate

    


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    
    count = 0

    for user in network:
        if len(user[1]) >= k:
            count += 1

    return count
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    maximum = 0

    for user in network:
        if len(user[1]) > maximum:
            maximum = len(user[1])

    return maximum
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    
    maximum = maximum_num_friends(network)

    for user in network:
        if len(user[1]) == maximum:
            max_friends.append(user[0])

    return    max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    if len(network) == 0:
        return 0.0

    total_friends = 0

    for user in network:
        total_friends += len(user[1])

    return total_friends / len(network)

    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    total_users = len(network)

    for user in network:
        if len(user[1]) == total_users - 1:
            return True

    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''

    while True:
        try:
            user_id = int(input("Enter an integer for a user ID: "))
        except ValueError:
            print("That was not an integer. Please try again.")
            continue

        if _find_user_index(network, user_id) == -1:
            print("That user ID does not exist. Try again.")
        else:
            return user_id
    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
