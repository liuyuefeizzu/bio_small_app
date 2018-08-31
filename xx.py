# -*- coding: utf-8 -*-
#import os
#os.chdir(r"E:\20180806C1A1-1_18个样本_普通转录组分析-复旦大学")
import xlrd

def gongneng(xinxi,shuju):
    data=xlrd.open_workbook(shuju)
    table=data.sheets()[0]
    data2=xlrd.open_workbook(xinxi)
    table2=data2.sheets()[0]

    list=table.col_values(24, start_rowx=0, end_rowx=None)
    list=list[1:]
    mulu=table.col_values(11, start_rowx=0, end_rowx=None)
    mulu=mulu[1:]
#mulu=table.cell_value(1,11).split("/")[:-1]
#mulu="/".join(mulu)+'/'
    sample_list=[]
    sample=table2.col_values(2, start_rowx=0, end_rowx=None)
    for i in range(11,len(sample)):
        if sample[i] == '':
            break
        sample_list.append(sample[i])
    group_list=[]
    group=table2.col_values(3, start_rowx=0, end_rowx=None)
    for i in range(11,len(group)):
        if group[i] == '':
            break
        group_list.append(group[i])
#print sample_list
#print group_list
    #data="实验名称\t数据类型\t实验描述\t样本名称\t分组\t描述\t文件名\tmd5\t保存路径\n"
    data=""
    for i in range(len(list)):
         data=data+"\t\t\t"+sample_list[i]+"\t"+group_list[i]+"\t\t"+list[i].split()[2].split("/")[6]+"\t\t"+"/".join( mulu[i].split("/")[:-1])+'/'+list[i].split()[2].split("/")[6]+"\n"
         data=data+"\t\t\t"+sample_list[i]+"\t"+group_list[i]+"\t\t"+list[i].split()[16].split("/")[6]+"\t\t"+"/".join( mulu[i].split("/")[:-1])+'/'+list[i].split()[16].split("/")[6]+"\n"
    #print data
    return data


'''
fh=open("样本分组表_test.xlsx","w")
fh.write("实验名称\t数据类型\t实验描述\t样本名称\t分组\t描述\t文件名\tmd5\t保存路径\n")
fh.write("mRNA\tRNA-Seq\n")
for i in range(len(list)):
    fh.write("\t\t\t"+sample_list[i]+"\t"+group_list[i]+"\t\t"+list[i].split()[2].split("/")[6]+"\t\t"+"/".join( mulu[i].split("/")[:-1])+'/'+list[i].split()[2].split("/")[6]+"\n")
    fh.write("\t\t\t"+sample_list[i]+"\t"+group_list[i]+"\t\t"+list[i].split()[16].split("/")[6]+"\t\t"+"/".join( mulu[i].split("/")[:-1])+'/'+list[i].split()[16].split("/")[6]+"\n")
    
 #   print"/".join( mulu[i].split("/")[:-1])+'/'
 #   print list[i].split()[2].split("/")[6]
 #   print list[i].split()[16].split("/")[6]
 #   print '#'
fh.close()

'''

