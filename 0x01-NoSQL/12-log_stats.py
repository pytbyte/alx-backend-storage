#!/usr/bin/env python3
'''print_nginx_request_logs module.
'''
from pymongo import MongoClient


def print_nginx_request_logs():
    '''Prints stats about Nginx request logs.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    all_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in all_methods:
        requsts_ = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, requsts_))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


if __name__ == '__main__':
    print_nginx_request_logs()
