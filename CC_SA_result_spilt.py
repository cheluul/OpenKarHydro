#导入包
import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei") #字体

Crop_type = 3 #作物类型
Model = "IPSL_CM5A_MR"
file_dir = "result/SA_result/CC/{}/Crop{}" .format(Model,Crop_type)     #读取模拟含水率数据
file_list = os.listdir(file_dir)  #获取指定路径下的全部文件


s1 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
s2 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
s3 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
w1 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
w2 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
w3 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
Rain = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
Inter = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
Roff =  {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
sed = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
Cov = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
AET1 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
AET2 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
AET3 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
Lw1 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
Lw2 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
Lw3 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}


for order,file in tqdm(enumerate(file_list,1)):
    df = pd.read_csv(os.path.join(file_dir, file), header=0, sep=",", dtype=str, engine="python", encoding='utf-8')
    s_data = df['Volumetric soil water content (nondim)']  #取index为含水率的列
    w_data = df['Water storage(mm)']
    Rain_data = df['Rain (mm/d)']
    AET_data = df['AET_imitate (mm/d)']
    Lw_data = df['Lw_imitate (mm/d)']
    Roff_data =df['Roff_imitate (mm/d)']
    sed_data = df['Soil erosion loss (g/m2*day)']
    Cov_data = df['Grow_Cov (%)']
    Inter_data = df['Inter_imitate (mm/d)']
    for day in np.arange(0, len(s_data), 1):
        if eval(s_data[day])[1] < 0:
           break
        s1["第{}种气候变化类型".format(order)].append(eval(s_data[day])[0])
        s2["第{}种气候变化类型".format(order)].append(eval(s_data[day])[1])
        s3["第{}种气候变化类型".format(order)].append(eval(s_data[day])[2])
        w1["第{}种气候变化类型".format(order)].append(eval(w_data[day])[0])
        w2["第{}种气候变化类型".format(order)].append(eval(w_data[day])[1])
        w3["第{}种气候变化类型".format(order)].append(eval(w_data[day])[2])
        Rain["第{}种气候变化类型".format(order)].append(Rain_data[day])
        Inter["第{}种气候变化类型".format(order)].append(Inter_data[day])
        Roff["第{}种气候变化类型".format(order)].append(Roff_data[day])
        sed["第{}种气候变化类型".format(order)].append(sed_data[day])
        Cov["第{}种气候变化类型".format(order)].append(Cov_data[day])
        AET1["第{}种气候变化类型".format(order)].append(eval(AET_data[day])[0])
        AET2["第{}种气候变化类型".format(order)].append(eval(AET_data[day])[1])
        AET3["第{}种气候变化类型".format(order)].append(eval(AET_data[day])[2])
        Lw1["第{}种气候变化类型".format(order)].append(eval(Lw_data[day])[0])
        Lw2["第{}种气候变化类型".format(order)].append(eval(Lw_data[day])[1])
        Lw3["第{}种气候变化类型".format(order)].append(eval(Lw_data[day])[2])
        
for key, value in list(s1.items()):
   if len(value) < 10957:      
      del s1[key]
      del s2[key]
      del s3[key]
      del w1[key]
      del w2[key]
      del w3[key]
      del Rain[key]
      del Inter[key]
      del Roff[key]
      del sed[key]
      del Cov[key]
      del AET1[key]
      del AET2[key]
      del AET3[key]
      del Lw1[key]
      del Lw2[key]
      del Lw3[key]
      continue

pd.DataFrame(s1).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/s1情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(s2).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/s2情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(s3).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/s3情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(w1).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/w1情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(w2).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/w2情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(w3).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/w3情景分析处理数据.csv".format(Model,Crop_type)) 
pd.DataFrame(Rain).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Rain情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(Inter).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Inter情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(Roff).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Roff情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(sed).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/sed情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(Cov).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Cov情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(AET1).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/AET1情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(AET2).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/AET2情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(AET3).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/AET3情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(Lw1).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Lw1情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(Lw2).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Lw2情景分析处理数据.csv".format(Model,Crop_type))
pd.DataFrame(Lw3).to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Lw3情景分析处理数据.csv".format(Model,Crop_type))


