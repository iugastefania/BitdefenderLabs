"""
Use Python 3.9+
Example event:
{
    “device”:{
        “id”: <random uuid that uniquely identifies machine>,
        “os”: <os type/version>
    }
    file:{
        “file_path”: <file path>,
        “file_hash": <md5/sha/anyhash>,
        “time”:{
            “a”: <time of last access>
            “m”: <time of last modification>
        }
    }
    “last_access”:{
        “pid”: <pid of process to last access file>,
        “path”: <process executable path>,
        “hash”: <hash of executable^>
    }
}
"""
import hashlib
import os
import random
import uuid
import time
from pprint import pprint


def generate_file_path():
    root_dirs = ["bin", "etc", "dev", "boot", "home", "run", "sys", "usr", "srv"]
    executables = [
        "bash",
        "brltty",
        "bunzip2",
        "busybox",
        "bzcat",
        "bzcmp",
        "bzdiff",
        "bzegrep",
        "bzexe",
        "bzfgrep",
        "bzgrep",
        "bzip2",
        "bzip2recover",
        "bzless",
        "bzmore",
        "cat",
        "chacl",
        "chgrp",
        "chmod",
        "chown",
        "chvt",
        "cp",
        "cpio",
        "dash",
        "date",
        "dd",
        "df",
        "dir",
        "dmesg",
        "dnsdomainname",
        "domainname",
        "dumpkeys",
        "echo",
        "ed",
        "efibootdump",
        "efibootmgr",
        "egrep",
        "false",
        "fgconsole",
        "fgrep",
        "findmnt",
        "fuser",
        "fusermount",
        "getfacl",
        "grep",
        "gunzip",
        "gzexe",
        "gzip",
        "hostname",
        "ip",
        "journalctl",
        "kbd_mode",
        "kill",
        "kmod",
        "less",
        "lessecho",
        "lessfile",
        "lesskey",
        "lesspipe",
        "ln",
        "loadkeys",
        "lowntfs",
        "ls",
        "lsblk",
        "lsmod",
        "mkdir",
        "mknod",
        "mktemp",
        "more",
        "mount",
        "mountpoint",
        "mt",
        "mv",
        "nano",
        "nc",
        "netcat",
        "netstat",
        "nisdomainname",
        "ntfs",
        "ntfs",
        "ntfscat",
        "ntfscluster",
        "ntfscmp",
        "ntfsfallocate",
        "ntfsfix",
        "ntfsinfo",
        "ntfsls",
        "ntfsmove",
        "ntfsrecover",
        "ntfssecaudit",
        "ntfstruncate",
        "ntfsusermap",
        "ntfswipe",
        "open",
        "openvt",
        "pidof",
        "ping",
        "ping4",
        "ping6",
        "plymouth",
        "ps",
        "pwd",
        "rbash",
        "readlink",
        "red",
        "rm",
        "rmdir",
        "rnano",
        "run",
        "sed",
        "setfacl",
        "setfont",
        "setupcon",
        "sh",
        "sleep",
        "ss",
        "stty",
        "sync",
        "tar",
        "tempfile",
        "touch",
        "true",
        "ulockmgr_server",
        "umount",
        "uname",
        "uncompress",
        "unicode_start",
        "vdir",
        "wdctl",
        "which",
        "whiptail",
        "ypdomainname",
        "zcat",
        "zcmp",
        "zdiff",
        "zegrep",
        "zfgrep",
        "zforce",
        "zgrep",
        "zless",
        "zmore",
        "znew",
        "zsh",
        "zsh5",
    ]
    return os.path.join(
        "/", random.choice(root_dirs), str(uuid.uuid4()), random.choice(executables)
    )


def generate_random_file(operating_system_type: str) -> str:
    """
    Generates a random file on the disk and returns its hash.
    """
    file_contents = []
    if operating_system_type == "windows":
        file_contents.extend([0x4D, 0x5A])

    file_contents.extend(random.randbytes(random.randint(10240, 1024000)))
    file_bytes = bytes(file_contents)

    file_hash = hashlib.md5(file_bytes).hexdigest()
    with open("generated_events/{}".format(file_hash), "wb") as file_handle:
        file_handle.write(file_bytes)

    return file_hash


def generate_event():
    os = ["windows"]
    chosen_os = random.choice(os)
    file_path = generate_file_path()
    process_path = generate_file_path()

    random_file_hash = generate_random_file(chosen_os)
    process_file_hash = generate_random_file(chosen_os)

    access_time = random.randint(1583241953000, 1646313953000)
    return {
        "device": {"id": str(uuid.uuid4()), "os": chosen_os},
        "file": {
            "file_path": file_path,
            "file_hash": random_file_hash,
            "time": {
                "a": random.randint(1583241953000, 1646313953000),
                "m": random.randint(1583241953000, access_time),
            },
        },
        "last_access": {
            "pid": random.randint(3000, 5000),
            "path": process_path,
            "hash": process_file_hash,
        },
    }


def main():
    generated_events = [generate_event() for _ in range(5)]
    for generated_event in generated_events:
        pprint(generated_event)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
