class FlaresolverrError(Exception):
    def __init__(self, status : str, version : str, err : str) -> None:
        super().__init__(err)
        self.status = status
        self.version = version
        self.err = err
    
    @classmethod
    def from_dict(cls, data : dict) -> FlaresolverrError:
        return cls(data['status'], data['version'], data['error'])
