# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:43:35 2022
用于运行正演，测试参数反演和敏感性分析程序
@author: liudongdong, yangya
"""

import os
import numpy as np
import pandas as pd
import Laio_main       #导入正演程序
import pre_Error       #导入目标函数
import MOCOM_UA_class  #导入反演程序
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei") #字体
os.environ.setdefault("FIPY_SOLVERS", "scipy")

'''
## problem说明： 
#:param num_vars:参数个数
#:param names:参数名称（自定义）
#:param bounds:参数对应范围（list）
#:param objNum:多目标函数个数
#:param population:种群数量
#:param func:正演程序 

## pre_input 说明： 
#:param goal:模型目的
#:param Treatment_type:试验处理（1：农地；2：长芒草；3：苜蓿草地）
#:param parameters：待校准参数
'''

flag = 3

if flag == 1: #反演-模型参数校准
    def test_Laio(parameters):
        pre_input = {'goal': 1,
                     'Crop_type':3,
                     'parameters': parameters,
                     'order':None}
        optical = Laio_main.Laio(pre_input)  #构建实例对象
        return optical.run_Laio_RK4()  #用RK4方法解常微分方程组，运行模型
    #定义MOCOM_UA相关参数
    problem = {'num_vars': 7,
               'names':  ['λ','ETw0','β0', 'ETw1', 'β1', 'ETw2','β2'],
               'bounds': [[0,0.4],[0,0.5],[13,18],[0,0.5],[13,18], [0,0.5],[13,18]],
               'objNum': 3,
               'population': 1000,
               'func': test_Laio,
               'outputs': flag,
               'Crop_type':3
               }
    optimal = MOCOM_UA_class.ParetoSet(problem)#构建实例对象
    optimal.MOCOM_UA()

if flag == 2:  #正演-模型验证
    pre_input = {'goal':2,
                 'Crop_type': 3,
                 'parameters': [],
                 'order': []}
    #读取模型校准参数-最后1000代的种群数据即ParetoSet.txt
    with open("result/MC_result/Population/Crop{}/ParetoSet.txt".format(pre_input['Crop_type']), "r") as f:
        ME_objectives = np.array([[0,0,0,0]])
        for line_index, lines in enumerate(f.readlines(), 1): #按行读取帕累托排序数据
            data = lines.split('\n\t')
            for str in data:
                MC_params = str.split(' ')  #按空格拆分
                if float(MC_params[10]) == 1.0:  #选择校准数据中帕累托排序为1的反演参数
                    pre_input['parameters'] = MC_params[0:7]  #将校准的7个参数赋给正演模型
                    pre_input['order'] = line_index
                    optical = Laio_main.Laio(pre_input)  #构建实例对象
                    data = optical.run_Laio_RK4()  #用RK4方法解常微分方程组，运行模型

                    #模型验证--评价指标的计算与保存
                    Error1 = pre_Error.Hydro_Err(pred=data[0][0], true=data[0][1])  #第一层的模拟值与实测值
                    Error2 = pre_Error.Hydro_Err(pred=data[1][0], true=data[1][1])  #第二层的模拟值与实测值
                    Error3 = pre_Error.Hydro_Err(pred=data[2][0], true=data[2][1])  #第三层的模拟值与实测值
                    ME_space1 = Error1['rmse'], Error1['mae'], Error1['me'], Error1['d'], Error1['dmod'], Error1['r_squared']
                    ME_space2 = Error2['rmse'], Error2['mae'], Error2['me'], Error2['d'], Error2['dmod'], Error2['r_squared']
                    ME_space3 = Error3['rmse'], Error3['mae'], Error3['me'], Error3['d'], Error3['dmod'], Error3['r_squared']
                    print("模型验证第一层的RMSE,MAE,ME,D,DMOD,R2分别为：{},{},{},{},{},{}".format(Error1['rmse'], Error1['mae'],Error1['me'], Error1['d'],Error1['dmod'],Error1['r_squared']))
                    print("模型验证第二层的RMSE,MAE,ME,D,DMOD,R2分别为：{},{},{},{},{},{}".format(Error2['rmse'], Error2['mae'],Error2['me'], Error2['d'],Error2['dmod'], Error2['r_squared']))
                    print("模型验证第三层的RMSE,MAE,ME,D,DMOD,R2分别为：{},{},{},{},{},{}".format(Error3['rmse'], Error3['mae'],Error3['me'], Error3['d'],Error3['dmod'], Error3['r_squared']))
                    flag = np.array([[line_index, ME_space1, ME_space2, ME_space3]])
                    ME_objectives = np.concatenate((ME_objectives,flag))
        ME_objectives = pd.DataFrame(ME_objectives, columns=['line_lindex', 'floor0[RMSE,MAE,ME,D,DMOD,R2]', 'floor1[RMSE,MAE,ME,D,DMOD,R2]', 'floor2[RMSE,MAE,ME,D,DMOD,R2]'])
        ME_objectives = ME_objectives[1:]  #去除第一行占位的初始值
        if pre_input['goal'] == 1:
            ME_objectives.to_csv('result/MC_result/Objectives/Crop{}_MCobjectives'.format(pre_input['Crop_type']),index=False)
        if pre_input['goal'] == 2:
            ME_objectives.to_csv('result/ME_result/Objectives/Crop{}_MEobjectives'.format(pre_input['Crop_type']),index=False)

if flag == 3: #情景分析
    pre_input = {'goal': 3,
                 'Crop_typeA':1,  #土地利用转换前植被
                 'Crop_typeB':3,  #土地利用转换后植被，CC情况下运行植被
                 'parameters':[],
                 'X':30,           #植被A种植X年后开始转换
                 'order':3}  #1:不考虑气候变化NCC；2：RCP26；3：RCP45；4：RCP85
    if pre_input['Crop_typeA'] or pre_input['Crop_typeB'] == 1:
        pre_input['parameters'] = 0.19,0.26,15.53,0.24,15.23,0.27,15.31
    if pre_input['Crop_typeA'] or pre_input['Crop_typeB'] == 2:
        pre_input['parameters'] = 0.18,0.25,15.11,0.28,14.90,0.24,15.28
    if pre_input['Crop_typeA'] or pre_input['Crop_typeB'] == 3:
        pre_input['parameters'] = 0.20,0.278,16.64,0.257,16.50,0.247,16.10
    optical = Laio_main.Laio(pre_input)  #构建实例对象
    optical.run_Laio_RK4()  #用RK4方法解常微分方程组，运行模型

   


