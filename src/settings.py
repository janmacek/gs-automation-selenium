from pathlib import Path
import sys


class Settings:
    PROJECT_DIR = Path(sys.argv[0]).parent
    DRIVER_DIR = PROJECT_DIR / 'driver'

    DRIVER_CHROME_LINUX = DRIVER_DIR / 'chromedriver'

    # How many times check exposure and vote if lower than max exposure value
    MAX_VOTE_CYCLES = 10

    # How many likes to do in one vote cycle for one challenge
    AMOUNT_PHOTOS_TO_VOTE = 20

    XPATH_LOGIN_SIGN_IN_BUTTON = '//header[@id="header"]//div[contains(@class, "gs-container")]//div[contains(@class, "user")]/a[contains(@class, "signin")]'

    XPATH_LOGIN_NAME_INPUT = '//div[contains(@class, "modal-login__input")]/input[contains(@name, "email")]'
    XPATH_LOGIN_PASSWORD_INPUT = '//div[contains(@class, "modal-login__input")]/input[contains(@name, "password")]'
    XPATH_LOGIN_SUBMIT_BUTTON = '//button[contains(@class, "modal-login__submit")]'

    XPATH_ADVERTISING_CLOSE_BUTTON = '//div[contains(@class, "ab-in-app-message")]/button[contains(@class, "ab-close-button")]'

    XPATH_CHALLENGES_ITEM_DIV = '//div[contains(@class, "my-challenges__items")]/div[contains(@class, "challenges__item")]'
    XPATH_CHALLENGES_VOTE_BUTTON = './/div[contains(@class, "c-challenges-item__btn")]/i[contains(@class, "icon-voting")]/..'
    XPATH_CHALLENGES_ENTER_VOTING_BUTTON = '//div[contains(@class, "gs-btn--blue") and text()="LET\'S GO"]'
    XPATH_CHALLENGES_EXPOSURE_METER_DIV = './/div[contains(@class, "c-challenges-item__exposure__meter__arrow")]'

    XPATH_CHALLENGE_NAME_DIV = './/div[contains(@class, "c-challenges-item__title__label")]'
    XPATH_CHALLENGE_PHOTO_DIV = '//div[contains(@class, "modal-vote__photo__vote")]'
    XPATH_CHALLENGE_SUBMIT_VOTES_DIV = '//div[contains(@class, "modal-vote__photos__actions")]/div[contains(@class, "modal-vote__submit on")]'
    XPATH_CHALLENGE_DONE_DIV = '//div[contains(@class, "modal-vote__message-wrap")]//div[contains(@class, "actions")]//div[contains(text(), "Done")]'

    REGEX_EXPOSURE_FROM_STYLE = r'transform: *rotate\((-?[0-9]+\.?[0-9]*)deg\);'

    MIN_CHALLENGE_EXPOSURE = 0.0
    MAX_CHALLENGE_EXPOSURE = 90.0

    URL_LOGIN_PAGE = 'https://gurushots.com/'
    URL_CHALLENGES_PAGE = 'https://gurushots.com/challenges/my-challenges/current'

    # Email settings
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465


settings = Settings()
