# -*- coding: utf-8 -*-
import pandas as pd


f = pd.read_excel("F:/桌面文件/文件/我的编程/P1 田间尺度模型/数据处理/SWDI.xls",index_col=0) #读取用于参数校准的气象数据
VR_F1_NOCC, VR_F1_RCP26, VR_F1_RCP45, VR_F1_RCP85 = f["VR-F1-NOCC"],f["VR-F1-RCP26"],f["VR-F1-RCP45"],f["VR-F1-RCP85"]
SB_F1_NOCC, SB_F1_RCP26, SB_F1_RCP45,	SB_F1_RCP85 = f["SB-F1-NOCC"],f["SB-F1-RCP26"],f["SB-F1-RCP45"],f["SB-F1-RCP85"]
MS_F1_NOCC,	MS_F1_RCP26, MS_F1_RCP45,	MS_F1_RCP85	= f["MS-F1-NOCC"],f["MS-F1-RCP26"],f["MS-F1-RCP45"],f["MS-F1-RCP85"]
VR_F2_NOCC,	VR_F2_RCP26, VR_F2_RCP45,	VR_F2_RCP85	= f["VR-F2-NOCC"],f["VR-F2-RCP26"],f["VR-F2-RCP45"],f["VR-F2-RCP85"]
SB_F2_NOCC,	SB_F2_RCP26, SB_F2_RCP45,	SB_F2_RCP85	= f["SB-F2-NOCC"],f["SB-F2-RCP26"],f["SB-F2-RCP45"],f["SB-F2-RCP85"]
MS_F2_NOCC,	MS_F2_RCP26, MS_F2_RCP45,	MS_F2_RCP85	= f["MS-F2-NOCC"],f["MS-F2-RCP26"],f["MS-F2-RCP45"],f["MS-F2-RCP85"]
VR_F3_NOCC,	VR_F3_RCP26, VR_F3_RCP45,	VR_F3_RCP85	= f["VR-F3-NOCC"],f["VR-F3-RCP26"],f["VR-F3-RCP45"],f["VR-F3-RCP85"]
SB_F3_NOCC,	SB_F3_RCP26, SB_F3_RCP45,	SB_F3_RCP85	= f["SB-F3-NOCC"],f["SB-F3-RCP26"],f["SB-F3-RCP45"],f["SB-F3-RCP85"]
MS_F3_NOCC,	MS_F3_RCP26, MS_F3_RCP45,	MS_F3_RCP85= f["MS-F3-NOCC"],f["MS-F3-RCP26"],f["MS-F3-RCP45"],f["MS-F3-RCP85"]

vr_F1_NOCC_1,vr_F1_NOCC_2,vr_F1_NOCC_3,vr_F1_NOCC_4,vr_F1_NOCC_5=[],[],[],[],[] 
vr_F1_RCP26_1,vr_F1_RCP26_2,vr_F1_RCP26_3,vr_F1_RCP26_4,vr_F1_RCP26_5=[],[],[],[],[] 
vr_F1_RCP45_1,vr_F1_RCP45_2,vr_F1_RCP45_3,vr_F1_RCP45_4,vr_F1_RCP45_5=[],[],[],[],[]  
vr_F1_RCP85_1,vr_F1_RCP85_2,vr_F1_RCP85_3,vr_F1_RCP85_4,vr_F1_RCP85_5=[],[],[],[],[] 
vr_F2_NOCC_1,vr_F2_NOCC_2,vr_F2_NOCC_3,vr_F2_NOCC_4,vr_F2_NOCC_5=[],[],[],[],[] 
vr_F2_RCP26_1,vr_F2_RCP26_2,vr_F2_RCP26_3,vr_F2_RCP26_4,vr_F2_RCP26_5=[],[],[],[],[] 
vr_F2_RCP45_1,vr_F2_RCP45_2,vr_F2_RCP45_3,vr_F2_RCP45_4,vr_F2_RCP45_5=[],[],[],[],[]  
vr_F2_RCP85_1,vr_F2_RCP85_2,vr_F2_RCP85_3,vr_F2_RCP85_4,vr_F2_RCP85_5=[],[],[],[],[] 
vr_F3_NOCC_1,vr_F3_NOCC_2,vr_F3_NOCC_3,vr_F3_NOCC_4,vr_F3_NOCC_5=[],[],[],[],[] 
vr_F3_RCP26_1,vr_F3_RCP26_2,vr_F3_RCP26_3,vr_F3_RCP26_4,vr_F3_RCP26_5=[],[],[],[],[] 
vr_F3_RCP45_1,vr_F3_RCP45_2,vr_F3_RCP45_3,vr_F3_RCP45_4,vr_F3_RCP45_5=[],[],[],[],[]  
vr_F3_RCP85_1,vr_F3_RCP85_2,vr_F3_RCP85_3,vr_F3_RCP85_4,vr_F3_RCP85_5=[],[],[],[],[] 

