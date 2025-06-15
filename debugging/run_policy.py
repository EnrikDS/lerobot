from lerobot.policies.pretrained import load_pretrained_policy
from lerobot.common.robots import make_robot

ckpt = "/home/enrique/Code/lerobot/outputs/train/act_so101_red_piece/checkpoints/040000/pretrained_model"
robot = make_robot(
    type="so100_follower",
    id="so101_follower",
    port="/dev/ttyACM4",
    cameras={"front": {"type": "opencv",
                       "index_or_path": "/dev/video0",
                       "width": 640, "height": 480, "fps": 30}},
)
policy = load_pretrained_policy(ckpt, device="cuda")  # o "cpu"

robot.connect()
try:
    obs = robot.reset()
    done = False
    while not done:
        action = policy.act(obs)
        obs, reward, done, info = robot.step(action)
finally:
    robot.disconnect()
