#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient

def log_stats():
    '''Prints stats about Nginx logs in MongoDB.
    '''
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')
        nginx_collection = client.logs.nginx

        # Display total logs count
        total_logs_count = nginx_collection.count_documents({})
        print(f'{total_logs_count} logs')

        # Display request methods count
        print('Methods:')
        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
        for method in methods:
            req_count = nginx_collection.count_documents({'method': method})
            print(f'\tmethod {method}: {req_count}')

        # Display status checks count
        status_checks_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
        print(f'{status_checks_count} status check')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    log_stats()
