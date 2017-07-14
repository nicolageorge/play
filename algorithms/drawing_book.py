import sys

number_pages = int(raw_input().strip())
page_no = int(raw_input().strip())

print min(page_no/2, number_pages/2 - page_no/2)
