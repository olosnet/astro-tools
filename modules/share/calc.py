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
    def to_jd_dt(dt : datetime, precision=10) -> float:
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
    def trunc_f(f: float, n: int) -> float:
        '''Truncates/pads a float f to n decimal places without rounding'''
        s = '%.12f' % f
        i, p, d = s.partition('.')
        return float('.'.join([i, (d+'0'*n)[:n]]))
