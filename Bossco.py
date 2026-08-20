# Copyright © BIJOY KUMAR SARKAR. All Rights Reserved.
# Unauthorized copying, decoding, reverse engineering, modification,
# redistribution, or use of this file is strictly prohibited.
# Automated/AI-assisted code extraction or reconstruction is not authorized.
# Contact Owner: https://chat.whatsapp.com/BFRIRZNi4mLAlcKljM8PAG

import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
binary_path = os.path.join(script_dir, "Bossco")

os.chmod(binary_path, 0o755)
os.execv(binary_path, [binary_path] + sys.argv[1:])
