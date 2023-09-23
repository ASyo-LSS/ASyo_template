# 强度设计
# 筒体计算壁厚δ_c
Pc = float(input('请输入计算压力Pc（在二、5）：'))
Di = float(input('请输入公称直径Di（在三、4）：'))
C1 = 0.8  # float(input('钢板厚度负偏差C1（在二、9）：'))
C2 = 1.5  # float(input('请输入腐蚀余量C2（在二、9）：'))
xu_ying_li = 189
han_jie_tou_xi_su = 1
TT_hd = (Pc * Di) / (2 * xu_ying_li * han_jie_tou_xi_su - Pc)
TT_hd1 = "%.3f" % TT_hd
four_1 = '1)目标：计算筒体和封头的壁厚，最终确定筒体和封头的名义壁厚\n1、筒体计算壁厚δ_c\n1）先假设筒体厚度为6-16mm,查“常用钢板的许用应力”表得设计温度为60℃时的许用应力[σ]t=189MPa，将以上参数代入公式得筒体计算厚度为\nδ_c=({0}*{1})/2*{2}*{3}-{0}≈{4}'.format(
    Pc, Di, xu_ying_li, han_jie_tou_xi_su, TT_hd1)
# 求设计壁厚δ_d
sjbh = TT_hd + C2
sjbh1 = "%.3f" % sjbh
four_2 = '2)求设计壁厚δ_d\nδ_d=δ_c+C_2={0}+{1}={2}mm'.format(TT_hd1, C2, sjbh1)
# 求名义厚度δ_n
mhd1 = sjbh + C1
mhd2 = "%.3f" % (sjbh + C1)
mhd = sjbh + C1
while mhd % 2 != 0:
    mhd = int(mhd)
    mhd += 1
else:
    tygj = mhd
    mhd1 = "%.3f" % mhd
four_3 = '3)求名义厚度δ_n\n确定名义壁厚需要考虑二个因素，一个是钢板的厚度负偏差，另外一个是钢板的标准厚度系列，C1={0}mm，{1}+{0}={4}mm（向上圆整到钢板的标准厚度系列）,故δ_n={3}mm（向上取偶数）'.format(
    C1, sjbh1, mhd, tygj, mhd2)
four_4 = '4）检查\nδ_n在假设筒体厚度范围为6-16mm范围，故最后得筒体的名义壁厚为{0}mm'.format(mhd)
print(four_1, four_2, four_3, four_4, sep='\n')
