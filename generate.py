import json
from transformers import PegasusTokenizer, TFPegasusForConditionalGeneration 
from longformer_for_pegasus import LongPegasus
if __name__=='__main__':
    l=LongPegasus()             
    model_name='google/pegasus-large'
    model,tokenizer=l.create_long_model(save_model="Pegasus_4k/", attention_window=4096, max_pos=4096,model_name=model_name)
    model = TFPegasusForConditionalGeneration.from_pretrained('Pegasus_4k/')
    tokenizer = PegasusTokenizer.from_pretrained('Pegasus_4k/')
    articles =[]
    with open("/home/duc/pegasus/Pegasus_with_Longformer_summarization/clean.json", encoding="utf-8") as f:
        # abstracts=[]
        data = f.read()
        js = json.loads(data)
        for x in js:
            article = js[x]
            articles.append(article)
        # abstract = [ab.replace("<S>", "").replace("</S>", "").strip() for ab in data["abstract_text"]]
        # abstract = " \n ".join(abstract)
        # abstracts.append(abstract)
    articles1 = articles[:10]
    for i in articles1:
        tosum = (i)
        inputs = tokenizer([tosum], max_length=512, return_tensors='tf')
        # Generate Summary
        summary_ids = model.generate(inputs['input_ids'])
        print([tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids])