"""Constants for the Fallback Conversation Agent integration."""

DOMAIN = "fallback_conversation"

CONF_DEBUG_LEVEL = 'debug_level'
CONF_PRIMARY_AGENT = 'primary_agent'
CONF_FALLBACK_AGENT = 'fallback_agent'

DEBUG_LEVEL_NO_DEBUG = "none"
DEBUG_LEVEL_LOW_DEBUG = "low"
DEBUG_LEVEL_VERBOSE_DEBUG = "verbose"

EVENT_CONVERSATION_NO_INTENT_MATCH = "fallback_conversation.no_intent_match"

DEFAULT_NAME = "Fallback Conversation Agent"
DEFAULT_DEBUG_LEVEL = DEBUG_LEVEL_NO_DEBUG

STRANGE_ERROR_RESPONSES = [
    "not any",
    "geen",
]