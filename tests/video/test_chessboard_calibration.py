# -*- coding: utf-8 -*-

import glob
import pytest
import numpy as np
import cv2
import sksurgeryimage.processing.chessboard_point_detector as pd
import sksurgerycalibration.video.video_calibration_driver_mono as mc
import sksurgerycalibration.video.video_calibration_driver_stereo as sc


def test_chessboard_mono():

    images = []

    files = glob.glob('tests/data/laparoscope_calibration/left/*.png')
    for file in files:
        image = cv2.imread(file)
        images.append(image)

    # This illustrates that the PointDetector sub-class holds the knowledge of the model.
    chessboard_detector = \
        pd.ChessboardPointDetector((14, 10),    # (Width, height), number of internal corners
                                   3,           # Actual square size in mm
                                   (1, 1)       # Scale factors. Here, images are 1920x1080 so no scaling needed.
                                   )            # If images were 1920x540, you'd pass in (1920, 540),
                                                # and PointDetector base class would scale it up.

    # Pass a PointDetector sub-class to the calibration driver.
    calibrator = \
        mc.MonoVideoCalibrationDriver(chessboard_detector, 140)

    # Repeatedly grab data, until you have enough.
    for image in images:
        successful = calibrator.grab_data(image)
        assert successful > 0

    # Extra checking, as its a unit test
    assert calibrator.get_number_of_views() == 9
    calibrator.pop()
    assert calibrator.get_number_of_views() == 8
    successful = calibrator.grab_data(images[-1])
    assert successful
    assert calibrator.get_number_of_views() == 9

    # Then do calibration
    reproj_err, recon_err, params = calibrator.calibrate()

    # Just for a regression test, checking reprojection error, and recon error.
    assert (np.abs(reproj_err - 0.59164921) < 0.000001)
    assert (np.abs(recon_err - 0.21561650) < 0.000001)


def test_chessboard_stereo():

    left_images = []
    files = glob.glob('tests/data/laparoscope_calibration/left/*.png')
    files.sort()
    for file in files:
        image = cv2.imread(file)
        left_images.append(image)
    assert(len(left_images) == 9)

    right_images = []
    files = glob.glob('tests/data/laparoscope_calibration/right/*.png')
    files.sort()
    for file in files:
        image = cv2.imread(file)
        right_images.append(image)
    assert (len(right_images) == 9)

    chessboard_detector = \
        pd.ChessboardPointDetector((14, 10),
                                   3,
                                   (1, 1)
                                   )

    calibrator = \
        sc.StereoVideoCalibrationDriver(chessboard_detector, 140)

    # Repeatedly grab data, until you have enough.
    for i in range(0, len(left_images)):
        successful = calibrator.grab_data(left_images[i], right_images[i])
        assert successful > 0

    # Then do calibration
    reproj_err, recon_err, params = calibrator.calibrate()

    # Just for a regression test, checking reprojection error, and recon error.
    assert (np.abs(reproj_err - 0.65521300) < 0.000001)
    assert (np.abs(recon_err - 1.25703999) < 0.000001)
