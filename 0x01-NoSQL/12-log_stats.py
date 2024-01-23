#!/usr/bin/env python3
'''print_nginx_request_logs module.
'''
from pymongo import MongoClient

def print_nginx_request_logs():
    '''Prints stats about Nginx request logs.
    '''
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Print total logs count
    total_logs_count = nginx_collection.count_documents({})
    print(f'{total_logs_count} logs')

    # Print request methods count
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {req_count}')

    # Print status checks count
    status_checks_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{status_checks_count} status check')

if __name__ == '__main__':
    print_nginx_request_logs()
