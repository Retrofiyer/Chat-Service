<div>
    <h1>Chat Microservice</h1>
</div>

## About The Project

The Chat Service microservice provides a real-time chat solution where users can join specific rooms and communicate with others in the same room. Built using Python and WebSockets, this service aims to offer a seamless and interactive chat experience with minimal latency and high performance.

## Table of Contents

<ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#configuration">Configuration</a></li>
        <li><a href="#running-the-service">Running the service</a></li>
      </ul>
    </li>
    <li>
      <a href="#contributing">Contributing</a>
    </li>
 </ol>

## Overview

The Chat Service is a lightweight Python-based microservice that facilitates real-time messaging between users. It supports multiple chat rooms, allowing users to join rooms and exchange messages instantly. This service is built to be easy to deploy and integrate with other applications.

## Features

<div>
  <ul>
      <li> <b>Real-Time Messaging:</b> Send and receive messages instantly using WebSockets.</li>
      <li> <b>Multiple Rooms:</b> Users can join specific rooms and chat with others in the same room.</li>
      <li> <b>Connection Management:</b> Handle user connections and disconnections gracefully.</li>
  </ul>
</div>


## Built With

[![Python][python.com]][python-url]
[![Docker][docker.com]][docker-url]

<!-- GETTING STARTED -->
## Getting Started

## Prerequisites

Before you begin, make sure you have the following tools installed on your machine:

- **Python 3.12.5 or higher** - [Download Python](https://www.python.org/downloads/)

If you don't have any of these tools installed, follow the provided links to install them.


## Installation

1.- Clone the repository
   ```sh
   git clone https://github.com/Retrofiyer/Chat-Service.git
   cd Chat-Service
   ```
2.- Create a virtual environment and install dependencies
 ```sh
    python -m venv .venv
    source .venv/bin/activate   # On Windows, use `.venv\Scripts\activate`
    pip install -r requirements.txt
   ```

## Configuration

The Chat Service does not require specific configuration files. However, ensure your environment is set up to allow WebSocket connections.

## Running the service

  ```sh
    python run.py
   ```

## Contributing

I would like you to contribute to this project. Whether it's fixing a bug, adding a new feature or improving the documentation, your help is always welcome. Please email me at `sebitas5225@gmail.com` with all the details for improvement.

<!-- LINKS & IMAGES -->

[docker.com]: https://img.shields.io/badge/Docker-black?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[python.com]: https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/