#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python standard library
import os
import sys
import argparse

# local pret classes
from discovery import discovery
from capabilities import capabilities
from postscript import postscript
from pjl import pjl
from pcl import pcl
from security import SecurityValidator

# ----------------------------------------------------------------------


def usage():
    parser = argparse.ArgumentParser(
        description="Printer Exploitation Toolkit.")
    parser.add_argument("target", nargs='?', help="printer device or hostname")
    parser.add_argument(
        "mode", nargs='?', choices=['ps', 'pjl', 'pcl'], help="printing language to abuse")
    parser.add_argument(
        "-s", "--safe", help="verify if language is supported", action="store_true")
    parser.add_argument(
        "-q", "--quiet", help="suppress warnings and chit-chat", action="store_true")
    parser.add_argument(
        "-d", "--debug", help="enter debug mode (show traffic)", action="store_true")
    parser.add_argument("-i", "--load", metavar="file",
                        help="load and run commands from file")
    parser.add_argument("-o", "--log", metavar="file",
                        help="log raw data sent to the target")

    args = parser.parse_args()

    # Handle discovery mode (no arguments)
    if not args.target:
        discovery(True)  # list local printers if no arguments given at all
        sys.exit(0)

    # Validate required arguments
    if not args.mode:
        print("Error: No printer language specified. Please choose: ps, pjl, or pcl" + os.linesep)
        parser.print_help()
        sys.exit(1)

    # Security validation
    if not SecurityValidator.is_safe_target(args.target):
        print(f"Error: Invalid or potentially dangerous target: {args.target}" + os.linesep)
        sys.exit(1)

    # Validate load file exists
    if args.load and not os.path.isfile(args.load):
        print(f"Error: Command file '{args.load}' not found" + os.linesep)
        sys.exit(1)

    return args

# ----------------------------------------------------------------------


def intro(quiet):
    if not quiet:
        print("      ________________                                             ")
        print("    _/_______________/|                                            ")
        print("   /___________/___//||   PRET | Printer Exploitation Toolkit v0.40")
        print("  |===        |----| ||    by Jens Mueller <jens.a.mueller@rub.de> ")
        print("  |           |   ô| ||                                            ")
        print("  |___________|   ô| ||                                            ")
        print("  | ||/.´---.||    | ||      「 pentesting tool that made          ")
        print("  |-||/_____\||-.  | |´         dumpster diving obsolete‥ 」       ")
        print("  |_||=L==H==||_|__|/                                              ")
        print("                                                                   ")
        print("     (ASCII art by                                                 ")
        print("     Jan Foerster)                                                 ")
        print("                                                                   ")

# ----------------------------------------------------------------------


def main():
    args = usage()     # parse args/options #
    intro(args.quiet)  # show asciitainment #
    capabilities(args)  # check capabilities #
    # connect to printer, use this language #
    if args.mode == 'ps':
        postscript(args)
    if args.mode == 'pjl':
        pjl(args)
    if args.mode == 'pcl':
        pcl(args)

# ----------------------------------------------------------------------


# clean exit
if __name__ == '__main__':
    try:
        main()
    # catch CTRL-C
    except (KeyboardInterrupt):
        pass
    finally:
        print("")
