#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

"""Test that certain packages are available though Apptainer."""

from emoji import emojize
from tabulate import tabulate
from urllib.request import urlopen


if (page := urlopen("https://canonical.com")).status == 200:
    print(tabulate(
        [[page.status, f"Able to connect to canonical.com {emojize(':thumbs_up:')}"]],
        headers=["Status", "Message"]
    ))
else:
    print(tabulate(
        [[page.status, f"Cannot connect to canonical.com {emojize(':thumbs_down:')}"]],
        headers=["Status", "Message"]
    ))
