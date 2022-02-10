from distutils.log import debug
from ipaddress import IPv4Address, AddressValueError
import os

from fastapi import FastAPI, Request, Response
import uvicorn
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

# Create the FastAPI application
app = FastAPI(
    debug=True,
    title="that's a nice argument unfortunatly dot com",
    description="display almost nonsensical information about requester's ip address",
    version="0.3.1",
    redoc_url=None,
    docs_url=None
)

# Intialize the IPInfoAPI and ProxyCheckAPI
__ipInfoAPI: IPInfoAPI = IPInfoAPI(os.getenv("IPINFO_API_KEY"))
__proxyCheckAPI: ProxyCheckAPI = ProxyCheckAPI(os.getenv("PROXYCHECK_API_KEY"))

# Create the NonsenseIPInformationGenerator
__superBasedInfo = NonsenseIPInformationGenerator(__ipInfoAPI, __proxyCheckAPI)


# Create the endpoint for "/"
@app.get("/")
def main_root(response_model=BasicResponseModel):
    """
    Return the message for root path.

    Returns:
        BasicResponseModel: The message.
    """
    return BasicResponseModel(
        error=None,
        result=IntroMessageResponseModel(
            message="Hello, welcome to thats-a-nice-argument-unfortunatly.com. \
It's just a joke, nothing serious. Although, if you do have any \
questions, please e-mail me: contact at vapronva.pw. \
Thanks for visiting!"),
    )


@app.get("/ip")
def main_ip(request: Request,
            response: Response,
            response_model=BasicResponseModel):
    """
    Spit out the information about the requester's IP address.

    Args:
        request (Request): Request object.
        response (Response): Response object.
        response_model ([type], optional). Defaults to BasicResponseModel.

    Returns:
        BasicResponseModel: The information about the requester's IP address.
    """
    try:
        # userIP = IPv4Address(request.client.host)
        try:
            userIP = IPv4Address(request.headers.get("X-Forwarded-For"))
        except AddressValueError:
            userIP = IPv4Address(request.headers.get("X-Forwarded-For").split(", ")[0])
        return BasicResponseModel(
            error=None,
            result=IPNonsenseResponseModel(
                user_ip=userIP, final_list=__superBasedInfo.generate(userIP)),
        )
    except RequestException as e:
        print(e)
        try:
            userIP = IPv4Address(request.headers.get("X-Forwarded-For"))
        except AddressValueError:
            userIP = IPv4Address(request.headers.get("X-Forwarded-For").split(", ")[0])
        response.status_code = 500
        return BasicResponseModel(
            error=ErrorResponseModel(
                name="Internal Server Error",
                description="Something went really wrong. Specifically: " +
                str(e),
            ),
            result=IPNonsenseResponseModel(
                user_ip=userIP,
                final_list=[
                    "AN ERROR OCCURRED WHILE PROCESSING YOUR REQUEST",
                    "YOU SEEM TO BE TOO POWERFUL",
                ],
            ),
        )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", debug=False)
