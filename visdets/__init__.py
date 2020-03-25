"""visdets - A package for visualizing results of object detection"""

__version__ = '0.1.0'
__author__ = 'eqs <murashige.satoshi.mi1 [at] is.naist.jp>'


from .visualizations import draw_bbox, draw_keypoint

__all__ = ['draw_bbox', 'draw_keypoint']
