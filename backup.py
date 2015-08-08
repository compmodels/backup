import time
import subprocess as sp
import argparse

def backup(source, dest, gpg_key):
    sp.call([
        "duplicity",
        "--verbosity", "notice",
        "--encrypt-key", gpg_key,
        "--full-if-older-than", "7D",
        "--num-retries", "3",
        "--asynchronous-upload",
        "--volsize", "10",
        "--allow-source-mismatch",
        source, dest
    ])

def cleanup(dest, gpg_key):
    sp.call([
        "duplicity", "remove-all-but-n-full", "2",
        "--force",
        "--verbosity", "notice",
        "--encrypt-key", gpg_key,
        "--allow-source-mismatch",
        dest
    ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Backup to Rackspace CloudFiles')
    parser.add_argument('source', help='the source directory to backup')
    parser.add_argument('dest', help='the destination container name')
    parser.add_argument('--gpg-key', dest='gpg_key', required=True, help='the GPG key to encrypt the files')
    parser.add_argument('--interval', default=60, help='the interval (in minutes) that the backup will be run at')

    args = parser.parse_args()

    while True:
        backup(args.source, args.dest, args.gpg_key)
        cleanup(args.dest, args.gpg_key)
        time.sleep(args.interval * 60)