sb_F1_NOCC_1,  sb_F1_NOCC_2,  sb_F1_NOCC_3,  sb_F1_NOCC_4, sb_F1_NOCC_5=[],[],[],[],[] 
sb_F1_RCP26_1, sb_F1_RCP26_2, sb_F1_RCP26_3, sb_F1_RCP26_4, sb_F1_RCP26_5=[],[],[],[],[] 
sb_F1_RCP45_1, sb_F1_RCP45_2, sb_F1_RCP45_3, sb_F1_RCP45_4, sb_F1_RCP45_5=[],[],[],[],[]  
sb_F1_RCP85_1, sb_F1_RCP85_2, sb_F1_RCP85_3, sb_F1_RCP85_4, sb_F1_RCP85_5=[],[],[],[],[] 
sb_F2_NOCC_1,  sb_F2_NOCC_2,  sb_F2_NOCC_3, sb_F2_NOCC_4, sb_F2_NOCC_5=[],[],[],[],[] 
sb_F2_RCP26_1, sb_F2_RCP26_2, sb_F2_RCP26_3, sb_F2_RCP26_4, sb_F2_RCP26_5=[],[],[],[],[] 
sb_F2_RCP45_1, sb_F2_RCP45_2, sb_F2_RCP45_3, sb_F2_RCP45_4, sb_F2_RCP45_5=[],[],[],[],[]  
sb_F2_RCP85_1, sb_F2_RCP85_2, sb_F2_RCP85_3, sb_F2_RCP85_4, sb_F2_RCP85_5=[],[],[],[],[] 
sb_F3_NOCC_1, sb_F3_NOCC_2,   sb_F3_NOCC_3, sb_F3_NOCC_4, sb_F3_NOCC_5=[],[],[],[],[] 
sb_F3_RCP26_1, sb_F3_RCP26_2, sb_F3_RCP26_3, sb_F3_RCP26_4, sb_F3_RCP26_5=[],[],[],[],[] 
sb_F3_RCP45_1, sb_F3_RCP45_2, sb_F3_RCP45_3, sb_F3_RCP45_4, sb_F3_RCP45_5=[],[],[],[],[]  
sb_F3_RCP85_1, sb_F3_RCP85_2, sb_F3_RCP85_3, sb_F3_RCP85_4, sb_F3_RCP85_5=[],[],[],[],[] 
 
