# Copyright © BIJOY KUMAR SARKAR. All Rights Reserved.
# Unauthorized copying, decoding, reverse engineering, modification,
# redistribution, or use of this file is strictly prohibited.
# Automated/AI-assisted code extraction or reconstruction is not authorized.
# Contact Owner: https://chat.whatsapp.com/BFRIRZNi4mLAlcKljM8PAG

import os
import platform

bit = platform.architecture()[0]

if bit == '64bit':
    import Bossco64
    Bossco64.start()
elif bit == '32bit':
#    import Bossco32
    print("32 Bit Is Not Support Yet")
#    Bossco32.start()
else:
    print("Unsupported Architecture")