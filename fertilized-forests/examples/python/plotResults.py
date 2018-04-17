#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 12:06:24 2018

@author: priyanka
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from statistics import mean,stdev
from itertools import repeat
import math

def plot_exps(al,pl,map_mean,line,map_line,width):
    for idx,_ in enumerate(al):
        if len(al[idx])>len(pl[0]):
            al[idx]=al[idx][:len(pl[0])+1]
        else:
            al[idx].extend(repeat(al[idx][-1], len(pl[0])+1 - len(al[idx])))
    
    for idx,_ in enumerate(al):
        al[idx].insert(0, 0)
        al[idx].insert(1,0)
    
    for idx,_ in enumerate(pl):
        pl[idx].insert(0, 0)
        pl[idx].insert(1,0)
        
    al_mean = np.mean(al,axis=0)
    pl_mean = np.mean(pl,axis=0)
    
    al_std = np.std(al, axis=0)
    pl_std = np.std(pl, axis=0)
  
    al_title = "mAP over "+str(len(al))+" experiments"

    plt.title(al_title)
    plt.xticks(range(2,len(pl[0])))
    plt.grid()

    plt.fill_between(range(len(al[0])),al_mean - al_std, al_mean + al_std, alpha=0.1,color="r")
    plt.fill_between(range(len(pl[0])),pl_mean - pl_std, pl_mean + pl_std, alpha=0.1,color="b")
    plt.plot(range(len(al[0])),al_mean, line, color="r",linewidth=width, label ="Active learning")
    plt.plot(range(len(pl[0])),pl_mean, line, color="b",linewidth=width, label ="Passive learning")
    
    plt.plot(range(12),[map_mean]*12,map_line,color="g",linewidth=width, label ="Fully Supervised learning")

    plt.legend(loc="best")


def al(xlim,ylim, n_jobs=1):
    plt.figure()
#    plt.ylim(ylim)
    plt.xlim(0,0.2)
    plt.xlabel("Images")
    plt.ylabel("mAP")

