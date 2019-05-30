# _*_ coding: utf-8 _*_
# @Time     : 2019/3/7 17:01
# @Author   : Ole211
# @Site     : 
# @File     : lane-detection.py    
# @Software : PyCharm
import cv2 as cv
import numpy as np
import os
import utils
# 安装moviepy 命令
# pip install moviepy
# conda install ffmpeg -c conda-forge
from moviepy.editor import VideoFileClip

os.chdir('d:\\img\\')

def get_obj_img_points(images, grid=(9, 6)):
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    object_points = []
    img_points = []
    for img in images:
        # 生成object points
        object_point = np.zeros((grid[0] * grid[1], 3), np.float32)
        object_point[:, :2] = np.mgrid[0:grid[0], 0:grid[1]].T.reshape(-1, 2)
        # 得到灰度图片
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # 得到图片的images_pointa
        ret, corners = cv.findChessboardCorners(gray, grid, None)
        if ret:
            object_points.append(object_point)
            corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            print('object_point,', object_point )
            print('corners,', corners)
            img_points.append(corners)
            cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            cv.drawChessboardCorners(img, grid, corners2, ret)
            cv.imshow('img', img)
            cv.waitKey(1)
    cv.destroyAllWindows()
    print(len(object_points), len(img_points))
    return object_points, img_points

# 计算校正矩阵和失真系数， 返回校正图片
def cal_undistort(img, objpoints, imgpoints):
    # 计算校正矩阵和失真系数, 使用cv2.calibrateCamera() 方法
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, img.shape[1::-1], None, None)
    # 得到校正图片， 使用 cv2,undistor() 方法
    dst = cv.undistort(img, mtx, dist, None, mtx)
    return dst

# 阈值过滤(sobel threshold)
def abs_sobel_thresh(img, orient='x', thresh_min=0, thresh_max=255):
    # 转换为灰度图片
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 使用cv2.Sobel()计算x方向或y方向导数
    if orient == 'x':
        abs_sobel = np.abs(cv.Sobel(gray, cv.CV_64F, 1, 0))
    if orient == 'y':
        abs_sobel = np.abs(cv.Sobel(gray, cv.CV_64F, 0, 1))
    # 阈值过滤
    scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))
    binary_output = np.zeros_like(scaled_sobel)
    binary_output[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1
    return binary_output

def mag_thresh(img, sobel_kernel=3, mag_thresh=(0, 255)):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=sobel_kernel)
    sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=sobel_kernel)
    gradmag = np.sqrt(sobelx**2 + sobely**2)
    scale_factor = np.max(gradmag)/255
    gradmag = (gradmag/scale_factor).astype(np.uint8)
    binary_output = np.zeros_like(gradmag)
    binary_output[(gradmag >= mag_thresh[0]) & (gradmag <= mag_thresh[1])] = 1
    return binary_output

def hls_select(img, channel='s', thresh=(0, 255)):
    hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
    if channel == 'h':
        channel = hls[:,:,0]
    elif channel == 'l':
        channel = hls[:,:,1]
    else:
        channel = hls[:,:,2]
    binary_output = np.zeros_like(channel)
    binary_output[(channel > thresh[0]) & (channel <= thresh[1])] = 1
    return binary_output

# 透视图变换鸟瞰图，
# 使用 cv2.getPerspectiveTransform()来获取变形矩阵，把图像变成鸟瞰视角
# 源点和目标点根据自己的实际需要进行选择
# 然后使用 cv.=2.warpPerspective() 传入相关值获得变形图片(warpped image)
# thresholded_wraped = cv.warpPerspective(thresholded, M, img.shape[1::-1], flags=cv.INTER_LINEAR)

# 透视变换， 返回变形矩阵和逆变形矩阵
def get_M_Minv():
    src = np.float32([[(203, 720), (585, 460), (695, 460), (1127, 720)]])
    dst = np.float32([[(320, 720), (320, 0), (960, 0), (960, 720)]])
    M = cv.getPerspectiveTransform(src, dst)
    Minv = cv.getPerspectiveTransform(dst, src)
    return M, Minv

# 阈值化，Canny算子进行边缘检测
def canny_threshod(img, min_thresh, max_thresh):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, min_thresh, max_thresh)
    return edges

