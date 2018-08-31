# -*- coding: utf-8 -*-
import wx
import os
from xx import gongneng

xin_xi_sou_ji_biao="##"
shu_ju_lu_jing_biao="##"

class myframe(wx.Frame):#文本编辑控件
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(900,500))
        self.control=wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.Show(True)
  

class mainwindow(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(600,380))
        self.control=wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu=wx.Menu()
        #open=filemenu.Append(wx.ID_OPEN,"open","open a file to textCtrl")
        filemenu.AppendSeparator()
        about=filemenu.Append(wx.ID_ABOUT,"about","information about this program")
        filemenu.AppendSeparator()
        exit=filemenu.Append(wx.ID_EXIT,"exit", "stop the program")
  
        menuBar=wx.MenuBar()
        menuBar.Append(filemenu,"file")

        #self.Bind(wx.EVT_MENU,self.onopen,open)
        self.Bind(wx.EVT_MENU,self.onabout,about)
        self.Bind(wx.EVT_MENU,self.onexit,exit)

        self.SetMenuBar(menuBar)
########################################
        self.sizer2=wx.BoxSizer(wx.HORIZONTAL)
        button1=wx.Button(self,-1,"上传信息搜集表")
        button2=wx.Button(self,-1,"上传数据路径表")
        button3=wx.Button(self,-1,"生成分组信息表")
        button4=wx.Button(self,-1,"保存分组信息表")
        self.sizer2.Add(button1,1,wx.EXPAND)
        self.sizer2.Add(button2,1,wx.EXPAND)
        self.sizer2.Add(button3,1,wx.EXPAND)
        self.sizer2.Add(button4,1,wx.EXPAND)

        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control,6,wx.EXPAND)
        self.sizer.Add(self.sizer2,1,wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        #self.sizer.Fit(self)
        
        self.Bind(wx.EVT_BUTTON,self.onopen_1,button1)
        self.Bind(wx.EVT_BUTTON,self.onopen_2,button2)
        self.Bind(wx.EVT_BUTTON,self.sheng_cheng_fen_zu_xin_xi_biao,button3)
        self.Bind(wx.EVT_BUTTON,self.bao_cun_fen_zu_xin_xi_biao,button4)
        self.Show(True)



    def onabout(self,event):
        dlg=wx.MessageDialog(self,"一个 hello world 程序","detail message",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        print "aaaa"
        
    def onexit(self,event):
        print "bbbbb"
        self.Close()

    def onopen_1(self,event):
        global xin_xi_sou_ji_biao
        self.dirname=""
        dlg=wx.FileDialog(self,"Choose a file", self.dirname, "","*.*")
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            xin_xi_sou_ji_biao=os.path.join(self.dirname,self.filename)
           # print xin_xi_sou_ji_biao
        dlg.Destroy()
        if xin_xi_sou_ji_biao != "##":
            self.control.SetValue("##########\n"+xin_xi_sou_ji_biao+"\nsuccessful\n##########")

    def onopen_2(self,event):
        global shu_ju_lu_jing_biao
        self.dirname=""
        dlg=wx.FileDialog(self,"Choose a file", self.dirname, "","*.*")
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            shu_ju_lu_jing_biao=os.path.join(self.dirname,self.filename)
            #print shu_ju_lu_jing_biao
        dlg.Destroy()
        if shu_ju_lu_jing_biao != "##":
            self.control.SetValue("##########\n"+shu_ju_lu_jing_biao+"\nsuccessfu\n##########l")
    def sheng_cheng_fen_zu_xin_xi_biao(self,event):
        print shu_ju_lu_jing_biao
        print xin_xi_sou_ji_biao
        if xin_xi_sou_ji_biao == "##":
            dlg=wx.MessageDialog(self,"警告：请上传信息搜集表","警告",wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        elif shu_ju_lu_jing_biao == "##":
            dlg=wx.MessageDialog(self,"警告：请上传数据路径表","警告",wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            group_list=[]
            sample_list=[]
            list=[]
            self.data2=gongneng(xin_xi_sou_ji_biao,shu_ju_lu_jing_biao)              
            #print data2
            self.control.SetValue("##########\n生成分组信息表.........\nsuccessful\n##########l")


    def bao_cun_fen_zu_xin_xi_biao(self,event):
        filesFilter="xlsx files(*.xlsx)|*.xlsx|" "all files (*.*)|*.*"
        dlg=wx.FileDialog(self,"save a file", wildcard=filesFilter,style=wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            path=dlg.GetPath()
            #print path
            #print self.control.GetValue()
            data="实验名称\t数据类型\t实验描述\t样本名称\t分组\t描述\t文件名\tmd5\t保存路径\nmRNA\tRNA-Seq\n"
            fh=open(path,"w")
            fh.write(data)
            fh.write(self.data2)
            fh.close()
            self.control.SetValue("##########\n.......保存分组信息表.........\nsuccessful\n##########l")
        dlg.Destroy()
        
        
app=wx.App(False)
#frame1=myframe(None,"hello world")
frame=mainwindow(None,"hello world")
app.MainLoop()
