# -*- codeing = utf-8 -*-
# Author：ASyo
# Date：2023-9-12
# Time：8:43
from Printer_out_Close import Printer, Programe_colse
from 过程设备.EHA_insidearea_v import EHA_area_v
'''
参数说明
Mpa：最高工作压力Pw
T_max最高工作温度：30℃
T_dmax：设计温度 根据工作温度加5-10℃
T_dmax_add：设计温度加数
Designed_Y：设计寿命：20年
V：容积
Pd：设计压力
D_Pressure：设计压力倍数
Pc：计算设计压力=Pd
Sm:设计寿命
Neurogen_level：危害程度 1.05-1.1倍
Rl：容器类别
Material：材料
C1钢板厚度负偏差C18 ：C1=0.3mm
Fai：焊接接头系数φ
C_2V：腐蚀速率每年按0.1mm/年
C_2：腐蚀余量 
gczj：公称直径
xu_ying_li：许应力
xu_ying_li = 189  # 压力

介质：空气
'''

Mpa = float(input('请输入最高工作压力（Mpa）：'))
T_max = float(input('最高工作温度（℃）：'))
Designed_Y = float(input('设计寿命（年）：'))
V = float(input('请输入容积(m^3)：'))
D_Pressure=float(input('设计压力倍数取值（1.05倍至1.1倍）：'))
Neurogen_level=input('介质危害程度高（输入g）低(输入d)：')
Rl = input('请输入容器类别（1或2）：')
Material=input('主要受压材料：Q245R（请输入：245），Q345R（请输入：345）：')
gczj = int(input('请输入公称直径：'))
C_1=0.3
Fai=1.0
C_2V=0.1
C_2=Designed_Y*C_2V
if Material ==245:
    xu_ying_li = 147
else:
    xu_ying_li = 189



# 第一章Yi
Yi_1 = '1、空气缓冲\n'
Yi_2 = '2、结构说明及管口表格\n'
Yi = '第一章 整体设计\n' + Yi_1 + Yi_2
# 第二章Er
Pd = D_Pressure * Mpa  # 设计压力
if Rl == 1:
    Rl = 'I'
else:
    Rl = 'II'

if Neurogen_level=="g":
    T_dmax_add=10
    T_dmax=T_max+10
else:
    T_dmax_add = 5
    T_dmax=T_max+5

if Material=="245":
    Material="Q245R"
else:
    Material = "Q345R"
Er_6 = '''
第二章 技术参数设计（12个参数）
1、介质：空气
2、最高工作压力Pw：{0}Mpa
3、最高工作温度：{1}℃
4、设计寿命：{2}年
5、容积：{3}m^3
6、设计压力Pd：一般取最高工作压力的1.05-1.1倍
故Pd={4}XPw={4}X{0}={0}Mpa\n'''.format(Mpa,T_max,Designed_Y,V,D_Pressure)
Er_7 = '''
7、设计温度Td：
根据工作温度加5-10℃，根据介质的危险程度确定工作温度的高低，如果介质危害程度低，取5℃反之取10℃
故Td={0}+{1}={2}℃
8、容器类别判定{3}（空气属于第二组介质）
'''.format(T_max,T_dmax_add,T_dmax,Rl)

'''
9、材料设计（确定主要受压元件材质）
选{0}
10、钢板厚度负偏差C_1：C_1={1}mm
11、焊接接头系数φ：
说明：双面焊、100%无损检测取φ={2}
12、腐蚀余量C_2：根据设计寿命，每年按{3}mm/年负数速率为参考
C_2={4}X0.1=2m\n'''.format(Material,C_1,Fai,C_2V,Designed_Y)
Er = Er_6 + Er_7

# 第三章 几何参数设计San

H,A,V_R=EHA_area_v(gczj)
# 输入设计总体积
V_Z = V
# 计算筒体的容积V筒体 V_TT
V_TT = V_Z - 2 * V_R
# 计算筒体长度L筒体 L_TT
d = float(gczj / 1000)
L_TT = ((4 * V_TT) / 3.14 / (d ** 2))
San_1 = '1、确定承压设备公称直径:依据GB/T9019-2001\n初选本设计的承压设备公称直径为{0}mm\n'.format(gczj)
San_21 = '''
（1）查公称直径为{0}mm标准椭圆形封头容积
得:V封头={1}m^3，总深度H={2}mm\n'''.format(gczj, V_R, H)
San_22 = '''
(2）计算筒体的容积V_筒体
V_筒体=V_总-2V_封头={0}-2*{1}={2}m^3\n'''.format(V_Z, V_R, V_TT)
San_23 = '''
（3）计算筒体长度L筒体
根据公式V_筒体=πD^2/4L筒体可得
L筒体=4V_筒体/π/D^2=4*{0}/π/{1}={2}m\n'''.format(V_TT, d, L_TT)
# 计算总长度L L_Z
h = H / 1000
L_Z = 2 * h + L_TT

# 计算长径比B
B = float(L_Z / d)

