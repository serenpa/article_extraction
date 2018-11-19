import article_extraction
	
def main():

	URL = "https://www.joelonsoftware.com/2006/09/01/language-wars/"

	data = article_extraction.full_extraction(URL)

    print("Full HTML: ", data["html"])
	print("Article text: ", data["pattern_extraction"]["article_text"])

if __name__ == '__main__':
	main()
