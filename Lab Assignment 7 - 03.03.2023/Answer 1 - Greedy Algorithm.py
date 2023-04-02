# Solution to Question 1: Greedy Algorithm

# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("output.txt", "w")
except:
    pass


# ---------------------- Code Starts Here ----------------------#

import random

# Create a list of 10 jobs with random start times and durations
jobs = []
for i in range(10):
    start_time = random.randint(0, 9)
    duration = random.randint(2, 6)
    finish_time = start_time + duration
    jobs.append((start_time, finish_time))

# Sort the jobs in ascending order by their finish time
jobs.sort(key=lambda x: x[1])

# Function to check if a job conflicts with the current to-do list


def has_conflict(job, to_do_list):
    for scheduled_job in to_do_list:
        if job[0] < scheduled_job[1] and job[1] > scheduled_job[0]:
            return True
    return False

# Function to count the number of conflicts a job has with other jobs


def count_conflicts(job, jobs):
    conflicts = 0
    for other_job in jobs:
        if job != other_job and job[0] < other_job[1] and job[1] > other_job[0]:
            conflicts += 1
    return conflicts


# Perform the greedy algorithm to generate a to-do list of jobs to schedule
to_do_list = []
for job in jobs:
    if not has_conflict(job, to_do_list):
        to_do_list.append(job)

# Output the to-do list
print("To-do list:", to_do_list)

# Output the number of conflicts for each job
for job in jobs:
    print(f"Job {job} has {count_conflicts(job, jobs)} conflicts")
