from ipaddress import IPv4Address
from typing import Optional, Union

import pydantic


class RequestException(Exception):
    """Request exception."""


class ErrorResponseModel(pydantic.BaseModel):
    """Error response model.

    Args:
    ----
        name (str): The error name.
        description (str): The error description.
    """

    name: str
    description: str


class IPNonsenseResponseModel(pydantic.BaseModel):
    """IPNonsense response model.

    Args:
    ----
        user_ip (IPv4Address): The user IP address.
        final_list (list): The list of nonsense information for the user IP address.
    """

    user_ip: IPv4Address
    final_list: list


class IntroMessageResponseModel(pydantic.BaseModel):
    """Intro message response model.

    Args:
    ----
        message (str): The intro message.
    """

    message: str


class BasicResponseModel(pydantic.BaseModel):
    """Basic response model.

    Args:
    ----
        error (Optional[ErrorResponseModel]): The error.
        result (Optional[IPNonsenseResponseModel,
            IntroMessageResponseModel]): The result.
    """

    error: Optional[ErrorResponseModel]
    result: Union[IPNonsenseResponseModel, IntroMessageResponseModel, None]
