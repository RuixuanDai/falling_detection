from collections import defaultdict
import math
from pprint import pprint
import click


@click.command()
@click.option("--filename", help="name of data file")
@click.option("--window_length", type=int, help="length of detection window")
@click.option("--th_y", type=float, help="threshold of y_diff")
@click.option("--th_smv", type=float, help="threshold of smv_avg")
def detect_falling(filename, window_length, th_y, th_smv):
    raw_data = get_rawdata(filename, window_length)
    window_count = len(raw_data)
    y_max = {}
    y_min = {}
    y_avg = {}
    y_diff = {}
    smv = defaultdict(list)
    smv_avg = {}
    calculate_data(raw_data, y_max, y_min, y_avg, y_diff, smv, smv_avg)
    echo_result(raw_data, y_max, y_min, y_avg, y_diff, smv, smv_avg)

    for window in range(window_count):
        if is_falling(y_diff[window],smv_avg[window], th_y, th_smv):
            print(
                "falling is detected during [%d, %d), y_diff is %f, smv_avg is %f" %
                (window * window_length, window * window_length + window_length, y_diff[window], smv_avg[window])
            )
        else:
            print(
                "only normal activities during [%d, %d), y_diff is %f, smv_avg is %f" %
                (window * window_length, window * window_length + window_length, y_diff[window], smv_avg[window])
            )


def is_falling(y_diff, smv_avg, th_y, th_smv):
    if (y_diff >= th_y) and (smv_avg >= th_smv):
        return True
    else:
        False


def get_rawdata(filename, window_length):
    raw_data = defaultdict(list)
    with open(filename) as f:
        f.next()
        for line in f:
            time, acc_x, acc_y, acc_z = line.split(",")
            item = (float(acc_x), float(acc_y), float(acc_z))
            raw_data[int(float(time)) / window_length].append(item)
    return raw_data


def calculate_data(raw_data, y_max, y_min, y_avg, y_diff, smv, smv_avg):
    for key, value in raw_data.items():
        y_max[key] = max(value, key=lambda item: item[1])[1]
        y_min[key] = min(value, key=lambda item: item[1])[1]
        y_avg[key] = sum(map(lambda item: item[1], value)) / len(value)
        y_diff[key] = y_max[key] - y_min[key]
        smv[key] = map(
            lambda item: math.sqrt(
                item[0] * item[0] + item[1] * item[1] + item[2] * item[2]
            ), value
        )
        smv_avg[key] = sum(smv[key]) / len(smv[key])


def echo_result(raw_data, y_max, y_min, y_avg, y_diff, smv, smv_avg):
    print "---------------"
    pprint(dict(raw_data))
    print "---------------"
    pprint(dict(y_max))
    print "---------------"
    pprint(dict(y_min))
    print "---------------"
    pprint(dict(y_avg))
    print "---------------"
    pprint(dict(y_diff))
    print "---------------"
    pprint(dict(smv))
    print "---------------"
    pprint(dict(smv_avg))


if __name__ == "__main__":
    detect_falling()
