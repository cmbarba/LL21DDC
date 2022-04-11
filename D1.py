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
names = ["Toronto","Ottawa","Montreal","Edmonton","Calgary"]
leg1price = [van_tor_price,van_ott_price,van_mon_price,van_edm_price,van_cal_price]
leg2price = [tor_mun_price,ott_ber_price,mon_lon_price,edm_lon_price,cal_lon_price]
leg1time = [van_tor_travel_time,van_ott_travel_time,van_mon_travel_time,van_edm_travel_time,van_cal_travel_time]
laytime = [tor_layover,ott_layover,mon_layover,edm_layover,cal_layover]
leg2time = [tor_mun_travel_time,ott_ber_travel_time,mon_lon_travel_time,edm_lon_travel_time,cal_lon_travel_time]

i = 0
j = len(names)
while i < j:
    val = (leg1price[i]+leg2price[i]) / (leg1time[i] + laytime[i] + leg2time[i])
    values.append([names[i],val])
    i += 1

i = 1
bestval = values[0]
while i < j:
    if values[i][1] < bestval[1]:
        bestval = values[i]
    i += 1

print("The best trip value comes from the",bestval[0],"route costing $",round(bestval[1],2),"per hour.")