San_24 = '（4）计算长径比B\n总长度L=2H+L_筒体=2*{0}+{1}={2}m\nB=L/D={2}/{3}≈{4}（近似值）\n'.format(h, L_TT, L_Z, d, B)
if 2 < B < 3:
    San_jl = '结论：以上公称直径选取{0}mm是合格的\n'.format(gczj)
else:
    San_jl = '结论：以上公称直径选取{0}mm是不合格的\n'.format(gczj)
San_2 = San_21 + San_22 + San_23 + San_24
San = '第三章几何参数设计\n目标:解决筒体长度和公称直径的问题 DN\n判定原理：长径比为2-3\n'

# 第四章强度设计

Pc = Pd  # 设计压力
Pcx = format(Pc, '.3f')
Di = gczj  # 公称直径


# 筒体计算厚度δ_c TT_hd
TT_hd = (Pc * Di) / (2 * xu_ying_li * Fai - Pc)
TT_hd1 = "%.3f" % TT_hd
Si_11 = '1）先假设筒体厚度为6-16mm,查“常用钢板的许用应力”表得设计温度为{0}℃时的许用应力[σ]t={1}MPa，将以上参数代入公式得筒体计算厚度为\nδ_c=(p_c D_i)/(2[σ]_tφ-p_c )=({2}*{3})/2*{1}*{4}-{2}≈{5}mm\n'.format(T_dmax,xu_ying_li,Pcx, Di, Fai, TT_hd1)
# 求设计壁厚δ_d sjbh
sjbh = TT_hd + C_2
sjbh1 = "%.3f" % sjbh
Si_12 = '2)求设计壁厚δ_d\nδ_d=δ_c+C_2={0}+{1}={2}mm\n'.format(TT_hd1, C_2, sjbh1)

# 求名义厚度δ_n Qo
mhd = sjbh + C_1
mhd2 = "%.3f" % (sjbh + C_1)

if mhd % 2 != 0:
    Qo = int(mhd)
    Qo += 1
else:
    Qo=int(mhd)
    Qo+=2
Si_13 = '3)求名义厚度δ_n\n确定名义壁厚需要考虑二个因素，一个是钢板的厚度负偏差，另外一个是钢板的标准厚度系列，C_1={0}mm，{1}+{0}={4}mm（向上圆整到钢板的标准厚度系列）,故δ_n={3}mm（向上取偶数）\n'.format(
    C_1, sjbh1, mhd,Qo, mhd2)
if 6<=Qo<=16:
    Si_14 = '4）检查\nδ_n在假设筒体厚度范围为6-16mm范围，故最后得筒体的名义壁厚δ_n为{0}mm\n'.format(Qo)
else:
    Si_14 = '4）检查\nδ_n不在假设筒体厚度范围为6-16mm范围，故最后得筒体的名义壁厚δ_n不为{0}mm\n'.format(Qo)
Si_1 = '1、筒体计算壁厚δ_c\n' + Si_11 + Si_13 + Si_14

p_c = Pd
D_i = gczj
a_t = xu_ying_li
fai = Fai
# 封头计算厚度
FTH = (p_c * D_i) / (2 * a_t - p_c)
FTHx = format(FTH, '.3f')
Si_21 = '1）先假设封头厚度为6-16mm，查“常用钢板的许用应力” (0)表得设计温度为{1}°C时的许用应力[σ]t={2}/MPa，将以上参数代入公式得封头计算厚度为\n(p_c D_i)/2[σ]_tφ-p_c={3}\n'.format(Material,T_dmax,xu_ying_li,FTHx)
# 求设计壁厚δd fai_d
fai_d = TT_hd + C_2
fai_dx = format(fai_d, '.3f')
Si_22 = '2）求设计壁厚δd\nδd=δc+C2={0}+{1}={2}mm\n'.format(TT_hd1, C_2, fai_dx)

# 求名义壁厚δn fai_n
fai_n = C_1 + fai_d
fai_nx = format(fai_n, '3f')
fai_n_int = int(fai_n)
if fai_n_int % 2 == 0:
    fai_n_int += 2
else:
    fai_n_int += 1

Si_23 = '3）求名义壁厚δn\n确定名义壁厚需要考虑二个因素，一个是钢板的厚度负偏差，另外一个是钢板的标准厚度系列，C_1={0}mm，{1}+{0}={2} mm（向上圆整到钢板的标准厚度系列）\n故δn={3}mm\n'.format(
    C_1, fai_dx, fai_nx, fai_n_int)
if 6 <= fai_n_int <= 16:
    Si_24 = 'δn={}mm在假设封头厚度为6-16mm范围，有效\n'.format(fai_n_int)
else:
    Si_24 = 'δn={}mm不在假设封头厚度为6-16mm范围，无效\n'.format(fai_n_int)
Si_2 = '2、标准椭圆形封头计算壁厚δc\n' + Si_21 + Si_22 + Si_23 + Si_24
Si = '第四章 强度设计（强度计算公式人工计算）\n目标：计算筒体和封头的壁厚，最终确定筒体和封头的名义壁厚\n' + Si_1 + Si_2

All = Yi + Er + San + Si
Printer(All)
Programe_colse()
# Q345R和Q245R
