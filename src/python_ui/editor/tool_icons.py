from PyQt5.QtCore import Qt, QPoint, QPointF, QRect, QRectF
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen, QBrush, QPainterPath, QPolygonF, QFont, QIcon, QLinearGradient, QRadialGradient
import math

C = QColor(230, 230, 230)
CP = QPen(C, 1.6)
CP_THIN = QPen(C, 1.0)
NOBRUSH = Qt.NoBrush


def _make(size=26):
    pix = QPixmap(size, size)
    pix.fill(Qt.transparent)
    p = QPainter(pix)
    p.setRenderHint(QPainter.Antialiasing)
    p.translate(1, 1)
    return pix, p


def _end(p):
    p.end()


def _path(p, pts, close=True):
    path = QPainterPath()
    path.moveTo(pts[0])
    for pt in pts[1:]:
        path.lineTo(pt)
    if close:
        path.closeSubpath()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawPath(path)


def icon_move():
    pix, p = _make()
    cx, cy = 12, 12
    s = 6
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    # arrows: up/down/left/right
    p.drawLine(cx, cy - s - 3, cx, cy - 3)
    p.drawLine(cx - 2, cy - s - 1, cx, cy - s - 3)
    p.drawLine(cx + 2, cy - s - 1, cx, cy - s - 3)
    p.drawLine(cx, cy + s + 3, cx, cy + 3)
    p.drawLine(cx - 2, cy + s + 1, cx, cy + s + 3)
    p.drawLine(cx + 2, cy + s + 1, cx, cy + s + 3)
    p.drawLine(cx - s - 3, cy, cx - 3, cy)
    p.drawLine(cx - s - 1, cy - 2, cx - s - 3, cy)
    p.drawLine(cx - s - 1, cy + 2, cx - s - 3, cy)
    p.drawLine(cx + s + 3, cy, cx + 3, cy)
    p.drawLine(cx + s + 1, cy - 2, cx + s + 3, cy)
    p.drawLine(cx + s + 1, cy + 2, cx + s + 3, cy)
    _end(p)
    return QIcon(pix)


def icon_rect_marquee():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawRect(3, 3, 18, 18)
    for x, y in [(3, 3), (21, 3), (3, 21), (21, 21)]:
        p.drawRect(x - 1, y - 1, 3, 3)
    _end(p)
    return QIcon(pix)


def icon_ellipse_marquee():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawEllipse(3, 4, 18, 16)
    _end(p)
    return QIcon(pix)


def icon_lasso():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    path = QPainterPath()
    path.moveTo(20, 4)
    path.cubicTo(16, 2, 6, 4, 4, 10)
    path.cubicTo(2, 16, 6, 20, 10, 18)
    path.cubicTo(12, 17, 12, 20, 10, 22)
    p.drawPath(path)
    _end(p)
    return QIcon(pix)


def icon_magic_wand():
    pix, p = _make()
    c = C
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    cx, cy = 12, 10
    sz = 7
    pts = []
    for i in range(5):
        angle = -math.pi / 2 + i * 2 * math.pi / 5
        pts.append(QPointF(cx + sz * math.cos(angle), cy + sz * math.sin(angle)))
        angle += math.pi / 5
        pts.append(QPointF(cx + sz * 0.4 * math.cos(angle), cy + sz * 0.4 * math.sin(angle)))
    poly = QPolygonF(pts)
    p.drawPolygon(poly)
    for x, y in [(18, 2), (22, 4), (20, 8)]:
        p.drawLine(x, y - 2, x, y + 2)
        p.drawLine(x - 2, y, x + 2, y)
    _end(p)
    return QIcon(pix)


def icon_crop():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawLine(3, 3, 3, 18)
    p.drawLine(3, 3, 18, 3)
    p.drawLine(21, 6, 21, 21)
    p.drawLine(6, 21, 21, 21)
    p.setPen(CP_THIN)
    p.drawLine(3, 21, 21, 3)
    _end(p)
    return QIcon(pix)


def icon_healing():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(C)
    p.drawEllipse(QPoint(12, 12), 10, 10)
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawLine(5, 12, 19, 12)
    p.drawLine(12, 5, 12, 19)
    _end(p)
    return QIcon(pix)