##计算月平均守恒
Rain = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Rain情景分析处理数据.csv".format(Model,Crop_type))
Inter = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Inter情景分析处理数据.csv".format(Model,Crop_type))
AET1 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/AET1情景分析处理数据.csv".format(Model,Crop_type))
Roff = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Roff情景分析处理数据.csv".format(Model,Crop_type))
Sed = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Sed情景分析处理数据.csv".format(Model,Crop_type))
Cov = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Cov情景分析处理数据.csv".format(Model,Crop_type))
Lw3 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Lw3情景分析处理数据.csv".format(Model,Crop_type))
Sws1 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/w1情景分析处理数据.csv".format(Model,Crop_type))
Sws2 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/w2情景分析处理数据.csv".format(Model,Crop_type))
Sws3 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/w3情景分析处理数据.csv".format(Model,Crop_type))


date = pd.date_range(start = '2021/1/1', end='2050/12/31',freq='D')
Rain.iloc[:,0],Inter.iloc[:,0],AET1.iloc[:,0],Sed.iloc[:,0],Cov.iloc[:,0],Roff.iloc[:,0],Lw3.iloc[:,0],Sws1.iloc[:,0],Sws2.iloc[:,0],Sws3.iloc[:,0]=date,date,date,date,date,date,date,date,date,date
Rain.index,Inter.index,AET1.index,Roff.index,Sed.index,Cov.index,Lw3.index,Sws1.index,Sws2.index,Sws3.index=date,date,date,date,date,date,date,date,date,date
Rain_NCC,Inter_NCC,AET1_NCC,Roff_NCC,Sed_NCC,Cov_NCC,Lw3_NCC,Sws1_NCC,Sws2_NCC,Sws3_NCC = Rain['第1种气候变化类型'],Inter['第1种气候变化类型'],AET1['第1种气候变化类型'],Roff['第1种气候变化类型'],Sed['第1种气候变化类型'],Cov['第1种气候变化类型'],Lw3['第1种气候变化类型'],Sws1['第1种气候变化类型'],Sws2['第1种气候变化类型'],Sws3['第1种气候变化类型']
Rain_RCP26,Inter_RCP26,AET1_RCP26,Roff_RCP26,Sed_RCP26,Cov_RCP26,Lw3_RCP26,Sws1_RCP26,Sws2_RCP26,Sws3_RCP26 = Rain['第2种气候变化类型'],Inter['第2种气候变化类型'],AET1['第2种气候变化类型'],Roff['第2种气候变化类型'],Sed['第2种气候变化类型'],Cov['第2种气候变化类型'],Lw3['第2种气候变化类型'],Sws1['第2种气候变化类型'],Sws2['第2种气候变化类型'],Sws3['第2种气候变化类型']
Rain_RCP45,Inter_RCP45,AET1_RCP45,Roff_RCP45,Sed_RCP45,Cov_RCP45,Lw3_RCP45,Sws1_RCP45,Sws2_RCP45,Sws3_RCP45 = Rain['第3种气候变化类型'],Inter['第3种气候变化类型'],AET1['第3种气候变化类型'],Roff['第3种气候变化类型'],Sed['第3种气候变化类型'],Cov['第3种气候变化类型'],Lw3['第3种气候变化类型'],Sws1['第3种气候变化类型'],Sws2['第3种气候变化类型'],Sws3['第3种气候变化类型']
Rain_RCP85,Inter_RCP85,AET1_RCP85,Roff_RCP85,Sed_RCP85,Cov_RCP85,Lw3_RCP85,Sws1_RCP85,Sws2_RCP85,Sws3_RCP85 = Rain['第4种气候变化类型'],Inter['第4种气候变化类型'],AET1['第4种气候变化类型'],Roff['第4种气候变化类型'],Sed['第4种气候变化类型'],Cov['第4种气候变化类型'],Lw3['第4种气候变化类型'],Sws1['第4种气候变化类型'],Sws2['第4种气候变化类型'],Sws3['第4种气候变化类型']

