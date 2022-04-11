## Day 1 Challenge ##

# Provided

van_tor_price = 250
van_ott_price = 280
van_mon_price = 240
van_edm_price = 160
van_cal_price = 180

van_tor_travel_time = 3.5
van_ott_travel_time = 4
van_mon_travel_time = 4
van_edm_travel_time = 1.5
van_cal_travel_time = 1

ott_ber_price = 1350
mon_lon_price = 1300
edm_lon_price = 1290
cal_lon_price = 1400
tor_mun_price = 990

ott_layover = 3.5
mon_layover = 2
edm_layover = 5
cal_layover = 2.5
tor_layover = 1.5

ott_ber_travel_time = 9
mon_lon_travel_time = 8
edm_lon_travel_time = 10
cal_lon_travel_time = 10
tor_mun_travel_time = 9.5

# Work

values = []

tor_price = van_tor_price + tor_mun_price
tor_time = van_tor_travel_time + tor_layover + tor_mun_travel_time
tor_value = tor_price / tor_time
#print("Toronto: ",tor_value," $/hr")
values.append(["Toronto",tor_value])

ott_price = van_ott_price + ott_ber_price
ott_time = van_ott_travel_time + ott_layover + ott_ber_travel_time
ott_value = ott_price / ott_time
#print("Ottawa: ",ott_value," $/hr")
values.append(["Ottawa",ott_value])

mon_price = van_mon_price + mon_lon_price
mon_time = van_mon_travel_time + mon_layover + mon_lon_travel_time
mon_value = mon_price / mon_time
#print("Montreal: ",mon_value," $/hr")
values.append(["Montreal",mon_value])

edm_price = van_edm_price + edm_lon_price
edm_time = van_edm_travel_time + edm_layover + edm_lon_travel_time
edm_value = edm_price / edm_time
#print("Edmonton: ",edm_value," $/hr")
values.append(["Edmonton",edm_value])

cal_price = van_cal_price + cal_lon_price
cal_time = van_cal_travel_time + cal_layover + cal_lon_travel_time
cal_value = cal_price / cal_time
#print("Calgary: ",cal_value," $/hr")
values.append(["Calgary",cal_value])

j = len(values)

i = 1
bestval = values[0]
while i < j:
    if values[i][1] < bestval[1]:
        bestval = values[i]
    i += 1

print(bestval)