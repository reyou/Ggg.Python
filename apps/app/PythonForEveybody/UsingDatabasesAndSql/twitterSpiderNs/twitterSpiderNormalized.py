import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('''create table if not exists People 
            (id integer primary key, name text unique, retrieved integer)''')
cur.execute('''create table if not exists Follows
            (from_id integer, to_id integer, unique(from_id, to_id))''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit, or press Enter to fetch account '
                 'from Database: ')
    if (acct == 'quit'):
        break;
    if (len(acct) < 1):
        cur.execute('Select id, name from People where retrieved = 0 limit 1')
        try:
            (id, acct) = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        cur.execute('select id from People where name = ? limit 1', (acct,))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('''insert or ignore into people 
            (name, retrieved) values (?, 0)''', (acct,))
            conn.commit()
            if (cur.rowcount != 1):
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': 100})
    print('Retrieving account', acct)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Failed to Retrieve', err)
        break

    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except:
        print('Unable to parse json')
        print(data)
        break

    # Debugging
    # print(json.dumps(js, indent=4))

    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    cur.execute('update People set retrieved=1 where name = ?', (acct,))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('Select id from People where name = ? limit 1', (friend,))
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''insert or ignore into People (name, retrieved) 
            values (?, 0)''', (friend,))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid
            countnew = countnew + 1
        cur.execute('''insert or ignore into Follows (from_id, to_id) 
        values (?, ?)''', (id, friend_id))

    print('New accounts=', countnew, ' revisited=', countold)
    print('Remaining', headers['x-rate-limit-remaining'])
    conn.commit()
cur.close()
