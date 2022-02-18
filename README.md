# Deliveroo Cron Parser

## Running the Code

After cloning the project, just run the following command to get your cron
string parsed. This is assuming you have python 3 installed:

`python cron-parser.py "SOME_CRON_STRING_TO_PARSE"`

For example:

`python cron-parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"`

For this input, you should then get the following output:

```
minute        0 15 30 45
hour          0
day of month  1 15 
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

### Future Development (based on https://en.wikipedia.org/wiki/Cron)
- Support text formats for month and day of week (JAN–DEC and MON-SUN)
- Support special characters (?, L, #)
- Add validations and smooth errors handling
- Take into account different number of days in different months (31 day is returned now for all months)
- Implement tests