def laplacian(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Laplacian(gray, cv.CV_64F)
    return edges

# 检测车道边界
def find_line(binary_warped):
    # 获取图像一半的底部直方图
    histogram = np.sum(binary_warped[binary_warped.shape[0]//2:,:], axis=0)
    # 找到左右一半直方图峰值， 可能是左右边界线的基点
    midpoint = np.int(histogram.shape[0]/2)
    left_base = np.argmax(histogram[:midpoint])
    right_base = np.argmax(histogram[midpoint:]) + midpoint

    # 选择滑动窗口的数量
    nwindows = 9
    # 设置窗口高度
    window_height = np.int(binary_warped.shape[0]/nwindows)
    # 识别图像中所有非0像素的x, y位置
    nonzero = binary_warped.nonzero()
    nonzeroy = np.array(nonzero[0])
    nonzerox = np.array(nonzero[1])
    # 对每个窗口更新当前位置
    leftx_current = left_base
    rightx_current = right_base
    # 设置窗口边界的宽度
    margin = 100
    # 设置当前窗口中心的像素最小数量
    minpix = 50
    # 创建空列表接受左右车道像素标记
    left_lane_inds = []
    right_lane_inds = []

    # 一步一步滑过窗口
    for window in range(nwindows):
        # 识别左右窗口边界
        win_y_low = binary_warped.shape[0] - (window+1)*window_height
        win_y_high = binary_warped.shape[0] - window*window_height
        win_xleft_low = leftx_current - margin
        win_xleft_high = leftx_current + margin
        win_xright_low = rightx_current - margin
        win_xright_high = rightx_current + margin
        # 识别窗口中x，y轴非0像素
        good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & (nonzerox >= win_xleft_low) & (nonzerox < win_xleft_high)).nonzero()[0]
        good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & (nonzerox >= win_xright_low) &  (nonzerox < win_xright_high)).nonzero()[0]
        # 添加到标记列表中
        left_lane_inds.append(good_left_inds)
        right_lane_inds.append(good_right_inds)

        if len(good_left_inds) > minpix:
            leftx_current = np.int(np.mean(nonzerox[good_left_inds]))
        if len(good_right_inds) > minpix:
            rightx_current = np.int(np.mean(nonzerox[good_right_inds]))

    # 合并识别的数组
    left_lane_inds = np.concatenate(left_lane_inds)
    right_lane_inds = np.concatenate(right_lane_inds)

    # 提取左右线像素位置
    leftx = nonzerox[left_lane_inds]
    lefty = nonzeroy[left_lane_inds]
    rightx = nonzerox[right_lane_inds]
    righty = nonzeroy[right_lane_inds]

    # 每2秒多项式拟合一次
    left_fit = np.polyfit(lefty, leftx, 2)
    right_fit = np.polyfit(righty, rightx, 2)

    return left_fit, right_fit, left_lane_inds, right_lane_inds


# 计算车道曲率及车辆相对车道的中心位置
# 利用检测车道得到的拟合值(find_line() 返回的left_fit, right_fit)
# 计算车道曲率，以及车辆相对车道的中心位置
def calculate_curv_and_pos(binary_warped, left_fit, right_fit):
    # 定义y值， 曲率半径
    ploty = np.linspace(0, binary_warped.shape[0]-1, binary_warped.shape[0])
    leftx = left_fit[0]*ploty**2 + left_fit[1]*ploty + left_fit[2]
    rightx = right_fit[0]*ploty**2 + right_fit[1]*ploty + right_fit[2]
    # 将x轴， y轴像素转换成米
    ym_per_pix = 30/720
    xm_per_pix = 3.7/700
    y_eval = np.max(ploty)
    # 在x, y空间拟合一个新的多项式
    left_fit_cr = np.polyfit(ploty*ym_per_pix, leftx*xm_per_pix, 2)
    right_fit_cr = np.polyfit(ploty*ym_per_pix, rightx*xm_per_pix, 2)
    # 计算新的曲率半径
    left_curverad = ((1 + (2 * left_fit_cr[0] * y_eval * ym_per_pix + left_fit_cr[1]) ** 2) ** 1.5) / np.absolute(2 * left_fit_cr[0])
    right_curverad = ((1 + (2 * right_fit_cr[0] * y_eval * ym_per_pix + right_fit_cr[1]) ** 2) ** 1.5) / np.absolute(2 * right_fit_cr[0])

    # 曲率
    curvature = ((left_curverad + right_curverad) / 2)
    print(curvature)
    lane_width = np.abs(leftx[719] - rightx[719])
    lane_xm_per_pix = 3.7 / lane_width
    veh_pos = (((leftx[719] + rightx[719]) * lane_xm_per_pix) / 2.)
    cen_pos = ((binary_warped.shape[1] * lane_xm_per_pix) / 2.)
    distance_from_center = veh_pos - cen_pos
    return curvature, distance_from_center

# 处理原图， 展示信息
# 使用逆变形矩阵把鸟瞰二进制图检测的车道镶嵌回原图， 并高亮车道区域
def draw_area(undist, binary_warped, Minv, left_fit, right_fit):
    # 生成x, y, 线段值
    ploty = np.linspace(0, binary_warped.shape[0]-1, binary_warped.shape[0])
    left_fitx = left_fit[0]*ploty**2 + left_fit[1]*ploty + left_fit[2]
    right_fitx = right_fit[0]*ploty**2 + right_fit[1]*ploty + right_fit[2]
    # 创建一个图片，并在上面画线
    warp_zero = np.zeros_like(binary_warped).astype(np.uint8)
    color_warp = np.dstack((warp_zero, warp_zero, warp_zero))

    pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
    pts = np.hstack((pts_left, pts_right))

    # 画warped图形框上画车道
    cv.fillPoly(color_warp, np.int_([pts]), (0, 255, 0))

    newwarp = cv.warpPerspective(color_warp, Minv, (undist.shape[1], undist.shape[0]))
    # 将结果和原始图像合并
    result = cv.addWeighted(undist, 1, newwarp, 0.3, 0)
    return result


# 标注信息
# 使用cv2.putText()方法处理原图展示车道，曲率及车辆相对车道中心位置信息
def draw_values(img, curvature, distance_from_center):
    font = cv.FONT_HERSHEY_SIMPLEX
    radius_text = 'Radius of Curvature: %sm' % (np.round(curvature))

    if distance_from_center > 0:
        pos_flag = 'right'
    else:
        pos_flag = 'left'

    cv.putText(img, radius_text, (100, 100), font, 1, (255, 255, 255), 3)
    center_text = 'Vehicle is %.3fm %s of center' % (np.abs(distance_from_center), pos_flag)
    cv.putText(img, center_text, (100, 150), font, 1, (255, 255, 255), 2)
    return img

def processing(img, object_points, img_points, M, Minv):
    img = cv.resize(img, (1280, 720))
    undist = cal_undistort(img, object_points, img_points)
    thresholded = canny_threshod(undist, 100, 200)
    # 透视变换， 返回变形后的鸟瞰图片
    thresholded_warped = cv.warpPerspective(thresholded, M, img.shape[1::-1], flags=cv.INTER_LINEAR)
    # 检测车道边界
    left_fit, right_fit, left_lane_inds, right_lane_inds = find_line(thresholded_warped)
    # 检测到的车道画图
    area_img = draw_area(undist, thresholded_warped, Minv, left_fit, right_fit)
    curvature, distance_from_center = calculate_curv_and_pos(thresholded_warped, left_fit, right_fit)
    result = draw_values(area_img, curvature, distance_from_center)
    return result

if __name__ == '__main__':


    # 获取棋盘格式图片
    cal_imgs = utils.get_images_by_dir('cal')
    # 计算object_points, img_points
    objpoints, imgpoints = get_obj_img_points(cal_imgs)
    # 透视变换， 返回变形矩阵和逆变形矩阵
    M, Minv = get_M_Minv()
    filename, ext = os.path.splitext('test2_challenge_video.mp4')
    project_outpath = filename + '_out' + ext

    project_video_clip = VideoFileClip('test2_challenge_video.mp4')
    project_video_out_clip = project_video_clip.fl_image(
        lambda clip:processing(clip, objpoints, imgpoints, M, Minv))
    project_video_out_clip.write_videofile(project_outpath, audio=False)
    print('ok')
    '''

    
    cap = cv.VideoCapture('harder_challenge_video.mp4')
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('out.mp4', fourcc, 20.0, (1280, 720))
    while(1):
        ret, frame = cap.read()
        result = processing(frame, objpoints, imgpoints, M, Minv)
        out.write(result)
        cv.imshow('result', result)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv.destroyAllWindows()
'''