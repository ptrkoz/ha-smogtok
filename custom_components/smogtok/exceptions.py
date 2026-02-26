"""Exceptions for the SmogTok integration."""

from homeassistant.exceptions import HomeAssistantError


class SmogTokException(HomeAssistantError):
    """Base exception for the SmogTok integration."""


class SmogTokClientError(SmogTokException):
    """Custom exception to indicate SmogTok API errors."""


class SmogTokClientCommunicationError(SmogTokClientError):
    """Exception to indicate a communication error."""


class SmogTokCannotConnect(SmogTokException):
    """Error to indicate we cannot connect."""


class SmogTokNoDataAvailable(SmogTokException):
    """Error to indicate there's no data available for that station."""


class SmogTokInvalidResponse(SmogTokException):
    """Error to indicate there is invalid response."""
