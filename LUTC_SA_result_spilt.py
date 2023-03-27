#导入包
import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei") #字体

Crop_typeA = 3 ##土地利用转换前植被类型
Crop_typeB = 2 #土地利用转换后植被类型
Model = "IPSL_CM5A_MR"

SWB_Y_NCC,SWB_Y_RCP26,SWB_Y_RCP45,SWB_Y_RCP85=pd.DataFrame(),pd.DataFrame(),pd.DataFrame(),pd.DataFrame()
SWB_M_NCC,SWB_M_RCP26,SWB_M_RCP45,SWB_M_RCP85=pd.DataFrame(),pd.DataFrame(),pd.DataFrame(),pd.DataFrame()
writer_Y_NCC = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/SWB_Y_NCC.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Y_RCP26 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/SWB_Y_RCP26.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Y_RCP45= pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/SWB_Y_RCP45.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Y_RCP85 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/SWB_Y_RCP85.xls".format(Model,Crop_typeA,Crop_typeB))
writer_M_NCC = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/SWB_M_NCC.xls".format(Model,Crop_typeA,Crop_typeB))
writer_M_RCP26 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/SWB_M_RCP26.xls".format(Model,Crop_typeA,Crop_typeB))
writer_M_RCP45 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/SWB_M_RCP45.xls".format(Model,Crop_typeA,Crop_typeB))
writer_M_RCP85 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/SWB_M_RCP85.xls".format(Model,Crop_typeA,Crop_typeB))

writer_s1 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/s1情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_s2 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/s2情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_s3 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/s3情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_w1 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/w1情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_w2 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/w2情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_w3 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/w3情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Rain = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/Rain情景分析处理数据5.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Inter = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/Inter情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Roff = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/Roff情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_sed = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/sed情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Cov = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/Cov情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_AET1 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/AET1情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_AET2 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/AET2情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_AET3 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/AET3情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Lw1 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/Lw1情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Lw2 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/Lw2情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))
writer_Lw3 = pd.ExcelWriter("result/SA_result/CC_LUTC/{}/Crop{}_{}/拆分处理后的数据/Lw3情景分析处理数据.xls".format(Model,Crop_typeA,Crop_typeB))


