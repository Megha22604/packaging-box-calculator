from django.db import models
import cv2

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')

    def get_dimensions(self):
        img = cv2.imread(self.image.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            pixel_to_cm = 0.1  # calibration factor
            length = w * pixel_to_cm
            height = h * pixel_to_cm
            width = (cv2.contourArea(c) / (w * h)) * length
            return round(length, 2), round(width, 2), round(height, 2)
        return 0, 0, 0

    def box_dimensions(self):
        l, w, h = self.get_dimensions()
        return l + 2, w + 2, h + 2

    def cost_estimation(self):
        l, w, h = self.box_dimensions()
        volume = l * w * h
        base_rate = 0.05
        return round(volume * base_rate, 2)
