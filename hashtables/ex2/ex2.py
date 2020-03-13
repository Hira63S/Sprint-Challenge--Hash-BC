#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        # source represents the starting airport
        # destination: next airport along the trip

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length   # empty list
    route = [None] * (length - 1)   # go backwards
    # I can't believe you scrambled all the tickets in the midst of Coronavirus epidemic
    # let's start with insert the tickets into the hashtable
    # we are going to hash the keys so that the source is the key and destination
    # is the value
    # lets start by inserting the tickets in the hash hash_table
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    # update the status of traveling
    current_location = "NONE"

    for i in range(length-1):
        route[i] = hash_table_retrieve(hashtable, current_location)
        # update the current_location
        current_location = route[i]

    return route
