# -*- coding: utf-8 -*-
"""
__author__ = "Liu dongdong Yangya"
__date__ = "2022-xx-xx"
__version__ = "1.0"
"""

import os
import numpy as np
import pandas as pd
import OpenKarHydro_main       
import pre_Error       
import Fanyan_function #模型反演函数   
import Weather_Generator 
from tqdm import tqdm
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei") 
os.environ.setdefault("FIPY_SOLVERS", "scipy")

#模型校准
flag = 2
if flag == 1: 
    def test_Laio(parameters):
        pre_input = {'goal': 1,
                     'Crop_type':3,
                     'parameters': parameters,
                     'order':None}
        optical =  OpenKarHydro_main.Laio(pre_input) 
        return optical.run_Laio_RK4()  

    problem = {'num_vars': 7,
               'names':  ['λ','ETw0','β0', 'ETw1', 'β1', 'ETw2','β2'],
               'bounds': [[0,0.4],[0,0.5],[13,18],[0,0.5],[13,18], [0,0.5],[13,18]],
               'objNum': 3,
               'population': 1000,
               'func': test_Laio,
               'outputs': flag,
               'Crop_type':3
               }
    optimal = Fanyan_function.ParetoSet(problem)
    optimal.XXX_method()
    
#模型验证
if flag == 2: 
    pre_input = {'goal':2,
                 'Crop_type': 3,
                 'parameters': [],
                 'order': []}
    with open("result/MC_result/Population/Crop{}/ParetoSet.txt".format(pre_input['Crop_type']), "r") as f:
        ME_objectives = np.array([[0,0,0,0]])
        for line_index, lines in enumerate(f.readlines(), 1): 
            data = lines.split('\n\t')
            for str in data:
                MC_params = str.split(' ')  
                if float(MC_params[10]) == 1.0:  
                    pre_input['parameters'] = MC_params[0:7]  
                    pre_input['order'] = line_index
                    optical =  OpenKarHydro_main.Laio(pre_input)  
                    data = optical.run_Laio_RK4() 
                    
                    Error1 = pre_Error.Hydro_Err(pred=data[0][0], true=data[0][1])  
                    Error2 = pre_Error.Hydro_Err(pred=data[1][0], true=data[1][1])  
                    Error3 = pre_Error.Hydro_Err(pred=data[2][0], true=data[2][1])  
                    ME_space1 = Error1['rmse'], Error1['mae'], Error1['me'], Error1['d'], Error1['dmod'], Error1['r_squared']
                    ME_space2 = Error2['rmse'], Error2['mae'], Error2['me'], Error2['d'], Error2['dmod'], Error2['r_squared']
                    ME_space3 = Error3['rmse'], Error3['mae'], Error3['me'], Error3['d'], Error3['dmod'], Error3['r_squared']
                    print("模型验证第一层的RMSE,MAE,ME,D,DMOD,R2分别为：{},{},{},{},{},{}".format(Error1['rmse'], Error1['mae'],Error1['me'], Error1['d'],Error1['dmod'],Error1['r_squared']))
                    print("模型验证第二层的RMSE,MAE,ME,D,DMOD,R2分别为：{},{},{},{},{},{}".format(Error2['rmse'], Error2['mae'],Error2['me'], Error2['d'],Error2['dmod'], Error2['r_squared']))
                    print("模型验证第三层的RMSE,MAE,ME,D,DMOD,R2分别为：{},{},{},{},{},{}".format(Error3['rmse'], Error3['mae'],Error3['me'], Error3['d'],Error3['dmod'], Error3['r_squared']))
                    flag = np.array([[line_index, ME_space1, ME_space2, ME_space3]])
                    ME_objectives = np.concatenate((ME_objectives,flag))
        ME_objectives = pd.DataFrame(ME_objectives, columns=['line_lindex', 'floor0[RMSE,MAE,ME,D,DMOD,R2]', 'floor1[RMSE,MAE,ME,D,DMOD,R2]', 'floor2[RMSE,MAE,ME,D,DMOD,R2]'])
        ME_objectives = ME_objectives[1:]  
        if pre_input['goal'] == 1:
            ME_objectives.to_csv('result/MC_result/Objectives/Crop{}_MCobjectives'.format(pre_input['Crop_type']),index=False)
        if pre_input['goal'] == 2:
            ME_objectives.to_csv('result/ME_result/Objectives/Crop{}_MEobjectives'.format(pre_input['Crop_type']),index=False)

#情景分析
if flag == 3: 
    Weather_Generator.N_random(N_sum=1000)
    pre_input = {'goal': 3,
                 'Crop_type':1,
                 'parameters': [],
                 'order': []}
    for i in tqdm(np.arange(1,1001,1)):
        pre_input['order'] = i
        if pre_input['Crop_type'] == 1:
            pre_input['parameters'] = 0.19,0.26,15.53,0.24,15.23,0.27,15.31
        if pre_input['Crop_type'] == 2:
            pre_input['parameters'] = 0.18,0.25,15.11,0.28,14.90,0.24,15.28
        if pre_input['Crop_type'] == 3:
            pre_input['parameters'] = 0.20,0.278,16.64,0.257,16.50,0.247,16.10
        optical =  OpenKarHydro_main.Laio(pre_input)  
        optical.run_Laio_RK4()  


   


