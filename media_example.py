"""
Example on how to use the Media Controller

"""

import argparse
import logging
import sys
import time

import chromecast

# Change to the friendly name of your Chromecast
CAST_NAME = 'Garage speaker'

# Change to an audio or video phrase
MEDIA_phrase = "I like Mozilla TTS."

parser = argparse.ArgumentParser(
    description="Example on how to use the Media Controller to play a phrase."
)
parser.add_argument("--show-debug", help="Enable debug log", action="store_true")
parser.add_argument(
    "--show-zeroconf-debug", help="Enable zeroconf debug log", action="store_true"
)
parser.add_argument(
    "--cast", help='Name of cast device (default: "%(default)s")', default=CAST_NAME
)
parser.add_argument(
    "--phrase", help='Media phrase (default: "%(default)s")', default=MEDIA_phrase
)
parser.add_argument(
    "--myip", help='Ip to give to google home, should be the ip this docker container is exposed on.)'
)
args = parser.parse_args()


if args.show_debug:
    logging.basicConfig(level=logging.DEBUG)
if args.show_zeroconf_debug:
    print("Zeroconf version: " + zeroconf.__version__)
    logging.getLogger("zeroconf").setLevel(logging.DEBUG)

chromecast.say(args.cast, args.phrase, args.myip)