CC_s1 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/s1情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_s2 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/s2情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_s3 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/s3情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_w1 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/w1情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_w2 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/w2情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_w3 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/w3情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_Rain = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Rain情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_Inter = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Inter情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_Roff = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Roff情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_sed = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Sed情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_Cov = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Cov情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_AET1 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/AET1情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_AET2 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/AET2情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_AET3 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/AET3情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_Lw1 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Lw1情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_Lw2 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Lw2情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
CC_Lw3 = pd.read_csv("result/SA_result/CC/{}/拆分处理后的数据/Crop{}/Lw3情景分析处理数据.csv".format(Model,Crop_typeA),usecols=[1,2,3,4])
date1 =pd.date_range(start='2021/1/1', end='2050/12/31',freq='D')
CC_s1.index,CC_s2.index,CC_s3.index,CC_w1.index,CC_w2.index,CC_w3.index,CC_AET1.index,CC_AET2.index,CC_AET3.index,CC_Rain.index,CC_Inter.index,CC_Roff.index,CC_sed.index,CC_Cov.index,CC_Lw1.index,CC_Lw2.index,CC_Lw3.index = date1,date1,date1,date1,date1,date1,date1,date1,date1,date1,date1,date1,date1,date1,date1,date1,date1
for X in range(1,30): #X:土地利用转换前植被A种植年限
    file_dir = "result/SA_result/CC_LUTC/{}/Crop{}_{}/植被A种植{}年后开始转换" .format(Model,Crop_typeA,Crop_typeB,X)     #读取模拟含水率数据
    file_list = os.listdir(file_dir)  #获取指定路径下的全部文件
    LUTC_s1 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_s2 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_s3 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_w1 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_w2 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_w3 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_Rain = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_Inter = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_Roff =  {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_sed = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_Cov = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_AET1 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_AET2 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_AET3 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_Lw1 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_Lw2 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
    LUTC_Lw3 = {"第{}种气候变化类型".format(order):[] for order in np.arange(1,len(file_list)+1,1)}
   
    date2 = pd.date_range(start = '20{}/1/1'.format(X+21), end='2050/12/31',freq='D') 
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
            LUTC_s1["第{}种气候变化类型".format(order)].append(eval(s_data[day])[0])
            LUTC_s2["第{}种气候变化类型".format(order)].append(eval(s_data[day])[1])
            LUTC_s3["第{}种气候变化类型".format(order)].append(eval(s_data[day])[2])
            LUTC_w1["第{}种气候变化类型".format(order)].append(eval(w_data[day])[0])
            LUTC_w2["第{}种气候变化类型".format(order)].append(eval(w_data[day])[1])
            LUTC_w3["第{}种气候变化类型".format(order)].append(eval(w_data[day])[2])
            LUTC_Rain["第{}种气候变化类型".format(order)].append(eval(Rain_data[day]))
            LUTC_Inter["第{}种气候变化类型".format(order)].append(eval(Inter_data[day]))
            LUTC_Roff["第{}种气候变化类型".format(order)].append(eval(Roff_data[day]))
            LUTC_sed["第{}种气候变化类型".format(order)].append(eval(sed_data[day]))
            LUTC_Cov["第{}种气候变化类型".format(order)].append(eval(Cov_data[day]))
            LUTC_AET1["第{}种气候变化类型".format(order)].append(eval(AET_data[day])[0])
            LUTC_AET2["第{}种气候变化类型".format(order)].append(eval(AET_data[day])[1])
            LUTC_AET3["第{}种气候变化类型".format(order)].append(eval(AET_data[day])[2])
            LUTC_Lw1["第{}种气候变化类型".format(order)].append(eval(Lw_data[day])[0])
            LUTC_Lw2["第{}种气候变化类型".format(order)].append(eval(Lw_data[day])[1])
            LUTC_Lw3["第{}种气候变化类型".format(order)].append(eval(Lw_data[day])[2])
    LUTC_s1,LUTC_s2,LUTC_s3,LUTC_w1, LUTC_w2,LUTC_w3,LUTC_Rain,LUTC_Inter,LUTC_Roff,LUTC_sed, LUTC_Cov,LUTC_AET1, LUTC_AET2, LUTC_AET3,LUTC_Lw1,LUTC_Lw2,LUTC_Lw3=pd.DataFrame(LUTC_s1,index=date2),pd.DataFrame(LUTC_s2,index=date2), pd.DataFrame(LUTC_s3,index=date2),pd.DataFrame(LUTC_w1,index=date2),pd.DataFrame(LUTC_w2,index=date2),pd.DataFrame(LUTC_w3,index=date2),pd.DataFrame(LUTC_Rain,index=date2),pd.DataFrame(LUTC_Inter,index=date2),pd.DataFrame(LUTC_Roff,index=date2),pd.DataFrame(LUTC_sed,index=date2), pd.DataFrame(LUTC_Cov,index=date2),pd.DataFrame(LUTC_AET1,index=date2),pd.DataFrame(LUTC_AET2,index=date2),pd.DataFrame(LUTC_AET3,index=date2),pd.DataFrame(LUTC_Lw1,index=date2),pd.DataFrame(LUTC_Lw2,index=date2), pd.DataFrame(LUTC_Lw3,index=date2)    
    CC_s12,CC_s22,CC_s32,CC_w12,CC_w22,CC_w32,CC_Rain2,CC_Inter2,CC_Roff2,CC_sed2,CC_Cov2,CC_AET12,CC_AET22,CC_AET32,CC_Lw12,CC_Lw22,CC_Lw32=CC_s1["20210101":"20{}1231".format(X+20)],CC_s2["20210101":"20{}1231".format(X+20)],CC_s3["20210101":"20{}1231".format(X+20)],CC_w1["20210101":"20{}1231".format(X+20)],CC_w2["20210101":"20{}1231".format(X+20)],CC_w3["20210101":"20{}1231".format(X+20)],CC_Rain["20210101":"20{}1231".format(X+20)],CC_Inter["20210101":"20{}1231".format(X+20)],CC_Roff["20210101":"20{}1231".format(X+20)],CC_sed["20210101":"20{}1231".format(X+20)],CC_Cov["20210101":"20{}1231".format(X+20)],CC_AET1["20210101":"20{}1231".format(X+20)],CC_AET2["20210101":"20{}1231".format(X+20)],CC_AET3["20210101":"20{}1231".format(X+20)],CC_Lw1["20210101":"20{}1231".format(X+20)],CC_Lw2["20210101":"20{}1231".format(X+20)],CC_Lw3["20210101":"20{}1231".format(X+20)]
    s1,s2,s3,w1,w2,w3,Rain,Inter,Roff,sed,Cov,AET1,AET2,AET3,Lw1,Lw2,Lw3 = CC_s12.append(LUTC_s1),CC_s22.append(LUTC_s2),CC_s32.append(LUTC_s3),CC_w12.append(LUTC_w1),CC_w22.append(LUTC_w2),CC_w32.append(LUTC_w3),CC_Rain2.append(LUTC_Rain),CC_Inter2.append(LUTC_Inter),CC_Roff2.append(LUTC_Roff),CC_sed2.append(LUTC_sed),CC_Cov2.append(LUTC_Cov),CC_AET12.append(LUTC_AET1),CC_AET22.append(LUTC_AET2),CC_AET32.append(LUTC_AET3),CC_Lw12.append(LUTC_Lw1),CC_Lw22.append(LUTC_Lw2),CC_Lw32.append(LUTC_Lw3)
    
    
    s1.to_excel(writer_s1,sheet_name="转换年限X={}".format(X))
    s2.to_excel(writer_s2,sheet_name="转换年限X={}".format(X))
    s3.to_excel(writer_s3,sheet_name="转换年限X={}".format(X))
    w1.to_excel(writer_w1,sheet_name="转换年限X={}".format(X))
    w2.to_excel(writer_w2,sheet_name="转换年限X={}".format(X))
    w3.to_excel(writer_w3,sheet_name="转换年限X={}".format(X))
    Rain.to_excel(writer_Rain,sheet_name="转换年限X={}".format(X))
    Inter.to_excel(writer_Inter,sheet_name="转换年限X={}".format(X))
    Roff.to_excel(writer_Roff,sheet_name="转换年限X={}".format(X))
    sed.to_excel(writer_sed,sheet_name="转换年限X={}".format(X))
    Cov.to_excel(writer_Cov,sheet_name="转换年限X={}".format(X))
    AET1.to_excel(writer_AET1,sheet_name="转换年限X={}".format(X))
    AET2.to_excel(writer_AET2,sheet_name="转换年限X={}".format(X))
    AET3.to_excel(writer_AET3,sheet_name="转换年限X={}".format(X))
    Lw1.to_excel(writer_Lw1,sheet_name="转换年限X={}".format(X))
    Lw2.to_excel(writer_Lw2,sheet_name="转换年限X={}".format(X))
    Lw3.to_excel(writer_Lw3,sheet_name="转换年限X={}".format(X))


    ##计算年水量守恒
    Rain_NCC,Cov_NCC,Inter_NCC,AET1_NCC,Roff_NCC,sed_NCC,Lw3_NCC,w1_NCC,w2_NCC,w3_NCC = Rain['第1种气候变化类型'],Cov['第1种气候变化类型'],Inter['第1种气候变化类型'],AET1['第1种气候变化类型'],Roff['第1种气候变化类型'],sed['第1种气候变化类型'],Lw3['第1种气候变化类型'],w1['第1种气候变化类型'],w2['第1种气候变化类型'],w3['第1种气候变化类型']
    Rain_RCP26,Cov_RCP26,Inter_RCP26,AET1_RCP26,Roff_RCP26,sed_RCP26,Lw3_RCP26,w1_RCP26,w2_RCP26,w3_RCP26 = Rain['第2种气候变化类型'],Cov['第2种气候变化类型'],Inter['第2种气候变化类型'],AET1['第2种气候变化类型'],Roff['第2种气候变化类型'],sed['第2种气候变化类型'],Lw3['第2种气候变化类型'],w1['第2种气候变化类型'],w2['第2种气候变化类型'],w3['第2种气候变化类型']
    Rain_RCP45,Cov_RCP45,Inter_RCP45,AET1_RCP45,Roff_RCP45,sed_RCP45,Lw3_RCP45,w1_RCP45,w2_RCP45,w3_RCP45 = Rain['第3种气候变化类型'],Cov['第3种气候变化类型'],Inter['第3种气候变化类型'],AET1['第3种气候变化类型'],Roff['第3种气候变化类型'],sed['第3种气候变化类型'],Lw3['第3种气候变化类型'],w1['第3种气候变化类型'],w2['第3种气候变化类型'],w3['第3种气候变化类型']
    Rain_RCP85,Cov_RCP85,Inter_RCP85,AET1_RCP85,Roff_RCP85,sed_RCP85,Lw3_RCP85,w1_RCP85,w2_RCP85,w3_RCP85 = Rain['第4种气候变化类型'],Cov['第4种气候变化类型'],Inter['第4种气候变化类型'],AET1['第4种气候变化类型'],Roff['第4种气候变化类型'],sed['第4种气候变化类型'],Lw3['第4种气候变化类型'],w1['第4种气候变化类型'],w2['第4种气候变化类型'],w3['第4种气候变化类型']
    
    ##年尺度 
    SWB_Y_NCC['Rain'],SWB_Y_RCP26['Rain'],SWB_Y_RCP45['Rain'],SWB_Y_RCP85['Rain'] = Rain_NCC.resample("Y").sum(),Rain_RCP26.resample("Y").sum(),Rain_RCP45.resample("Y").sum(),Rain_RCP85.resample("Y").sum()
    SWB_Y_NCC['Inter'],SWB_Y_RCP26['Inter'],SWB_Y_RCP45['Inter'],SWB_Y_RCP85['Inter'] = Inter_NCC.resample("Y").sum(),Inter_RCP26.resample("Y").sum(),Inter_RCP45.resample("Y").sum(),Inter_RCP85.resample("Y").sum()
    SWB_Y_NCC['Roff'],SWB_Y_RCP26['Roff'],SWB_Y_RCP45['Roff'],SWB_Y_RCP85['Roff'] = Roff_NCC.resample("Y").sum(),Roff_RCP26.resample("Y").sum(),Roff_RCP45.resample("Y").sum(),Roff_RCP85.resample("Y").sum()
    SWB_Y_NCC['AET1'],SWB_Y_RCP26['AET1'],SWB_Y_RCP45['AET1'],SWB_Y_RCP85['AET1'] = AET1_NCC.resample("Y").sum()-3,AET1_RCP26.resample("Y").sum()-3,AET1_RCP45.resample("Y").sum()-3,AET1_RCP85.resample("Y").sum()-3 
    SWB_Y_NCC['Lw3'],SWB_Y_RCP26['Lw3'],SWB_Y_RCP45['Lw3'],SWB_Y_RCP85['Lw3'] = Lw3_NCC.resample("Y").sum(),Lw3_RCP26.resample("Y").sum(),Lw3_RCP45.resample("Y").sum(),Lw3_RCP85.resample("Y").sum()
    SWB_Y_NCC['DS1'],SWB_Y_RCP26['DS1'],SWB_Y_RCP45['DS1'],SWB_Y_RCP85['DS1'] = w1_NCC.resample("Y").last()-w1_NCC.resample("Y").first()+3,w1_RCP26.resample("Y").last()-w1_RCP26.resample("Y").first()+3,w1_RCP45.resample("Y").last()-w1_RCP45.resample("Y").first()+3,w1_RCP85.resample("Y").last()-w1_RCP85.resample("Y").first()+3
    SWB_Y_NCC['DS2'],SWB_Y_RCP26['DS2'],SWB_Y_RCP45['DS2'],SWB_Y_RCP85['DS2'] = w2_NCC.resample("Y").last()-w2_NCC.resample("Y").first(),w2_RCP26.resample("Y").last()-w2_RCP26.resample("Y").first(),w2_RCP45.resample("Y").last()-w2_RCP45.resample("Y").first(),w2_RCP85.resample("Y").last()-w2_RCP85.resample("Y").first()
    SWB_Y_NCC['DS3'],SWB_Y_RCP26['DS3'],SWB_Y_RCP45['DS3'],SWB_Y_RCP85['DS3'] = w3_NCC.resample("Y").last()-w3_NCC.resample("Y").first(),w3_RCP26.resample("Y").last()-w3_RCP26.resample("Y").first(),w3_RCP45.resample("Y").last()-w3_RCP45.resample("Y").first(),w3_RCP85.resample("Y").last()-w3_RCP85.resample("Y").first()
    SWB_Y_NCC['Sed'],SWB_Y_RCP26['Sed'],SWB_Y_RCP45['Sed'],SWB_Y_RCP85['Sed'] = sed_NCC.resample("Y").sum(),sed_RCP26.resample("Y").sum(),sed_RCP45.resample("Y").sum(),sed_RCP85.resample("Y").sum()
    SWB_Y_NCC['Cov'],SWB_Y_RCP26['Cov'],SWB_Y_RCP45['Cov'],SWB_Y_RCP85['Cov'] = Cov_NCC.resample("Y").mean(),Cov_RCP26.resample("Y").mean(),Cov_RCP45.resample("Y").mean(),Cov_RCP85.resample("Y").mean()
    
    #月尺度
    SWB_M_NCC['Rain'],SWB_M_RCP26['Rain'],SWB_M_RCP45['Rain'],SWB_M_RCP85['Rain'] = pd.DataFrame(Rain_NCC.resample("M").sum()),pd.DataFrame(Rain_RCP26.resample("M").sum()),pd.DataFrame(Rain_RCP45.resample("M").sum()),pd.DataFrame(Rain_RCP85.resample("M").sum())
    SWB_M_NCC['Inter'],SWB_M_RCP26['Inter'],SWB_M_RCP45['Inter'],SWB_M_RCP85['Inter'] = pd.DataFrame(Inter_NCC.resample("M").sum()),pd.DataFrame(Inter_RCP26.resample("M").sum()),pd.DataFrame(Inter_RCP45.resample("M").sum()),pd.DataFrame(Inter_RCP85.resample("M").sum()) 
    SWB_M_NCC['Roff'],SWB_M_RCP26['Roff'],SWB_M_RCP45['Roff'],SWB_M_RCP85['Roff'] = pd.DataFrame(Roff_NCC.resample("M").sum()),pd.DataFrame(Roff_RCP26.resample("M").sum()),pd.DataFrame(Roff_RCP45.resample("M").sum()),pd.DataFrame(Roff_RCP85.resample("M").sum())
    SWB_M_NCC['AET1'],SWB_M_RCP26['AET1'],SWB_M_RCP45['AET1'],SWB_M_RCP85['AET1'] = pd.DataFrame(AET1_NCC.resample("M").sum()),pd.DataFrame(AET1_RCP26.resample("M").sum()),pd.DataFrame(AET1_RCP45.resample("M").sum()),pd.DataFrame(AET1_RCP85.resample("M").sum()) 
    SWB_M_NCC['Lw3'],SWB_M_RCP26['Lw3'],SWB_M_RCP45['Lw3'],SWB_M_RCP85['Lw3'] = pd.DataFrame(Lw3_NCC.resample("M").sum()),pd.DataFrame(Lw3_RCP26.resample("M").sum()),pd.DataFrame(Lw3_RCP45.resample("M").sum()),pd.DataFrame(Lw3_RCP85.resample("M").sum()) 
    SWB_M_NCC['DS1'],SWB_M_RCP26['DS1'],SWB_M_RCP45['DS1'],SWB_M_RCP85['DS1'] = pd.DataFrame(w1_NCC.resample("M").last())-pd.DataFrame(w1_NCC.resample("M").first()),pd.DataFrame(w1_RCP26.resample("M").last())-pd.DataFrame(w1_RCP26.resample("M").first()),pd.DataFrame(w1_RCP45.resample("M").last())-pd.DataFrame(w1_RCP45.resample("M").first()),pd.DataFrame(w1_RCP85.resample("M").last())-pd.DataFrame(w1_RCP85.resample("M").first())
    SWB_M_NCC['DS2'],SWB_M_RCP26['DS2'],SWB_M_RCP45['DS2'],SWB_M_RCP85['DS2'] = pd.DataFrame(w2_NCC.resample("M").last())-pd.DataFrame(w2_NCC.resample("M").first()),pd.DataFrame(w2_RCP26.resample("M").last())-pd.DataFrame(w2_RCP26.resample("M").first()),pd.DataFrame(w2_RCP45.resample("M").last())-pd.DataFrame(w2_RCP45.resample("M").first()),pd.DataFrame(w2_RCP85.resample("M").last())-pd.DataFrame(w2_RCP85.resample("M").first())
    SWB_M_NCC['DS3'],SWB_M_RCP26['DS3'],SWB_M_RCP45['DS3'],SWB_M_RCP85['DS3'] =pd.DataFrame(w3_NCC.resample("M").last())-pd.DataFrame(w3_NCC.resample("M").first()),pd.DataFrame(w3_RCP26.resample("M").last())-pd.DataFrame(w3_RCP26.resample("M").first()),pd.DataFrame(w3_RCP45.resample("M").last())-pd.DataFrame(w3_RCP45.resample("M").first()),pd.DataFrame(w3_RCP85.resample("M").last())-pd.DataFrame(w3_RCP85.resample("M").first())
    SWB_M_NCC['Sed'],SWB_M_RCP26['Sed'],SWB_M_RCP45['Sed'],SWB_M_RCP85['Sed'] = pd.DataFrame(sed_NCC.resample("M").sum()),pd.DataFrame(sed_RCP26.resample("M").sum()),pd.DataFrame(sed_RCP45.resample("M").sum()),pd.DataFrame(sed_RCP85.resample("M").sum()) 
    SWB_M_NCC['Cov'],SWB_M_RCP26['Cov'],SWB_M_RCP45['Cov'],SWB_M_RCP85['Cov'] = pd.DataFrame(Cov_NCC.resample("M").mean()),pd.DataFrame(Cov_RCP26.resample("M").mean()),pd.DataFrame(Cov_RCP45.resample("M").mean()),pd.DataFrame(Cov_RCP85.resample("M").mean()) 

   
    SWB_Y_NCC.to_excel(writer_Y_NCC,sheet_name="转换年限X={}".format(X))
    SWB_Y_RCP26.to_excel(writer_Y_RCP26,sheet_name="转换年限X={}".format(X))
    SWB_Y_RCP45.to_excel(writer_Y_RCP45,sheet_name="转换年限X={}".format(X))
    SWB_Y_RCP85.to_excel(writer_Y_RCP85,sheet_name="转换年限X={}".format(X))
    SWB_M_NCC.to_excel(writer_M_NCC,sheet_name="转换年限X={}".format(X))
    SWB_M_RCP26.to_excel(writer_M_RCP26,sheet_name="转换年限X={}".format(X))
    SWB_M_RCP45.to_excel(writer_M_RCP45,sheet_name="转换年限X={}".format(X))
    SWB_M_RCP85.to_excel(writer_M_RCP85,sheet_name="转换年限X={}".format(X))
    
writer_s1.save(),writer_s2.save() ,writer_s3.save() ,writer_w1.save() ,writer_w2.save() ,writer_w3.save() ,writer_Rain.save() ,writer_Inter.save(),writer_Roff.save() ,writer_sed.save() ,writer_Cov.save() ,writer_AET1.save() ,writer_AET2.save(),writer_AET3.save() ,writer_Lw1.save() ,writer_Lw2.save() ,writer_Lw3.save() 
writer_s1.close(),writer_s2.close() ,writer_s3.close() ,writer_w1.close() ,writer_w2.close() ,writer_w3.close() ,writer_Rain.close() ,writer_Inter.close(),writer_Roff.close() ,writer_sed.close() ,writer_Cov.close() ,writer_AET1.close() ,writer_AET2.close(),writer_AET3.close() ,writer_Lw1.close() ,writer_Lw2.close() ,writer_Lw3.close()    
writer_Y_NCC.save(),writer_Y_RCP26.save() ,writer_Y_RCP45.save() ,writer_Y_RCP85.save() ,writer_M_NCC.save() ,writer_M_RCP26.save() ,writer_M_RCP45.save() ,writer_M_RCP85.save() 
writer_Y_NCC.close(),writer_Y_RCP26.close() ,writer_Y_RCP45.close() ,writer_Y_RCP85.close() ,writer_M_NCC.close() ,writer_M_RCP26.close() ,writer_M_RCP45.close() ,writer_M_RCP85.close()    

    