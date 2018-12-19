import timeit
import re

#region Problem 1
#
# The instructions specify a series of steps and requirements about which steps must be finished before others
# can begin (your puzzle input). Each step is designated by a single letter. For example, suppose you have the
# following instructions:
# 
# "Step C must be finished before step A can begin.
# "Step C must be finished before step F can begin.
# "Step A must be finished before step B can begin.
# "Step A must be finished before step D can begin.
# "Step B must be finished before step E can begin.
# "Step D must be finished before step E can begin.
# "Step F must be finished before step E can begin.
# 
# Visually, these requirements look like this:
# 
# 
#   -->A--->B--
#  /    \      \
# C      -->D----->E
#  \           /
#   ---->F-----
# 
# Your first goal is to determine the order in which the steps should be completed. If more than one step is
# ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:
# 
# Only C is available, and so it is done first.
# Next, both A and F are available. A is first alphabetically, so it is done next.
# Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of the three.
# After that, only D and F are available. E is not available because only some of its prerequisites are complete.
# Therefore, D is completed next.
# F is the only choice, so it is done next.
# Finally, E is completed.
# 
# "So, in this example, the correct order is CABDFE.
#
#endregion

### Test cases:

p1_a = ([
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
    ], "CABDFE")

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:

# Passes test case fails on official data. Crap answer
def p1answer1(ls, *args, **kwargs):
    order = ""
    counter = 0
    for instruction in ls:
        counter += 1
        words = re.split(" ", instruction)
        (one, two) = (words[1], words[7])
        if counter == 1:
            order = "{0}{1}".format(one,two)
        elif (one not in order) and (two not in order):
            order = "{0}{1}{2}".format(order,one,two)
        elif (two in order) and (one not in order):
            order = re.sub(two, "{0}{1}".format(one, two), order)
        # Sorting all after here ruins the order and is flawed logic
        else:
            ones_index = order.index(one)
            order = re.sub(one, "{0}{1}".format(one,two), order)
            order = "{0}{1}".format(order[:ones_index+1], "".join(sorted(order[ones_index+1:])))
            order = re.sub(r'(\w)\1', "", order)
    return(order)

# Ahhh... maybe...
def p1answer2(ls, *args, **kwargs):

    # Function to build instruction dict with prerequisites and conditions.
    def build_instr_dict(ls, forward=True):

        if not forward:
            ls.reverse()

        parsed_instructions = []
        for instruction in ls:
            words = re.split(" ", instruction)
            (one,two) = words[1], words[7]

            if not forward:
                parsed_instructions.append((two, one))

            else:
                parsed_instructions.append((one,two))

        all_pieces = list(dict.fromkeys("".join([i+j for(i,j) in parsed_instructions])))

        instr_order = {k:[] for k in all_pieces}

        for (one,two) in parsed_instructions:
            instr_order[one].append(two)

        for (k,v) in instr_order.items():
            instr_order[k] = sorted(list(set(v)))

        return instr_order, all_pieces

    instr_order_forward, all_pieces = build_instr_dict(ls)
    instr_order_reversed, _ = build_instr_dict(ls, forward=False)

    # Build instruction dictionary.
    prereqs_conditions = {}

    for value in instr_order_forward:
        prereqs_conditions[value] = [instr_order_reversed[value], instr_order_forward[value]]

    # Decide where to start, official input data starts with a tie...
    starting_points = sorted([k for (k,v) in prereqs_conditions.items() if len(v[0]) == 0])

    first_pop = starting_points[0]

    answer_string = ""

    # Loop to remove ready items and then find next available item.
    while len(prereqs_conditions) > 1:
        answer_string = answer_string + first_pop
        enabled_guys = prereqs_conditions[first_pop][1]

        prereqs_conditions.pop(first_pop)

        for (k,v) in prereqs_conditions.items():
            if k in enabled_guys:
                prereqs_conditions[k][0].remove(first_pop)

        enabled = []

        for (k,v) in prereqs_conditions.items():
            if not v[0]:
                enabled.append(k)

        enabled = sorted(enabled)

        first_pop = enabled[0]

    # Deal with last item left in queue
    answer_string = answer_string + "".join(prereqs_conditions.keys())

    return answer_string

p1answers = {
    "p1answer1":p1answer1,
    "p1answer2":p1answer2,
}

### Problem 1 tests:

