# flaresolverr-wrapper
## A Python Wrapper for using Flaresolverr easily.


## Disclaimer 

- It was originally meant for me to use it for [this project](https://github.com/Esteban795/SushiscanScraper), but due to a discussion with people on the original Flaresolverr repo, being unable to download images through it was a dealbreaker for me.

### __What does it do__ ?

- It helps you encapsulate every request you need to make through [Flaresolverr](https://github.com/FlareSolverr/FlareSolverr), whether they are post or get requests. It also implements the sessions, as used by Flaresolverr.

### __Requirements__

- Flaresolverr. See the installation docker [here](https://github.com/FlareSolverr/FlareSolverr#installation).


### __How to install it on your computer ?__

- Just clone it wherever you want in your computer, using : 
```ps
git clone https://github.com/Esteban795/flaresolverr-wrapper.git
```

## __How to use it ?__
- Every argument with an equal after means it's optional, and there are default values.

```python
fs = Flaresolverr() #initialize a default instance
#or 
fs = Flaresolverr(host="ip adress",port="the port",protocol="protocol (http or https)",headers="headers",version="version endpoint. default is /v1")

#List of session can be accessed through 
sessions = fs.sessions

#You can create a session using :
response = fs.createSession(session_id="somethingsomething")

#Delete a session using
response = fs.deleteSession(session_id)

#Perform post and get requests using :
response = fs.get(url,session="yoursessionID",...) #lookup the other parameters
response = fs.post(url,post_data,session="yoursessionID")
```