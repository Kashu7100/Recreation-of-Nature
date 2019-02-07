from swarm_visualizer import Visualizer, Agents
from vispy.scene import visuals

class Swarm(Visualizer):
    def __init__(self):
        super().__init__(show_axis=False)
        self.arrow1 = visuals.Arrow(arrow_size=10, arrow_type='angle_30', arrow_color=(0.5,0.5,1,1), parent=self.view.scene)
        self.agents1 = Agents(512,dim=3,boundary=0.5)

    def update(self):
        super().update()
        self.view.camera.orbit(1,0)
        self.arrow1.set_data(arrows=self.agents1.update())


if __name__ == '__main__':
    from moviepy.editor import VideoClip
    canvas = Swarm()
    while canvas:
        canvas.update()

    # to save the simlation, use following codes befor the while statement.
    #
    #clip = VideoClip(canvas.animation, duration=150)
    #clip.write_videofile('swarm_predator_prey.mp4', fps=20)
    #clip.write_gif('brain.gif', fps=20, opt='OptimizePlus', fuzz=10)
