from gs_toolkit.render.renderer import Renderer
from pathlib import Path
import numpy as np

from gs_toolkit.utils.rich_utils import CONSOLE

# Parameters
pose = np.array(
    [
        [
            -0.2114434540271759,
            -0.21456517279148102,
            0.9535478353500366,
            0.7391851544380188,
        ],
        [
            0.9757110476493835,
            0.010824061930179596,
            0.2187936156988144,
            0.2835785448551178,
        ],
        [
            -0.05726674944162369,
            0.9766497015953064,
            0.2070649415254593,
            0.058663368225097656,
        ],
        [0.0, 0.0, 0.0, 1.0],
    ],
)

load_config = Path(
    "/mnt/d/Projects/Gaussian-Splatting-Toolkit/outputs/microwave_fine/gaussian-splatting/2024-02-14_173020/config.yml"
)


def main():
    renderer = Renderer(load_config)
    renderer.get_output_from_pose(pose, width=1280, height=720)
    renderer.show()
    # Get rgb image
    rgb = renderer.rgb
    CONSOLE.print(f"rgb shape: {rgb.shape}")
    # cv2.imwrite(
    #     "exports/student_lounge_object/rgb.png",
    #     cv2.cvtColor(255 * rgb, cv2.COLOR_RGB2BGR),
    # )
    # Get depth image
    depth = renderer.depth
    CONSOLE.print(f"depth shape: {depth.shape}")
    depth = (depth * 1000).astype(np.uint32)
    # im = Image.fromarray(depth[:, :, 0])
    # im.save("exports/student_lounge_object/depth.png")


if __name__ == "__main__":
    main()
