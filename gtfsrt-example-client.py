import os
import logging
from websocket import create_connection
from time import time
from datetime import datetime
from protobuf import gtfs_realtime_pb

logging.basicConfig(level=5, format='%(levelname)-8s %(message)s')


class Client():

    def __init__(self, websocket_url):
        self.stats = {'start': time(), 'total_messages': 0}
        self.websocket_url = websocket_url
        self.feed_message = gtfs_realtime_pb.FeedMessage()

    def listen(self):
        self._connect()
        
        while True:
            try:
                data = self.connection.recv()
            except:
                logging.info('\nConnection lost')
                self.connection.close()
                self._connect()
                data = self.connection.recv()

            try:
                self.feed_message.ParseFromString(data)
                self._handle_feed_message()
                self._log_stats()
            except:
                logging.error('\nParsing failed')


    def _connect(self):
        logging.info('\nConnecting with: %s' % self.websocket_url)
        self.connection = create_connection(self.websocket_url)
        logging.info('\nConnected with: %s' % self.websocket_url)

    def _handle_feed_message(self):
        for feed_entity in self.feed_message.entity:
            if feed_entity.HasField('alert'):
                logging.info("ALERT: \n %s" % feed_entity.alert.description_text)
            elif feed_entity.HasField('vehicle'):
                logging.info("VEHICLE: \n %s" % feed_entity.vehicle.position)
            elif feed_entity.HasField('trip_update'):
                logging.info("TRIP UPDATE: \n %s" % feed_entity.trip_update)
                pass
            else:
                logging.error('Unhandled field entity type')
                pass

    def _log_stats(self):
        now = time()
        self.stats['total_messages'] += 1
        logging.info('''\nNow: %(now)s
                        \nTotal uptime: %(uptime)s
                        \nTotal Messages: %(total_messages)s''' %
            {   'now': str(now),
                'uptime': now - self.stats['start'],
                'total_messages': self.stats['total_messages']
            })


if __name__ == '__main__':
    websocket_url = os.environ.get('stream')
    if websocket_url is None:
        logging.error('No `stream` environment variable defined. Try starting this with: \n\n`stream="ws://server.com:port/tripUpdates" python gtfsrt-example-client.py`')
    else:
        client = Client(websocket_url)
        try:
            client.listen()
        except KeyboardInterrupt:
            logging.error("Caught KeyboardInterrupt, disconnecting from %s" % websocket_url)
            client.connection.close()
