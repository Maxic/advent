import re
from datetime import datetime


def main():
    with open("sorted_input.txt", "r+") as file:
        logs = file.readlines()

    guard_sleep_count = {}
    current_guard = 0

    # get minutes slept for each guard
    for log in logs:

        log_match = re.match(r'\[(.*)\] (.*)', log)
        message = log_match.group(2)
        date = datetime.strptime(log_match.group(1), '%Y-%m-%d %H:%M')

        if 'Guard' in message:
            current_guard = int(re.match(r'(.*) \#(.*) (.*) (.*)', message).group(2))
            sleep_start = 0
            if current_guard not in guard_sleep_count:
                guard_sleep_count[current_guard] = {}
        elif 'falls' in message:
            sleep_start = date.minute
        elif 'wakes' in message:
            for i in range(sleep_start, date.minute):
                if i not in guard_sleep_count[current_guard]:
                    guard_sleep_count[current_guard][i] = 1
                else:
                    guard_sleep_count[current_guard][i] += 1

    # Check which guard slept the most
    sleepiest_guard = -1
    max_minutes_slept = -1

    for guard_id in guard_sleep_count.keys():
        minutes_slept = sum(guard_sleep_count[guard_id].values())
        if minutes_slept > max_minutes_slept:
            max_minutes_slept = minutes_slept
            sleepiest_guard = guard_id

    # Check which minute he sleeps the most
    sleepiest_minute = max(guard_sleep_count[sleepiest_guard], key=lambda key: guard_sleep_count[sleepiest_guard][key])

    print(sleepiest_guard * sleepiest_minute)


if __name__ == '__main__':
    main()
