import point_cloud_processing as pcp
import global_registration as gr
import numpy as np
import open3d as o3d
import copy

# def draw_registration_result(source, target, transformation):
#     source_temp = copy.deepcopy(source)
#     target_temp = copy.deepcopy(target)
#     source_temp.paint_uniform_color([1, 0.706, 0])
#     target_temp.paint_uniform_color([0, 0.651, 0.929])
#     source_temp.transform(transformation)
#     o3d.visualization.draw_geometries([source_temp, target_temp],
#                                       zoom=0.4459,
#                                       front=[0.9288, -0.2951, -0.2242],
#                                       lookat=[1.6784, 2.0612, 1.4451],
#                                       up=[-0.3402, -0.9189, -0.1996])
#
#
#
# # source = pcp.point_cloud('/home/martin/Point-Cloud-Registration/Data/001/1719040733900000.pcd')
# # target = pcp.point_cloud('/home/martin/Point-Cloud-Registration/Data/001/1719040733900.pcd')
#
# source = o3d.io.read_point_cloud('/home/martin/Point-Cloud-Registration/Data/002/1719040752000000.pcd')
# target = o3d.io.read_point_cloud('/home/martin/Point-Cloud-Registration/Data/002/1719040752000.pcd')
#
#
# draw_registration_result(source,target, np.identity(4))
#
# threshold = 0.5
# trans_init = np.array([[1.0, 0.0, 0.0, 0.0],
#                        [0.0, 1.0, 0.0, 0.0],
#                        [0.0, 0.0, 1.0, 0.0],
#                        [0.0, 0.0, 0.0, 1.0]])
#
# trans_2 = np.asarray([[0.0, 0.0, 1.0, 0.0],
#                       [-1.0, 0.0, 0.0, 0.0],
#                       [0.0, -1.0, 0.0, 0.0],
#                       [0.0, 0.0, 0.0, 1.0]])
#
# source.transform(trans_2)
# # trans_3   =      np.asarray([[1.0, 0.0, 0.0, 2.3],
# #                              [0.0, 1.0, 0.0, 2.3],
# #                              [0.0, 0.0, 1.0, 1.0],
# #                              [0.0, 0.0, 0.0, 1.0]])
# #
# # source.transform(trans_3)
#
# draw_registration_result(source, target, np.identity(4))
#
# # gr.get_golbal_registration_transformation(source, target)
#
#
# #
# # ****************************************************************
#
#
# reg_p2p = o3d.pipelines.registration.registration_icp(
#     source, target, threshold, trans_init,
#     o3d.pipelines.registration.TransformationEstimationPointToPoint(),
#     o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=2000))
# print(reg_p2p)
# print("Transformation is:")
# print(reg_p2p.transformation)
# draw_registration_result(source, target, reg_p2p.transformation)

class ICP_Registrator(object):
    def __init__(self, template, target):
        self.template = template
        self.target = target

        self.global_transformation_matrix = np.asarray([[0.0, 0.0, 1.0, 0.0],
                                                       [-1.0, 0.0, 0.0, 0.0],
                                                       [0.0, -1.0, 0.0, 0.0],
                                                       [0.0, 0.0, 0.0, 1.0]])

        self.trans_init = np.array([[1.0, 0.0, 0.0, 0.0],
                                    [0.0, 1.0, 0.0, 0.0],
                                    [0.0, 0.0, 1.0, 0.0],
                                    [0.0, 0.0, 0.0, 1.0]])

        self.threshold = 0.5

    def icp_registration(self):

        # self.target = self.target.transform(self.global_transformation_matrix)
        reg_p2p = o3d.pipelines.registration.registration_icp(
            self.target, self.template, self.threshold, self.trans_init,
            o3d.pipelines.registration.TransformationEstimationPointToPoint(),
            o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=2000))

        icp_result =self.target.transform(reg_p2p.transformation)
        fitness = reg_p2p.fitness
        rmse = reg_p2p.inlier_rmse
        icp_transformation_matrix = reg_p2p.transformation
        print(icp_transformation_matrix)

        return icp_result, icp_transformation_matrix, fitness, rmse