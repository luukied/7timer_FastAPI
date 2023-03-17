# 7timer FastAPI
FastAPI calling 7timer to generate time-series response

## Container overview
```

                      ________container________
                     |                         |
Exposed port   80 <-:|:-> 0.0.0.0:80           |
                     |_________________________|

<--|--> = volume mount
---|-->$ = environment variable
<-:|:-> = port forward					 
```

## Run container
You can run the container by `docker compose up` or 
`docker build -t weather-api . && docker run -p 80:80 weather-api:latest`

## API request
The API can be called by URL `http://127.0.0.1/weather?lon=4.463179&lat=51.922893` for e.g. Rotterdam. The request requires `lon` and `lat` parameters.