def icon_brush():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    # handle
    p.drawLine(5, 21, 10, 12)
    # ferrule
    p.drawLine(9, 13, 11, 10)
    # brush tip
    path = QPainterPath()
    path.moveTo(10, 12)
    path.lineTo(18, 3)
    path.lineTo(20, 5)
    path.lineTo(12, 14)
    path.closeSubpath()
    p.drawPath(path)
    p.setPen(CP_THIN)
    p.drawLine(18, 3, 19, 1)
    p.drawLine(19, 4, 21, 3)
    _end(p)
    return QIcon(pix)


def icon_pencil():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    path = QPainterPath()
    path.moveTo(4, 21)
    path.lineTo(12, 10)
    path.lineTo(14, 12)
    path.lineTo(6, 23)
    path.closeSubpath()
    p.drawPath(path)
    p.drawLine(12, 10, 17, 4)
    p.drawLine(17, 4, 19, 6)
    p.drawLine(19, 6, 14, 12)
    _end(p)
    return QIcon(pix)


def icon_clone_stamp():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawRoundedRect(4, 9, 16, 12, 2, 2)
    p.drawRoundedRect(9, 2, 6, 7, 1, 1)
    p.drawLine(4, 9, 20, 9)
    _end(p)
    return QIcon(pix)


def icon_eraser():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    path = QPainterPath()
    path.moveTo(4, 8)
    path.lineTo(18, 8)
    path.lineTo(22, 16)
    path.lineTo(4, 16)
    path.closeSubpath()
    p.drawPath(path)
    p.drawLine(4, 12, 22, 12)
    _end(p)
    return QIcon(pix)


def icon_gradient():
    pix, p = _make()
    rect = QRect(3, 5, 18, 14)
    grad = QLinearGradient(3, 12, 21, 12)
    grad.setColorAt(0.0, Qt.white)
    grad.setColorAt(0.5, QColor(160, 160, 160))
    grad.setColorAt(1.0, Qt.black)
    p.setPen(QPen(C, 1.2))
    p.setBrush(QBrush(grad))
    p.drawRect(rect)
    _end(p)
    return QIcon(pix)


def icon_pen():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    path = QPainterPath()
    path.moveTo(12, 2)
    path.lineTo(4, 20)
    path.lineTo(8, 22)
    path.lineTo(14, 18)
    path.closeSubpath()
    p.drawPath(path)
    p.setBrush(C)
    p.drawEllipse(QPoint(12, 2), 2, 2)
    _end(p)
    return QIcon(pix)


def icon_type():
    pix, p = _make()
    p.setPen(QPen(C, 2.0))
    p.drawLine(4, 3, 20, 3)
    p.drawLine(12, 3, 12, 21)
    p.setPen(CP)
    p.drawLine(7, 21, 17, 21)
    _end(p)
    return QIcon(pix)


def icon_shape():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawRoundedRect(3, 5, 18, 14, 3, 3)
    p.drawEllipse(QPoint(12, 12), 3, 3)
    _end(p)
    return QIcon(pix)


def icon_hand():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    s = QPainterPath()
    s.moveTo(10, 14)
    s.lineTo(10, 6)
    s.lineTo(8, 6)
    s.lineTo(8, 16)
    s.lineTo(6, 16)
    s.lineTo(6, 8)
    s.lineTo(4, 8)
    s.lineTo(4, 16)
    s.lineTo(10, 22)
    s.lineTo(18, 22)
    s.lineTo(22, 18)
    s.lineTo(22, 14)
    s.lineTo(20, 14)
    s.lineTo(16, 14)
    s.lineTo(16, 4)
    s.lineTo(14, 4)
    s.lineTo(14, 14)
    s.lineTo(12, 14)
    s.lineTo(12, 2)
    s.lineTo(10, 2)
    s.lineTo(10, 14)
    s.closeSubpath()
    p.drawPath(s)
    _end(p)
    return QIcon(pix)


def icon_zoom():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawEllipse(2, 2, 14, 14)
    p.drawLine(13, 13, 21, 21)
    cx, cy = 9, 9
    p.drawLine(cx - 4, cy, cx + 4, cy)
    p.drawLine(cx, cy - 4, cx, cy + 4)
    _end(p)
    return QIcon(pix)


