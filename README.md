[![DeepSource Issues](https://deepsource.io/gh/vapronva/thats_a_nice_argument_unfortunately_dot_com-website.svg/?label=active+issues&show_trend=true&token=tCl_vlRCSOrAOb7rxIyPBERo)](https://deepsource.io/gh/vapronva/thats_a_nice_argument_unfortunately_dot_com-website/?ref=repository-badge)
[![API Uptime](https://status.vapronva.pw/api/v1/endpoints/websites-thatsaniceargumentunfortunatelly_thats-a-nice-argument-unfortunately-dot-com-backend-url-ping/uptimes/7d/badge.svg)](https://status.vapronva.pw/endpoints/websites-thatsaniceargumentunfortunatelly_thats-a-nice-argument-unfortunately-dot-com-backend-url-ping)
[![Website Uptime](https://status.vapronva.pw/api/v1/endpoints/websites-thatsaniceargumentunfortunatelly_thats-a-nice-argument-unfortunately-dot-com-frontend-url-ping/uptimes/7d/badge.svg)](https://status.vapronva.pw/endpoints/websites-thatsaniceargumentunfortunatelly_thats-a-nice-argument-unfortunately-dot-com-frontend-url-ping)
[![Continuous Integration](https://gitlab.vapronva.pw/vapronva/thats_a_nice_argument_unfortunately_dot_com-website/badges/main/pipeline.svg)](https://gitlab.vapronva.pw/vapronva/thats_a_nice_argument_unfortunately_dot_com-website/pipelines/latest)

# **[thats-a-nice-argument-unfortunately.com](https://ping.thats-a-nice-argument-unfortunately.com)** — Troll Website

> *yep, that's true. i know your ip. how'd you tell? oh, maybe 'cause here's all your info and location?*

## Why? & History

Saw [this meme](https://youtube.com/watch?v=wT0iWY0_-sI) on Discord one day — laughed so hard for several minutes straight.

A week passed, I decided to make a website for it. Bought the domain, but never got to making it, since ~~skill issue~~ didn't have time to proprely build it.\
After several more weeks passed, finally got to do it. In a few sprints, the website and the API were ready!

But it wouldn't see the light of day until I randomly sent the link as [a reply](https://canary.discord.com/channels/385387666415550474/755597803102928966/953044551457722388) to one of the Geoxor's message on his Discord server.


## What? & Screenshots

![Example of how the website looks upon the visit](https://static.images.vapronva.pw/_websites/thatsaniceargumentunfortunatelydotcom/screenshot-example-mcsshadow.png)

## How?

> Visitor's request comes in, the IP is extracted, API gateway checks if the result was cached, the request is made to the DB to check whether the strings were already generated, up to two requests are made to the IPInfo and ProxyCheck, random information is generated with faker and custom lists, the result is cached and the result is sent back to the visitor.

### Video Background

One night sitting with friends on Discord, I [recreated the video in 4K](https://live.vapronva.pw/e94d6b7e-49b5-45f4-97bb-6e26f684d4f8) transition by transition with KineMaster on a phone and perfected it frame by frame in Final Cut Pro.

Couldn't find the original anime artwork in the beginning of the video, so a New Year Linus picture was used instead.

### Wesbite

The website is built using *Boostrap 5*.\
It's pretty simple, yet very responsive.

JavaScript is used minimally, though required for text animations and API requests.

### API

The API is built in Python using [FastAPI](https://github.com/tiangolo/fastapi) and ton of [pydantic](https://github.com/samuelcolvin/pydantic/) models.\
MongoDB is used for the database.\
[faker](https://github.com/joke2k/faker) is used for the fake data generation.

It was one those projects where I tried to make everything perfect (documeneted every other detail, made models and caught all exceptions, etc)~~, but it's not perfect, let's be honest~~.

#### Third-party APIs

The project utilises the following third-party APIs:
1. [ipinfo.io](https://ipinfo.io)
2. [proxycheck.io](https://proxycheck.io)

Why those?\
Because have seen those been used in production by many companies, and they offer free API calls up to a certain point. Also, their privacy policy seemed good enough to use safely.

## Privacy Policy

Eveything's [stated](https://thats-a-nice-argument-unfortunately.com/ipp#privacy-policy) on the website.

Though, the *TL;DR* would be:
- I store your IPs
- I send your IP to the third-party APIs which I trust
- I store the responses from the third-party APIs
- I log minimally
- I collect analytics via first-party serivce
