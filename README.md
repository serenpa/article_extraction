# Article extraction

A collection of functions that can be used for extracting HTML and article text from a URL.

## Example 1
Take the following URL:

```python
    URL = "https://www.joelonsoftware.com/2006/09/01/language-wars/"
```

Using the library, the article text and HTML can be extracted:

```python
    data = article_extraction.full_extraction(URL)

    print("Full HTML: ", data["html"])
	print("Article text: ", data["pattern_extraction"]["article_text"])
```

## Functions

| Function | Explaination |
| ------ | ------ |
| get_html(url) | Given a URL, will return the HTML using urllib3. |
| pattern_article_extraction(url) | Extract the article using Pattern. Pattern uses the url, not the HTML. |
| full_extraction(url) | Runs a complete end-to-end extraction using all other functions. |



## License
MIT
