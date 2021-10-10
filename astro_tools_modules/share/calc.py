import math

class Calc:

    @staticmethod
    def ccd_resolution(ccd_pixel_size, focal_lenght, multi_factor = 206.265, round_result = True, round_digits = 3):
        result = (ccd_pixel_size / focal_lenght) * multi_factor

        if round_result:
            result = round(result, round_digits)

        return result

    @staticmethod
    def ccd_focal_lenght(ccd_pixel_size, ccd_resolution, multi_factor = 206.265, round_result = True, round_digits = 0):
        result = (ccd_pixel_size * multi_factor) / ccd_resolution

        if round_result:
            result = round(result, round_digits)

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