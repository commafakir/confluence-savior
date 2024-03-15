 # CoFlUEnCE Savior

 Run with

```
pip install -r requirements.txt
uvicorn server:app --reload
```

Pray the bit gods, because this is couple of hours POC.

Head to `localhost:8000` and see the amazing (htmx!) UI.

## The Scope

You hate confluence. You don't hate the confluence because what confluence is. You hate it because it contains outdated information. And even worse, it contains conflicting information.

The idea was that if we could fix some pages in confluence to be exact and true, could we leverage AI to detect pages which contain conflicting information.

At this initial stage this implementation merely tells if some pages are conflicting or not and why they are conflicting. The big idea would naturally be to examine the whole document base.

