with open("story.txt" ) as b:
	content= b.readlines()
	contentz=content.copy()
	b.close()

pringles=(' '. join(contentz))
bam= pringles.split(' ')


story={
	"stress": 1,
	}
	
	words= bam
	for items in words:
		count= words.count(items)
		story[items]= count
	print(story)