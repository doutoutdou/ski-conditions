# ski-conditions

# Installation
## Tutorials
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

## Command
To install all dependencies : 
``
pip install -r requirements.txt
`` 

To update dependency file after adding 
``
pip freeze > requirements.txt 
``

## Run the application
Run the application : 

``` shell
uvicorn app:app
```

With debug : 
``` shell
uvicorn app:app --reload
```

## API
### Base path
Base path used is `/api/v1`

### Endpoints
`/conditions`  
`/ui`

## Documentation 
TODO

