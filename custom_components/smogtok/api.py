"""SmogTok API Client."""

from __future__ import annotations

import asyncio
import socket
from typing import Any

import aiohttp

from .const import LIST_OF_STATIONS_API_URL, STATION_DETAILS_API_URL


class SmogTokClientError(Exception):
    """Custom exception to indicate SmogTok API errors."""


class SmogTokClientCommunicationError(SmogTokClientError):
    """Exception to indicate a communication error."""


class SmogTokClient:
    """SmogTok API client."""

    def __init__(self, session: aiohttp.ClientSession) -> None:
        """SmogTok API client."""
        self._session = session

    async def async_get_list_of_stations(self) -> list[dict[str, Any]]:
        """Get list of stations from SmogTok API."""
        return await self._api_wrapper(method="get", url=LIST_OF_STATIONS_API_URL)

    async def async_get_data(self, stationId: str) -> Any:
        """Get data from SmogTok API."""
        return await self._api_wrapper(
            method="get", url=STATION_DETAILS_API_URL.format(station_id=stationId)
        )

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> Any:
        """Get information from the API."""
        try:
            async with asyncio.timeout(10):
                response = await self._session.request(
                    method=method, url=url, headers=headers, json=data
                )
                return await response.json()
        except TimeoutError as exception:
            msg = f"Timeout errror fetching information - {exception}"
            raise SmogTokClientCommunicationError(msg) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            msg = f"Error fetching information - {exception}"
            raise SmogTokClientCommunicationError(msg) from exception
        except Exception as exception:
            msg = f"Unexpected error fetching information - {exception}"
            raise SmogTokClientError(msg) from exception
