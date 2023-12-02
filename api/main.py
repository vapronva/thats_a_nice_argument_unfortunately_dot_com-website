import os
from ipaddress import AddressValueError, IPv4Address

import sentry_sdk
import uvicorn
from DB import DB
from fastapi import FastAPI, Request, Response
from IPInfoAPI import IPInfoAPI
from models import (
    BasicResponseModel,
    ErrorResponseModel,
    IntroMessageResponseModel,
    IPNonsenseResponseModel,
    RequestException,
)
from NonsenseTextGenerator import NonsenseIPInformationGenerator
from ProxyCheckAPI import ProxyCheckAPI

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN_BACKEND"),
    traces_sample_rate=1.0,
    release=os.getenv("ASSETS_VERSION"),
)

app = FastAPI(
    debug=True,
    title="that's a nice argument unfortunatly dot com",
    description="display almost nonsensical information about requester's ip address",
    version="0.3.1",
    redoc_url=None,
    docs_url=None,
)

__ipInfoAPI: IPInfoAPI = IPInfoAPI(os.getenv("IPINFO_API_KEY"))
__proxyCheckAPI: ProxyCheckAPI = ProxyCheckAPI(os.getenv("PROXYCHECK_API_KEY"))

__db = DB(os.getenv("MONGODB_URI"))

__superBasedInfo = NonsenseIPInformationGenerator(__ipInfoAPI, __proxyCheckAPI)


@app.get("/")
def main_root(response_model=BasicResponseModel):
    """Return the message for root path.

    Returns
    -------
        BasicResponseModel: The message.
    """
    return BasicResponseModel(
        error=None,
        result=IntroMessageResponseModel(
            message="Hello, welcome to thats-a-nice-argument-unfortunatly.com. \
It's just a joke, nothing serious. Although, if you do have any \
questions, please e-mail me: contact at vapronva.pw. \
Thanks for visiting!",
        ),
    )


@app.get("/ip")
def main_ip(
    request: Request,
    response: Response,
    response_model=BasicResponseModel,
    disableICMPhopsInfo: bool = False,
):
    """Spit out the information about the requester's IP address.

    Args:
    ----
        request (Request): Request object.
        response (Response): Response object.
        response_model ([BasicResponseModel], optional). Defaults to BasicResponseModel.
        disableICMPhopsInfo ([bool], optional). Defaults to False.

    Returns:
    -------
        BasicResponseModel: The information about the requester's IP address.
    """
    try:
        try:
            userIP = IPv4Address(request.headers.get("X-Forwarded-For"))
        except AddressValueError:
            userIP = IPv4Address(request.headers.get("X-Forwarded-For").split(", ")[0])
        return BasicResponseModel(
            error=None,
            result=IPNonsenseResponseModel(
                user_ip=userIP,
                final_list=__db.add_nni(
                    userIP,
                    __superBasedInfo.generate(userIP, disableICMPhopsInfo),
                )
                if __db.get_nni(userIP.__str__()) is None
                else __db.get_nni(userIP.__str__()),
            ),
        )
    except RequestException as e:
        print(e)
        try:
            userIP = IPv4Address(request.headers.get("X-Forwarded-For"))
        except AddressValueError:
            userIP = IPv4Address("104.18.100.148")
        response.status_code = 500
        return BasicResponseModel(
            error=ErrorResponseModel(
                name="Internal Server Error",
                description=f"Something went really wrong. Specifically: {str(e)}",
            ),
            result=IPNonsenseResponseModel(
                user_ip=userIP,
                final_list=[
                    "AN ERROR OCCURRED WHILE PROCESSING YOUR REQUEST",
                    "YOU SEEM TO BE TOO POWERFUL",
                ],
            ),
        )


@app.get("/health")
def main_health(
    request: Request,
    response: Response,
    response_model=BasicResponseModel,
):
    """Check the health of the server.

    Args:
    ----
        request (Request): Request object.
        response (Response): Response object.
        response_model ([BasicResponseModel], optional). Defaults to BasicResponseModel.

    Returns:
    -------
        BasicResponseModel: The health description of the internal components.
    """
    if __db.check_health():
        return BasicResponseModel(
            error=None,
            result=IntroMessageResponseModel(
                message="I'm healthy! I'm healthy! I'm healthy!",
            ),
        )
    response.status_code = 500
    return BasicResponseModel(
        error=None,
        result=IntroMessageResponseModel(
            message="I'm not healthy! I'm not healthy! I'm not healthy!",
        ),
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )
