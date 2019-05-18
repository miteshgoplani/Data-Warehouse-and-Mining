import pandas as pd 

def getprobability(columns,decisioncol,category,label,df):
    x = df.groupby([columns,decisioncol]).size()
    y = df.groupby(decisioncol).size()
    try:
        nA = x[category][label]
    except:
        nA = 0
    nS = y[label]
    return nA/nS

def bayesClassifier(test,decisioncol,labels,df):

    cols = [x.split('=')[0] for x in test]
    vals = [x.split('=')[1] for x in test]
    results = []

    for decision in labels:
        p = 1
        for col,cat in zip(cols,vals):
            t = getprobability(col,decisioncol,cat,decision,df)
            p = p*t
        p = p*t
        results.append(p)
    
    i = results.index(max(results))
    return labels[i]

df=pd.read_csv("data.csv")
test=['Homeowner=no','Status=Business','Income=High']
decisioncol='Defaulted'
labels=['Yes','No']	
print('\nThe decision for the given test instance is - ',bayesClassifier(test,decisioncol,labels,df))	
# df=pd.read_csv("data2.csv")
# test=['Size=Small','Color=Green','Shape=Square','Weight=Light']
# decisioncol='Expensive'
# labels=['Yes','No']	
# print('\nThe decision for the given test instance is - ',bayesClassifier(test,decisioncol,labels,df))	