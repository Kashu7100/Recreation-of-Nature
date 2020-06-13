from ..boids import Visualizer, Agents
from vispy.scene import visuals

class Swarm(Visualizer):
    def __init__(self):
        super().__init__(show_axis=False)
        self.arrow1 = visuals.Arrow(arrow_size=10, arrow_type='angle_30', arrow_color=(0.5,0.5,1,1), parent=self.view.scene)
        self.agents1 = Agents(256,dim=2,boundary=0.5)

        self.arrow2 = visuals.Arrow(arrow_size=15, arrow_type='angle_30', arrow_color=(1,0.1,0.1,1), parent=self.view.scene)
        self.agents2 = Agents(5,dim=2,boundary=0.5,cohesion_force=0.001,cohesion_dist=0.1,separation_dist=0.5,max_speed=0.045)

    def update(self):
        super().update()
        self.arrow1.set_data(arrows=self.agents1.update(predator=self.agents2))
        self.arrow2.set_data(arrows=self.agents2.update(prey=self.agents1))


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
