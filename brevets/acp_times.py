"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    openTime = arrow.get(brevet_start_time)    
    cont = control_dist_km
    if cont > brevet_dist_km and cont <= (brevet_dist_km + (brevet_dist_km*.20)):
        cont = brevet_dist_km 
    if cont >= 800 and cont <= 905:
        openTime = openTime.shift(minutes=+1)
    if cont > 600 and cont <=1000:
        hr = (cont-600)//28
        mn = (((cont-600)/28)-((cont-600)//28))*(60)
        openTime = openTime.shift(hours=+hr, minutes=+mn)
        cont = 600
    if cont > 400 and cont <=600:
        hr = (cont-400)//30
        mn = (((cont-400)/30)-((cont-400)//30))*(60)
        openTime = openTime.shift(hours=+hr, minutes=+mn)
        cont = 400
    if cont > 200 and cont <=400:
        hr = (cont-200)//32
        mn = (((cont-200)/32)-((cont-200)//32))*(60)
        openTime = openTime.shift(hours=+hr, minutes=+mn)
        cont = 200
    if cont > 0 and cont <=200:
        hr = cont//34
        mn = round(((cont/34)-(cont//34))*(60))
        openTime = openTime.shift(hours=+hr, minutes=+mn)

    return openTime


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    return arrow.now()
