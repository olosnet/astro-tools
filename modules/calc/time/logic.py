from datetime import datetime, date, timedelta
import math
import pytz

class CalcTime:

    @staticmethod
    def time_to_jd_dt(dt: datetime, precision=10) -> float:
        return CalcTime.time_to_jd(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, precision)

    @staticmethod
    def time_to_jd(year: int, month: int, day: int, hh: int, mm: int, ss: int, precision=10) -> float:
        jd_offset = 1721424.5
        od = date(year, month, day).toordinal() + jd_offset
        hh_mm_ss = (3600 * hh + 60 * mm + ss) / 86400

        return CalcTime.trunc_f(od + hh_mm_ss, precision)

    @staticmethod
    def time_from_jd(jd_date: float, precision=10) -> datetime:
        jd_offset = 1721424.5

        or_date = jd_date - jd_offset
        int_or_date = int(or_date)
        d_or_date = CalcTime.trunc_f(or_date - int_or_date, precision)

        day_offset = d_or_date * 86400
        hh = int(day_offset / 3600)
        mm = int((day_offset - 3600 * hh) / 60)
        ss = int(day_offset - 3600 * hh - 60 * mm)

        dt = datetime.fromordinal(int_or_date)
        dt = dt.replace(hour=hh, minute=mm, second=ss)

        return dt

    @staticmethod
    def time_calc_gmst(year: int, month: int, day: int, hh: int, mm: int, ss: int) -> float:
        jd_j2000 = 2451545.0
        jd_now = CalcTime.time_to_jd(year, month, day, hh, mm, ss)
        jd_difference = jd_now - jd_j2000
        jc = jd_difference / 36525.0

        res = 280.46061837 + 360.98564736629*jd_difference + \
            0.000387933 * (jc ** 2) - (jc ** 3)/38710000

        if res > 0.0:
            while res > 360.0:
                res -= 360.0
        else:
            while res < 0.0:
                res += 360.0

        return res

    @staticmethod
    def time_calc_gmst_hour_angle_dt(dt: datetime):
        return CalcTime.time_calc_gmst_hour_angle(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    @staticmethod
    def time_calc_gmst_hour_angle(year: int, month: int, day: int, hh: int, mm: int, ss: int):
        res = CalcTime.time_calc_gmst(year, month, day, hh, mm, ss)
        return CalcTime.deg_to_hour_angle(res)

    @staticmethod
    def time_calc_gmst_hhmmss(year: int, month: int, day: int, hh: int, mm: int, ss: int):
        res = CalcTime.time_calc_gmst(year, month, day, hh, mm, ss)
        return CalcTime.deg_to_hhmmss(res)

    @staticmethod
    def time_calc_gmst_hhmmss_dt(dt: datetime):
        return CalcTime.time_calc_gmst_hhmmss(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    @staticmethod
    def time_calc_lst(year: int, month: int, day: int, hh: int, mm: int, ss: int, longitude: float):

        gmst = CalcTime.time_calc_gmst(year, month, day, hh, mm, ss)
        lst = gmst + longitude

        if lst > 0.0:
            while lst > 360.0:
                lst -= 360.0
        else:
            while lst < 0.0:
                lst += 360.0

        return lst

    @staticmethod
    def time_calc_lst_hour_angle(year: int, month: int, day: int, hh: int, mm: int, ss: int, longitude: float):
        res = CalcTime.time_calc_lst(year, month, day, hh, mm, ss, longitude)
        return CalcTime.deg_to_hour_angle(res)

    @staticmethod
    def time_calc_lst_hour_angle_dt(dt: datetime, longitude: float):
        return CalcTime.time_calc_lst_hour_angle(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, longitude)

    @staticmethod
    def time_calc_lst_hhmmss_dt(dt: datetime, longitude: float):
        return CalcTime.time_calc_lst_hhmmss(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, longitude)

    @staticmethod
    def time_calc_lst_hhmmss(year: int, month: int, day: int, hh: int, mm: int, ss: int, longitude: float):
        res = CalcTime.time_calc_lst(year, month, day, hh, mm, ss, longitude)
        return CalcTime.deg_to_hhmmss(res)

    @staticmethod
    def deg_to_hhmmss(deg: float):
        obj = deg / 15.0
        hours = math.floor(obj)

        tmin = obj - hours
        tmin = tmin * 60
        minutes = math.floor(tmin)

        tsec = tmin - minutes
        tsec = tsec * 60
        seconds = math.floor(tsec)

        return hours, minutes, seconds

    @staticmethod
    def deg_to_hour_angle(deg: float):

        angle = math.floor(deg)
        curr = (deg - angle) * 60
        min = math.floor(curr)
        curr = (curr - min) * 60
        sec = math.floor(curr)

        return angle, min, sec

    @staticmethod
    def time_difference(dt1hh : int, dt1mm : int, dt1ss : int, dt2hh : int, dt2mm : int, dt2ss : int):

        t1 = timedelta(hours=dt1hh, minutes=dt1mm, seconds=dt1ss)
        t2 = timedelta(hours=dt2hh, minutes=dt2mm, seconds=dt2ss)

        total_seconds = (t1 - t2).total_seconds()
        negative = False

        if total_seconds < 0:
            negative = True
            total_seconds = total_seconds * -1


        m, s = divmod(total_seconds, 60)
        h, m = divmod(m, 60)

        if negative:
            h *= -1

        return int(h), int(m), int(s)

    def ra_to_local_ra(ut_dt : datetime, longitude: float, ra_hh : int, ra_mm : int, ra_ss : int):
        hh1, mm1, ss1 = CalcTime.time_calc_lst_hhmmss_dt(ut_dt, longitude)
        return CalcTime.time_difference(hh1, mm1, ss1, ra_hh, ra_mm, ra_ss)

    @staticmethod
    def trunc_f(f: float, n: int) -> float:
        '''Truncates/pads a float f to n decimal places without rounding'''
        s = '%.12f' % f
        i, p, d = s.partition('.')
        return float('.'.join([i, (d+'0'*n)[:n]]))

    @staticmethod
    def is_dst(zonename):
        tz = pytz.timezone(zonename)
        now = pytz.utc.localize(datetime.utcnow())
        return now.astimezone(tz).dst() != timedelta(0)