def icon_eyedropper():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawLine(3, 21, 10, 8)
    p.drawLine(12, 8, 20, 5)
    p.drawLine(20, 5, 19, 3)
    p.drawLine(19, 3, 17, 4)
    p.drawLine(17, 4, 10, 12)
    p.drawLine(10, 8, 12, 8)
    p.setBrush(C)
    p.drawEllipse(QPoint(3, 21), 2, 2)
    _end(p)
    return QIcon(pix)


def icon_paint_bucket():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    path = QPainterPath()
    path.moveTo(5, 7)
    path.lineTo(4, 18)
    path.lineTo(20, 18)
    path.lineTo(19, 7)
    path.closeSubpath()
    p.drawPath(path)
    p.drawLine(3, 7, 21, 7)
    p.drawLine(12, 18, 12, 22)
    p.drawEllipse(QPoint(12, 22), 2, 2)
    _end(p)
    return QIcon(pix)


def icon_dodge():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    r = QRect(2, 2, 20, 20)
    grad = QRadialGradient(12, 12, 10)
    grad.setColorAt(0.0, Qt.white)
    grad.setColorAt(0.6, C)
    grad.setColorAt(1.0, QColor(80, 80, 80))
    p.setBrush(QBrush(grad))
    p.drawEllipse(r)
    p.setPen(CP)
    for x, y in [(8, 6), (16, 6), (6, 10), (18, 10), (12, 12), (6, 14), (18, 14), (8, 18), (16, 18)]:
        p.drawPoint(x, y)
    _end(p)
    return QIcon(pix)


def icon_burn():
    pix, p = _make()
    p.setPen(QPen(C, 1.2))
    r = QRect(2, 2, 20, 20)
    grad = QRadialGradient(12, 12, 10)
    grad.setColorAt(0.0, QColor(80, 80, 80))
    grad.setColorAt(0.6, C)
    grad.setColorAt(1.0, Qt.black)
    p.setBrush(QBrush(grad))
    p.drawEllipse(r)
    p.setPen(QPen(C, 1.0))
    for x, y in [(8, 6), (16, 6), (6, 10), (18, 10), (12, 12), (6, 14), (18, 14), (8, 18), (16, 18)]:
        p.drawPoint(x, y)
    _end(p)
    return QIcon(pix)


def icon_sponge():
    pix, p = _make()
    p.setPen(CP)
    p.setBrush(NOBRUSH)
    p.drawRoundedRect(4, 5, 16, 14, 3, 3)
    p.setPen(QPen(C, 1.0))
    for x, y in [(7, 9), (13, 9), (19, 9), (7, 15), (13, 15), (19, 15)]:
        p.drawRect(x - 1, y - 1, 3, 3)
    _end(p)
    return QIcon(pix)


TOOL_ICONS = {
    "Move Tool": icon_move,
    "Rectangular Marquee Tool": icon_rect_marquee,
    "Elliptical Marquee Tool": icon_ellipse_marquee,
    "Lasso Tool": icon_lasso,
    "Magic Wand Tool": icon_magic_wand,
    "Crop Tool": icon_crop,
    "Spot Healing Brush Tool": icon_healing,
    "Brush Tool": icon_brush,
    "Pencil Tool": icon_pencil,
    "Clone Stamp Tool": icon_clone_stamp,
    "Eraser Tool": icon_eraser,
    "Gradient Tool": icon_gradient,
    "Pen Tool": icon_pen,
    "Horizontal Type Tool": icon_type,
    "Rectangle Tool": icon_shape,
    "Hand Tool": icon_hand,
    "Zoom Tool": icon_zoom,
    "Eyedropper Tool": icon_eyedropper,
    "Paint Bucket Tool": icon_paint_bucket,
    "Dodge Tool": icon_dodge,
    "Burn Tool": icon_burn,
    "Sponge Tool": icon_sponge,
}


def get_tool_icon(tool_name):
    fn = TOOL_ICONS.get(tool_name)
    if fn:
        return fn()
    return QIcon()
