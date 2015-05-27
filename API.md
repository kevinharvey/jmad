# List Albums

 * URL: /api/albums/
 * HTTP Method: GET
 
## Example Response

    [
        {
            "name": "My Favorite Things",
            "slug": "my-favorite-things",
            "url": "http://jmad.us/api/albums/1/"
        },
        {
            "name": "Kind of Blue",
            "slug": "kind-of-blue",
            "url": "http://jmad.us/api/albums/2/
        }
        ...
    ]

# Get an Album with Tracks

 * URL: /api/albums/\<pk\>/
 * HTTP Method: GET
 
## Example Response

    {
        "name": "The Shape of Jazz to Come",
        "slug": "the-shape-of-jazz-to-come",
        "tracks": [
            {
                "name": "Lonely Woman",
                "track_number": 1,
                "slug": "lonely-woman",
                "url": "http://jmad.us/api/tracks/42/"
            }
            ...
        ] 
    }
    
# Get a Track with Solos

 * URL: /api/tracks/\<pk\>/
 * HTTP Method: GET
 
## Example Response

    {
        "name": "All Blues",
        "slug": "all-blues",
        "album": {
            "name": "Kind of Blue",
            "url": "http://jmad.us/api/albums/2/"
        },
        "solos": [
            {
                "artist": "Cannonball Adderley",
                "instrument": "saxophone",
                "start_time": "4:05",
                "end_time": "6:04",
                "slug": "cannonball-adderley",
                "url": "http://jmad.us/api/solos/281/"
            },
            ...
        ]
    }

# Add a Solo to a Track

 * URL: /api/solos/
 * HTTP Method: POST
 
## Example Request

    {
        "track": “/api/tracks/83/”,
        "artist": "Don Cherry",
        "instrument": "cornet",
        "start_time": "2:13",
        "end_time": "3:54"
    }
    
## Example Response

    {
        "url": "http://jmad.us/api/solos/64/",
        "artist": "Don Cherry",
        "slug": "don-cherry",
        "instrument": "cornet",
        "start_time": "2:13",
        "end_time": "3:54",
        "track": "http://jmad.us/api/tracks/83/"
    }
    
# Update a Solo

 * URL: /api/solos/\<pk\>/
 * HTTP Method: PATCH
 
## Example Request

    {
        "start_time": "1:46",
        "end_time": "4:04"
    }
    
## Example Response

    HTTP 200 OK
    {
        "artist": "Miles Davis",
        "instrument": "trumpet",
        "start_time": "1:46",
        "end_time": "4:04",
        "track": {
            "name": "All Blues",
            "url": "http://jmad.us/api/tracks/113/"
        }
    }