for (answer_name, answer) in p1answers.items():
    for test_name, (test,sol) in p1_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 1] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 1] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 1] Test: PASS, Function: p1answer1 Input: ['Step C must be finished before step A can begin.', 'Step C must be finished before step F can begin.', 'Step A must be finished before step B can begin.', 'Step A must be finished before step D can begin.', 'Step B must be finished before step E can begin.', 'Step D must be finished before step E can begin.', 'Step F must be finished before step E can begin.']
# [Problem 1] Test: PASS, Function: p1answer2 Input: ['Step F must be finished before step E can begin.', 'Step D must be finished before step E can begin.', 'Step B must be finished before step E can begin.', 'Step A must be finished before step D can begin.', 'Step A must be finished before step B can begin.', 'Step C must be finished before step F can begin.', 'Step C must be finished before step A can begin.']

#region Problem 2
#
# As you're about to begin construction, four of the Elves offer to help. "The sun will set soon; it'll go faster
# if we work together." Now, you need to account for multiple people working on steps simultaneously. If multiple
# steps are available, workers should still begin them in alphabetical order.
#
# Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and so on. So, step A takes
# 60+1=61 seconds, while step Z takes 60+26=86 seconds. No time is required between steps.
#
# To simplify things for the example, however, suppose you only have help from one Elf (a total of two workers) and
# that each step takes 60 fewer seconds (so that step A takes 1 second and step Z takes 26 seconds). Then, using the
# same instructions as above, this is how each second would be spent:
#
# Second   Worker 1   Worker 2   Done
#    0        C          .
#    1        C          .
#    2        C          .
#    3        A          F       C
#    4        B          F       CA
#    5        B          F       CA
#    6        D          F       CAB
#    7        D          F       CAB
#    8        D          F       CAB
#    9        D          .       CABF
#   10        E          .       CABFD
#   11        E          .       CABFD
#   12        E          .       CABFD
#   13        E          .       CABFD
#   14        E          .       CABFD
#   15        .          .       CABFDE
#
# Each row represents one second of time. The Second column identifies how many seconds have passed as of the
# beginning of that second. Each worker column shows the step that worker is currently doing (or . if they are idle).
# The Done column shows completed steps.
#
# Note that the order of the steps has changed; this is because steps now take time to finish and multiple workers
# can begin multiple steps simultaneously.
#
# In this example, it would take 15 seconds for two workers to complete these steps.
#
#endregion

### Test cases:

p2_a = ([
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
    ], 15)


