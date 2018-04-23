import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('insert into Tracks (title, plays) values (?, ?)',
            ('Thunderstruck', 20))

cur.execute('insert into Tracks (title, plays) values (?, ?)',
            ('My Way', 15))

conn.commit()

print('Tracks: ')
cur.execute('select title, plays from Tracks')
for row in cur:
    print(row)

cur.execute('Delete from Tracks where plays < 100')
conn.commit()
cur.close()
