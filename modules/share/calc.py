import math
from datetime import datetime, date


class Calc:

    @staticmethod
    def ccd_resolution(ccd_pixel_size, focal_lenght, multi_factor=206.265):
        result = (ccd_pixel_size / focal_lenght) * multi_factor

        return result

    @staticmethod
    def ccd_focal_lenght(ccd_pixel_size, ccd_resolution, multi_factor=206.265):
        result = (ccd_pixel_size * multi_factor) / ccd_resolution

        return result

    @staticmethod
    def ccd_pixel_size(h_size, v_size, h_resolution, v_resolution):
        h_pixel_size = h_size / h_resolution
        v_pixel_size = v_size / v_resolution

        return h_pixel_size, v_pixel_size

    @staticmethod
    def ccd_chip_size(pixel_size, h_resolution, v_resolution):
        ccd_h_size = pixel_size / h_resolution
        ccd_v_size = pixel_size / v_resolution
        diagonally = math.sqrt(ccd_h_size ** 2 + ccd_v_size ** 2)

        return ccd_h_size, ccd_v_size, diagonally

    @staticmethod
    def to_jd_dt(dt: datetime, precision=10) -> float:
        return Calc.to_jd(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, precision)

    @staticmethod
    def to_jd(year: int, month: int, day: int, hh: int, mm: int, ss: int, precision=10) -> float:
        jd_offset = 1721424.5
        od = date(year, month, day).toordinal() + jd_offset
        hh_mm_ss = (3600 * hh + 60 * mm + ss) / 86400

        return Calc.trunc_f(od + hh_mm_ss, precision)

    @staticmethod
    def from_jd(jd_date: float, precision=10) -> datetime:
        jd_offset = 1721424.5

        or_date = jd_date - jd_offset
        int_or_date = int(or_date)
        d_or_date = Calc.trunc_f(or_date - int_or_date, precision)

        day_offset = d_or_date * 86400
        hh = int(day_offset / 3600)
        mm = int((day_offset - 3600 * hh) / 60)
        ss = int(day_offset - 3600 * hh - 60 * mm)

        dt = datetime.fromordinal(int_or_date)
        dt = dt.replace(hour=hh, minute=mm, second=ss)

        return dt

    @staticmethod
    def calc_gmst(year: int, month: int, day: int, hh: int, mm: int, ss: int) -> float:
        jd_j2000 = 2451545.0
        jd_now = Calc.to_jd(year, month, day, hh, mm, ss)
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
    def calc_gmst_hour_angle_dt(dt: datetime):
        return Calc.calc_gmst_hour_angle(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    @staticmethod
    def calc_gmst_hour_angle(year: int, month: int, day: int, hh: int, mm: int, ss: int):
        res = Calc.calc_gmst(year, month, day, hh, mm, ss)
        return Calc.deg_to_hour_angle(res)

    @staticmethod
    def calc_gmst_hhmmss(year: int, month: int, day: int, hh: int, mm: int, ss: int):
        res = Calc.calc_gmst(year, month, day, hh, mm, ss)
        return Calc.deg_to_hhmmss(res)

    @staticmethod
    def calc_gmst_hhmmss_dt(dt: datetime):
        return Calc.calc_gmst_hhmmss(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    @staticmethod
    def calc_lst(year: int, month: int, day: int, hh: int, mm: int, ss: int, longitude: float):

        gmst = Calc.calc_gmst(year, month, day, hh, mm, ss)
        lst = gmst + longitude

        if lst > 0.0:
            while lst > 360.0:
                lst -= 360.0
        else:
            while lst < 0.0:
                lst += 360.0

        return lst

    @staticmethod
    def calc_lst_hour_angle(year: int, month: int, day: int, hh: int, mm: int, ss: int, longitude: float):
        res = Calc.calc_lst(year, month, day, hh, mm, ss, longitude)
        return Calc.deg_to_hour_angle(res)

    @staticmethod
    def calc_lst_hour_angle_dt(dt: datetime, longitude: float):
        return Calc.calc_lst_hour_angle(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, longitude)

    @staticmethod
    def calc_lst_hhmmss_dt(dt: datetime, longitude: float):
        return Calc.calc_lst_hhmmss(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, longitude)

    @staticmethod
    def calc_lst_hhmmss(year: int, month: int, day: int, hh: int, mm: int, ss: int, longitude: float):
        res = Calc.calc_lst(year, month, day, hh, mm, ss, longitude)
        return Calc.deg_to_hhmmss(res)

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
    def trunc_f(f: float, n: int) -> float:
        '''Truncates/pads a float f to n decimal places without rounding'''
        s = '%.12f' % f
        i, p, d = s.partition('.')
        return float('.'.join([i, (d+'0'*n)[:n]]))
