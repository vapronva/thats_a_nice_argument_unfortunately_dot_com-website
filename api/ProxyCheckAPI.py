from ipaddress import IPv4Address
import requests
import pydantic


class ProxyCheckAnswerModel(pydantic.BaseModel):
    """
    Answer model for the proxy check API.

    Args:
        ip (IPv4Address): The IP address of the proxy.
        proxy (str): The proxy status.
        type (str): The IP address type.
    """
    ip: IPv4Address
    proxy: str
    type: str


class ProxyCheckAPI:
    """
    Proxy check API model.
    """
    def __init__(self, apiKey: str):
        """
        Initialize the API.

        Args:
            apiKey (str): The API key.
        """
        self.__apiKey = apiKey
        self.baseURL = "https://proxycheck.io/v2/"

    def getInfo(self, ip: IPv4Address) -> ProxyCheckAnswerModel:
        """
        Get the proxy check information for the given IP address.

        Args:
            ip (IPv4Address): [description]

        Raises:
            Exception: If the request failed.

        Returns:
            ProxyCheckAnswerModel: The proxy check information.
        """
        url = self.baseURL + "/" + str(ip) + "?key=" + self.__apiKey
        response = requests.get(url)
        try:
            if response.status_code == 200:
                data = response.json()
                return ProxyCheckAnswerModel(
                    ip = ip,
                    proxy = data[str(ip)]["proxy"],
                    type = data[str(ip)]["type"]
                )
            else:
                raise Exception("Error: " + response.text)
        except Exception as e:
            print(e)
            return ProxyCheckAnswerModel(
                ip = ip,
                proxy = "no",
                type = "Regular"
            )
