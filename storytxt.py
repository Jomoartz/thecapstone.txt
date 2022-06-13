def read_file_content(filename):
    with open(filename) as b:
    	content= b.readlines()
    	contentz=content.copy()
    	return(content)
    	b.close()
	
	
f=read_file_content('story.txt')
print(f)