
def log(tag="",message=""):
    with open('app.log','a') as log:
        log.write(f"\n{tag}: {message}")