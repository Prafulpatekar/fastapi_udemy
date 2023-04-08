
def log(tag="",message=""):
    with open('app.log','w+') as log:
        log.write(f"{tag}: {message}")