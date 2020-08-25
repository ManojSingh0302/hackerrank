#!/bin/python3
def countMeetings(firstDay, lastDay):
    # set containing all unique days possible
    days_full_set = set(list(range(min(firstDay), max(lastDay) + 1)))

    # count of possible meetings
    mtng_cnt = 0

    # assuming all the investors have a defined firstDay and lastDay
    # that is, len(firstDay) = len(lastDay)
    # iterating through investors - one at a time
    for i in range(len(firstDay)):

        # if there are no meeting days left, break out of the loop
        if not bool(days_full_set):
            break

        # check for the day availability starting from the first day for the current investor
        for val in range(firstDay[i], lastDay[i] + 1):
            if val in days_full_set:
                days_full_set.remove(val)
                mtng_cnt += 1
                break

    # return the consolidated meeting count
    return mtng_cnt

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #firstDay_count = int(input().strip())
    firstDay_count = 4

    firstDay = [1,1,2,2]
    #firstDay = [1,2,1,2,2]

    # for _ in range(firstDay_count):
    #     firstDay_item = int(input().strip())
    #     firstDay.append(firstDay_item)

    #lastDay_count = int(input().strip())
    lastDay_count = 4

    lastDay = [2,2,4,4]
    #lastDay = [3,2,1,3,3]

    # for _ in range(lastDay_count):
    #     lastDay_item = int(input().strip())
    #     lastDay.append(lastDay_item)

    result = countMeetings(firstDay, lastDay)
    print('results',result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
