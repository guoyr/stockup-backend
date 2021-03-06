from tornado.options import  define

TEST_IPAD_TOKEN = 'bead382dc014c9f73246f9f5b6d606ddf87b1237701eca8e743cf3641089c79d'

COOKIE_KEY = "2BGQuaOqQwOOjPRhuYwgk95iG767I0xPmstRiVNMzDg="


DEBUG = True

define("port", default=8000, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode", type=bool)
define("run_crawler", default=True, help="run the crawler", type=bool)
define("run_server", default=True, help="run the server", type=bool)
define("cookie_secret", default=COOKIE_KEY,
       help="the key to generate secure cookies", type=str)
define("dbhost", default="119.29.16.193", help="mongodb host ip address ", type=str)
define("skip", default=0, help="start line in stocks_all.txt", type=int)
define("limit", default=256, help="number of stocks to lookup", type=int)
define("maxConnections", default=256,
       help="max number of open connections allowed", type=int)
define("interval", default=2470*30, help="fetch data interval in ms", type=int)
define("segmentSize", default=20, help="batch size of each request to sina",
       type=int)

def debug_log(logger, msg):
    if DEBUG:
        logger.info(msg)


def datetime_repr():
    return '%Y-%m-%dT%H:%M:%S'
