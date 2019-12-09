# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

__all__ = ['BaseSkeletonStyle', 'COCOHumanSkeletonStyle']


class BaseSkeletonStyle:
    def __init__(self):
        self.skeleton = []
        self.points = []
        self.keypoints = []
        self.keypoints_color = []

    @property
    def nkeypoints(self):
        return len(self.keypoints)

    def visualize_skeleton(self, ax=None):

        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111)

        # Plot edges between each keypoints
        for p1, p2 in self.skeleton:
            s = self.points[p1]
            e = self.points[p2]
            cl = self.keypoints_color[p2]
            ax.plot([s[0], e[0]], [s[1], e[1]], color=cl)

        # Plot markers and its names
        for k, p in enumerate(self.points):
            cl = self.keypoints_color[k]
            ax.plot(p[0], p[1],
                    marker='o', markerfacecolor=cl, markeredgecolor='black')
            ax.text(p[0], p[1], self.keypoints[k],
                    color='black', rotation=30)

        return ax


class COCOHumanSkeletonStyle(BaseSkeletonStyle):
    def __init__(self):
        self.skeleton = [[15, 13], [13, 11], [16, 14], [14, 12], [11, 12],
                         [5, 11], [6, 12], [5, 6], [5, 7], [6, 8],
                         [7, 9], [8, 10], [1, 2], [0, 1], [0, 2],
                         [1, 3], [2, 4], [3, 5], [4, 6]]

        self.points = [(0, 2),
                       (0.5, 3), (-0.5, 3), (1, 2), (-1, 2),
                       (1, 1), (-1, 1), (2, 0), (-2, 0), (2, -1), (-2, -1),
                       (1, -1), (-1, -1), (1, -3), (-1, -3), (1, -5), (-1, -5)]

        self.keypoints = ['nose',
                          'left_eye', 'right_eye', 'left_ear', 'right_ear',
                          'left_shoulder', 'right_shoulder',
                          'left_elbow', 'right_elbow',
                          'left_wrist', 'right_wrist',
                          'left_hip', 'right_hip',
                          'left_knee', 'right_knee',
                          'left_ankle', 'right_ankle']

        self.keypoints_color = ['#FF0000', '#FF4100', '#FF8200', '#FFC300',
                                '#F9FF00', '#B8FF00', '#77FF00', '#36FF00',
                                '#00FF0A', '#00FF4B', '#00FF8C', '#00FFCD',
                                '#00EFFF', '#00AEFF', '#006DFF', '#002CFF',
                                '#1400FF']