ms_F1_NOCC_1,  ms_F1_NOCC_2, ms_F1_NOCC_3, ms_F1_NOCC_4, ms_F1_NOCC_5=[],[],[],[],[] 
ms_F1_RCP26_1, ms_F1_RCP26_2, ms_F1_RCP26_3, ms_F1_RCP26_4, ms_F1_RCP26_5=[],[],[],[],[] 
ms_F1_RCP45_1, ms_F1_RCP45_2, ms_F1_RCP45_3, ms_F1_RCP45_4, ms_F1_RCP45_5=[],[],[],[],[]  
ms_F1_RCP85_1, ms_F1_RCP85_2, ms_F1_RCP85_3, ms_F1_RCP85_4, ms_F1_RCP85_5=[],[],[],[],[] 
ms_F2_NOCC_1,  ms_F2_NOCC_2, ms_F2_NOCC_3, ms_F2_NOCC_4, ms_F2_NOCC_5=[],[],[],[],[] 
ms_F2_RCP26_1, ms_F2_RCP26_2, ms_F2_RCP26_3, ms_F2_RCP26_4, ms_F2_RCP26_5=[],[],[],[],[] 
ms_F2_RCP45_1, ms_F2_RCP45_2, ms_F2_RCP45_3, ms_F2_RCP45_4, ms_F2_RCP45_5=[],[],[],[],[]  
ms_F2_RCP85_1, ms_F2_RCP85_2, ms_F2_RCP85_3, ms_F2_RCP85_4, ms_F2_RCP85_5=[],[],[],[],[] 
ms_F3_NOCC_1,  ms_F3_NOCC_2, ms_F3_NOCC_3, ms_F3_NOCC_4, ms_F3_NOCC_5=[],[],[],[],[] 
ms_F3_RCP26_1, ms_F3_RCP26_2, ms_F3_RCP26_3, ms_F3_RCP26_4, ms_F3_RCP26_5=[],[],[],[],[] 
ms_F3_RCP45_1, ms_F3_RCP45_2, ms_F3_RCP45_3, ms_F3_RCP45_4, ms_F3_RCP45_5=[],[],[],[],[]  
ms_F3_RCP85_1, ms_F3_RCP85_2, ms_F3_RCP85_3, ms_F3_RCP85_4, ms_F3_RCP85_5=[],[],[],[],[] 

