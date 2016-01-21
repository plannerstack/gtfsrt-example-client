# GTFS-RT Example Client

GTFS-RT is a standard to communicate about (public) transport data in Real Time.

This is a very simple GTFS-RT example client written in Python. It shows how to connect over websockets and start handling GTFS-RT messages received in the Protocol Buffer protocol.

While the client runs it will log *Alerts*, *Trip Updates* or *Vehicle Positions* depending on the content of the stream. This will look like long list of items like:

```
INFO     VEHICLE:
 latitude: 52.3706130981
 longitude: 4.87039995193

INFO     ALERT:
 translation {
  text: "Maatregelen : Geen \nMetro E rijdt op 12 feb van 23:30 uur niet tussen Leidschenveen en Den Haag. Gebruik pendelbus 63 HTM. Op 13 en 14 feb rijdt metro E niet Laan van NOI en Den Haag. Gebruik lijn 3/4 HTM.\n"
  language: "nl"
}

INFO     TRIP UPDATE:
 trip {
  trip_id: "28729980"
  start_time: "17:35:00"
  start_date: "20160121"
  schedule_relationship: SCHEDULED
  route_id: "18998"
}
```

## Prerequisites

This example client expects python >2.7 and pip to be installed on the system.

## Installation

1) Clone this example client

```
git clone https://github.com/plannerstack/gtfsrt-example-client.git
```

2) Install its requirements with pip, make a virtualenv first if you want.

```
pip install -r requirements.txt
```

### Troubleshooting

* Not sure how to set up a vrtualenv, or not sure what it is? Read: http://docs.python-guide.org/en/latest/dev/virtualenvs/ 

## Running

Run the example client by defining the stream as a environment variable and starting the process with python.

```
stream="ws://gtfsrt.plannerstack.com:8089/tripUpdates" python gtfsrt-example-client.py
```

For available demo streams see the docs at [docs.plannerstack.org](http://docs.plannerstack.org/). You can alos join us on our Slack channel to get in direct contact. Visit: [slack.plannerstack.org](http://slack.plannerstack.org)

## Development

This is only a simple example client to get some GTFS RT quickly on your screen. It can provide pointers to what is needed, but is not meant to be used as a base for any further development.

### Third party libraries and Standards

* Python Protocol Buffers: https://developers.google.com/protocol-buffers/docs/pythontutorial
* GTFS-RT standard: https://developers.google.com/transit/gtfs-realtime/

## Tests

* Non existent in this example.

## Credits

* Jasper Hartong - PlannerStack - 2016

## License

```
The MIT License (MIT)

Copyright (c) 2016 PlannerStack

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```