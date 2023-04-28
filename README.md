# Bank Account (Python)
![enter image description here](https://res.cloudinary.com/dloadb2bx/image/upload/v1682645784/python3_x4gdei.png)

## Tecnologias utilizadas
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

This project was created using Docker to studying the basic concepts of Python learned at day 01 and day 02 in the 100 **Days of Code: The Complete Python Pro Bootcamp**.

## Summary
**Day 01:** Working with variables in Python to manage data
**Day 02:** Understanding Data Types and How to Manipulate Strings

**Plus:** To add some complexity I applied just on these beginning topics some conditional flow with while and if/else.

## How to run this project
This project was created with Docker, the Dockerfile is:

    FROM  python:3
    
    WORKDIR  /app
    
    COPY  .  .
    
    CMD  ["python",  "app/main.py"]

To run just download this project and run the follow commands:  `docker build -t bank-account .`  then run `docker run -it bank-account`. 