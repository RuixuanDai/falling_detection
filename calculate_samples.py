import click
import os
import math
from collections import defaultdict


@click.command()
@click.option("--directory", help="sample directory")
def calculate_samples(directory):
    files = os.listdir(directory)
    summary_directory = "summary"
    try:
        os.mkdir(summary_directory)
    except:
        pass
    header = ",".join([
        "Activities",
        "max", "avg", "min", "diff",
        "max", "avg", "min", "diff",
        "max", "avg", "min", "diff",
        "max", "avg", "min", "diff",
    ])
    summary_data = defaultdict(list)
    for filename in files:
        if not filename.endswith("csv"):
            continue
        activity = filter(lambda item: item.isalpha(), filename.split(".")[0])
        x = []
        y = []
        z = []
        smv = []

        with open(os.path.join(directory, filename)) as f:
            f.next()
            for line in f:
                time, acc_x, acc_y, acc_z = line.strip().split(",")
                acc_x = float(acc_x)
                acc_y = float(acc_y)
                acc_z = float(acc_z)

                x.append(acc_x)
                y.append(acc_y)
                z.append(acc_z)
                smv.append(
                    math.sqrt(acc_x * acc_x + acc_y * acc_y + acc_z * acc_z))
            x_max = max(x)
            x_min = min(x)
            x_avg = sum(x) / len(x)
            x_diff = x_max - x_min

            y_max = max(y)
            y_min = min(y)
            y_avg = sum(y) / len(y)
            y_diff = y_max - y_min

            z_max = max(z)
            z_min = min(z)
            z_avg = sum(z) / len(z)
            z_diff = z_max - z_min

            smv_max = max(smv)
            smv_min = min(smv)
            smv_avg = sum(smv) / len(smv)
            smv_diff = smv_max - smv_min
            output = ",".join(
                [filename.split(".")[0]] +
                ["{:.2f}".format(key) for key in [
                    x_max, x_avg, x_min, x_diff,
                    y_max, y_avg, y_min, y_diff,
                    z_max, z_avg, z_min, z_diff,
                    smv_max, smv_avg, smv_min, smv_diff
                ]])
            summary_data[activity].append(output)

        for activity, items in summary_data.items():
            summary_file = os.path.join(summary_directory, activity + ".csv")
            with open(summary_file, "w") as f:
                items.sort(
                    key=lambda item: int(
                        filter(lambda item: item.isdigit(), item.split(",")[0])
                    )
                )
                map(lambda item: f.write(item + "\n"), [header] + items)

if __name__ == "__main__":
    calculate_samples()