#    mAP_rgb = [0.89889052887336685, 0.91251215361844829, 0.90808955354051024, 0.89093943386073449, 0.91032165305423163, 0.913825671566872, 0.90327223281385915, 0.91162764003336016, 0.90659455798534783, 0.90959100925217218]
#    al_rgb = [[0.60569560479925444, 0.61760847788375772, 0.55019717920795075, 0.72130617020417465, 0.85830541064748611], [0.70973370063918817, 0.52361372475480816, 0.79484782893627348, 0.65111451699926959, 0.82818496014769871], [0.50225666953442283, 0.70867248230754643, 0.67534505898416486, 0.65167093007681598], [0.6617309458182693, 0.7261803956061359, 0.64170447793064633, 0.76682736455054745, 0.77193941115969922], [0.55378223559603779, 0.76141250739689648, 0.7647769940295065, 0.69666235458675041, 0.64490671769296337, 0.734535471362595, 0.77355311354980305, 0.75398355860409549, 0.8061628003397181], [0.63760986488061611, 0.70665069468521924, 0.78653874900852538, 0.804481417036924], [0.57073984925657562, 0.64895875460278052, 0.58104912763819105, 0.70679063360482985, 0.74225206611341843, 0.70936639118168876], [0.63602197775818126, 0.54929016062320302, 0.71113157592245413, 0.82690831212119176], [0.7484825690778576, 0.72604503012526511, 0.72607213966119599, 0.79240036935410496, 0.79965545763806101], [0.4415584415559542, 0.48814483126797836, 0.68125911236448755, 0.85978191941334003]]
#    pl_rgb = [[0.58973845153109994, 0.72281582579042492, 0.63938983995389287, 0.5942042093941563, 0.71545862525425141], [0.5739210284647438, 0.75313425396839639, 0.79630825298193897, 0.69301462720202978, 0.80084098907225643], [0.30064279155026197, 0.63973384547164946, 0.77834066860532769, 0.66438854015126969, 0.74683870793154528], [0.46857704337019268, 0.74003454564828897, 0.67408429007560888, 0.76649822389724387, 0.67754019820430322], [0.61970921375257815, 0.71204369610392493, 0.7469184325643371, 0.66326728826389991, 0.65478376841662578], [0.57531711489580994, 0.58273024001290508, 0.62834387834153604, 0.58557385375199322, 0.71382001836199382], [0.43065607357953384, 0.34917355371795, 0.65791947249947436, 0.69287477872599457, 0.64713568617733563], [0.50529315353218263, 0.51792840035230259, 0.53618707410503175, 0.62300030794788641, 0.80248800984342683], [0.41911810920849241, 0.65896804560888489, 0.65393530080620421, 0.5594405594377847, 0.72192941003738287], [0.096707622372618887, 0.13887253906728506, 0.47296144548205293, 0.4064561657020066, 0.36690204340160804]]
#    map_mean_rgb = np.mean(mAP_rgb)
#    plot_exps(al_rgb,pl_rgb,map_mean_rgb,'o:',':',1.5)
##    
##    mAP_hog = [0.9667125803456702, 0.98484848484550047, 0.98484848484550036, 0.98484848484550036, 0.98484848484550058, 0.9668273645513894, 0.98484848484550014, 0.98484848484550047, 0.96659779613995034, 0.96682736455138918]
#    al_hog = [[0.57176235623568539, 0.70707070706856423, 0.56955922864714492, 0.93365472910537373], [0.80578397612076236, 0.84431075257985722, 0.74145228591405998, 0.8622219260004278], [0.61103279883799666, 0.8294981904560601, 0.80262855830584745, 0.82750582750140567, 0.82644628098923123], [0.57671003870311599, 0.74297907302272936, 0.80963668947111656, 0.76034002926394184], [0.80141554216684796, 0.86994605142083209, 0.90618652119668257, 0.94444510034987223], [0.64604178370669563, 0.71163911845343797, 0.8117116137413416, 0.8863237114185738, 0.8899260826857105, 0.83566503711460904, 0.91343087049919116, 0.97603305784734919, 0.98779614324627173], [0.77026035957207684, 0.81818181817791569, 0.90984848484425618, 0.72259615384243214, 0.76557785648316723, 0.84308999081350366, 0.97522049244815894], [0.59817827252224454, 0.74246494246088024, 0.71345589893587757, 0.79843893479898853, 0.81244260789342404], [0.89706563470268859, 0.916592124452696719, 0.96638659320164594], [0.78057005040291472, 0.82254349322888221, 0.89586895295946469, 0.91473829200744829, 0.96307336032736722]]
#    pl_hog = [[0.62474747474500036, 0.72354224058519356, 0.83875552056968061, 0.84825528006972639, 0.73595041321956289], [0.58065587834481713, 0.74104683195255683, 0.66957249249421702, 0.83608815426610927, 0.69911916786589445], [0.77352256329059965, 0.72213039485342756, 0.81324992453656542, 0.84653351698423496, 0.83358590039759684], [0.68650340768940599, 0.73938703958575169, 0.80039026629529153, 0.80136593204395867, 0.91472968319169068], [0.56972628066052122, 0.7483149678563451, 0.70821854912474769, 0.82840038748688027, 0.85550677226373362], [0.75987144168657483, 0.76048570666565374, 0.82960865556186025, 0.83333333332962589, 0.78799357208099152], [0.70352357874729743, 0.64338187065164165, 0.75619260789335407, 0.85358733128489972, 0.84774695001582512], [0.64724135291916274, 0.59454915985727519, 0.7325138560898663, 0.711662075295318, 0.74707300275131827], [0.58064917595378518, 0.73484848484552323, 0.73588154269639217, 0.59839390051354757, 0.76262626262298749], [0.53974390764065017, 0.62466314206968054, 0.66942148760127718, 0.661923209363109, 0.75432424368947759]]
#    map_mean_hog = np.mean(mAP_hog)
#    plot_exps(al_hog,pl_hog,map_mean_hog,'o-','-',2.0)
    
