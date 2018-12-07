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

    max_sleep = -1
    sleepiest_guard = -1
    sleepiest_minute = -1

    for guard_id in guard_sleep_count.keys():
        if guard_sleep_count[guard_id]:
            max_minute = max(guard_sleep_count[guard_id], key=lambda key: guard_sleep_count[guard_id][key])
            if max_sleep < guard_sleep_count[guard_id][max_minute]:
                max_sleep = guard_sleep_count[guard_id][max_minute]
                sleepiest_guard = guard_id
                sleepiest_minute = max_minute

    print(sleepiest_guard * sleepiest_minute)


if __name__ == '__main__':
    main()
