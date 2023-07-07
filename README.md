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
http://schema.org/WebPage
https://www.google.com/imghp?hl=en&tab=wi
https://maps.google.com/maps?hl=en&tab=wl
https://play.google.com/?hl=en&tab=w8
https://www.youtube.com/?tab=w1
...
```
