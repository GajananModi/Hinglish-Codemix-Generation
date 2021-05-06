from nltk.tag import CRFTagger

crflan = CRFTagger()
crf = CRFTagger()

crflan.set_model_file('model.crf.tagger')
crf.set_model_file('model1.crf.tagger')
a_file = "postag.txt"
response = open(a_file).read()
response = response.lower()
#response=response.replace('\n','')
data = response.split(' ')
data =' '.join(data)
data = response.split('\n')
print(len(data))
f = open("rnnlm_op.txt", "w")


print("Give a sentence...")
# Test
for sentence in data[0:2000]:
	test_sent =sentence
	test_sent = test_sent.encode('utf-8').decode('utf-8').split(' ')
	half_ans= crflan.tag(test_sent)
	#print(half_ans)
	tags=crf.tag(test_sent)
	for i in range(len(tags)):
		f.write(half_ans[i][0]+'\t'+half_ans[i][1] + '\t'+tags[i][1]+'\n')
	f.write('.'+'\n')
		
