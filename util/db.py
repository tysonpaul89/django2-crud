def to_dict(cursor, result):
    """
    Converts raw sql result which is a tuple into a dictionary
    example:
        from django.db import connection
        from app.util.db import to_dict

        sql = 'SELECT id, name FROM user'
        cursor = connection.cursor()

        result = cursor.execute(sql)
        # Output: [(1, 'Test'), (1, 'Foo')]

        data = to_dict(cursor, result)
        # Output: [{'id': 1, 'name': 'Test'}, {'id': 2, 'name': 'Foo'}]

    """
    data = None
    if (cursor and result):
        columns = tuple([c[0] for c in cursor.description])
        if isinstance(result, tuple):
            data = dict(zip(columns, result))
        elif isinstance(result, list):
            data = []
            for row in result:
                data.append(dict(zip(columns, row)))
    # Returns final data
    return data
