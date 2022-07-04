Recently I came across an interesting project called HTMX. See htmx.org In short, it allows Ajax functionality on a web page without a single Ajax calling.

Of course, behind the curtain still runs heavy Ajax code, but all plumbings are inside the lightweight htmx library. The declarative way you manipulate DOM frees you from tons of Ajax code under normal circumstances spoils HTML. Sure, you still need a little help from your backend to manipulate DOM, but logic is in standard Flask or FastApi routes, leaving HTML clean and tidy.

Examples in the official documentation are brisk, clean self-explaining. What caught my attention was SSE which, according to doc Server-Sent-Events are a way for servers to send events to browsers .

What is cool because you can, by a declarative way, push events from the backend directly to the browser. Now you have opened a new horizon for web online monitoring apps, messaging apps, e-commerce, and much more.

What is not clear from a doc is how to configure a working example combining frontend and Flask/FastApi backend. What I figured out, for SSE you should use the FastApi engine together with Jinja templating because SSE magic lies in sse_starlette package. I prepared the complete app that demonstrates FastApi-SSE hooking to the frontend for your benefit.

## Instalation

***************

1. Save downloaded scripts into any folder
2. Cd to script folder
3. Create and activate venv environment
4. Install dependecies from requirements.txt

    ```pip install -r requirements.txt```

## Running demo

***************

1. Cd to script folder
2. Activate venv environment
3. Run demo:

```py app.py```  

4. Go to URL <http://localhost:5000>

### Notes

********************************

- Demo runs once a time. To run demo again, refresh page
