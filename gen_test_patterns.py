import random
import json
count = 40
set_size = 5
stable = "standing"
normal_activities = ["Sit&Up", "Lie&Up", "Walk", "Bend&Up", "BF-recovery", "FF-recovery", "RF-recovery", "LF-recovery"]
fallings = ["BF-Sitting", "BF-Lying", "BF3-Lateral", "FF-Knee", "FF-ArmProtection", "FF-LyingFlat", "FF-LateralRight", "FF-LateralLeft", "RF-Lying", "LF-Lying"]
stable_duration = 10
activity_duration = 10


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
        time = 0
        l = []
        for item in final_set:
            duration = stable_duration if item == stable else activity_duration
            item = [item, time, time + duration]
            l.append(item)
            time += duration
        final_sets.append(l)

    return final_sets



normal_tests, falling_tests = generate_activity_sets(set_size, normal_activities, fallings, count)
final_normal_tests = generate_final_sets(normal_tests, stable)
final_falling_tests = generate_final_sets(falling_tests, stable)

f1 = open("normal_activity.txt", "w")
f2 = open("normal_activity.json", "w")
print("normal activity test sets are:")
for (index, test) in enumerate(final_normal_tests):
    f1.write("test %s: %s\n\n" %
          (index, " ".join(
              map(lambda item: "%s(%s~%s)" % (item[0], item[1], item[2]), test))))
    f2.write(json.dumps(test) + "\n")

f3 = open("falling.txt", "w")
f4 = open("falling.json", "w")
print("falling activity test sets are:")
for (index, test) in enumerate(final_falling_tests):
    f3.write("test %s: %s\n\n" %
          (index, " ".join(
              map(lambda item: "%s(%s~%s)" % (item[0], item[1], item[2]), test))))
    f4.write(json.dumps(test) + "\n")
