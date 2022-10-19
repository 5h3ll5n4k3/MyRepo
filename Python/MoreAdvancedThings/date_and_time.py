from datetime import datetime as dt

print(dt.now())

"""
%Y - four digit year
%M - two digit month
%d - two digit day
%H -twentyfour hour time
%M - two digit minute
%S - two digit second
"""

now = dt.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

def ts():
    dt.now().strftime('%Y-%m-%d %H:%M:%S')

print(ts())                                    