from transformers import PegasusTokenizer, TFPegasusForConditionalGeneration
from longformer_for_pegasus import LongPegasus
import evaluate
import json
if __name__=='__main__':
    with open("/home/duc/pegasus/Pegasus_with_Longformer_summarization/summary.json", encoding="utf-8") as f:
        gold =[]
        for id_, row in enumerate(f):
            data = json.loads(row)
            gold.append(data)
    with open("/home/duc/pegasus/Pegasus_with_Longformer_summarization/predict_xsum_512_1024.json", encoding="utf-8") as f:
        predict1 =[]
        data = json.load(f)
        for x in data:
            predict1.append(''.join(data[x]))
    with open("/home/duc/pegasus/Pegasus_with_Longformer_summarization/predict_xsum_512_1024_tiep.json", encoding="utf-8") as f:
        predict2 =[]
        data = json.load(f)
        for x in data:
            predict2.append(''.join(data[x]))
    predict = predict1 + predict2
    predict3 =[]
    gold1=[]
    for i in range(len(predict)):
        if predict[i] != '"':
            predict3.append(predict[i])
            gold1.append(gold[i])  
    print(len(predict3))
    print(len(gold1))
    rouge = evaluate.load('rouge')
    predictions = predict3
    references = gold1
    results = rouge.compute(predictions=predictions, references=references)
    print(results)