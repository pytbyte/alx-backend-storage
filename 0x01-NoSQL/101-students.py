def top_students(mongo_collection):
    '''Returns all students in a collection sorted by average score.
    '''
    # Define the aggregation pipeline
    aggregation_pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score',
                },
            },
        },
        {
            '$sort': {'averageScore': -1},
        },
    ]

    # Execute the aggregation pipeline
    top_students_cursor = mongo_collection.aggregate(aggregation_pipeline)

    # Convert the cursor to a list and return the result
    top_students_list = list(top_students_cursor)
    return top_students_list
