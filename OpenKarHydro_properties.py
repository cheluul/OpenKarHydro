# -*- coding: utf-8 -*-
"""
__author__ = "Liu dongdong Yangya"
__date__ = "2022-xx-xx"
__version__ = "1.0"
"""

import numpy as np
import pandas as pd

pro = {'Time_Method': {'days': [],'J': [], 'dt': 1},   
       'Loc_thr': {'Psi': 0.67748,'Z': 1184,'ht':2000,'λ':[]},  
       'Atmosphere': {'T_max':[],'T_min':[],'T_mean':[],'Rh':[],'U2':[],'Rain':[]}, 
       'Actual_value': {'s_actual':[],'Irr':[],'Cov':[],'Ron':[], 'Roff':[]},
       'params': {},  
       }

def Read_canshu(goal,Crop_type,N,parameters):
    #模型校准数据
    if goal == 1 :
        Table1 = pd.read_excel('data/MC_data/crop%d/Daily_change_data.xls'%(Crop_type), sheet_name='气象数据', index_col=0) 
        pro['params'] = pd.read_csv(r'data/MC_data/crop%d/Layer_parameters_cxve.csv' % (Crop_type))
        s_init = []
        Table2 = Table1.dropna(axis=0,subset=["实测含水率"])  
        for index,s_value in zip(range(len(np.array(Table2).T[12:])),np.array(Table2).T[12:]):
            s_init.append(s_value[0])
            pro['Actual_value']['s_actual'].append(s_value)
        pro['params']['s_init'] = s_init 
        
    #模型验证数据
    elif goal == 2 :
        Table1 = pd.read_excel('data/ME_data/crop%d/Daily_change_data.xls'%(Crop_type), sheet_name='气象数据', index_col=0)
        pro['params'] = pd.read_csv(r'data/ME_data/crop%d/Layer_parameters_cxve.csv'%(Crop_type))
        s_init = []
        Table2 = Table1.dropna(axis=0,subset=["实测含水率"])  
        for index,s_value in zip(range(len(np.array(Table2).T[12:])),np.array(Table2).T[12:]): 
            s_init.append(s_value[0])  
            pro['Actual_value']['s_actual'].append(s_value)
        pro['params']['s_init'] = s_init 
    
    #情景分析数据
    elif goal == 3:
        Table1 = pd.read_excel('data/SA_data/未来30年气象预测/第{}次未来30年气象数据.xls'.format(N), sheet_name='Sheet1', index_col=0 )
        pro['params'] = pd.read_csv(r'data/SA_data/Observed_parameters/Layer_parameters_crop{}.csv'.format(Crop_type))
        s_init = [0.35,0.35,0.35]  
        pro['params']['s_init'] = s_init
        
    if goal != 4:
        x, x11, x12, x21, x22, x31, x32 = parameters
        pro['Loc_thr']['λ'] = x
        for floor in range(pro['params'].shape[0]):
            [a, b] = [x11, x12] if floor == 0 else [x21, x22] if floor == 1 else [x31, x32]
            pro['params']['ETw'][floor], pro['params']['beta'][floor] = a, b
     
   #敏感性分析数据
    if goal == 4:
        Table1 = pd.read_excel('data/Sensitivity_data/crop%d/Daily_change_data.xls'%(Crop_type), sheet_name='气象数据', index_col=0)
        pro["params"] = pro['params'] = pd.read_csv(r'data/Sensitivity_data/crop%d/Layer_parameters_cxve.csv'%(Crop_type))
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = parameters
        pro['Loc_thr']['λ'], pro['Loc_thr']['ht'] = x8, x12
        for floor in range(pro['params'].shape[0]):
            [a, b,c,d,e,f,g,h,i,j] = [x1, x2, x3, x4, x5, x6, x7, x9, x10, x11] 
            pro['params']['s_init'][floor], pro['params']['n'][floor], pro['params']['Ks'][floor], pro['params']['sfc'][floor],pro['params']['sh'][floor], pro['params']['sw'][floor], pro['params']['st'][floor], pro['params']['ETw'][floor], pro['params']['beta'][floor], pro['params']['Inter_max'][floor] = [a, b,c,d,e,f,g,h,i,j]

  
    pro['Time_Method']['J'] = Table1['年日序数']  
    pro['Time_Method']['days'] = len(pro['Time_Method']['J'])  
    print('模拟时长为:{}天'.format(pro['Time_Method']['days']))

    pro['Atmosphere']['T_max'] = Table1['最高温度']  
    pro['Atmosphere']['T_min'] = Table1['最低温度'] 
    pro['Atmosphere']['T_mean'] = Table1['平均温度'] 
    pro['Atmosphere']['Rh'] = Table1['湿度']         
    pro['Atmosphere']['U2'] = Table1['风速']        
    pro['Atmosphere']['h'] = Table1['实际日照时数']  
    pro['Atmosphere']['Rain'] = Table1['降雨']      

    pro['Actual_value']['Irr'] = Table1['灌溉']      
    pro['Actual_value']['Roff'] = Table1['径流']    
    pro['Actual_value']['Cov'] = Table1['盖度']      
    pro['Actual_value']['Kc'] = Table1['作物系数']  