SWB_Y_NCC,SWB_Y_RCP26,SWB_Y_RCP45,SWB_Y_RCP85=pd.DataFrame(),pd.DataFrame(),pd.DataFrame(),pd.DataFrame()
SWB_Y_NCC['Rain'],SWB_Y_RCP26['Rain'],SWB_Y_RCP45['Rain'],SWB_Y_RCP85['Rain'] = pd.DataFrame(Rain_NCC.resample("M").sum()),pd.DataFrame(Rain_RCP26.resample("M").sum()),pd.DataFrame(Rain_RCP45.resample("M").sum()),pd.DataFrame(Rain_RCP85.resample("M").sum())
SWB_Y_NCC['Inter'],SWB_Y_RCP26['Inter'],SWB_Y_RCP45['Inter'],SWB_Y_RCP85['Inter'] = pd.DataFrame(Inter_NCC.resample("M").sum()),pd.DataFrame(Inter_RCP26.resample("M").sum()),pd.DataFrame(Inter_RCP45.resample("M").sum()),pd.DataFrame(Inter_RCP85.resample("M").sum()) 
SWB_Y_NCC['Roff'],SWB_Y_RCP26['Roff'],SWB_Y_RCP45['Roff'],SWB_Y_RCP85['Roff'] = pd.DataFrame(Roff_NCC.resample("M").sum()),pd.DataFrame(Roff_RCP26.resample("M").sum()),pd.DataFrame(Roff_RCP45.resample("M").sum()),pd.DataFrame(Roff_RCP85.resample("M").sum())
SWB_Y_NCC['Sed'],SWB_Y_RCP26['Sed'],SWB_Y_RCP45['Sed'],SWB_Y_RCP85['Sed'] = pd.DataFrame(Sed_NCC.resample("M").sum()),pd.DataFrame(Sed_RCP26.resample("M").sum()),pd.DataFrame(Sed_RCP45.resample("M").sum()),pd.DataFrame(Sed_RCP85.resample("M").sum()) 
SWB_Y_NCC['Cov'],SWB_Y_RCP26['Cov'],SWB_Y_RCP45['Cov'],SWB_Y_RCP85['Cov'] = pd.DataFrame(Cov_NCC.resample("M").mean()),pd.DataFrame(Cov_RCP26.resample("M").mean()),pd.DataFrame(Cov_RCP45.resample("M").mean()),pd.DataFrame(Cov_RCP85.resample("M").mean()) 
SWB_Y_NCC['AET1'],SWB_Y_RCP26['AET1'],SWB_Y_RCP45['AET1'],SWB_Y_RCP85['AET1'] = pd.DataFrame(AET1_NCC.resample("M").sum()),pd.DataFrame(AET1_RCP26.resample("M").sum()),pd.DataFrame(AET1_RCP45.resample("M").sum()),pd.DataFrame(AET1_RCP85.resample("M").sum()) 
SWB_Y_NCC['Lw3'],SWB_Y_RCP26['Lw3'],SWB_Y_RCP45['Lw3'],SWB_Y_RCP85['Lw3'] = pd.DataFrame(Lw3_NCC.resample("M").sum()),pd.DataFrame(Lw3_RCP26.resample("M").sum()),pd.DataFrame(Lw3_RCP45.resample("M").sum()),pd.DataFrame(Lw3_RCP85.resample("M").sum()) 
SWB_Y_NCC['DS1'],SWB_Y_RCP26['DS1'],SWB_Y_RCP45['DS1'],SWB_Y_RCP85['DS1'] = pd.DataFrame(Sws1_NCC.resample("M").last())-pd.DataFrame(Sws1_NCC.resample("M").first()),pd.DataFrame(Sws1_RCP26.resample("M").last())-pd.DataFrame(Sws1_RCP26.resample("M").first()),pd.DataFrame(Sws1_RCP45.resample("M").last())-pd.DataFrame(Sws1_RCP45.resample("M").first()),pd.DataFrame(Sws1_RCP85.resample("M").last())-pd.DataFrame(Sws1_RCP85.resample("M").first())
SWB_Y_NCC['DS2'],SWB_Y_RCP26['DS2'],SWB_Y_RCP45['DS2'],SWB_Y_RCP85['DS2'] = pd.DataFrame(Sws2_NCC.resample("M").last())-pd.DataFrame(Sws2_NCC.resample("M").first()),pd.DataFrame(Sws2_RCP26.resample("M").last())-pd.DataFrame(Sws2_RCP26.resample("M").first()),pd.DataFrame(Sws2_RCP45.resample("M").last())-pd.DataFrame(Sws2_RCP45.resample("M").first()),pd.DataFrame(Sws2_RCP85.resample("M").last())-pd.DataFrame(Sws2_RCP85.resample("M").first())
SWB_Y_NCC['DS3'],SWB_Y_RCP26['DS3'],SWB_Y_RCP45['DS3'],SWB_Y_RCP85['DS3'] =pd.DataFrame(Sws3_NCC.resample("M").last())-pd.DataFrame(Sws3_NCC.resample("M").first()),pd.DataFrame(Sws3_RCP26.resample("M").last())-pd.DataFrame(Sws3_RCP26.resample("M").first()),pd.DataFrame(Sws3_RCP45.resample("M").last())-pd.DataFrame(Sws3_RCP45.resample("M").first()),pd.DataFrame(Sws3_RCP85.resample("M").last())-pd.DataFrame(Sws3_RCP85.resample("M").first())

