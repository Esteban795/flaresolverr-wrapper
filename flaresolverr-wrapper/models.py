from typing import List
from dataclasses import dataclass

@dataclass   
class FlaresolverrReady:

    start_timestamp: int
    end_timestamp: int
    version : int
    status : str
    message : str

    @classmethod
    def from_dict(cls, data : dict) -> 'FlaresolverrReady':
        return cls(data['status'], data['message'])
    
@dataclass
class SessionsListResponse:
    start_timestamp : int
    end_timestamp : int
    version : int
    status : int
    message : int
    sessions : int

    @classmethod
    def from_dict(cls, data : dict) -> 'SessionsListResponse':
        return cls(data['start_timestamp'], data['end_timestamp'], data['version'], data['status'], data['message'], data['sessions'])

@dataclass
class SessionCreateResponse:
    start_timestamp : int
    end_timestamp : int
    version : int
    status : int
    message : int
    session : int

    @classmethod
    def from_dict(cls, data : dict) -> 'SessionCreateResponse':
        return cls(data['startTimestamp'], data['endTimestamp'], data['version'], data['status'], data['message'], data['session'])
    
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

@dataclass
class PostRequestResponse:
    start_timestamp : int
    end_timestamp : int
    version : int
    status : int
    message : int
    solution : Solution

    @classmethod 
    def from_dict(cls, data: dict) -> 'PostRequestResponse':
        return cls(
            data['start_timestamp'],
            data['end_timestamp'],
            data['version'],
            data['status'],
            data['message'],
            Solution.from_dict(data['solution'])
        )