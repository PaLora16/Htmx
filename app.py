from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from sse_starlette.sse import EventSourceResponse
import time

app = FastAPI()

templates = Jinja2Templates(directory="templates")


class GenClass():
    """ Create stream of events which payload is binded to HTML element

    Yields:
        event
    """
    response = ""
    source = ""

    def generator(self):
        if self.source:
            self.source = self.source.upper()
            for x in self.source:
                self.response += x
                yield {
                    # binding event name to HTML element
                    "event": "animated",
                    # event payload to HTML element
                    "data": self.response
                }
                # simulate delay from backend
                time.sleep(0.5)
        # stop animation after one cycle, otherwise endless loop
        if self.source == self.response:
            self.source = ""
            self.response = ""


gen = GenClass()


@app.get("/event_source")
async def generate_events():
    # connect generated events to UI
    return EventSourceResponse(gen.generator())


@app.post("/run/", response_class=HTMLResponse)
def run_animation(text_to_animate: str = Form(...)):
    # value from form text input feeded to generator
    gen.source = text_to_animate


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # templated index.html
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=5000)
