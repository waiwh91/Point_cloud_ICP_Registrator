import open3d

class point_cloud:
    def __init__(self, filepath):
        self.path = filepath
        self.data = open3d.io.read_point_cloud(filepath)
    def show_down_sampled_picture(self):
        down_pcd = self.data.voxel_down_sample(voxel_size=0.005)
        open3d.visualization.draw_geometries([down_pcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
    def show_picture(self):
        open3d.visualization.draw_geometries([self.data],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
