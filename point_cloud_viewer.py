from pyqtgraph.opengl import GLViewWidget, GLScatterPlotItem
import numpy as np
import open3d as o3d


class PointCloudViewer(GLViewWidget):
    def __init__(self, parent=None, pcd=None, type = None):
        GLViewWidget.__init__(self, parent)
        self.pcd = pcd
        if type == "Target" :
            self.point_color = (0, 0.651, 0.929, 1)
        if type == "Template" :
            self.point_color = (0.929, 0.651, 0, 1)

        if type == "Result" :
            self.point_color = (0.6, 0.706, 1, 1)
        # self.pcd = o3d.io.read_point_cloud(pcd_path)
        self.pcd_points = self.pcd.points
        # print(np.asarray(self.pcd.points))
        # print(np.asarray(self.pcd_points).shape)

        self.pcd_plot_item = GLScatterPlotItem(parentItem=None, pos=self.pcd_points, color=self.point_color, size=3)

        # self.addItem(self.pcd_plot_item)

    def pcd_to_array(self):
        return self.pcd_plot_item

