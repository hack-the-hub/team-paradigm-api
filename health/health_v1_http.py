import pyrestful.rest
from pyrestful import mediatypes
from pyrestful.rest import get
import tornado.web
from vb_util import encoder


class HealthResource(pyrestful.rest.RestHandler):

    @get(_path="/health", _types=[], _produces=mediatypes.APPLICATION_JSON)
    def get_health(self):
        """
        @api {get} /health Read Health
        @apiName GetHealth
        @apiGroup Health
        @apiVersion 1.0.0
        @apiDescription Returns the health of the API.

        @apiSuccess {String} status active

        @apiExample {curl} Example usage:
            curl -i http://localhost:8000/health

        @apiSampleRequest http://localhost:8000/health
        """

        return {'status': 'active'}
