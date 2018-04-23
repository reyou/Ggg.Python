from datetime import tzinfo, timedelta, datetime


class TZ(tzinfo):
    def utcoffset(self, dt):
        return timedelta(minutes=-399)


# class datetime(args, kwargs)
"""Return the time formatted according to ISO.
The full format looks like 'YYYY-MM-DD HH:MM:SS.mmmmmm'. 
By default, the fractional part is omitted if self.microsecond == 0."""
res = datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
print("\n res:")
print(res)
