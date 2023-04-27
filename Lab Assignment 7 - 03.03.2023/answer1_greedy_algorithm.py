# Solution to Question 1: Greedy Algorithm

# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""

# ---I/O from file---#
import sys
import random

try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as __:
    pass


# ---------------------- Code Starts Here ----------------------#

jobListType = list[tuple[int, int]]
jobType = tuple[int, int]


def has_conflict(job: jobType, to_do_list: jobListType) -> bool:
    """a function to check if a job conflicts with the current to-do list

    Args:
        job (tuple[int, int]): the job to be checked\n
        to_do_list (list[tuple[int, int]]): the current to-do list

    Returns:
        bool: True if the job conflicts with the current to-do list, False otherwise
    """
    for scheduled_job in to_do_list:
        if job[0] < scheduled_job[1] and job[1] > scheduled_job[0]:
            return True
    return False


# Function to count the number of conflicts a job has with other jobs
def count_conflicts(job: jobType, jobs: jobListType) -> int:
    """a function to count the number of conflicts a job has with other jobs

    Args:
        job (tuple[int,int]): the job to be checked\n
        jobs (list[tuple[int,int]]): the list of jobs to be checked against

    Returns:
        int: number of conflicts the job has with other jobs
    """
    conflicts = 0
    for other_job in jobs:
        if job != other_job and job[0] < other_job[1] and job[1] > other_job[0]:
            conflicts += 1
    return conflicts


# Create a list of 10 jobs with random start times and durations
tasks: jobListType = []
for i in range(10):
    start_time = random.randint(0, 9)
    duration = random.randint(2, 6)
    finish_time = start_time + duration
    tasks.append((start_time, finish_time))
print(f"The input list: {tasks}")

# Sort the jobs in ascending order by their finish time
tasks.sort(key=lambda x: x[1])

# Perform the greedy algorithm to generate a to-do list of jobs to schedule
to_do: jobListType = []
for task in tasks:
    if not has_conflict(task, to_do):
        to_do.append(task)

# Output the to-do list
print("To-do list:", to_do)

# Output the number of conflicts for each job
print("Number of conflicts for each job:")
for task in tasks:
    print(f"Job {task} has {count_conflicts(task, to_do)} conflicts")

# Complexity Analysis of above solution:
# Time Complexity: O(X*log(N))
# where X is the difference between maximum and minimum times and N is the number of jobs
# Space Complexity: O(N^2)
