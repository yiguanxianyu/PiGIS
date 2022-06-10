import math

from PiConstant import PiProjectionTypeConstant, PiLinearUnitConstant

"""常数
"""
PI = 2 * math.acos(0)
HALFPI = 0.5 * PI
DOUBLEPI = 2 * PI
EPSILON = 1e-10
UNITCONS = PiLinearUnitConstant()
PROJCONS = PiProjectionTypeConstant()


class PiProjection():
    def __init__(self):
        self.__proj_name = ""  # 投影坐标系名称
        """地理坐标系参数"""
        self.__geo_name = ""  # 地理坐标系名称
        self.__datum_name = ""  # 大地坐标系名称
        self.__spheroid_Name = ""  # 椭球体名称
        self.__semi_major = 0  # 地理坐标系长半轴
        self.__semi_minor = 0  # 地理坐标系短半轴
        self.__inverse_flattening = 0  # 扁率倒数
        self.__PrimeMeridian = ""  # 本初子午线名称
        """投影参数"""
        self.__proj_type = 0  # 投影类型
        self.__proj_name = ""  # 投影名称
        self.__central_meridian = 0  # 中央经线（度）
        self.__origin_latitude = 0  # 原点纬度（度）
        self.__standard_parallel_one = 0  # 第一标准纬线
        self.__standard_parallel_two = 0  # 第二标准纬线
        self.__scale_factor = 0  # 投影比例因子
        self.__false_easting = 0  # 东伪偏移值
        self.__false_northing = 0  # 北伪偏移值
        self.__linear_unit = 0  # 投影后的长度单位类型
        """计算参数"""
        self.a, self.b, self.alpha = 0, 0, 0  # 长半轴，短半轴，扁率
        self.e, self.e2, self.e4, self.e6, self.e8 = 0, 0, 0, 0, 0  # 第一偏心率及其幂值
        self.ep, self.ep2 = 0, 0  # 第二偏心率，第二偏心率的平方
        self.lambda0 = 0  # 中央经线（弧度制）
        self.phi0, self.phi1, self.phi2 = 0, 0, 0  # 原点纬线，第一、第二纬线（弧度制）
        # 墨卡托投影参数
        self.ak = 0
        # Lambert和Albers投影参数
        self.n, self.f0, self.r0, self.af0, self.frac_1_n = 0, 0, 0, 0, 0
        # 高斯克吕格投影参数
        self.m0, self._e, self._e2, self._e3, self._e4 = 0, 0, 0, 0, 0

    def load(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            attr = {}
            for line in lines:
                temp = line.strip().split("：")
                if len(temp) == 2:
                    attr[temp[0]] = temp[1]
            # print(attr)
        self.__proj_name = attr["投影坐标系统"]  # 投影坐标系名称
        """地理坐标系参数"""
        self.__geo_name = attr["地理坐标系统"]  # 地理坐标系名称
        self.__datum_name = attr["大地坐标系"]  # 大地坐标系名称
        self.__spheroid_Name = attr["椭球体"]  # 椭球体名称
        self.__semi_major = eval(attr["长半轴"])  # 地理坐标系长半轴
        self.__semi_minor = eval(attr["短半轴"])  # 地理坐标系短半轴
        self.__inverse_flattening = eval(attr["扁率倒数"])  # 扁率倒数
        self.__PrimeMeridian = attr["主经线"]  # 本初子午线名称
        """投影参数"""
        self.__proj_name = attr["投影"]  # 投影名称
        self.__proj_type = PROJCONS.get_type(self.__proj_name.replace(' ', '_').lower())  # 投影类型
        self.__central_meridian = eval(attr["中央经线"])  # 中央经线（度）
        self.__origin_latitude = eval(attr["原点纬度"])  # 原点纬度（度）
        self.__standard_parallel_one = eval(attr["标准纬线1"])  # 第一标准纬线
        self.__standard_parallel_two = eval(attr["标准纬线2"])  # 第二标准纬线
        self.__scale_factor = eval(attr["比例因子"])  # 投影比例因子
        self.__false_easting = eval(attr["东伪偏移"])  # 东伪偏移值
        self.__false_northing = eval(attr["北伪偏移"])  # 北伪偏移值
        self.__linear_unit_name = attr["线性单位"].lower()  # 长度单位名称
        self.__linear_unit_type = UNITCONS.get_type(self.__linear_unit_name)  # 投影后的长度单位类型

        self.calculate_attr()

    def calculate_attr(self):
        """通用变量计算"""
        self.lambda0 = self.to_radian(self.__central_meridian)
        self.phi0 = self.to_radian(self.__origin_latitude)
        self.a = self.__semi_major
        self.b = self.__semi_minor
        self.alpha = 1 / self.__inverse_flattening
        self.e = math.sqrt(1 - (self.b / self.a) ** 2)
        self.e2 = self.e ** 2
        self.e4 = self.e ** 4
        self.e6 = self.e ** 6
        self.e8 = self.e ** 8
        self.ep = math.sqrt((self.a / self.b) ** 2 - 1)
        self.ep2 = self.ep ** 2
        """各投影参数计算"""
        if self.__proj_type == PROJCONS.none:
            pass
        elif self.__proj_type == PROJCONS.mercator:
            pass
        elif self.__proj_type == PROJCONS.utm:
            pass
        elif self.__proj_type == PROJCONS.gauss_kruger:
            pass
        elif self.__proj_type == PROJCONS.lambert_conformal_conic_2sp:
            self.phi1 = self.to_radian(self.__standard_parallel_one)
            self.phi2 = self.to_radian(self.__standard_parallel_two)
            if abs(self.phi1 + self.phi2) < EPSILON:
                return False
            e_sinphi0 = self.e * math.sin(self.phi0)
            e_sinphi1 = self.e * math.sin(self.phi1)
            e_sinphi2 = self.e * math.sin(self.phi2)
            cosphi1 = math.cos(self.phi1)
            cosphi2 = math.cos(self.phi2)
            t = math.tan(0.5 * (HALFPI - self.phi0)) / math.pow((1.0 - e_sinphi0) / (1.0 + e_sinphi0), 0.5 * self.e)
            m1 = cosphi1 / math.sqrt(1 - e_sinphi1 ** 2)
            t1 = math.tan(0.5 * (HALFPI - self.phi1)) / math.pow((1.0 - e_sinphi1) / (1.0 + e_sinphi1), 0.5 * self.e)
            m2 = cosphi2 / math.sqrt(1 - e_sinphi2 ** 2)
            t2 = math.tan(0.5 * (HALFPI - self.phi2)) / math.pow((1.0 - e_sinphi2) / (1.0 + e_sinphi2), 0.5 * self.e)
            if abs(self.phi1 - self.phi2) > EPSILON:
                self.n = math.log(m1 / m2) / math.log(t1 / t2)
            else:
                self.n = math.sin(self.phi1)
            if (self.n > 0):
                self.frac_1_n = 1 / self.n
            self.f0 = m1 / (self.n * math.pow(t1, self.n))
            self.af0 = self.a * self.f0
            self.r0 = self.af0 * math.pow(t, self.n)
        elif self.__proj_type == PROJCONS.albers_equal_area:
            pass
        else:
            return False
        return True

    def lnglat_to_proj(self, lng_degree, lat_degree):
        proj_x, proj_y = 0, 0
        lng_r = self.to_radian(lng_degree)
        lat_r = self.to_radian(lat_degree)
        if self.__proj_type == PROJCONS.none:
            pass
        elif self.__proj_type == PROJCONS.mercator:
            pass
        elif self.__proj_type == PROJCONS.utm:
            pass
        elif self.__proj_type == PROJCONS.gauss_kruger:
            pass
        elif self.__proj_type == PROJCONS.lambert_conformal_conic_2sp:
            con = abs(abs(lat_r) - HALFPI)
            if con > EPSILON:
                e_sinlat = self.e * math.sin(lat_r)
                t = math.tan(0.5 * (HALFPI - lat_r)) / math.Pow((1.0 - e_sinlat) / (1.0 + e_sinlat), 0.5 * self.e)
                r = self.af0 * math.pow(t, self.n)
            else:
                con = lat_r * self.n
                r = 0
            theta = self.n * (lng_r - self.lambda0)
            r = self.to_unit(r)
            proj_x = self.__false_easting + r * math.sin(theta)
            proj_y = self.__false_northing + self.r0 - r * math.cos(theta)
        elif self.__proj_type == PROJCONS.albers_equal_area:
            pass
        else:
            return False
        return proj_x, proj_y

    def proj_to_lnglat(self, proj_x, proj_y):
        lng_d, lat_d = 0, 0
        if self.__proj_type == PROJCONS.none:
            pass
        elif self.__proj_type == PROJCONS.mercator:
            pass
        elif self.__proj_type == PROJCONS.utm:
            pass
        elif self.__proj_type == PROJCONS.gauss_kruger:
            pass
        elif self.__proj_type == PROJCONS.lambert_conformal_conic_2sp:
            dx = proj_x - self.__false_easting
            dy = self.r0 - proj_y + self.__false_northing
            con = -1 if (self.n < 0) else 1
            r = con * math.sqrt(dx * dx + dy * dy)
            if (r != 0):
                theta = math.atan2(con * dx, con * dy)
            else:
                theta = 0
            if r != 0 or self.n > 0:
                r = self.to_meter(r)
                t = math.pow((r / self.af0), self.frac_1_n)
                lat_r = HALFPI - 2 * math.atan(t)
                for i in range(5):
                    e_sinlat = self.e * math.sin(lat_r)
                    dphi = HALFPI - 2 * math.atan(
                        t * math.pow((1.0 - e_sinlat) / (1.0 + e_sinlat), 0.5 * self.e)) - lat_r
                    lat_r += dphi
                    if abs(dphi) < EPSILON:
                        break
            else:
                lat_r = -HALFPI
            lng_r = theta / self.n + self.lambda0
            lat_d = self.to_degree(lat_r)
            lng_d = self.to_degree(lng_r)
        elif self.__proj_type == PROJCONS.albers_equal_area:
            pass
        else:
            return False
        return lng_d, lat_d

    def to_unit(self, num):
        return num * UNITCONS.scale_dict[self.__linear_unit_type]

    def to_meter(self, num):
        return num / UNITCONS.scale_dict[self.__linear_unit_type]

    def to_degree(self, num):
        return num / PI * 180

    def to_radian(self, num):
        return num / 180 * PI


if __name__ == "__main__":
    p = PiProjection()
    p.load("图层文件/图层文件坐标系统说明.txt")
