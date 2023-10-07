def error(true_vals, rounded_vals):

    rel_errors = [0] * len(true_vals)
    abs_errors = [0] * len(true_vals)
    
    for i in range(len(true_vals)):

        absolute_err = abs(true_vals[i] - rounded_vals[i])
        
        abs_errors[i] = absolute_err

        rel_err = absolute_err/true_vals[i]

        rel_errors[i] = rel_err
 
    return rel_errors


