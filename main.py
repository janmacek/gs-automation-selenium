#!/usr/bin/env python3

import argparse
import logging

from src.driver import Driver
from src.pages.gs import GSLoginPage, GSChallengesPage
from src.settings import settings
from src.emails import send_error_email


def _init_logging():
    logger = logging.getLogger(str(settings.PROJECT_DIR))
    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    console.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s\t[%(filename)s:%(lineno)d] %(message)s', '%Y-%m-%d %H:%M:%S')
    )
    logger.addHandler(console)


def _parse_args():
    parser = argparse.ArgumentParser(description='Automate likes at GS webpage.')
    parser.add_argument('-n', '--name', required=True, type=str, help='Name of user for login form.')
    parser.add_argument('-p', '--password', required=True, type=str, help='Password of user for login form.')
    parser.add_argument('-f', '--from-address', type=str, help='Sender email address for error emails.')
    parser.add_argument('-t', '--to-address', type=str, help='Recipient email address for error emails.')
    parser.add_argument('-a', '--from-password', type=str, help='Password of sender email account.')
    parser.add_argument('-e', '--headless', action='store_true', default=False,  help='Run browser in headless mode.')
    return parser.parse_args()


if __name__ == '__main__':

    _init_logging()
    args = _parse_args()
    driver = Driver(headless=args.headless)
    try:
        GSLoginPage(driver=driver).login(args.name, args.password)
        GSChallengesPage(driver=driver).process_all_challenges()
    except Exception as e:
        logging.getLogger(str(settings.PROJECT_DIR)).error(
            f'Because of following error, automation is stopped and email is sent: {e}'
        )
        send_error_email(args.from_address, args.from_password, args.to_address, str(e))
    finally:
        driver.close()
