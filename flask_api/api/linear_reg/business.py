def do_prediction(prediction_input):
    value_1 = prediction_input['value_1']
    value_2 = prediction_input['value_2']
    prediction = 1 + 2*value_1 + 3*value_2
    return value_1, value_2, prediction