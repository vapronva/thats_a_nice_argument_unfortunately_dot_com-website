# **[thats-a-nice-argument-unfortunately.com](https://thats-a-nice-argument-unfortunately.com)** — Troll Website

> _yep, that's true. i know your ip. how'd you tell? oh, maybe 'cause here's all your info and location?_

## Why? & Origin

Saw [a particularly amusing meme](https://youtube.com/watch?v=wT0iWY0_-sI) on Discord one day, and laughed my ass off for several minutes straight.

A week lapsed... And I finally decided to make a website for it: domain was secured, yet the site's development was delayed due to a ~~skill issue~~ time constraints somewhere else. \
Weeks evolved into months, and with a burst of determination, the website and its accompanying API materialized.

But it wouldn't see the light of day until I randomly sent the link as [a reply](https://discord.com/channels/385387666415550474/755597803102928966/953044551457722388) to one of the Geoxor's message on his Discord server.

## What? & Screenshots

![sneak peek of the website upon entry](./_assets/screenshot-example-mcsshadow-1.png)

## How?

> Visitor's request comes in, the IP is extracted, API gateway checks if the result was cached, the request is made to the DB to check whether the strings were already generated, up to two requests are made to the IPInfo and ProxyCheck, random information is generated with faker and custom lists, the result is cached and the result is sent back to the visitor.

### Video Background

One night sitting with friends on Discord, I [recreated the video in 4K](https://peertube.vapronva.pw/w/7QQnoMUr9B8a2AiPV9coi4) transition by transition with KineMaster on a phone and perfected it frame by frame in Final Cut Pro.

Couldn't find the original anime artwork in the beginning of the video, so a New Year Linus picture was used instead.

### Wesbite

The website is built using _Boostrap 5_. \
It's pretty simple, yet very responsive.

JavaScript is used minimally, though required for text animations and API requests.

### API

The API is built in Python using [FastAPI](https://github.com/tiangolo/fastapi) and ton of [pydantic](https://github.com/samuelcolvin/pydantic) models. \
MongoDB is used for the database. \
[faker](https://github.com/joke2k/faker) is used for the fake data generation.

It was one those projects where I tried to make everything perfect (documeneted every other detail, made models and caught all exceptions, etc)~~, but it's not perfect, let's be honest~~.

#### Third-party APIs

The project utilises the following third-party APIs:

1. [ipinfo.io](https://ipinfo.io)
2. [proxycheck.io](https://proxycheck.io)

Why those? \
Because have seen those been used in production by many companies, and they offer free API calls up to a certain point. Also, their privacy policy seemed good enough to use safely.

## Privacy Policy

The full [Privacy Policy](https://thats-a-nice-argument-unfortunately.com/ipp#privacy-policy) is detailed on the website.

In essence:

- Your IP is logged
- Said IP is shared with trusted third-party APIs
- Their \[3P\] responses are stored
- Logging is kept to the bare minimum
- Analytics are collected exclusively in-house