SWB_Y_NCC.to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/SWB_M_NCC.csv".format(Model,Crop_type))
SWB_Y_RCP26.to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/SWB_M_RCP26.csv".format(Model,Crop_type))
SWB_Y_RCP45.to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/SWB_M_RCP45.csv".format(Model,Crop_type))
SWB_Y_RCP85.to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/SWB_M_RCP85.csv".format(Model,Crop_type))

SWB_Y_NCC,SWB_Y_RCP26,SWB_Y_RCP45,SWB_Y_RCP85=pd.DataFrame(),pd.DataFrame(),pd.DataFrame(),pd.DataFrame()
SWB_Y_NCC['Rain'],SWB_Y_RCP26['Rain'],SWB_Y_RCP45['Rain'],SWB_Y_RCP85['Rain'] = pd.DataFrame(Rain_NCC.resample("Y").sum()),pd.DataFrame(Rain_RCP26.resample("Y").sum()),pd.DataFrame(Rain_RCP45.resample("Y").sum()),pd.DataFrame(Rain_RCP85.resample("Y").sum())
SWB_Y_NCC['Inter'],SWB_Y_RCP26['Inter'],SWB_Y_RCP45['Inter'],SWB_Y_RCP85['Inter'] = pd.DataFrame(Inter_NCC.resample("Y").sum()),pd.DataFrame(Inter_RCP26.resample("Y").sum()),pd.DataFrame(Inter_RCP45.resample("Y").sum()),pd.DataFrame(Inter_RCP85.resample("Y").sum()) 
SWB_Y_NCC['Roff'],SWB_Y_RCP26['Roff'],SWB_Y_RCP45['Roff'],SWB_Y_RCP85['Roff'] = pd.DataFrame(Roff_NCC.resample("Y").sum()),pd.DataFrame(Roff_RCP26.resample("Y").sum()),pd.DataFrame(Roff_RCP45.resample("Y").sum()),pd.DataFrame(Roff_RCP85.resample("Y").sum())
SWB_Y_NCC['Sed'],SWB_Y_RCP26['Sed'],SWB_Y_RCP45['Sed'],SWB_Y_RCP85['Sed'] = pd.DataFrame(Sed_NCC.resample("Y").sum()),pd.DataFrame(Sed_RCP26.resample("Y").sum()),pd.DataFrame(Sed_RCP45.resample("Y").sum()),pd.DataFrame(Sed_RCP85.resample("Y").sum()) 
SWB_Y_NCC['Cov'],SWB_Y_RCP26['Cov'],SWB_Y_RCP45['Cov'],SWB_Y_RCP85['Cov'] = pd.DataFrame(Cov_NCC.resample("Y").mean()),pd.DataFrame(Cov_RCP26.resample("Y").mean()),pd.DataFrame(Cov_RCP45.resample("Y").mean()),pd.DataFrame(Cov_RCP85.resample("Y").mean()) 
SWB_Y_NCC['AET1'],SWB_Y_RCP26['AET1'],SWB_Y_RCP45['AET1'],SWB_Y_RCP85['AET1'] = pd.DataFrame(AET1_NCC.resample("Y").sum()),pd.DataFrame(AET1_RCP26.resample("Y").sum()),pd.DataFrame(AET1_RCP45.resample("Y").sum()),pd.DataFrame(AET1_RCP85.resample("Y").sum()) 
SWB_Y_NCC['Lw3'],SWB_Y_RCP26['Lw3'],SWB_Y_RCP45['Lw3'],SWB_Y_RCP85['Lw3'] = pd.DataFrame(Lw3_NCC.resample("Y").sum()),pd.DataFrame(Lw3_RCP26.resample("Y").sum()),pd.DataFrame(Lw3_RCP45.resample("Y").sum()),pd.DataFrame(Lw3_RCP85.resample("Y").sum()) 
SWB_Y_NCC['DS1'],SWB_Y_RCP26['DS1'],SWB_Y_RCP45['DS1'],SWB_Y_RCP85['DS1'] = pd.DataFrame(Sws1_NCC.resample("Y").last())-pd.DataFrame(Sws1_NCC.resample("Y").first()),pd.DataFrame(Sws1_RCP26.resample("Y").last())-pd.DataFrame(Sws1_RCP26.resample("Y").first()),pd.DataFrame(Sws1_RCP45.resample("Y").last())-pd.DataFrame(Sws1_RCP45.resample("Y").first()),pd.DataFrame(Sws1_RCP85.resample("Y").last())-pd.DataFrame(Sws1_RCP85.resample("Y").first())
SWB_Y_NCC['DS2'],SWB_Y_RCP26['DS2'],SWB_Y_RCP45['DS2'],SWB_Y_RCP85['DS2'] = pd.DataFrame(Sws2_NCC.resample("Y").last())-pd.DataFrame(Sws2_NCC.resample("Y").first()),pd.DataFrame(Sws2_RCP26.resample("Y").last())-pd.DataFrame(Sws2_RCP26.resample("Y").first()),pd.DataFrame(Sws2_RCP45.resample("Y").last())-pd.DataFrame(Sws2_RCP45.resample("Y").first()),pd.DataFrame(Sws2_RCP85.resample("Y").last())-pd.DataFrame(Sws2_RCP85.resample("Y").first())
SWB_Y_NCC['DS3'],SWB_Y_RCP26['DS3'],SWB_Y_RCP45['DS3'],SWB_Y_RCP85['DS3'] =pd.DataFrame(Sws3_NCC.resample("Y").last())-pd.DataFrame(Sws3_NCC.resample("Y").first()),pd.DataFrame(Sws3_RCP26.resample("Y").last())-pd.DataFrame(Sws3_RCP26.resample("Y").first()),pd.DataFrame(Sws3_RCP45.resample("Y").last())-pd.DataFrame(Sws3_RCP45.resample("Y").first()),pd.DataFrame(Sws3_RCP85.resample("Y").last())-pd.DataFrame(Sws3_RCP85.resample("Y").first())

