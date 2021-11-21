'''
The datetime module supplies classes for manipulating dates and times.
Available Types
  - date
  - time
  - datetime
  - timedelta
  - timezone

  The objects type date, time, datime and timezone:
    - are immutable
    - are hashable (can be used as dictionary keys)
'''

from datetime import datetime, date, timedelta

#date
today = date.today()
print('# date')
print('Type:', type(today))
print('today:', today)
print('year:', today.year)
print('month:', today.month)
print('day:', today.day)
print('weekday():', today.weekday()) #(0=Monday,...6=Sunday)

my_birthday = date(1972, 3, 25)
print('my_birthday:', my_birthday)
print(f'{my_birthday.day}/{my_birthday.month}/{my_birthday.year}')


#datetime
print('\n# datime')
now = datetime.now()
print('Type:', type(now))
print(now)
print(now.hour)
print(now.minute)
print(now.second)

# Formating datetime using strftime function
'''
Directive/Meaning
%a	Weekday as locale’s abbreviated name.
%A	Weekday as locale’s full name.
%w	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%d	Day of the month as a zero-padded decimal number.
%b	Month as locale’s abbreviated name.
%B	Month as locale’s full name.
%m	Month as a zero-padded decimal number.
%y	Year without century as a zero-padded decimal number.
%Y	Year with century as a decimal number.
%H	Hour (24-hour clock) as a zero-padded decimal number.
%I	Hour (12-hour clock) as a zero-padded decimal number.
%p	Locale’s equivalent of either AM or PM.
%M	Minute as a zero-padded decimal number.
%S	Second as a zero-padded decimal number.
%f	Microsecond as a decimal number, zero-padded on the left.
%z	UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
%Z	Time zone name (empty string if the object is naive).
%j	Day of the year as a zero-padded decimal number.
%U	Week number of the year (Sunday as the first day of the week) as a zero padded decimal number.
%W	Week number of the year (Monday as the first day of the week) as a decimal number.
%c	Locale’s appropriate date and time representation.
%x	Locale’s appropriate date representation.
%X	Locale’s appropriate time representation.
%%	A literal '%' character.

'''
print('\n# Formatting string')
print(now.strftime('%A, %B, %Y'))
print(now.strftime('%Y%m%d'))
print(now.strftime('%Y/%m/%d'))
print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))

# Converting strings to datetime using strptime function
print('\n# Converting string')
date_str = '25/03/1972 14:00'
my_birth = datetime.strptime(date_str, '%d/%m/%Y %H:%M')
print(my_birth)

# timedelta
print('\n# Timedelta')
print(today)
in_15_days = today + timedelta(days=15)
print(in_15_days)
_15_days_ago = today - timedelta(days=15)
print(_15_days_ago)
in_10_hours = now + timedelta(hours=10)
print(in_10_hours)
