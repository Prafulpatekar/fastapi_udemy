from fastapi.requests import Request
def log(tag="",message="",request:Request=None):
    with open('app.log','a+') as log:
        log.write(f"\n{tag}: {message}\n")
        log.write(f"\t{request.url}")