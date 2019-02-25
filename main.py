#!/usr/bin/python3

from robotoy.projects import autodrive
import sys


def main(arg):
    projects = {
        "autodrive": autodrive.run
    }
    projects[arg]()


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except KeyboardInterrupt:
        print("Good bye.")
