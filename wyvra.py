#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

from wyvra.networking import wyvra_server
from wyvra.logging import wyvra_logging
from wyvra.blockchain import wyvra_blockchain

def main():
    wyvra_logging("info", "Wyvra node starting")
    wyvra_server("wyvra.xyz", 4444)


def quit():
    wyvra_logging("info", "Wyvra node terminating")

if __name__ == "__main__":
    main()