#    mAP_deep = [0.38236]
#    
#    al_deep = [[0.069860999148718461, 0.099664275388919824, 0.092293783224498271, 0.187194627557668145,0.197194627557668145,0.187194627557668145, 0.29320096283344495, 0.30132626207061392], [0.079710644818092855,0.084620173547883482,0.164620173547883482,0.184620173547883482, 0.284620173547883482, 0.32408970416569609], [0.053498565178164655,0.094227570383812589,0.154227570383812589, 0.254227570383812589, 0.335558202864775872], [0.057444049305732256, 0.346831377316922343,0.246831377316922343, 0.30586637680516961], [0.036631319909059455, 0.054153860170317855, 0.087790551966681979, 0.066736050935543412, 0.061860022268564199, 0.097676753802561631, 0.145062760683437279, 0.249751595800371515, 0.157546169365806706, 0.265269090299277618, 0.171110075239896389, 0.281189235102982413, 0.288864015019983714, 0.31550578869272866, 0.3274774566319691, 0.33668222885557163, 0.33678576794467009]]
#    pl_deep = [[0.076002851789166034, 0.11926321796935477, 0.10235810578713876, 0.11606445183942871, 0.20599041277875599, 0.19094589793349717], [0.043081639095321075, 0.093031521443572102, 0.071598480625027563, 0.15125629104181687, 0.17259518745224914, 0.20004665033349395], [0.081320603286558574, 0.090165875376192695, 0.089155836468128857, 0.1085949465150205, 0.18902087865441219, 0.16551102971529566], [0.036416550970507985, 0.068819113689247924, 0.12733977130848825, 0.089577485478531921, 0.13001403142973608, 0.15138955769867532], [0.0057713334327238811, 0.021852830787308646, 0.029492379517504129, 0.048864549327284644, 0.068840435424188898, 0.096141519219415175]]
    
    mAP_deep = [0.16]
    
    al_deep = [[0.043665216325562237, 0.108684454261150124, 0.131445201495514512], [0.04368208030093134, 0.096870551390759244, 0.111553575092213284, 0.134196383537709686, 0.12229315710734581], [0.056189657916646547, 0.099429521051553141, 0.123238735394750337, 0.132588806731286862, 0.137127306842253842, 0.117603725960837539, 0.135985013187847817, 0.141756002781214576, 0.14010533022711785, 0.14036520281222125], [0.013993817927311121, 0.06148928787932473, 0.1088413170398646476], [0.029790967426611255, 0.087916853558399655, 0.094815692866611195, 0.111592304147176092]]
    pl_deep = [[0.015080629151620411, 0.038187789870634265, 0.051852598545593172, 0.06584323148515902, 0.0825036657008797445], [0.017837261138593252, 0.029114653735875335, 0.038324859476088643, 0.053593708384442437, 0.0771280244367981005], [0.02184994232044913, 0.038556947220766749, 0.053440736106802283, 0.06408932036788952, 0.087928199660265976], [0.0076045666966667001, 0.0162785938833206378, 0.0237481037712731738, 0.0354260539941634687, 0.0525519588125236456], [0.01097095992651939, 0.014047849019084695, 0.021445784602971538, 0.041014152360366583, 0.0666064730941950318]]
    
    
    map_mean_deep = np.mean(mAP_deep)
    plot_exps(al_deep,pl_deep,map_mean_deep,'o-','-',2.5)
    plt.savefig("voc_alpl.png")
    plt.show()
    
#    mAP_rgb = [0.0981, 0.1032, 0.0932, 0.1156,  0.1254]
#    mAP_hog = [0.3962, 0.4082, 0.3620, 0.3662, 0.3792]
#    mAP_deep = [0.3131, 0.3155, 0.3254, 0.3301, 0.3168]
#    objects = ('RGB', 'Hog', 'Deep')z
#    y_pos = np.arange(len(objects))
#    print(mean(mAP_rgb),mean(mAP_hog),mean(mAP_deep))
#    performance = [mean(mAP_rgb),mean(mAP_hog),mean(mAP_deep)]
#    plt.grid()
#    pm, pc, pn = plt.bar(y_pos, performance, align='center', alpha=0.5)
#    pm.set_facecolor('r')
#    pc.set_facecolor('g')
#    pn.set_facecolor('b')
#    plt.xticks(y_pos, objects)
#    plt.ylabel('mean mAP')
#    x = range(3)
#    for a,b in zip(x, performance):
#        plt.text(a, b, str(b))
#    plt.title('Features')
#    low = min(performance)
#    high = 0.50
#    plt.ylim([low-0.05, high])
#    plt.savefig("hila_rgbhogdeep")
#    plt.show()

            
def plotOffsets(points,clr):
#    points = 
    bbCenter=[77.0, 121.0]
    plt.plot(bbCenter[0],bbCenter[1],'ro')
    for pt in points:
        plt.plot(bbCenter[0]+pt[0],bbCenter[1]+pt[1],clr+'.')
        

#points = [[ -2.,  23.], [ 27., -66.], [ 28.,  52.], [-37., -32.], [ 45.,  53.]]
#plotOffsets(points,'b')
#points = [[-42.,  41.], [-40.,  25.], [-44., -63.], [-39., -41.]]
#plotOffsets(points,'g')
#plt.show()
    
    
al( xlim=(0, 0.2), ylim=(0, 1.01), n_jobs=4)
