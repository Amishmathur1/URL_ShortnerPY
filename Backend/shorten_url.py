'''
Helper File To Store the URL Link into the DataBase and Generate the Base62 Encoded Code and again
store it into the database table
'''

def shortening_logic (id):
    # Performing Base62 on the provided id number
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    short_code = ''

    while id > 0:
        ind = id % 62
        short_code += s[ind]
        id = id // 62

    return short_code[::-1]
