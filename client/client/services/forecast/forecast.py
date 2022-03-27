from ..base import BaseService


class Forecast(BaseService):

    def __init__(self, endpoint, loader, credentials, s3_endpoint):
        super().__init__(endpoint, loader, credentials, s3_endpoint)

    def create_predictor(self, name, algorithm, forecast_horizon,
                         bucket_name, perform_hpo=False):
        api_params = self._create_api_params(name, algorithm, forecast_horizon,
                                             bucket_name, perform_hpo)
        return self._make_api_call(api_params)

    def _create_api_params(self, name, algorithm, forecast_horizon,
                           bucket_name, perform_hpo):
        return {
            'name': name,
            'algorithm': algorithm,
            'forecast_horizon': forecast_horizon,
            'bucket_name': bucket_name,
            'perform_hpo': perform_hpo
        }
