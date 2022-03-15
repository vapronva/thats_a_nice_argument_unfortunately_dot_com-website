from ipaddress import AddressValueError, IPv4Address

from flask import Flask, jsonify, render_template, request

app = Flask("web-thats_a_nice_argument_unfortunately_dot_com")


@app.errorhandler(404)
def error_404(e):
    return (
        jsonify({
            "error": {
                "name": "PATH_NOT_FOUND",
                "description": "The requested path was not found.",
            },
            "result": None,
        }),
        404,
    )


@app.errorhandler(500)
def error_500(e):
    return (
        jsonify({
            "error": {
                "name":
                "ISE",
                "description":
                "Internal server error occurred. That's really fricking bad!",
            },
            "result": None,
        }),
        500,
    )


@app.route("/")
def main_root():
    return render_template("index.html")


@app.route("/ipp")
def main_ipp():
    try:
        userIP = IPv4Address(request.headers.get("X-Forwarded-For"))
    except AddressValueError:
        userIP = IPv4Address(
            request.headers.get("X-Forwarded-For").split(", ")[0])
    return render_template("ipp.html", userIP=str(userIP))


app.run(debug=False, host="0.0.0.0", port=8000)
