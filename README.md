# UniHack2019
Bayleef's project for UniHack 2019, an app that finds you the closest and least crowded workspace.

### Tech stack
Using chalice aws framework to host API with AWS Services including Lambda, API Gateway
Swift is used to write the app, Alamofire framework calls the API with latitude and longitude, returning a JSON with study/work space information

### Directory information

Note: resources folder has the old implementation of getstudyspace without using chalice

Now the .py files and algorithms, google map popular times and the scrapers are in chalice/getstudyspace/chalicelib
