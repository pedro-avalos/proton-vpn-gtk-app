#!/usr/bin/env python3
"""
This module modifies the latest version with a pre-release.


Copyright (c) 2023 Proton AG

This file is part of Proton VPN.

Proton VPN is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Proton VPN is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ProtonVPN.  If not, see <https://www.gnu.org/licenses/>.
"""
import os
from typing import List, Dict, Union
import argparse

# The root of this repo
ROOT = os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))
)

VERSIONS = os.path.join(ROOT, "versions.yml")  # Name of this applications versions.yml


def read_from_file() -> List[Dict[str, Union[str, int]]]:
    """Read content from file."""
    content = None
    with open(VERSIONS, encoding="utf-8") as versions_file:
        content = versions_file.readlines()

    if content is None:
        raise RuntimeError("Empty versions file")

    return content


def write_to_file(new_content: List[Dict[str, Union[str, int]]]) -> None:
    """Write content to file."""
    with open(VERSIONS, mode="w", encoding="utf-8") as versions_file:
        for line in new_content:
            versions_file.write(line)


def append_pre_release_to_latest_version(_pre_release: str) -> None:
    """Appends a release channel to the latest version."""
    content = read_from_file()
    cleaned_version = content[0].rstrip()
    cleaned_version += f"{_pre_release}\n"
    content[0] = cleaned_version
    write_to_file(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Pre-release version append.",
        description="Update versions.yml file with pre-release."
    )
    parser.add_argument("-r", "--pre-release", nargs="?")
    parser.parse_args()

    pre_release = parser.parse_args().pre_release

    # If release channel is set, then append it to version.
    if pre_release is not None:
        append_pre_release_to_latest_version(pre_release)
