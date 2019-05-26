#first made on 2019.05.26, JAM

class BGR_gradation:
    def __init__(self):
        x = 0

    @staticmethod
    # x_ratio is 0.0~1.0
    def _get_dec(x_ratio, max_intensity=255):
        return max_intensity - x_ratio * max_intensity

    @staticmethod
    def _get_inc(x_ratio, max_intensity=255):
        return x_ratio * max_intensity

    @staticmethod
    def _get_color(x_ratio):
        retval = (0, 0, 0)
        interval1 = "i1";
        interval2 = "i2"
        range = interval1 if x_ratio < 0.5 else interval2
        if (range is "i1"):
            normalized_x_ratio = x_ratio * 2
            retval = (BGR_gradation._get_dec(normalized_x_ratio), BGR_gradation._get_inc(normalized_x_ratio), 0)

        elif (range is "i2"):
            normalized_x_ratio = (x_ratio - 0.5) * 2
            retval = (0, BGR_gradation._get_dec(normalized_x_ratio), BGR_gradation._get_inc(normalized_x_ratio))

        return retval

    @staticmethod
    def fill_BGR_gradadation(img):
        width = img.shape[1]
        for x in range(width):
            img[:, x] = BGR_gradation._get_color(x / width)