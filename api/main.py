from ipaddress import IPv4Address

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

# Create the FastAPI application
app = FastAPI(
    debug=True,
    title="that's a nice argument unfortunatly dot com",
    description="display almost nonsensical information about requester's ip address",
    version="0.1.0",
)

# Intialize the IPInfoAPI and ProxyCheckAPI
__ipInfoAPI: IPInfoAPI = IPInfoAPI("7a8fa0d48b8c12")
__proxyCheckAPI: ProxyCheckAPI = ProxyCheckAPI("g17958-o519z8-395z83-82212d")

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
Thanks for visiting!"
        ),
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
        userIP = IPv4Address(request.client.host)
        userIP = IPv4Address("93.92.199.194")
        return BasicResponseModel(
            error=None,
            result=IPNonsenseResponseModel(
                user_ip=userIP, final_list=__superBasedInfo.generate(userIP)),
        )
    except RequestException as e:
        print(e)
        userIP = IPv4Address(request.client.host)
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
