import random
count = 5
set_size = 5
stable = "standing"
normal_activities = ["SIT&UP", "LIE&UP", "WALK", "BEND&UP", "BF4", "FF6", "RF2", "LF2"]
fallings = ["BF1", "BF2", "BF3", "FF1", "FF2", "FF3", "FF4", "FF5", "RF1", "LF1"]
stable_duration = 10
activity_duration = 5


def generate_activity_set(set_size, normal_activities, test_set):
    while True:
        activity = random.choice(normal_activities)
        test_set.add(activity)
        if len(test_set) == set_size:
            break
    return test_set


def generate_activity_sets(set_size, normal_activities, fallings, count):
    normal_tests = set()
    falling_tests = set()
    while True:
        normal_test_set = generate_activity_set(set_size, normal_activities, set())
        normal_tests.add(tuple(normal_test_set))
        falling_test_set = generate_activity_set(set_size, normal_activities, set([random.choice(fallings)]))
        falling_tests.add(tuple(falling_test_set))
        if len(normal_tests) == count and len(falling_tests) == count:
            break
    return normal_tests, falling_tests


def generate_final_sets(test_sets, stable):
    final_sets = []
    for test_set in test_sets:
        l = list(test_set)
        random.shuffle(l)
        stables = [stable] * 5
        final_set = []
        map(lambda item: final_set.extend(item), zip(stables, l))
        final_sets.append(final_set)
    return final_sets


def format_test_set(test_set, activity_duration, stable_duration, stable):
    result = []
    time = 0
    for activity in test_set:
        if activity == stable:
            duration = stable_duration
        else:
            duration = activity_duration
        item = "%s(%s-%ss)" % (activity, time, time + duration)
        result.append(item)
        time += duration
    return " ".join(result)



normal_tests, falling_tests = generate_activity_sets(set_size, normal_activities, fallings, count)
final_normal_tests = generate_final_sets(normal_tests, stable)
final_falling_tests = generate_final_sets(falling_tests, stable)

print("normal activity test sets are:")
for (index, test) in enumerate(final_normal_tests):
    print("test %s: %s" % (index, format_test_set(test, activity_duration, stable_duration, stable)))


print("falling activity test sets are:")
for (index, test) in enumerate(final_falling_tests):
    print("test %s: %s" % (index, format_test_set(test, activity_duration, stable_duration, stable)))
