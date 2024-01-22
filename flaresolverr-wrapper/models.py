from typing import List
from dataclasses import dataclass

@dataclass
class Response:
    start_timestamp: int
    end_timestamp: int
    version : int
    status : str
    
    @classmethod
    def from_dict(cls, data : dict) -> 'Response':
        return cls(data['start_timestamp'], data['end_timestamp'], data['version'], data['status'])
    
class FlaresolverrOK(Response):

    def __init__(self,start_timestamp : int ,end_timestamp : int, version : int,status : int,message : int) -> None:
        super().__init__(start_timestamp,end_timestamp,version,status)
        self.message = message

    @classmethod
    def from_dict(cls, data : dict) -> 'FlaresolverrOK':
        return cls(data['start_timestamp'], data['end_timestamp'], data['version'], data['status'], data['message'])
    
class SessionListResponse(Response):
    
    def __init__(self,start_timestamp : int ,end_timestamp : int, version : int ,status : int ,message : int ,sessions : int) -> None:
        super().__init__(start_timestamp,end_timestamp,version,status)
        self.sessions = sessions
        self.message = message

    @classmethod
    def from_dict(cls, data : dict) -> 'SessionListResponse':
        return cls(data['start_timestamp'], data['end_timestamp'], data['version'], data['status'], data['message'], data['sessions'])
    
class SessionCreateResponse(Response):
    
    def __init__(self,start_timestamp : int,end_timestamp : int, version : int,status : int,message : int,session : int) -> None:
        super().__init__(start_timestamp,end_timestamp,version,status)
        self.session = session
        self.message = message

    @classmethod
    def from_dict(cls, data : dict) -> 'SessionCreateResponse':
        return cls(data['start_timestamp'], data['end_timestamp'], data['version'], data['status'], data['message'], data['session'])
    
@dataclass
class Solution:

    url : str
    status : int
    cookies : dict 
    user_agent : str
    headers : dict
    response : str

    @classmethod
    def from_dict(cls, data : dict) -> 'Solution':
        return cls(data['url'], data['status'], data['cookies'], data['user-agent'], data['headers'], data['response'])


class PostRequestResponse(Response):

    def __init__(self,start_timestamp : int, end_timestamp : int,version : str, status : str, message : str, solution : Solution) -> None:
        super().__init__(start_timestamp,end_timestamp,version,status)
        self.message = message
        self.solution = solution

    @classmethod 
    def from_dict(cls, data: dict) -> Response:
        return cls(
            data['start_timestamp'],
            data['end_timestamp'],
            data['version'],
            data['status'],
            data['message'],
            Solution.from_dict(data['solution'])
        )