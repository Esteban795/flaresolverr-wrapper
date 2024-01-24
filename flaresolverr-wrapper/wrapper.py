from models import SessionsListResponse,SessionCreateResponse,SessionDeleteResponse,FlaresolverrReady,PostRequestResponse
from exceptions import FlaresolverrError,ProxyNotFound


from typing import Union, Optional,Literal,List
from urllib.parse import urlencode
import requests

TEST_URL = "https://nowsecure.nl/"


class Flaresolverr:
    
    def __init__(self,
                 host : str = "127.0.0.1",
                 port : Optional[Union[int,str]] = 8191,
                 protocol : Literal["http","https"] = "http",
                 headers : dict = {},
                 version : str = "v1"
                ) -> None:
        self.session = requests.Session()
        self.headers = headers
        self.session.headers.update = {"Content-Type": "application/json",**self.headers}
        self.host = host
        self.port =  str(port)
        self.protocol = protocol
        self.version = version
        self.proxy_url = f"{self.protocol}://{self.host}:{self.port}/{self.version}"
        
    def checkFSOnline(self) -> bool:
        """Check if the proxy is online"""
        data = {
            "cmd" : "request.get",
            "url" : TEST_URL,
            "maxTimeout" : 10000
        }
        try:
            response = self.session.post(self.proxy_url,json=data)
            response_json = response.json()
            if response_json.get("status") == "ok":
                print("FlareSolverr is online and working.")
                return True
        except requests.exceptions.ConnectionError:
            raise ProxyNotFound("Proxy is not online. Please start FlareSolverr.")
    
    @property
    def sessions(self) -> List[str]:
        params = {
            "cmd" : "sessions.list"
        }
        response = self.session.post(self.proxy_url,json=params)
        response_json = response.json()
        if response_json.get("error") is not None:
            raise FlaresolverrError.from_dict(response_json)
        return SessionsListResponse.from_dict(response_json).sessions
    
    def createSession(self, session_id : str = None) -> SessionCreateResponse:
        params = {
            "cmd" : "sessions.create"
        }
        if session_id:
            params["session"] = session_id
        response = self.session.post(self.proxy_url,json=params)
        response_json = response.json()
        if response_json["status"] != "ok":
            raise FlaresolverrError.from_dict(response_json)
        return SessionCreateResponse.from_dict(response_json)
    
    def deleteSession(self, session_id : str) -> SessionDeleteResponse:
        params = {
            "cmd" : "sessions.destroy",
            "session" : session_id
        }
        response = self.session.post(self.proxy_url,json=params)
        response_json = response.json()
        if response_json.get("error") is not None:
            raise FlaresolverrError.from_dict(response_json)
        response_json["session"] = session_id
        return SessionDeleteResponse.from_dict(response_json)
    
    def _perform_post_request(self, params : dict) -> PostRequestResponse:
        response = self.session.post(self.proxy_url,params=params)
        response_json = response.json()
        if response_json.status != "ok":
            raise FlaresolverrError.from_dict(response_json)
        return PostRequestResponse.from_dict(response_json)
    
    def _add_optional_args(self, params : dict, session, session_ttl, cookies) -> PostRequestResponse:
        if session:
            params["session"] = session
        if session_ttl:
            params["sessionTTL"] = session_ttl
        if cookies:
            params["cookies"] = cookies
        return self._perform_post_request(params)
    
    def get(self,url : str,session : str = None, session_ttl : int = None, max_timeout : int = None, cookies : List[dict] = None,only_cookies : bool = False):
        params = {
            "cmd" : "request.get",
            "url" : url,
            "maxTimeout" : max_timeout,
            "returnOnlyCookies" : only_cookies
        }
        return self._add_optional_args(params, session, session_ttl, cookies,)


    def post(self,url : str,post_data : dict,session : str = None, session_ttl : int = None, max_timeout : int = None, cookies : List[dict] = None,only_cookies : bool = False):
        params = {
            "cmd" : "request.post",
            "url" : url,
            post_data : urlencode(post_data),
            "maxTimeout" : max_timeout,
            "returnOnlyCookies" : only_cookies
        }
        return self._add_optional_args(params, session, session_ttl, cookies)
    

if __name__ == "__main__":
    fs = Flaresolverr()
    headers = {
        "Connection" : "keep-alive"
    }
    fs.checkFSOnline()
    fs.createSession("1")
    print(fs.sessions)
    fs.deleteSession("1")
    print(fs.sessions)