for i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36 in zip(VR_F1_NOCC, VR_F1_RCP26, VR_F1_RCP45, VR_F1_RCP85,VR_F2_NOCC,	VR_F2_RCP26, VR_F2_RCP45,	VR_F2_RCP85,VR_F3_NOCC,VR_F3_RCP26, VR_F3_RCP45,VR_F3_RCP85,SB_F1_NOCC, SB_F1_RCP26, SB_F1_RCP45,	SB_F1_RCP85,SB_F2_NOCC,	SB_F2_RCP26, SB_F2_RCP45,SB_F2_RCP85,SB_F3_NOCC,SB_F3_RCP26, SB_F3_RCP45,SB_F3_RCP85,MS_F1_NOCC,MS_F1_RCP26, MS_F1_RCP45,MS_F1_RCP85,MS_F2_NOCC,MS_F2_RCP26, MS_F2_RCP45,MS_F2_RCP85,MS_F3_NOCC,	MS_F3_RCP26, MS_F3_RCP45,MS_F3_RCP85):
    if i1 >=0:
       vr_F1_NOCC_1.append(i1)
    if -2<=i1<0:
        vr_F1_NOCC_2.append(i1)
    if -5<=i1<-2:
        vr_F1_NOCC_3.append(i1)
    if -10<=i1<-5:
        vr_F1_NOCC_4.append(i1)
    if i1<-10:
        vr_F1_NOCC_5.append(i1)       
    if i2 >=0:
       vr_F1_RCP26_1.append(i2)
    if -2<=i2<0:
        vr_F1_RCP26_2.append(i2)
    if -5<=i2<-2:
        vr_F1_RCP26_3.append(i2)
    if -10<=i2<-5:
        vr_F1_RCP26_4.append(i2)
    if i2<-10:
        vr_F1_RCP26_5.append(i2)    
    if i3 >=0:
       vr_F1_RCP45_1.append(i3)
    if -2<=i3<0:
        vr_F1_RCP45_2.append(i3)
    if -5<=i3<-2:
        vr_F1_RCP45_3.append(i3)
    if -10<=i3<-5:
        vr_F1_RCP45_4.append(i3)
    if i3<-10:
        vr_F1_RCP45_5.append(i3)     
    if i4 >=0:
       vr_F1_RCP85_1.append(i4)
    if -2<=i4<0:
        vr_F1_RCP85_2.append(i4)
    if -5<=i4<-2:
        vr_F1_RCP85_3.append(i4)
    if -10<=i4<-5:
        vr_F1_RCP85_4.append(i4)
    if i4<-10:
        vr_F1_RCP85_5.append(i4)        
    if i5 >=0:
       vr_F2_NOCC_1.append(i5)
    if -2<=i5<0:
        vr_F2_NOCC_2.append(i5)
    if -5<=i5<-2:
        vr_F2_NOCC_3.append(i5)
    if -10<=i5<-5:
        vr_F2_NOCC_4.append(i5)
    if i5<-10:
        vr_F2_NOCC_5.append(i5)       
    if i6 >=0:
       vr_F2_RCP26_1.append(i6)
    if -2<=i6<0:
        vr_F2_RCP26_2.append(i6)
    if -5<=i6<-2:
        vr_F2_RCP26_3.append(i6)
    if -10<=i6<-5:
        vr_F2_RCP26_4.append(i6)
    if i6<-10:
        vr_F2_RCP26_5.append(i6)    
    if i7 >=0:
       vr_F2_RCP45_1.append(i7)
    if -2<=i7<0:
        vr_F2_RCP45_2.append(i7)
    if -5<=i7<-2:
        vr_F2_RCP45_3.append(i7)
    if -10<=i7<-5:
        vr_F2_RCP45_4.append(i7)
    if i7<-10:
        vr_F2_RCP45_5.append(i7)     
    if i8 >=0:
       vr_F2_RCP85_1.append(i8)
    if -2<=i8<0:
        vr_F2_RCP85_2.append(i8)
    if -5<=i8<-2:
        vr_F2_RCP85_3.append(i8)
    if -10<=i8<-5:
        vr_F2_RCP85_4.append(i8)
    if i8<-10:
        vr_F2_RCP85_5.append(i8)   
    if i9 >=0:
       vr_F3_NOCC_1.append(i9)
    if -2<=i9<0:
        vr_F3_NOCC_2.append(i9)
    if -5<=i9<-2:
        vr_F3_NOCC_3.append(i9)
    if -10<=i9<-5:
        vr_F3_NOCC_4.append(i9)
    if i9<-10:
        vr_F3_NOCC_5.append(i9)       
    if i10 >=0:
       vr_F3_RCP26_1.append(i10)
    if -2<=i10<0:
        vr_F3_RCP26_2.append(i10)
    if -5<=i10<-2:
        vr_F3_RCP26_3.append(i10)
    if -10<=i10<-5:
        vr_F3_RCP26_4.append(i10)
    if i10<-10:
        vr_F3_RCP26_5.append(i10)    
    if i11 >=0:
       vr_F3_RCP45_1.append(i11)
    if -2<=i11<0:
        vr_F3_RCP45_2.append(i11)
    if -5<=i11<-2:
        vr_F3_RCP45_3.append(i11)
    if -10<=i11<-5:
        vr_F3_RCP45_4.append(i11)
    if i11<-10:
        vr_F3_RCP45_5.append(i11)     
    if i12 >=0:
       vr_F3_RCP85_1.append(i12)
    if -2<=i12<0:
        vr_F3_RCP85_2.append(i12)
    if -5<=i12<-2:
        vr_F3_RCP85_3.append(i12)
    if -10<=i12<-5:
        vr_F3_RCP85_4.append(i12)
    if i12<-10:
        vr_F3_RCP85_5.append(i12) 

    
    if i13 >=0:
       sb_F1_NOCC_1.append(i13)
    if -2<=i13<0:
        sb_F1_NOCC_2.append(i13)
    if -5<=i13<-2:
        sb_F1_NOCC_3.append(i13)
    if -10<=i13<-5:
        sb_F1_NOCC_4.append(i13)
    if i13<-10:
        sb_F1_NOCC_5.append(i13)       
    if i14 >=0:
       sb_F1_RCP26_1.append(i14)
    if -2<=i14<0:
        sb_F1_RCP26_2.append(i14)
    if -5<=i14<-2:
        sb_F1_RCP26_3.append(i14)
    if -10<=i14<-5:
        sb_F1_RCP26_4.append(i14)
    if i14<-10:
        sb_F1_RCP26_5.append(i14)    
    if i15 >=0:
       sb_F1_RCP45_1.append(i15)
    if -2<=i15<0:
        sb_F1_RCP45_2.append(i15)
    if -5<=i15<-2:
        sb_F1_RCP45_3.append(i15)
    if -10<=i15<-5:
        sb_F1_RCP45_4.append(i15)
    if i15<-10:
        sb_F1_RCP45_5.append(i15)     
    if i16 >=0:
       sb_F1_RCP85_1.append(i16)
    if -2<=i16<0:
        sb_F1_RCP85_2.append(i16)
    if -5<=i16<-2:
        sb_F1_RCP85_3.append(i16)
    if -10<=i16<-5:
        sb_F1_RCP85_4.append(i16)
    if i16<-10:
        sb_F1_RCP85_5.append(i16)        
    if i17 >=0:
       sb_F2_NOCC_1.append(i17)
    if -2<=i17<0:
        sb_F2_NOCC_2.append(i17)
    if -5<=i17<-2:
        sb_F2_NOCC_3.append(i17)
    if -10<=i17<-5:
       sb_F2_NOCC_4.append(i17)
    if i17<-10:
        sb_F2_NOCC_5.append(i17)       
    if i18 >=0:
       sb_F2_RCP26_1.append(i18)
    if -2<=i18<0:
        sb_F2_RCP26_2.append(i18)
    if -5<=i18<-2:
        sb_F2_RCP26_3.append(i18)
    if -10<=i18<-5:
        sb_F2_RCP26_4.append(i18)
    if i18<-10:
        sb_F2_RCP26_5.append(i18)    
    if i19 >=0:
       sb_F2_RCP45_1.append(i19)
    if -2<=i19<0:
        sb_F2_RCP45_2.append(i19)
    if -5<=i19<-2:
        sb_F2_RCP45_3.append(i19)
    if -10<=i19<-5:
        sb_F2_RCP45_4.append(i19)
    if i19<-10:
        sb_F2_RCP45_5.append(i19)     
    if i20 >=0:
       sb_F2_RCP85_1.append(i20)
    if -2<=i20<0:
        sb_F2_RCP85_2.append(i20)
    if -5<=i20<-2:
        sb_F2_RCP85_3.append(i20)
    if -10<=i20<-5:
        sb_F2_RCP85_4.append(i20)
    if i20<-10:
        sb_F2_RCP85_5.append(i20)   
    if i21 >=0:
       sb_F3_NOCC_1.append(i21)
    if -2<=i21<0:
       sb_F3_NOCC_2.append(i21)
    if -5<=i21<-2:
        sb_F3_NOCC_3.append(i21)
    if -10<=i21<-5:
        sb_F3_NOCC_4.append(i21)
    if i21<-10:
        sb_F3_NOCC_5.append(i21)       
    if i22 >=0:
       sb_F3_RCP26_1.append(i22)
    if -2<=i22<0:
        sb_F3_RCP26_2.append(i22)
    if -5<=i22<-2:
        sb_F3_RCP26_3.append(i22)
    if -10<=i22<-5:
        sb_F3_RCP26_4.append(i22)
    if i22<-10:
        sb_F3_RCP26_5.append(i22)    
    if i23 >=0:
       sb_F3_RCP45_1.append(i23)
    if -2<=i23<0:
        sb_F3_RCP45_2.append(i23)
    if -5<=i23<-2:
        sb_F3_RCP45_3.append(i23)
    if -10<=i23<-5:
        sb_F3_RCP45_4.append(i23)
    if i23<-10:
        sb_F3_RCP45_5.append(i23)     
    if i23>=0:
       sb_F3_RCP85_1.append(i24)
    if -2<=i24<0:
        sb_F3_RCP85_2.append(i24)
    if -5<=i24<-2:
        sb_F3_RCP85_3.append(i24)
    if -10<=i24<-5:
        sb_F3_RCP85_4.append(i24)
    if i24<-10:
        sb_F3_RCP85_5.append(i24) 
  
        
    if i25 >=0:
       ms_F1_NOCC_1.append(i25)
    if -2<=i25<0:
        ms_F1_NOCC_2.append(i25)
    if -5<=i25<-2:
        ms_F1_NOCC_3.append(i25)
    if -10<=i25<-5:
        ms_F1_NOCC_4.append(i25)
    if i25<-10:
        ms_F1_NOCC_5.append(i25)       
    if i26 >=0:
       ms_F1_RCP26_1.append(i26)
    if -2<=i26<0:
        ms_F1_RCP26_2.append(i26)
    if -5<=i26<-2:
        ms_F1_RCP26_3.append(i26)
    if -10<=i26<-5:
        ms_F1_RCP26_4.append(i26)
    if i26<-10:
        ms_F1_RCP26_5.append(i26)    
    if i27 >=0:
       ms_F1_RCP45_1.append(i27)
    if -2<=i27<0:
        ms_F1_RCP45_2.append(i27)
    if -5<=i27<-2:
        ms_F1_RCP45_3.append(i27)
    if -10<=i27<-5:
        ms_F1_RCP45_4.append(i27)
    if i27<-10:
        ms_F1_RCP45_5.append(i27)     
    if i28 >=0:
       ms_F1_RCP85_1.append(i28)
    if -2<=i28<0:
        ms_F1_RCP85_2.append(i28)
    if -5<=i28<-2:
        ms_F1_RCP85_3.append(i28)
    if -10<=i28<-5:
        ms_F1_RCP85_4.append(i28)
    if i28<-10:
        ms_F1_RCP85_5.append(i28)        
    if i29 >=0:
       ms_F2_NOCC_1.append(i29)
    if -2<=i29<0:
        ms_F2_NOCC_2.append(i29)
    if -5<=i29<-2:
        ms_F2_NOCC_3.append(i29)
    if -10<=i29<-5:
       ms_F2_NOCC_4.append(i29)
    if i29<-10:
        ms_F2_NOCC_5.append(i29)       
    if i30 >=0:
       ms_F2_RCP26_1.append(i30)
    if -2<=i30<0:
        ms_F2_RCP26_2.append(i30)
    if -5<=i30<-2:
        ms_F2_RCP26_3.append(i30)
    if -10<=i30<-5:
        ms_F2_RCP26_4.append(i30)
    if i30<-10:
        ms_F2_RCP26_5.append(i30)    
    if i31 >=0:
       ms_F2_RCP45_1.append(i31)
    if -2<=i31<0:
        ms_F2_RCP45_2.append(i31)
    if -5<=i31<-2:
        ms_F2_RCP45_3.append(i31)
    if -10<=i31<-5:
        ms_F2_RCP45_4.append(i31)
    if i31<-10:
        ms_F2_RCP45_5.append(i31)     
    if i32 >=0:
       ms_F2_RCP85_1.append(i32)
    if -2<=i32<0:
        ms_F2_RCP85_2.append(i32)
    if -5<=i32<-2:
        ms_F2_RCP85_3.append(i32)
    if -10<=i32<-5:
        ms_F2_RCP85_4.append(i32)
    if i32<-10:
        ms_F2_RCP85_5.append(i32)   
    if i33 >=0:
       ms_F3_NOCC_1.append(i33)
    if -2<=i33<0:
       ms_F3_NOCC_2.append(i33)
    if -5<=i33<-2:
        ms_F3_NOCC_3.append(i33)
    if -10<=i33<-5:
        ms_F3_NOCC_4.append(i33)
    if i33<-10:
        ms_F3_NOCC_5.append(i33)       
    if i34 >=0:
       ms_F3_RCP26_1.append(i34)
    if -2<=i34<0:
        ms_F3_RCP26_2.append(i34)
    if -5<=i34<-2:
        ms_F3_RCP26_3.append(i34)
    if -10<=i34<-5:
        ms_F3_RCP26_4.append(i34)
    if i34<-10:
        ms_F3_RCP26_5.append(i34)    
    if i35 >=0:
       ms_F3_RCP45_1.append(i35)
    if -2<=i35<0:
        ms_F3_RCP45_2.append(i35)
    if -5<=i35<-2:
        ms_F3_RCP45_3.append(i35)
    if -10<=i35<-5:
        ms_F3_RCP45_4.append(i35)
    if i35<-10:
        ms_F3_RCP45_5.append(i35)     
    if i36>=0:
       ms_F3_RCP85_1.append(i36)
    if -2<=i36<0:
        ms_F3_RCP85_2.append(i36)
    if -5<=i36<-2:
        ms_F3_RCP85_3.append(i36)
    if -10<=i36<-5:
        ms_F3_RCP85_4.append(i36)
    if i36<-10:
        ms_F3_RCP85_5.append(i36) 
