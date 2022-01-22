from ipaddress import IPv4Address

import pydantic
import requests
from models import RequestException


class IPInfoResponse(pydantic.BaseModel):
    """
    IPInfo API response model.

    Args:
        ip (IPv4Address): The IP address.
        hostname (str): The hostname.
        city (str): The city.
        region (str): The region.
        country (str): The country.
        loc (str): The location.
        org (str): The organization.
        postal (str): The postal code.
        timezone (str): The timezone.
    """

    ip: IPv4Address
    hostname: str
    city: str
    region: str
    country: str
    loc: str
    org: str
    postal: str
    timezone: str


class IPInfoAPI:
    """IPInfo API."""

    def __init__(self, apiKey: str):
        """
        Initialize the API.

        Args:
            apiKey (str): The API key.
        """
        self.__apiKey = apiKey
        self.baseURL = "https://ipinfo.io/"

    def getInfo(self, ip: IPv4Address) -> IPInfoResponse:
        """
        Get the IP information for the given IP address.

        Args:
            ip (IPv4Address): IP address.

        Raises:
            Exception: If the request failed.

        Returns:
            IPInfoResponse: The IP information.
        """
        url = self.baseURL + str(ip) + "/json?token=" + self.__apiKey
        response = requests.get(url)
        if response.status_code == 200:
            return IPInfoResponse(**response.json())
        raise RequestException("Error: " + response.text)
