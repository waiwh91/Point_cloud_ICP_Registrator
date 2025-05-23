from pyqtgraph.opengl import GLViewWidget, GLScatterPlotItem
import numpy as np
import open3d as o3d


class PreChangeViewer(GLViewWidget):
    def __init__(self, parent=None, pcd_target=None, pcd_template=None):
        GLViewWidget.__init__(self, parent)
        self.pcd_target = pcd_target
        self.pcd_template = pcd_template

        target_color = (0, 0.651, 0.929, 1)
        template_color = (0.929, 0.651, 0, 1)

        self.target_points = self.pcd_target.points
        self.template_points = self.pcd_template.points

        # print(np.asarray(self.target_points).shape)
        # print(np.asarray(self.template_points).shape)

        self.target_plot_item = GLScatterPlotItem(parentItem=None, pos=self.target_points, color=target_color, size=3)
        self.template_plot_item = GLScatterPlotItem(parentItem=None, pos=self.template_points, color=template_color, size=3)

        # self.addItem(self.pcd_plot_item)

    def pcd_to_array(self):
        pass
