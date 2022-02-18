from enum import Enum
from sys import argv


class CronField(Enum):
    MINUTE = 0
    HOUR = 1
    DAY = 2
    MONTH = 3
    WEEK_DAY = 4


# Possible ranges for the different cron fields
CRON_FIELD_VALUES_MAP = {
    CronField.MINUTE: [i for i in range(0, 60)],
    CronField.HOUR: [i for i in range(0, 24)],
    CronField.DAY: [i for i in range(1, 32)],
    CronField.MONTH: [i for i in range(1, 13)],
    CronField.WEEK_DAY: [i for i in range(0, 7)]
}


def parse_cron_field(input: str, field: CronField) -> list:
    """
    Parses the provided input string as a cron field parameter

    :param input: string to parse
    :param field: target cron field
    :return: List of extracted int time periods for the field provided
    """

    # Return all possible values for "*"
    if input == '*':
        return CRON_FIELD_VALUES_MAP.get(field)

    # Process lists
    if ',' in input:
        return list(map(int, input.split(',')))

    # Process ranges
    if '-' in input:
        range_from, range_to = input.split('-')
        return list(range(int(range_from), int(range_to) + 1))

    # Process intervals
    if '/' in input:
        # Return all values giving zero reminder
        _, interval = input.split('/')
        return list(filter(lambda x: x % int(interval) == 0, CRON_FIELD_VALUES_MAP.get(field)))

    return [int(input)]


def print_cron_field(input: str, field: CronField) -> str:
    return " ".join(map(str, parse_cron_field(input, field)))


def parse_cron(cron_str):
    """
    INPUT: cron_str = The input string containing the entire cron string from
    the user.
    OUTPUT: A formatted string containing the minute, hour, day, month,
    weekday and command that will run.
    """
    try:
        minute, hour, day, month, week_day, command = cron_str.split(' ')
    except ValueError:
        raise Exception('Not enough parameters passed.')

    return '\n'.join([
        f'minute        {print_cron_field(minute, CronField.MINUTE)}',
        f'hour          {print_cron_field(hour, CronField.HOUR)}',
        f'day of month  {print_cron_field(day, CronField.DAY)}',
        f'month         {print_cron_field(month, CronField.MONTH)}',
        f'day of week   {print_cron_field(week_day, CronField.WEEK_DAY)}',
        f'command       {command}'
    ])


def main():
    print(parse_cron(argv[1]))


if __name__ == '__main__':
    main()