# Smart Bus stop
  About smart Bus stop computing API
  This is an API to calculate bus arriving time 
  by using latitude and longitude from each bus stop with a bus contains, speed, diatance between bus stop and a bus.

## API Specs
  This is a RESTful API or called RESTful web service, more suitable in internet usages.
  
### Input and output for this API
  From code we have to specify location of each 4 bus stops in a form of latitude and longitude
  and convert to distance of each bus stops to meter (Thanks to [This forum](https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude)) 
 we've not complement with the bus stop model yet. This only generate the number to test and run API service.
 And output is estimated arriving time in minutes.
 
#### Response 
Will represent in JSON form.
```python
[
  {
    "name": "Smart bus Stop (Gas station)"
  }, 
  {
    "Destination": "Bus stop - Port"
  }, 
  {
    "time": {
      "Estimated arriving time in minutes": "5"
    }
  }
]
```
  
