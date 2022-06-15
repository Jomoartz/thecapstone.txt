def read_file_content(story_txt):
	with open("story.txt" ) as b:
		content= b.readlines()
		contentz=content.copy()
		return(contentz)
		b.close()


	
def count_words(contentz):
	get=read_file_content(contentz)
	text=(' '. join(get))
	split = text.split(' ')
		
		
	story={
	"professor": 1,
	}
			
	words= split
	for items in words:
		count= words.count(items)
		story[items]= count
		print(story)
	

print(count_words("story.txt"))
	
		
		
		
		

	
		
	
	
	
		
		
	
	
	
			
	
	
		
		
		

	
	
		
		
	
	
	
			
	
	
	
		
				
		
	
	
	
	







	
	


	
		
	
