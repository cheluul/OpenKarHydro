# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:01:08 2021

@author: Lenovo
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from spotpy.parameter import Uniform
from spotpy.objectivefunctions import rmse
import Laio_main
import spotpy
import numpy as np
import pandas as pd

Crop_type = 1
class spot_setup(object): 
    treatment = 1
    s_init = Uniform(low=0.0,high=1)
    n = Uniform(low=0.0,high=0.6)
    Ks = Uniform(low=1.3,high=1956.8)
    sfc= Uniform(low=0,high=0.6)
    sh = Uniform(low=0,high=0.6)
    sw = Uniform(low=0,high=0.6)
    st = Uniform(low=0,high=0.6)
    λ = Uniform(low=0.0,high=0.5)
    ETw = Uniform(low=0.0,high=1)
    β = Uniform(low=13.0,high=26)
    Imax = Uniform(low=0,high=5)
    ht = Uniform(low=0,high=4000)

    def __init__(self, treatment=treatment,obj_func=None):
        self.treatment = treatment
        self.obj_func = obj_func  
 
    def simulation(self, x):
        optical = Laio_main.Laio({'goal': 4,'Crop_type':self.treatment,'parameters':[ x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8],x[9], x[10], x[11]],'order': None})
        RSWC_sim = optical.run_Laio_RK4()
        return RSWC_sim
        
    def evaluation(self):
        Obs_data = pd.read_excel('data/RSWCData_For_sensitivity.xlsx', sheet_name='Sheet1', index_col=0 )
        RSWC_obs = Obs_data['Crop{}'.format(self.treatment)]
        return RSWC_obs
    
    def objectivefunction(self,simulation,evaluation, params=None):
        #SPOTPY expects to get one or multiple values back, 
        #that define the performance of the model run
        if not self.obj_func:
            # This is used if not overwritten by user
            like = rmse(evaluation,simulation)
        else:
            #Way to ensure flexible spot setup class
            like = self.obj_func(evaluation,simulation)    
        return like

if __name__ == "__main__":
    parallel ='seq'
    # Initialize the Hymod example
    spot_setup = spot_setup()
    
    #Select number of maximum repetitions
    # CHeck out https://spotpy.readthedocs.io/en/latest/Sensitivity_analysis_with_FAST/
    # How to determine an appropriate number of repetitions
    parameters_number=12
    inference_factor=4
    frequency_step =2
    rep = (1+4*inference_factor**2*(1+(parameters_number-2)*frequency_step))*parameters_number
    
    # #Start a sensitivity analysis
    sampler = spotpy.algorithms.fast(spot_setup, dbname='result/Sensitivity/FAST_OpenKarHydro_Crop{}'.format(Crop_type), dbformat='csv', db_precision=np.float32)
    sampler.sample(rep)
    
    # Load the results gained with the fast sampler, stored in FAST_hymod.csv
    results = spotpy.analyser.load_csv_results('result/Sensitivity/FAST_OpenKarHydro_Crop{}'.format(Crop_type))
    
    # Example plot to show the sensitivity index of each parameter
    spotpy.analyser.plot_fast_sensitivity(results, number_of_sensitiv_pars=3)
    
    # Example to get the sensitivity index of each parameter    
    SI = spotpy.analyser.get_sensitivity_of_fast(results)