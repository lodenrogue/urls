# Extract URLs

Extract urls from stdin

## Usage 

```
$ command | python3 urls.py
```

Example:

```
$ curl -s https://www.google.com | python3 urls.py
```

Output:

```
curl -s https://www.google.com | python3 urls.py
http://schema.org/WebPage
https://www.google.com/imghp?hl=en&tab=wi
...
```
