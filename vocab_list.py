import pyfiglet

def info():
	print("---------------------------------------------------------------------------------------------------------------------------------")
	print(pyfiglet.figlet_format("Vocab List \n Generator"))
	print("---------------------------------------------------------------------------------------------------------------------------------")
	print("- Enter a list of words and this program will return their definitions from Google, Oxford or Wikipedia - Whichever \nis available(in that order)")
	print("- As this program is still in alpha, the software might not be stable. Please contact the developer if you face any bugs :)")
	print()
	print("Alpha version 0.2.5")
	print("This version now comes with an update feature that automatically updates chromedriver to the latest version.")
	print()
	print("Developled by museHD @ https://github.com/musehd/vocab-list-gen")
	print("---------------------------------------------------------------------------------------------------------------------------------")
	print("Loading Browser...Please wait")
	print()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

#Driver options
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--disable-logging")
options.add_argument("--disable-crash-reporter")
options.add_argument("--disable-extensions")
options.add_argument("--disable-in-process-stack-traces")
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")
options.add_argument("--output=/dev/null")
options.add_experimental_option("excludeSwitches", ["enable-logging"])


driver = webdriver.Chrome(options=options)

#Base URLS + intialising lists
oxford = "https://www.lexico.com/en/definition/"
google = "https://google.com/search?q="
pages = []
defs = []
queries = []
error_list = []


def get_ans():
	global pages, defs, queries, error_list
	print("\nGetting Answers\n")

	for query in queries:
		#capitalized so that looks pretty while printing on the screen
		query = query.strip().capitalize()
		print(query + ': ', end='')

		driver.get((google+str("define " + query)))	

		#for ans in driver.find_elements_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/span/div/div/div[3]/div/div[4]/div/div/ol/li/div/div'):
		try:
			# Google displays text with style=display:inline so this searches for that specific style and picks ONLY the first ones as there are often multiple definitions
			span = driver.find_element_by_class_name('vmod')
			division = span.find_element_by_xpath("//*[@style='display:inline']").text
			xdivision = division.split("\n")
			print(xdivision[0])

			if xdivision[0] is not None and len(xdivision[0]) > 0:
				defs.append(xdivision[0])
			# Bunch of Failsafes: First it checks the definition tab; if not, it checks the wikipedia page text on the right hand side; if not, it just gets the text description from the first website
		except:
			try:
				try:
					# Pretty sure this one's broken because google keeps changing the xpath of the def.
					span = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/span/div/div/div[3]/div/div[4]/div/div/ol/li/div/div/div[1]/div/div/div[1]/span")
				except:
					# Text description from first website on Google
					span = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/span")
					
				if span.text is not None and len(span.text) > 0:
					defs.append(span.text)
					print(span.text)
			except:
				#If google fails, it goes to oxford dictionary to find the definition
				try:
					driver.get((oxford+str(query)))		
					span = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div/section[1]/ul/li/div/p/span[2]")
					if span.text is not None and len(span.text) > 0:
						#print('plana')
						defs.append(span.text)
						print(span.text)

				except:	

					try:
						driver.get((google+str("define " + query)))	
						#--- Fixed in "optimise-wp" branch - changed it from volatile xpath to stable (??) class and tag names. Safeguarded it to prevent outputting blank answers
						# This is the one that checks Wikipedia text on the right hand side
						wiki_sector = driver.find_element_by_class_name("kp-wholepage")
						descs = wiki_sector.find_elements_by_tag_name("span")
						for desc in descs:
							if len(desc.text)>10 and (desc.text.lower()) != query.lower():
								print(desc.text)
						defs.append(desc)

					except:

						# uSeFuL eRrOr mSg LmAo
						error_list.append(query)
						print()
						print("I can't find your word... \n Please make sure that the computer has an active internet connection and retry.\nIf all else fails, call the developer for help if this issue is recurring")
		try:
			# This part still broken - need to figure out how to fix About Featured Snippets
			if ("..." or '' or ' ' or "About Featured Snippets") in defs[-1]:
				error_list.append(query)
			elif defs[-1] == (None or False):
				error_list.append(query) 
		except:
			pass
		try:
			#Removing 'None' or Null entries
			defs.remove('')
		except:
			pass
		defs = list(filter(None, defs))
		defs = set(defs)
		defs = list(defs)
		print()
	if len(error_list) > 0:
		#print Words that need to be manually searched
		print("The following words may need to be manually searched: ")
		for word in error_list:
			print(word)
		error_list.clear()



#	if single_def == False:
#		for page in pages:
#			index = pages.index(page)
#			print(queries[index] + ': ', end='')
#			driver.get(page)
#			for ans in driver.find_elements_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/span/div/div/div[3]/div/div[4]/div/div/ol/li/div/div'):
#
#				abc = ''
#				for span in ans.find_elements_by_xpath(".//span"):
#					defs.append(span.text)
#					print(span.text,end='')
#			defs.remove('')
#			defs = list(filter(None, defs))
#		print()


def main():
	loopon = True
	while loopon == True:
		global queries
		words = input("Enter words separated by commas: ")
		if words == '':
			continue
		#Trying to fix user input and removing newliens so that it doesn't break
		words = words.replace('\n',',')
		words = words.replace('\t',',')
		words = words.rstrip("\n")
		queries = words.split(',')
		#Redundant - Multiple definitions feature:
		#n = input("Would you like a single definition? y/n: ")
		#if n != 'y' or 'n':
		#	print("Please retry with either 'y' or 'n' ")
		#	main()
		#gen_pages()
		get_ans()
		print()
		print("Finished!")
		print()
		exitcon = input("Press any key to go again or type 'exit' or 'quit' to close the program: ")
		if exitcon in ('quit', 'exit'):
			loopon = False
			driver.quit()
			sys.exit(0)
			quit()
		else:
			print("Running Again!\n")


info()
# Main thing where we call everything
main()
driver.quit()
sys.exit(0)
