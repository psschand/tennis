# Tennis data crud
A simple CRUD application using Flask,MySQL and docker

### Built With

* Python
* Python Libraries: flask and pymysql
* MySQL
* AdminLTE 2

### Running on Docker

```
docker-compose up -d
```

After executing, you will have 2 running cointainers on your Docker host: `book-app` and `book-mysql`. For accessing the web application, open your browser and go to http://your-docker-host-ip-address:8181

To destroy the containers, execute:

```
docker-compose down --rmi all
```


### Batch API Request 

Post API endpoint
http://your-docker-host-ip-address:8181/batch
with below sample data format

[
   {
    "ATP": "11",
    "Court": "Brisbane International",
    "Date": "02-01-2011",
    "Location": "ATP250",
    "Loser": "Outdoor",
    "Round": "Hard",
    "Series": "1st Round",
    "Surface": "49",
    "Tournament": "Istomin D.",
    "Winner": "De Bakker T."
},

   {
    "ATP": "12",
    "Court": "Brisbane International",
    "Date": "02-01-2011",
    "Location": "ATP250",
    "Loser": "Outdoor",
    "Round": "Hard",
    "Series": "2nd Round",
    "Surface": "49",
    "Tournament": "Berrer M.",
    "Winner": "Sela D."
},
   {
    "ATP": "13",
    "Court": "Chennai",
    "Date": "02-01-2016",
    "Location": "ATP250",
    "Loser": "Outdoor",
    "Round": "Hard",
    "Series": "2nd Round",
    "Surface": "49",
    "Tournament": "Berdych T.",
    "Winner": "Phau B."
}
]


#Result
[{"response": "successful"}, {"response": "successful"}, {"response": "successful"}]