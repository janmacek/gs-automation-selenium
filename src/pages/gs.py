import time
from selenium.common.exceptions import TimeoutException
from random import randint
import re

from src.pages.base import BasePage
from src.settings import settings


class GSPage(BasePage):
    """
        Base page for GS webpage automation. Additional functionality is that it
        will close advertising popup window if visible.
    """

    def cancel_advertising(self):
        try:
            self.click_element_by_xpath(settings.XPATH_ADVERTISING_CLOSE_BUTTON)
        except TimeoutException:
            pass


class GSLoginPage(GSPage):
    """ Login page of GS automation. It fills credentials info and click login button. """

    URL = settings.URL_LOGIN_PAGE

    def login(self, name, password):
        self.click_element_by_xpath(settings.XPATH_LOGIN_SIGN_IN_BUTTON)
        self.set_value_by_xpath(settings.XPATH_LOGIN_NAME_INPUT, name)
        self.set_value_by_xpath(settings.XPATH_LOGIN_PASSWORD_INPUT, password)
        self.click_element_by_xpath(settings.XPATH_LOGIN_SUBMIT_BUTTON)
        time.sleep(1)
        self.logger.info('Login page successfully processed.')
        return self


class GSChallengesPage(GSPage):
    """
        Challenges age of GS automation. Processes all challenges one by one by opening
        the challenge and liking photos while exposure is not max.
    """

    URL = settings.URL_CHALLENGES_PAGE

    def get_challenge_exposure(self, challenge_el):
        """ Get challenge exposure from exposure meter element. It checks angle of moving hand. """
        meter_el = self.get_child_by_xpath(challenge_el, settings.XPATH_CHALLENGES_EXPOSURE_METER_DIV)
        match = re.search(settings.REGEX_EXPOSURE_FROM_STYLE, meter_el.get_attribute('style'))
        return match and float(match.group(1)) or None

    def process_all_challenges(self):
        self.cancel_advertising()
        challenges = self.get_elements_by_xpath(settings.XPATH_CHALLENGES_ITEM_DIV)
        for challenge in challenges:
            self.process_challenge(challenge)
        self.logger.info('All challenges successfully processed.')

    def process_challenge(self, challenge_el):
        """
            Opens challenge, click multiple pictures to add like to them and then submit this votes.
            Repeats while not max exposure.
        """

        for _ in range(settings.MAX_VOTE_CYCLES):
            challenge_name = self.get_child_text_by_xpath(challenge_el, settings.XPATH_CHALLENGE_NAME_DIV)
            challenge_exposure = self.get_challenge_exposure(challenge_el)
            if not challenge_exposure:
                self.logger.warning(f'Unable to get exposure from exposure meter for challenge: {challenge_name}. '
                                    f'Skipping this challenge.')
                return

            self.logger.info(f'Exposure bonus of challenge with name \'{challenge_name}\' '
                             f'is {challenge_exposure}. Maximum value is {settings.MAX_CHALLENGE_EXPOSURE}.')

            if challenge_exposure >= settings.MAX_CHALLENGE_EXPOSURE:
                self.logger.info(f'Voting will not continue as challenge is at max exposure bonus.')
                return
            else:
                self.click_child_by_xpath(challenge_el, settings.XPATH_CHALLENGES_VOTE_BUTTON)
                self.click_element_by_xpath(settings.XPATH_CHALLENGES_ENTER_VOTING_BUTTON)
                position = 1
                el_count = len(self.get_elements_by_xpath(settings.XPATH_CHALLENGE_PHOTO_DIV))
                for _ in range(settings.AMOUNT_PHOTOS_TO_VOTE):
                    if el_count < position:
                        self.logger.warning(f'Unable to like picture at position {position} '
                                            f'as count of pictures is {el_count}.')
                        break
                    self.click_element_by_xpath(
                        xpath='(' + settings.XPATH_CHALLENGE_PHOTO_DIV + f')[position()={position}]',
                        scroll_to=True
                    )
                    position += randint(1, 10)
                self.click_element_by_xpath(settings.XPATH_CHALLENGE_SUBMIT_VOTES_DIV)
                self.click_element_by_xpath(settings.XPATH_CHALLENGE_DONE_DIV)

