# Alko project backend

A backend for displaying and fetching alcoholic beverages.

Just for fun and learning.

## Setting up project

### Install PostgreSQL

On MacOS with Homebrew

`brew install postgresql`

On Linux / Windows

Follow instructions [here](https://www.postgresql.org/download/)

### Install Poetry

https://python-poetry.org/

Run `poetry install` in project root

## Heroku related things

Ask to be added as a collaborator to the project.

### Install Heroku CLI

https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli

Run `heroku login`

Get the DB dump by running `heroku pg:pull postgresql-vertical-68691 <dbname> --app alko-project-backend`

`<dbname>` can be anything you specify e.g. `beerdb`. This will be your local db name.

Set the `DATABASE_NAME` and `DATABASE_USER` in `.env` for local development.

## Running the project

Run `uvicorn app.main:app --reload` in root folder

## Deployment

Pushes to `main` get deployed in Heroku
