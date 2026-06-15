#!/usr/bin/env python3
import os
pairs = [
    ('/home/parv/Projects/demo/Mapping.mp4', '/home/parv/Projects/Portfolio/media/mapping_demo.mp4'),
    ('/home/parv/Projects/demo/SAC_agent_running_on_Power_grid_simulator.webm', '/home/parv/Projects/Portfolio/media/sac_demo.webm'),
    ('/home/parv/Projects/demo/Treasure_hunt.mp4', '/home/parv/Projects/Portfolio/media/treasure_demo.mp4'),
]
for src, dst in pairs:
    try:
        if os.path.lexists(dst): os.remove(dst)
        os.symlink(src, dst)
        print(f'OK: {dst}')
    except Exception as e:
        print(f'FAIL {dst}: {e}')
