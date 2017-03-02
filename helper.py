from datetime import timedelta


def parse_date(string):
    h, m, s = string.split('(')[0].split(':')
    return timedelta(hours=int(h), minutes=int(m), seconds=int(s))
