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

    # tickets is a list of Ticket objects
    # iterate through it and insert into hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # initialize empty list 
    trip = []

    # find origin
    dest = hash_table_retrieve(hashtable, 'NONE')

    while dest is not 'NONE':
        trip.append(dest)
        dest = hash_table_retrieve(hashtable, dest)

    return trip
