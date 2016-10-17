@echo off
color 0b
title Mongo DB
mongod --dbpath C:\git\HaBoger\mongodb_data

REM IMPORT DB:
REM mongoimport --db test --collection restaurants --drop --file ~/downloads/primer-dataset.json
