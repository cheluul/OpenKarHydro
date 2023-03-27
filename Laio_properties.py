# -*- coding: utf-8 -*-
"""
驱动模型运行的前数据处理
集成研究区的地理位置特征，读取不同目的（校准，验证，情景分析）对应的数据
不同试验处理、不同气象模式，不同土壤层对应的模型参数
__author__ = "Yangya"
__email__ = "cll986627yy@gmail.com"
__date__ = "2022-xx-xx"
__version__ = "1.0"
"""

###数据前处理
import numpy as np
import pandas as pd

pro = {'Time_Method': {'days': [],'J': [], 'dt': 1},   #days：生长期长度；J：日序数；dt:步长【d】
       'Loc_thr': {'Psi': 0.67748,'Z': 1184,'ht':2000,'λ':[]},   #[PSi:纬度【rad】，Z：海拔【m】
       'Atmosphere': {'T_max':[],'T_min':[],'T_mean':[],'Rh':[],'U2':[],'Rain':[]}, #气象数据数据(最高/最低/平均温度、相对湿度、每日辐射、降雨/灌溉)
       'Actual_value': {'s_actual':[],'Irr':[],'Cov':[],'Ron':[], 'Roff':[]},  #Actual_value：实测数据（蒸发、截留、含水率、蓄水量、入流、出流、径流、冠层截留）
       'params': {},  #与土地利用方式及土壤层相关的参数
       }

#定义函数，根据不同的目的【校准，验证，情景分析】读取不同数据
def Read_canshu(goal,X,Model,Crop_type,N,parameters):
    #进行模型参数校准
    if goal == 1 :
        Table1 = pd.read_excel('data/MC_data/crop%d/Daily_change_data.xls'%(Crop_type), sheet_name='气象数据', index_col=0) #读取用于参数校准的气象数据
        pro['params'] = pd.read_csv(r'data/MC_data/crop%d/Layer_parameters_cxve.csv' % (Crop_type))  #读取土壤相关参数
        s_init = []
        Table2 = Table1.dropna(axis=0,subset=["实测含水率"])  #丢弃以"实测含水率"为index的列中有缺失值的行---》集成实测含水率
        for index,s_value in zip(range(len(np.array(Table2).T[12:])),np.array(Table2).T[12:]): #从输入表格中识别各层实测含水率值[table13:]从13列开始为实测含水率，多少列共多少层
            s_init.append(s_value[0])  #识别实测值中的各层初始含水率
            pro['Actual_value']['s_actual'].append(s_value)
        pro['params']['s_init'] = s_init #将读取的实测含水率初始值赋值给模拟初始值，并追加到参数集中
        
    #进行模型验证
    elif goal == 2 :
        Table1 = pd.read_excel('data/ME_data/crop%d/Daily_change_data.xls'%(Crop_type), sheet_name='气象数据', index_col=0)
        pro['params'] = pd.read_csv(r'data/ME_data/crop%d/Layer_parameters_cxve.csv'%(Crop_type))
        s_init = []
        Table2 = Table1.dropna(axis=0,subset=["实测含水率"])  
        for index,s_value in zip(range(len(np.array(Table2).T[12:])),np.array(Table2).T[12:]): 
            s_init.append(s_value[0])  
            pro['Actual_value']['s_actual'].append(s_value)
        pro['params']['s_init'] = s_init #
    
    #进行情景分析
    elif goal == 3:
        Table1 = pd.read_excel('data/SA_data/未来30年气象数据/CC/{}/第{}种气候变化类型.xls'.format(Model,N), sheet_name='Sheet1', index_col=0)
        #Table1 = pd.read_excel('data/SA_data/未来30年气象数据/LUTC/{}/第{}种气候变化类型/植被A种植{}年后开始转换.xls'.format(Model,N,X), sheet_name='Sheet1', index_col=0)
        pro['params'] = pd.read_csv(r'data/SA_data/Observed_parameters/Layer_parameters_crop{}.csv'.format(Crop_type))
        s_init = [0.35,0.35,0.35]   #给定三层初始RSWC
        pro['params']['s_init'] = s_init
        
    if goal != 4:
        x, x11, x12, x21, x22, x31, x32 = parameters
        pro['Loc_thr']['λ'] = x
        for floor in range(pro['params'].shape[0]):
            [a, b] = [x11, x12] if floor == 0 else [x21, x22] if floor == 1 else [x31, x32]
            pro['params']['ETw'][floor], pro['params']['beta'][floor] = a, b
     
    #敏感性分析
    if goal == 4:
        Table1 = pd.read_excel('data/Sensitivity_data/crop%d/Daily_change_data.xls'%(Crop_type), sheet_name='气象数据', index_col=0)
        pro["params"] = pro['params'] = pd.read_csv(r'data/Sensitivity_data/crop%d/Layer_parameters_cxve.csv'%(Crop_type))
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = parameters
        pro['Loc_thr']['λ'], pro['Loc_thr']['ht'] = x8, x12
        for floor in range(pro['params'].shape[0]):
            [a, b,c,d,e,f,g,h,i,j] = [x1, x2, x3, x4, x5, x6, x7, x9, x10, x11] 
            pro['params']['s_init'][floor], pro['params']['n'][floor], pro['params']['Ks'][floor], pro['params']['sfc'][floor],pro['params']['sh'][floor], pro['params']['sw'][floor], pro['params']['st'][floor], pro['params']['ETw'][floor], pro['params']['beta'][floor], pro['params']['Inter_max'][floor] = [a, b,c,d,e,f,g,h,i,j]

    #读取时间离散
    pro['Time_Method']['J'] = Table1['年日序数']    #模拟期间的日序数
    pro['Time_Method']['days'] = len(pro['Time_Method']['J'])  #模拟时长【d】
    print('模拟时长为:{}天'.format(pro['Time_Method']['days']))

    #读取气象数据
    pro['Atmosphere']['T_max'] = Table1['最高温度']  #最高气温【℃】
    pro['Atmosphere']['T_min'] = Table1['最低温度']  #最低气温【℃】
    pro['Atmosphere']['T_mean'] = Table1['平均温度'] #平均气温【℃】
    pro['Atmosphere']['Rh'] = Table1['湿度']         #平均相对湿度【%】
    pro['Atmosphere']['U2'] = Table1['风速']         #2m高平均风速【m/s】
    pro['Atmosphere']['h'] = Table1['实际日照时数']  #实际日照时数【h】
    pro['Atmosphere']['Rain'] = Table1['降雨']       #每日降雨【mm】

    #读取实测水量平衡机制数据
    pro['Actual_value']['Irr'] = Table1['灌溉']      #灌溉量【mm】
    pro['Actual_value']['Roff'] = Table1['径流']     #作物盖度【%】
    pro['Actual_value']['Cov'] = Table1['盖度']      #径流量【mm】
    pro['Actual_value']['Kc'] = Table1['作物系数']   #作物系数【-】