SWB_Y_NCC.to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/SWB_Y_NCC.csv".format(Model,Crop_type))
SWB_Y_RCP26.to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/SWB_Y_RCP26.csv".format(Model,Crop_type))
SWB_Y_RCP45.to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/SWB_Y_RCP45.csv".format(Model,Crop_type))
SWB_Y_RCP85.to_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/SWB_Y_RCP85.csv".format(Model,Crop_type))

"""
s1 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/s1情景分析处理数据.csv".format(Model,Crop_type))
s2 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/s2情景分析处理数据.csv".format(Model,Crop_type))
s3 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/s3情景分析处理数据.csv".format(Model,Crop_type))

sfc1 = 0.34676356980353806 if Crop_type ==1  else 0.34472193824075387
sw1 = 0.1809134822192267 if Crop_type ==1  else 0.12446378300482966
sfc2, sw2 = 0.3208024742181802 if Crop_type ==1  else 0.33736352237827744
sfc2, sw2 = 0.16736413942052608 if Crop_type ==1  else 0.1320443599326393
sfc3, sw3 = 0.3208024742181802 if Crop_type ==1  else 0.33736352237827744
sfc3, sw3 = 0.16736413942052608 if Crop_type ==1  else 0.1320443599326393
SWDI_F1,SWDI_F2,SWDI_F3=[],[],[]
for i1, i2,i3 in zip(s1,s2,s3):
    s1_swdi = (i1- sfc1)/(sfc1-sw1)
    s2_swdi = (i2- sfc2)/(sfc2-sw2)
    s3_swdi = (i3- sfc3)/(sfc3-sw3)
    SWDI_F1.append(s1_swdi)
    SWDI_F2.append(s2_swdi)
    SWDI_F3.append(s3_swdi)
"""





































