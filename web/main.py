import os
from ipaddress import AddressValueError, IPv4Address

from flask import Flask, jsonify, render_template, request
import sentry_sdk


sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN_FRONTEND_BACKEND"),
    traces_sample_rate=1.0,
    release=os.getenv("ASSETS_VERSION"),
)

app = Flask("web-thats_a_nice_argument_unfortunately_dot_com")

ASSETS_VERSION = os.environ.get("ASSETS_VERSION")


@app.errorhandler(404)
def error_404(e):
    return (
        jsonify(
            {
                "error": {
                    "name": "PATH_NOT_FOUND",
                    "description": "The requested path was not found.",
                },
                "result": None,
            },
        ),
        404,
    )


@app.errorhandler(500)
def error_500(e):
    return (
        jsonify(
            {
                "error": {
                    "name": "ISE",
                    "description": "Internal server error occurred. That's really fricking bad!",
                },
                "result": None,
            },
        ),
        500,
    )


@app.route("/")
def main_root():
    enableOGPreviews = request.args.get("n") is None
    return render_template(
        "index.html",
        enableOGPreviews=enableOGPreviews,
        ASSETS_VERSION=ASSETS_VERSION,
    )


@app.route("/ipp")
def main_ipp():
    try:
        userIP = IPv4Address(request.headers.get("X-Forwarded-For"))
    except AddressValueError:
        userIP = IPv4Address(request.headers.get("X-Forwarded-For").split(", ")[0])
    except BaseException:
        userIP = IPv4Address("104.18.100.148")
    return render_template(
        "ipp.html",
        userIP=str(userIP),
        ASSETS_VERSION=ASSETS_VERSION,
    )
