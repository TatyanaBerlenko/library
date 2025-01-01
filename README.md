# Library project

## Description

An application in which users can manage their bibliography: add, delete and edit books.

## Link

[Welcome!](https://library-production-a9cd.up.railway.app/)

## Setup

```
docker build -t library_image .
docker run --name library -p 8080:8080 -v $(pwd):/app library_image
```

## Requirements

Flask, flask_sqlalchemy

## Features

* User can add, edit and delete books
* Books are shown in a list for each user 

## Git

main

## Success Criteria

* User can add, edit and delete books

## Video

[Demo](https://drive.google.com/file/d/1mW4zVfYCT0gcEJdbJOa7y7ck9mCzFgGE/view?usp=sharing)