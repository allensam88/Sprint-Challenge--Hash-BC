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


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Initialize the hash table with all ticket nodes
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Initialize the starting destination to be the source origin of 'NONE'
    destination = 'NONE'

    # Loop through indices
    for index in range(length):
        # find the next location using the destination as a key
        destination = hash_table_retrieve(hashtable, destination)
        # add the location to the route list
        route[index] = destination

    # return the route, but chop off the last destination of 'NONE'
    return route[:-1]
