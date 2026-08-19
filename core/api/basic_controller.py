import requests
class BasicController:
    @staticmethod
    def _execute_request(method, url, params=None, data=None, json=None, headers=None, files=None, cookies=None):
        # request_attr = getattr(requests, method)
        # if method == "get" => requests.get
        # if method == "post" => requests.post

        response = getattr(requests, method)(url=url, params=params,
                                             data=data, json=json, headers=headers, files=files, cookies=cookies)

        return response