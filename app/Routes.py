from flask import jsonify
from app.modules.MerchantsGuide import MerchantsGuide
from app.modules.Sample import SampleA
from app.modules.SampleB import SampleB


class Routes:

    def set_route(self, app):

        @app.route('/')
        def home():
            return 'It works!'\

        @app.route('/sample-module-a')
        def sampleA():
            sample = SampleA()
            return sample.fooSampleA()

        @app.route('/sample-module-b')
        def sampleB():
            sample = SampleB()
            return sample.fooSampleB()

        # @app.route('/mg-api/<query>')
        # def converter(query):
        #     m = MerchantsGuide()
        #     query = m.url_to_query(query)
        #     result = m.converter(query)
        #
        #     jsonResult = {}
        #
        #     if result is not False:
        #         jsonResult["status"] = "success"
        #         jsonResult["value"] = str(result)
        #     else:
        #         jsonResult = {"status": "error", "value": "invalid query"}
        #
        #     return jsonify(jsonResult)
