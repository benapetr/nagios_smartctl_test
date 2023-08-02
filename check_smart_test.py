#!/usr/bin/env python

import subprocess
import sys

def main():
    # Check command line arguments
    if len(sys.argv) < 2:
        print("UNKNOWN - Device identifier missing")
        sys.exit(3)

    device = sys.argv[1]

    # Run smartctl command
    process = subprocess.Popen(['smartctl', '-l', 'selftest', device], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Check for failed tests
    if 'Completed: read failure' in output:
        print("CRITICAL - SMART self-test read failure on {}".format(device))
        sys.exit(2)
    elif process.returncode != 0:
        print("UNKNOWN - smartctl command failed: {}".format(error.strip()))
        sys.exit(3)
    else:
        print("OK - No SMART self-test read failures on {}".format(device))
        sys.exit(0)

if __name__ == "__main__":
    main()
