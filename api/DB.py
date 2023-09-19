from ipaddress import IPv4Address
from typing import List, Optional

import pydantic
import pymongo


class IPObjectModel(pydantic.BaseModel):
    """Model for the IP object in the DB.

    Args:
    ----
        ip: The IP address.
        nni: List string'ed of nonsense information.
    """

    ip: str
    nni: List[str]


class DB:
    """Database methods for the TNAUDC cache."""

    def __init__(self, mongodbURI: str) -> None:
        """Initialize the DB.

        Args:
        ----
            mongodbURI (str): The URI of the MongoDB instance.
        """
        self.__client = pymongo.MongoClient(mongodbURI)
        self.__cll = self.__client["tnauc"]["ipaddresses"]

    def add_nni(self, ip: IPv4Address, nni: List[str]) -> List[str]:
        """Add the IP address to the DB.

        Args:
        ----
            ip (IPv4Address): The IP address.
            nni (List[str]): The list of nonsense information.

        Returns:
        -------
            List[str]: The list of nonsense information.
        """
        self.__cll.insert_one(IPObjectModel(ip=str(ip), nni=nni).dict())
        return nni

    def get_nni(self, ip: IPv4Address) -> Optional[List[str]]:
        """Get the nonsense information for the given IP address.

        Args:
        ----
            ip (IPv4Address): The IP address.

        Returns:
        -------
            Optional[List[str]]: The list of nonsense information.
        """
        return (
            self.__cll.find_one({"ip": ip})["nni"]
            if self.__cll.find_one({"ip": ip})
            else None
        )

    def check_health(self) -> bool:
        """Check the health of the DB.

        Returns
        -------
            bool: True if the DB is healthy, False otherwise.
        """
        try:
            self.__client.server_info()
            return True
        except pymongo.errors.ServerSelectionTimeoutError:
            return False
