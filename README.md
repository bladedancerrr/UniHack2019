# UniHack2019
Bayleef's project for UniHack 2019, an app that finds you the closest and least crowded workspace.

### Tech stack
Using chalice aws framework to host API with AWS Services including Lambda, API Gateway
Swift is used to write the app, Alamofire framework calls the API with latitude and longitude, returning a JSON with study/work space information

#### API information
* API endpoint: https://4132052exb.execute-api.us-east-1.amazonaws.com/api/

* API Usage

  You can run test_data in chalice/ OR run the following command (before that: `pip install httpie` if you don't have it)
  `
  echo '{"lat":-37.796773, "long":144.964456}' | http POST https://4132052exb.execute-api.us-east-1.amazonaws.com/api/getstudyspace
  `
  
  If anyone changes the codebase, please do testing and make sure it works, then ask Lexon to deploy chalice to update the API

#### Front end
note: Swift files and other front end code in Peter's repo https://github.com/YAOS5/ProjBL-1

### Repository directory information

Note: resources folder has the old implementation of getstudyspace without using chalice

Now the .py files and algorithms, google map popular times and the scrapers are in chalice/getstudyspace/chalicelib

