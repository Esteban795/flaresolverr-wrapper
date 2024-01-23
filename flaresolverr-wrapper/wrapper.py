from models import SessionsListResponse,SessionCreateResponse,FlaresolverrReady,PostRequestResponse
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
            "cmd" : "session.list"
        }
        response = self.session.post(self.proxy_url,params=params)
        print(response.content)
        response_json = response.json()
        if response_json.get("error") is not None:
            raise FlaresolverrError.from_dict(response_json)
        return SessionsListResponse.from_dict(response_json)
    
    def createSession(self, session_id : str = None) -> SessionCreateResponse:
        params = {
            "cmd" : "sessions.create"
        }
        if session_id:
            params["session"] = session_id
        response = self.session.post(self.proxy_url,json=params)
        response_json = response.json()
        print(response_json)
        if response_json["status"] != "ok":
            raise FlaresolverrError.from_dict(response_json)
        return SessionCreateResponse.from_dict(response_json)
    
