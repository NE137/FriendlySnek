####################
# Generic
####################

## Misc
COMMAND_PREFIX = "-"
TIME_FORMAT = "%Y-%m-%d %I:%M %p"
SCHEDULE_CANCEL = "Enter `cancel` to abort this command."
CHANGELOG_URL = "https://steamcommunity.com/sharedfiles/filedetails/changelog/{0}"

## Error
ERROR_TIMEOUT = ":clock3: You were too slow, aborting!"

## Logging
LOG_COG_READY = "{0} cog is ready!"

## Time in seconds
TIME_ONE_MIN = 60  # Short
TIME_TEN_MIN = 600  # Normal
TIME_THIRTY_MIN = 1800  # Long


###################
# Poll.py
####################

POLL_PERCENT_REGEX = r"\(\d+\.?\d*%\)\s*"


####################
# Schedule.py
####################

SCHEDULE_TEMPLATE_REMOVE_FROM_EVENT = ("authorId", "type", "time", "endTime", "messageId", "accepted", "declined", "tentative")
SCHEDULE_EVENT_SELECTED_TIME_ZONE = "Your current time zone preference is `{0}`."

## Errors
SCHEDULE_EVENT_ERROR_DESCRIPTION = "Enter `edit` to input a new time.\nEnter `override` to override this warning."
