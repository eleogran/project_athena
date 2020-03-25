# sir_base.py

Basic SIR model with default model parameters:
- (basic reproduction number) r0 = 2.5 
- (mean recovery rate) gamma = 1/sick_days = 1/14
- (contact rate) beta = r0 * gamma

NB: parameters will have to be optimized by fitting the model to the data

# run_model.py

Script to run the SIR model per country.
First parameter is the country, second parameter is the starting date in the form M/D/YY, e.g.:
$ run_model.py Italy 2/18/20
Figure template: Figure_1.png