p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1(ls, how_many_workers=2, time_offset=0, *args, **kwargs):

    # Function to build instruction dict with prerequisites and conditions.
    def build_instr_dict(ls, forward=True):

        if not forward:
            ls.reverse()

        parsed_instructions = []
        for instruction in ls:
            words = re.split(" ", instruction)
            (one,two) = words[1], words[7]

            if not forward:
                parsed_instructions.append((two, one))

            else:
                parsed_instructions.append((one,two))

        all_pieces = list(dict.fromkeys("".join([i+j for(i,j) in parsed_instructions])))

        instr_order = {k:[] for k in all_pieces}

        for (one,two) in parsed_instructions:
            instr_order[one].append(two)

        for (k,v) in instr_order.items():
            instr_order[k] = sorted(list(set(v)))

        return instr_order, all_pieces

    instr_order_forward, all_pieces = build_instr_dict(ls)
    instr_order_reversed, _ = build_instr_dict(ls, forward=False)

    # Build instruction dictionary.
    prereqs_conditions = {}

    for value in instr_order_forward:
        prereqs_conditions[value] = [instr_order_reversed[value], instr_order_forward[value]]

    for i in prereqs_conditions.items():
        print(i)

    # Find time per job key.
    alphabet = [chr(97+i).upper() for i in range(26)]
    time_per_letter = {k:(v+time_offset) for (k,v) in zip(alphabet,range(1,27))}

    # Decide where to start.
    starting_points = sorted([k for (k,v) in prereqs_conditions.items() if len(v[0]) == 0])

    # Generate worker queues.
    all_queues = []
    for i in range(how_many_workers):
        all_queues.append((None, None))

    # Current job.
    current_jobs = starting_points

    # Current time.
    current_time = 0

    # All jobs completed master list.
    completed_master = []

    # Fill worker queues with first available jobs.
    for (worker_id, job_key) in enumerate(current_jobs):
        this_jobs_time = time_per_letter[job_key]
        all_queues[worker_id] = ((this_jobs_time + current_time), job_key)

    print("[INFO] beginning worker queue status: {0}".format(all_queues))

    enabled_tasks = []

    # While there is a job key in the queue.
    while len([i[0] for i in all_queues if i == (None, None)]) < how_many_workers:

        # Increment timekeeper.
        current_time += 1

        # Check for jobs that should be done at this point in time and add to completed queue.
        for (idx,(task_time, job_key)) in enumerate(all_queues):
            if task_time == current_time:
                completed_master.append(job_key)
                all_pieces.remove(job_key)

        print("[INFO] all completed jobs: {0}".format(completed_master))
        print("[INFO] this iterations worker queue status: {0}".format(all_queues))

        # Remove completed jobs from any worker queue where they are present.
        for completed_job_key in completed_master:
            for (idx, (task_time, job_key)) in enumerate(all_queues):
                if completed_job_key == job_key:
                    all_queues[idx] = (None, None)

        print("[INFO] worker queue with completed tasks removed: {0}".format(all_queues))

        # Remove completed jobs from prereq_conditions dict.
        for job_key in completed_master:
            if job_key in prereqs_conditions:
                prereqs_conditions.pop(job_key)
            if job_key in enabled_tasks:
                enabled_tasks.remove(job_key)

        # Check to see which jobs have now become enabled with this iteration's completed tasks.
        for job_key in completed_master:
            for (k, v) in prereqs_conditions.items():
                if job_key in v[0]:
                    prereqs_conditions[k][0].remove(job_key)
                    print("[INFO] removed {0} from {1}'s prereqs".format(job_key, k))

        for (k, v) in prereqs_conditions.items():
            if not v[0] and k not in enabled_tasks:
                enabled_tasks.append(k)

        # Find empty spots and what is in queue.
        empty_spots = [idx for (idx, i) in enumerate(all_queues) if i == (None, None)]
        job_keys_currently_in_queue = [i[1] for i in all_queues if i[1] != None]

        # Generate expected completion times for available tasks.
        enabled_time_log = []

        for job_key in enabled_tasks:
            if job_key not in job_keys_currently_in_queue:
                expected_completion_time = time_per_letter[job_key] + current_time
                enabled_time_log.append((expected_completion_time, job_key))

        print("[INFO] enabled time log: {0}".format(enabled_time_log))

        # Fill empty spots.
        for ((expected_completion_time, enabled_job_key), empty) in zip(enabled_time_log, empty_spots):
            if (enabled_job_key not in job_keys_currently_in_queue) and (enabled_job_key not in completed_master):
                all_queues[empty] = (expected_completion_time, enabled_job_key)
                enabled_tasks.remove(enabled_job_key)
                print("[INFO] removed: {0}".format(enabled_job_key))

        print("[INFO] worker queue after refill: {0}".format(all_queues))

        # Get jobs in queue at iteration's end.
        job_keys_in_queue_at_loop_end = [i[1] for i in all_queues if i[1] != None]

        print("[INFO] jobs in queue at iterations end: {0}".format(job_keys_in_queue_at_loop_end))
        print("[INFO] jobs left to complete: {0}".format(all_pieces))
        print("[INFO] current time: {0}".format(current_time))

    return current_time

def p2answer2(*args, **kwargs):
    pass

p2answers = {
    "p2answer1":p2answer1,
    "p2answer2":p2answer2,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 2] Test: PASS, Function: p2answer1 Input: ['Step F must be finished before step E can begin.', 'Step D must be finished before step E can begin.', 'Step B must be finished before step E can begin.', 'Step A must be finished before step D can begin.', 'Step A must be finished before step B can begin.', 'Step C must be finished before step F can begin.', 'Step C must be finished before step A can begin.']
# [Problem 2] Test: FAIL, Function: p2answer2 Input: ['Step F must be finished before step E can begin.', 'Step D must be finished before step E can begin.', 'Step B must be finished before step E can begin.', 'Step A must be finished before step D can begin.', 'Step A must be finished before step B can begin.', 'Step C must be finished before step F can begin.', 'Step C must be finished before step A can begin.']


####### Official Input Data #######

### CSV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_07_input.txt"

with open(file_path) as my_file:
    data = my_file.read().splitlines()

# Data was the same for problem one and two for this day.


####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1, testing=False, *args, **kwargs):
    for (answer_name, answer) in answer_dict.items():
        if not testing:
            time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        else:
            time = timeit.timeit("{0}(data, testing=False)".format(answer_name), globals=globals(), number=loops)

        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

# [Problem 1] Time: 0.00075 seconds on 1 loops, Function: p1answer1
# [Problem 1] Time: 0.00039 seconds on 1 loops, Function: p1answer2
# [Problem 2] Time: 0.00833 seconds on 1 loops, Function: p2answer1
# [Problem 2] Time: 0.0 seconds on 1 loops, Function: p2answer2