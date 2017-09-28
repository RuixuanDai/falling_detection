import click
import os

@click.command()
@click.option("--directory", help="name of data directory")
@click.option("--start", type=float, help="the start time of data")
@click.option("--end", type=float, help="the end time of date")
def trimdata(directory, start, end):
    files = os.listdir(directory)
    dest_directory = "trim"
    try:
        os.mkdir(dest_directory)
    except:
        pass
    for filename in files:
        dest_file = os.path.join(dest_directory, filename)
        src_file = os.path.join(directory, filename)
        with open(dest_file, "w") as fdest:
            with open(src_file) as fsrc:
                header = fsrc.next()
                fdest.write(header)
                for line in fsrc:
                    try:
                        time, x, y, z = line.strip().split(",")
                    except:
                        print("Broken file %s, line %s" % (src_file, line))
                    else:
                        if end > float(time) > start:
                            fdest.write(",".join([time, x, y, z]))
                            fdest.write("\n")
                        elif float(time) > end:
                            break


if __name__ == "__main__":
    trimdata()
