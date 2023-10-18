from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(tm,am,sm,cm,sym,fdm,tse,ase,sse,cse,syse,fdse,sw,cw,syw,fdw):



    import pickle
    model = pickle.load(open("breast_prediction_ml_model.sav", "rb"))
    
    prediction = model.predict([[tm,am,sm,cm,sym,fdm,tse,ase,sse,cse,syse,fdse,sw,cw,syw,fdw]])
    
    if prediction == 0:
        return "no cancer predicted"
    elif prediction == 1:
        return "cancer predicted"
    else:
        return "error"

def getPredictions2(tm,am,sm,cm,sym,fdm,tse,ase,sse,cse,syse,fdse,sw,cw,syw,fdw):



    import pickle
    model = pickle.load(open("breast_prediction_ml_model.sav", "rb"))
    
    prediction = model.predict([[tm,am,sm,cm,sym,fdm,tse,ase,sse,cse,syse,fdse,sw,cw,syw,fdw]])
    
    if prediction == 0:
        return "no cancer predicted"
    elif prediction == 1:
        return "cancer predicted"
    else:
        return "error"
        

# our result page view
def result(request):
    tm = float(request.GET['tm'])
    am = float(request.GET['am'])
    sm = float(request.GET['sm'])
    cm = float(request.GET['cm'])
    sym = float(request.GET['sym'])
    fdm = float(request.GET['fdm'])
    tse = float(request.GET['tse'])
    ase = float(request.GET['ase'])
    sse = float(request.GET['sse'])
    cse = float(request.GET['cse'])
    syse = float(request.GET['syse'])
    fdse = float(request.GET['fdse'])
    sw = float(request.GET['sw'])
    cw = float(request.GET['cw'])
    syw = float(request.GET['syw'])
    fdw = float(request.GET['fdw'])
    

    result = getPredictions(tm,am,sm,cm,
                 sym,fdm,tse,ase,sse,cse,syse,fdse,sw,cw,syw,fdw)
    result2= getPredictions2(tm,am,sm,cm,
                 sym,fdm,tse,ase,sse,cse,syse,fdse,sw,cw,syw,fdw)

    return render(request, 'result.html', {'result':result})