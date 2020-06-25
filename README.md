
[![Maintainability](https://api.codeclimate.com/v1/badges/73be1cbdf6bd4131d763/maintainability)](https://codeclimate.com/github/Lambda-School-Labs/quake-ds-pt9/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/73be1cbdf6bd4131d763/test_coverage)](https://codeclimate.com/github/Lambda-School-Labs/quake-ds-pt9/test_coverage)


# Epicentral

You can find the project at [Epicentral on Heroku](https://epicentral.herokuapp.com/).

## Contributors

|[Tally Wiesenberg](https://github.com/tallywiesenberg)||[Rob LeCheminant](https://github.com/lechemrc)                                        |[Jerimiah Willhite](https://github.com/razzlestorm)|  

|[<img src="https://avatars0.githubusercontent.com/u/37545969?s=400&u=c6b3b2110b672bd025f071825b38090d4a3eae08&v=4" width = "200" />](https://github.com/lechemrc)                       |                      [<img src="https://avatars0.githubusercontent.com/u/32030231?s=460&u=79b4a80f17718ff4802beffa14816964ebe6ce86&v=4" width = "200" />](https://github.com/razzlestorm) 
|[<img src="https://avatars2.githubusercontent.com/u/52666297?s=400&u=5c1d3e3d7a0b53e23ee63de81cab1af7d563678b&v=4" width = "200" />](https://github.com/tallywiesenberg)

[ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/tally-wiesenberg-5a4505159/)                                         |                       [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/robert-lecheminant-21315b60/)                       |                       [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/jerimiah-willhite/) |  


:-----------------------------------------------------------------------------------------------------------: |


## Project Overview


[Trello Board](https://trello.com/b/Ja41ROfX/quake)

[Product Canvas](https://www.notion.so/Vision-Problem-Objectives-2a47f1d8f3e54b2db4d4c119c3e3b5fe)

Earthquake data is spread out on the internet and finding up-to-date data on your location involves sifting through complicated user interfaces and technical jargon. Personal safety and earthquake/emergency resources shouldn't be this hard to find. Knowledge about earthquakes also should also be more available, so people can manage their risk appropriately.

Earthquake data is spread out on the internet and finding up-to-date data on your location involves sifting through complicated user interfaces and technical jargon. Personal safety and earthquake/emergency resources shouldn't be this hard to find. Knowledge about earthquakes also should also be more available, so people can manage their risk appropriately.

Epicentral intends to centralize Earthquake data on an accessible, easy-to-understand platform. The center of the project is a live map that reports the magnitude of recent earthquakes. Later iterations will include SMS notifications of earthquakes and predictions of aftershocks.

[Deployed Front End](https://epicentral.herokuapp.com/)

### Tech Stack

Python, geopandas, flask, Folium, leaflet, numpy, pandas, pytorch, scikit-learn

### Predictions

 This is scheduled for RC3

### Explanatory Variables

-   Scheduled for RC3

### Data Sources

-   [USGS Geojson](https://earthquake.usgs.gov/earthquakes/feed/v1.0/)
-   [USGS Centennial Report](https://earthquake.usgs.gov/data/centennial/)
-   [Folium](https://python-visualization.github.io/folium/)


### How to connect to the data API  

The Flask app currently has four routes that can be used by the Front End or other users to both store and access data:  
  * /grabquakes:  
     * This pulls earthquakes from the USGS api and stores them in the Heroku database. This currently pulls every 24 hours from USGS's day-long geojson api and includes all earthquakes (https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson).  
  * /map:  
     * This displays a Folium map with the earthquake information in the database.  
  * /getquakes:  
      * This returns all earthquake data by default, but can be filtered with string queries, with the 'mag' and 'date' arguments allowed.  
      * Expected values for 'mag' are: any float.  
      * Expected values for 'date' are: w, 2w, or m.  
      * These stand for 'week', '2 weeks', and 'month' respectively.  
  * /emergency/<city>:  
      * This route looks up the name of the city passed into it, and returns a summarization of the city's official earthquake emergency                  preparedness-related website.  
    
### How to Reproduce locally

Run the following commands to install all necessary packages:

```
conda create --name quake python==3.7
conda activate quake
conda install -c conda-forge --file requirements.txt
```
## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](https://github.com/Lambda-School-Labs/quake-be-pt9/blob/master/README.md) for details on the backend of our project.

See [Front End Documentation](https://github.com/Lambda-School-Labs/quake-fe-pt9/blob/master/README.md) for details on the front end of our project.
