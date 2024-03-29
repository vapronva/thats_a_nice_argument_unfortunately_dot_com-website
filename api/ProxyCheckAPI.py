import os
from ipaddress import IPv4Address

import pydantic
import requests
from models import RequestException


SKIP_PROXYCHECK = os.environ.get("SKIP_PROXYCHECK", "false").lower() == "true"


class ProxyCheckAnswerModel(pydantic.BaseModel):
    """Answer model for the proxy check API.

    Args:
    ----
        ip (IPv4Address): The IP address of the proxy.
        proxy (str): The proxy status.
        type (str): The IP address type.
    """

    ip: IPv4Address
    proxy: str
    type: str


class ProxyCheckAPI:
    """Proxy check API."""

    def __init__(self, apiKey: str) -> None:
        """Initialize the API.

        Args:
        ----
            apiKey (str): The API key.
        """
        self.__apiKey = apiKey
        self.baseURL = "https://proxycheck.io/v2"

    def getInfo(self, ip: IPv4Address) -> ProxyCheckAnswerModel:
        """Get the proxy check information for the given IP address.

        Args:
        ----
            ip (IPv4Address): [description]

        Raises:
        ------
            Exception: If the request failed.

        Returns:
        -------
            ProxyCheckAnswerModel: The proxy check information.
        """
        url = f"{self.baseURL}/{ip!s}?key={self.__apiKey}"
        try:
            if SKIP_PROXYCHECK:
                return ProxyCheckAnswerModel(ip=ip, proxy="no", type="Regular")
            response = requests.get(url, timeout=(0.75, 2.0))
            if response.status_code == 200:
                data = response.json()
                return ProxyCheckAnswerModel(
                    ip=ip,
                    proxy=data[str(ip)]["proxy"],
                    type=data[str(ip)]["type"],
                )
            msg = f"Error: {response.text}"
            raise RequestException(msg)
        except RequestException as e:
            print(e)
        return ProxyCheckAnswerModel(ip=ip, proxy="no", type="Regular")
