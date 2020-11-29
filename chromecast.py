"""
Example on how to use the Media Controller

"""

import argparse
import logging
import sys
import time

import pychromecast
import zeroconf
import urllib.parse

def say(cast, phrase, ttsip):
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[cast])
    if not chromecasts:
        chromecasts, browser = pychromecast.get_chromecasts()
        err = 'No chromecast with name "{}" discovered. Try one of the following: {}'.format(cast, [cc.device.friendly_name for cc in chromecasts])
        raise Exception(err)

    cast = chromecasts[0]
    # Start socket client's worker thread and wait for initial status update
    cast.wait()
    logging.info(
        'Found chromecast with name "{}", attempting to say "{}"'.format(
            cast, phrase
        )
    )
    url = f"http://{ttsip}:5002/api/tts?text={urllib.parse.quote_plus(phrase)}."
    cast.media_controller.play_media(url, "audio/wav")

    player_state = None
    t = 30
    has_played = False
    while True:
        try:
            if player_state != cast.media_controller.status.player_state:
                player_state = cast.media_controller.status.player_state
                logging.info("Player state:", player_state)
            if player_state == "PLAYING":
                sys.exit(0)
            if cast.socket_client.is_connected and has_played and player_state != "PLAYING":
                has_played = False
                cast.media_controller.play_media(url)
            time.sleep(0.1)
            t = t - 0.1
        except KeyboardInterrupt:
            break

    # Shut down discovery
    pychromecast.discovery.stop_discovery(browser)