"""
Rain_Y = pd.DataFrame(Rain.resample("Y").sum()) #年降雨
Inter_Y = pd.DataFrame(Inter.resample("Y").sum()) #年截留
Roff_Y = pd.DataFrame(Roff.resample("Y").sum()) #年径流
Sed_Y = pd.DataFrame(Sed.resample("Y").sum()) #年土壤流失
AET1_Y = pd.DataFrame(AET1.resample("Y").sum()) #年蒸散发
Lw3_Y = pd.DataFrame(Lw3.resample("Y").sum()) #年底层渗漏
S1_Y1 = pd.DataFrame(S1.resample("Y").first()) #年第1层xxxx.01.01土壤储水量
S1_Y2 = pd.DataFrame(S1.resample("Y").last()) #年第1层xxxx.12.31土壤储水量
DS1_Y = S1_Y2-S1_Y1
S2_Y1 = pd.DataFrame(S2.resample("Y").first()) #年第2层xxxx.01.01土壤储水量
S2_Y2 = pd.DataFrame(S2.resample("Y").last()) #年第2层xxxx.12.31土壤储水量
DS2_Y = S2_Y2-S2_Y1
S3_Y1 = pd.DataFrame(S3.resample("Y").first()) #年第3层xxxx.01.01土壤储水量
S3_Y2 = pd.DataFrame(S3.resample("Y").last()) #年第3层xxxx.12.31土壤储水量
DS3_Y = S3_Y2-S3_Y1
"""
"""
Rain_Y.to_csv("result/SA_result/CC/年尺度统计数据/Crop{}/Rain.csv".format(Crop_type))
Inter_Y.to_csv("result/SA_result/CC/年尺度统计数据/Crop{}/Inter.csv".format(Crop_type))
AET1_Y.to_csv("result/SA_result/CC/年尺度统计数据/Crop{}/AET1.csv".format(Crop_type))
Roff_Y.to_csv("result/SA_result/CC/年尺度统计数据/Crop{}/Roff.csv".format(Crop_type))
Sed_Y.to_csv("result/SA_result/CC/年尺度统计数据/Crop{}/Sed.csv".format(Crop_type))
Lw3_Y.to_csv("result/SA_result/CC/年尺度统计数据/Crop{}/Lw3.csv".format(Crop_type))
DS1_Y.to_csv("result/SA_result/CC/年尺度统计数据/Crop{}/DS1.csv".format(Crop_type))
DS2_Y.to_csv("result/SA_result/CC/年尺度统计数据/Crop{}/DS2.csv".format(Crop_type))
DS3_Y.to_csv("result/SA_result/CC/年尺度统计数据/Crop{}/DS3.csv".format(Crop_type))
"""



