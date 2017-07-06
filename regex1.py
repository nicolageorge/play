import re, string

# print re.split('\W+', 'words, words, Words, ords treesm,! asd,Woards, words')

# print re.split('(\W+)', 'Words words, workds.wrods')

# print re.split('\W+', 'words , wordsl , words, sadowa, ', 2)

# print re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)

# print re.split('(?<=pula)\w+', 'pula pula doua trei pula pa PUla PuLa da PPULA PULA', flags=re.IGNORECASE)

# print re.escape('python.exe')

# legal_chars = string.ascii_lowercase + string.digits + string.ascii_uppercase  + "mm#$W+"
# print re.escape(legal_chars)


# operators = ['+', '-', '*', '/', '**']
# print re.escape('   separator '.join(operators))


pattern = re.compile("[a-g]")
print pattern.findall("dogdogdohdog", 0, 4)
