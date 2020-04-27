# -*- coding: utf-8 -*-

""" Various functions to help with IO. """

import os
import glob
from fnmatch import filter as file_filter


def _get_calib_prefix(file_prefix: str):

    prefix = 'calib'
    if file_prefix:
        prefix = file_prefix
    return prefix


def _get_left_prefix(file_prefix: str):

    left_prefix = "calib.left"
    if file_prefix:
        left_prefix = file_prefix + ".left"
    return left_prefix


def _get_right_prefix(file_prefix: str):

    right_prefix = "calib.right"
    if file_prefix:
        right_prefix = file_prefix + ".right"
    return right_prefix


def _get_intrinsics_file_name(dir_name: str,
                              file_prefix: str):

    intrinsics_file = os.path.join(dir_name,
                                   _get_calib_prefix(file_prefix) +
                                   ".intrinsics.txt")
    return intrinsics_file


def _get_distortion_file_name(dir_name: str,
                              file_prefix: str):

    dist_coeff_file = os.path.join(dir_name,
                                   _get_calib_prefix(file_prefix) +
                                   ".distortion.txt")
    return dist_coeff_file


def _get_enumerated_file_name(dir_name: str,
                              file_prefix: str,
                              type_prefix: str,
                              view_number: str,
                              extension_wth_dot: str
                              ):

    # Keep in synch with _get_enumerated_file_glob
    file_name = \
        os.path.join(dir_name,
                     _get_calib_prefix(file_prefix)
                     + "."
                     + type_prefix
                     + "."
                     + str(view_number) + extension_wth_dot)
    return file_name


def _get_enumerated_file_glob(dir_name: str,
                              file_prefix: str,
                              type_prefix: str,
                              extension_wth_dot: str
                              ):

    # Keep in synch with _get_enumerated_file_name
    file_glob = \
        os.path.join(dir_name,
                     _get_calib_prefix(file_prefix)
                     + "."
                     + type_prefix
                     + "."
                     + "*" + extension_wth_dot)
    return file_glob


def _get_extrinsics_file_name(dir_name: str,
                              file_prefix: str,
                              view_number: int
                              ):

    extrinsics_file = _get_enumerated_file_name(dir_name,
                                                file_prefix,
                                                "extrinsics",
                                                view_number,
                                                ".txt")
    return extrinsics_file


def _get_extrinsic_file_names(dir_name: str,
                              file_prefix: str):

    files = file_filter(os.listdir(dir_name),
                        _get_calib_prefix(file_prefix) + ".extrinsics.*.txt")
    return files


def _get_l2r_file_name(dir_name: str,
                       file_prefix: str):
    l2r_file = os.path.join(dir_name,
                            _get_calib_prefix(file_prefix) + ".l2r.txt")
    return l2r_file


def _get_images_file_name(dir_name: str,
                          file_prefix: str,
                          view_number: int
                          ):
    images_file = _get_enumerated_file_name(dir_name,
                                            file_prefix,
                                            "images",
                                            view_number,
                                            ".png")
    return images_file


def _get_ids_file_name(dir_name: str,
                       file_prefix: str,
                       view_number: int
                       ):
    ids_file = _get_enumerated_file_name(dir_name,
                                         file_prefix,
                                         "ids",
                                         view_number,
                                         ".txt")
    return ids_file


def _get_objectpoints_file_name(dir_name: str,
                                file_prefix: str,
                                view_number: int
                                ):
    object_points_file = _get_enumerated_file_name(dir_name,
                                                   file_prefix,
                                                   "object_points",
                                                   view_number,
                                                   ".txt")
    return object_points_file


def _get_imagepoints_file_name(dir_name: str,
                               file_prefix: str,
                               view_number: int
                               ):
    image_points_file = _get_enumerated_file_name(dir_name,
                                                  file_prefix,
                                                  "image_points",
                                                  view_number,
                                                  ".txt")
    return image_points_file


def _get_device_tracking_file_name(dir_name: str,
                                   file_prefix: str,
                                   view_number: int
                                   ):
    device_tracking = _get_enumerated_file_name(dir_name,
                                                file_prefix,
                                                "device_tracking",
                                                view_number,
                                                ".txt")
    return device_tracking


def _get_calibration_tracking_file_name(dir_name: str,
                                        file_prefix: str,
                                        view_number: int
                                        ):
    calibration_tracking = _get_enumerated_file_name(dir_name,
                                                     file_prefix,
                                                     "calib_obj_tracking",
                                                     view_number,
                                                     ".txt")
    return calibration_tracking


def _get_filenames_by_glob_expr(dir_name: str,
                                file_prefix: str,
                                type_prefix: str,
                                extension_with_dot: str
                                ):

    file_glob = _get_enumerated_file_glob(dir_name,
                                          file_prefix,
                                          type_prefix,
                                          extension_with_dot)
    files = glob.glob(file_glob)
    files.sort()
    return files

