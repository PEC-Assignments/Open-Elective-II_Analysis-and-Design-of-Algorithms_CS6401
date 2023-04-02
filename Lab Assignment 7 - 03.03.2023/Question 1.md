# Question 1

As you saw in class, greedy algorithms are often used when we have an optimization problem involving a series of choices. In today’s lab, we will explore one such example problem. We would like to maximize the number of jobs that can be done over a period of time.
If we are given, say, 10 jobs, each with its start time and finish time, we want to select the largest possible subset of these jobs in such a way that no two jobs in the subset overlap in time. In other words, we can only work on one job at any one time. For simplicity, assume that time is measured by whole numbers. The smallest interval of time we will measure will be between consecutive integers. It’s okay for one job to begin at the same instant another job finishes.
We’re going to solve this problem using a greedy algorithm, as we did in class. Here is the pseudocode:

1. Sort the jobs ascending by finish time.
2. Let W be our chosen subset of jobs to-do, and initialize it to be empty.
3. for j = 1 to n
   if job j does not overlap in time with W
   add j to W

To test this algorithm, we need an initial set of candidate jobs. So, we’ll create a collection of 10 jobs. Their start and finish times will be random. For example, the start time for each job can be a random integer value from 0 to 9 inclusive. And we can set the duration of each job to be a random integer from 2 to 6 inclusive. But these constants are just implementation parameters that have no effect on the optimality of the algorithm, and we can tweak these numbers later if necessary.

Your script should contain:
Attributes for start time, duration of job, and how many other jobs it conflicts with
• Function that sets attributes
• Methods for start time, duration, finish time, number of conflicts.
Method for the number of conflicts (because at the time of creation we won’t know this value).
• Methods to give the start time, ending time and the number of conflicts.

Main Script should do the following:
Create a list of 10 jobs.
• Perform the greedy algorithm above to generate a “to-do” subset list of jobs to schedule.
• Output the to-do list.
• Functions to determine: o whether a job has a conflict with an existing to-do list o for each job, the number of conflicts it has with the other jobs in the entire list.
