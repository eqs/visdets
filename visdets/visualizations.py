# -*- coding: utf-8 -*-
import cv2

__all__ = ['draw_keypoint', 'draw_bbox']


def color_str2int(style):
    r = style[1:3]
    g = style[3:5]
    b = style[5:7]
    return (int(r, 16), int(g, 16), int(b, 16))


def draw_keypoint(frame, keypoint, keypoint_scores, skeleton_style,
                  kp_thresh=0.2, skeleton_color=None, marker_size=8):
    # Draw line segments between two keypoints
    for p1, p2 in skeleton_style.skeleton:
        if keypoint_scores[p1] > kp_thresh and keypoint_scores[p2] > kp_thresh:

            if skeleton_color is None:
                cl = color_str2int(skeleton_style.keypoints_color[p2])
            else:
                cl = skeleton_color

            cv2.line(frame,
                     (int(keypoint[p1][0]), int(keypoint[p1][1])),
                     (int(keypoint[p2][0]), int(keypoint[p2][1])), cl, 2)

    # Draw marker on kerypoints
    for kp, kp_score, style in zip(keypoint,
                                   keypoint_scores,
                                   skeleton_style.keypoints_color):
        if kp_score > kp_thresh:

            if skeleton_color is None:
                cl = color_str2int(style)
            else:
                cl = skeleton_color

            cv2.circle(frame, (int(kp[0]), int(kp[1])), marker_size, cl, -1)


def draw_bbox(frame, x, y, w, h, score=None, label=None,
              facecolor=(0, 255, 0), textcolor=(0, 0, 0), thickness=4,
              fontScale=1.5, fontThickness=4):

    is_render_caption = score is not None or label is not None

    if is_render_caption:

        if label is None:
            text = f'{score:.2f}'
        elif score is None:
            text = f'{label}'
        else:
            text = f'{label}: {score:.2f}'

        text_data = dict(
            text=text,
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=fontScale,
            thickness=fontThickness
        )

        (tw, th), baseline = cv2.getTextSize(**text_data)

        margin = int(min(tw, th) * 0.2)

    cv2.rectangle(frame, (x, y), (x+w, y+h), facecolor, thickness)

    if is_render_caption:
        # Draw face
        cv2.rectangle(frame, (x-margin, y),
                      (x+tw+margin, y-th-margin*2), facecolor, -1)
        # Draw text
        cv2.putText(frame, org=(x, y-margin), color=textcolor, **text_data)

    return frame
